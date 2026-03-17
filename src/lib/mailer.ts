import nodemailer from 'nodemailer';

const transport = nodemailer.createTransport({
  host: process.env.SMTP_HOST,
  port: Number(process.env.SMTP_PORT) || 465,
  secure: (Number(process.env.SMTP_PORT) || 465) === 465,
  auth: {
    user: process.env.SMTP_USER,
    pass: process.env.SMTP_PASS,
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
    from: process.env.SMTP_FROM || 'Hinzke Digital <noreply@hinzke.de>',
    to,
    subject,
    html,
    ...(replyTo && { replyTo }),
  });
}
