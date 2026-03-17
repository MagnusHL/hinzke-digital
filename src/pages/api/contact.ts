export const prerender = false;

import type { APIRoute } from 'astro';
import { sendMail } from '../../lib/mailer';

export const POST: APIRoute = async ({ request }) => {
  try {
    const formData = await request.formData();
    const name = formData.get('name')?.toString();
    const email = formData.get('email')?.toString();
    const message = formData.get('message')?.toString();
    if (!name || !email || !message) {
      return new Response(JSON.stringify({ error: 'Bitte alle Pflichtfelder ausfüllen' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    await sendMail({
      to: import.meta.env.CONTACT_EMAIL,
      replyTo: email,
      subject: `Kontaktanfrage: ${name}`,
      html: `
        <h1>Neue Kontaktanfrage</h1>
        <p><strong>Name:</strong> ${name}</p>
        <p><strong>E-Mail:</strong> ${email}</p>
        <hr>
        <p>${message.replace(/\n/g, '<br>')}</p>
      `,
    });

    return new Response(JSON.stringify({ success: true }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (error) {
    const msg = error instanceof Error ? error.message : 'Fehler beim Senden';
    return new Response(JSON.stringify({ error: msg }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
};
