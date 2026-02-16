export const prerender = false;

import type { APIRoute } from 'astro';
import Stripe from 'stripe';
import { sendMail } from '../../lib/mailer';

const stripe = new Stripe(import.meta.env.STRIPE_SECRET_KEY);

export const POST: APIRoute = async ({ request }) => {
  const signature = request.headers.get('stripe-signature');

  if (!signature) {
    return new Response('Keine Stripe-Signatur', { status: 400 });
  }

  try {
    const body = await request.text();
    const event = stripe.webhooks.constructEvent(
      body,
      signature,
      import.meta.env.STRIPE_WEBHOOK_SECRET
    );

    if (event.type === 'checkout.session.completed') {
      const session = event.data.object as Stripe.Checkout.Session;
      const customerEmail = session.customer_details?.email;

      if (customerEmail) {
        await sendMail({
          to: customerEmail,
          subject: 'Ihre Buchung bei Hinzke Digital - Bestätigung',
          html: `
            <h1>Vielen Dank für Ihre Buchung!</h1>
            <p>Wir haben Ihre Bestellung erhalten und melden uns in Kürze bei Ihnen.</p>
            <p>Mit freundlichen Grüßen,<br>Magnus Hinzke</p>
          `,
        });

        await sendMail({
          to: import.meta.env.CONTACT_EMAIL,
          subject: `Neue Buchung: ${customerEmail}`,
          html: `
            <h1>Neue Buchung eingegangen</h1>
            <p><strong>Kunde:</strong> ${customerEmail}</p>
            <p><strong>Session ID:</strong> ${session.id}</p>
            <p><strong>Betrag:</strong> ${(session.amount_total ?? 0) / 100} EUR</p>
          `,
        });
      }
    }

    return new Response(JSON.stringify({ received: true }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (error) {
    const message = error instanceof Error ? error.message : 'Webhook-Fehler';
    return new Response(JSON.stringify({ error: message }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' },
    });
  }
};
