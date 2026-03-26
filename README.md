# Hinzke Digital

Website for digital products and consulting by [Magnus Hinzke](https://hinzke.digital/ueber-mich) -- websites, AI modules, and automation for SMBs.

**Live:** [hinzke.digital](https://hinzke.digital)

## What This Is

A business website selling two product categories:

- **Website Packages** -- Three tiers (Web Start / Web Business / Web Pro) for SMBs that need a professional web presence with SEO and AI optimization
- **Digital Modules** -- 16 consulting products covering AI chatbots, automation, CRM integration, newsletter systems, and more -- each with its own product page
- **Hosting Packages** -- Managed WordPress hosting with optional maintenance

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | [Astro 5](https://astro.build) (Hybrid -- static pages + server API routes) |
| Styling | [Tailwind CSS](https://tailwindcss.com) with Typography plugin |
| Payments | [Stripe](https://stripe.com) Checkout Sessions + Webhooks |
| Email | SMTP via [Nodemailer](https://nodemailer.com) |
| Analytics | [Matomo](https://matomo.org) (self-hosted, GDPR-compliant) |
| Hosting | [Dokploy](https://dokploy.com) on Hetzner VPS |
| Content | Markdown-based Content Collections (modules + blog) |

## Project Structure

```
src/
├── content/
│   ├── module/          # 16 digital modules (Markdown + Zod schema)
│   └── blog/            # Blog posts (Markdown)
├── pages/
│   ├── index.astro      # Landing page
│   ├── webseiten.astro  # Website packages + hosting
│   ├── module/          # Module overview + dynamic detail pages
│   ├── blog/            # Blog overview + dynamic posts
│   ├── kontakt.astro    # Contact form
│   ├── ueber-mich.astro # About page + tech stack grid
│   ├── rss.xml.ts       # RSS feed
│   └── api/             # Stripe checkout, webhooks, contact form
├── components/          # Astro components (cards, hero, CTA, etc.)
└── layouts/             # Base layout with SEO, Open Graph, structured data
```

## Getting Started

```bash
npm install
npm run dev          # http://localhost:4321
npm run build        # Production build
npm run preview      # Preview production build
```

Requires a `.env` file -- see `.env.example` for required variables.

## Architecture Decisions

- **Static-first**: All pages are pre-rendered at build time. Only `/api/*` routes run server-side
- **Content Collections**: Modules and blog posts are Markdown files with strict Zod schemas -- add a new `.md` file to publish a new page
- **No auth layer**: No user accounts, no stored user data -- minimal GDPR surface
- **Self-hosted stack**: Analytics (Matomo), newsletter (Listmonk), email validation (Reacher) -- no vendor lock-in
- **SEO + AIO**: Schema.org structured data, Open Graph, sitemaps, RSS feed, optimized for both search engines and AI assistants

## License

All rights reserved. This repository is public for transparency and portfolio purposes.
