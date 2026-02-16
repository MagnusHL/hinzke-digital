import nodemailer from 'nodemailer';

const transport = nodemailer.createTransport({
  host: import.meta.env.SMTP_HOST,
  port: Number(import.meta.env.SMTP_PORT) || 465,
  secure: (Number(import.meta.env.SMTP_PORT) || 465) === 465,
  auth: {
    user: import.meta.env.SMTP_USER,
    pass: import.meta.env.SMTP_PASS,
  },
});

interface MailOptions {
  to: string;
  subject: string;
  html: string;
  replyTo?: string;
}

export async function sendMail({ to, subject, html, replyTo }: MailOptions) {
  return transport.sendMail({
    from: import.meta.env.SMTP_FROM || 'Hinzke Digital <noreply@hinzke.de>',
    to,
    subject,
    html,
    ...(replyTo && { replyTo }),
  });
}
