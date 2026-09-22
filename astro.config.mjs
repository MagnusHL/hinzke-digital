import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import node from '@astrojs/node';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://hinzke.digital',
  trailingSlash: 'always',
  security: { checkOrigin: false },
  image: {
    service: { entrypoint: 'astro/assets/services/sharp' },
  },
  adapter: node({ mode: 'standalone' }),
  redirects: {
    // Case Study entfernt: nannte Preise und ein Buchungsmodell, das es nicht mehr gibt
    '/blog/buchbare-beratungswebsite-an-einem-tag/': '/projekte/hygiene-luebeck-de/',
  },
  integrations: [
    tailwind(),
    sitemap({
      customPages: ['https://hinzke.digital/kontakt/'],
      filter: (page) => !page.includes('/danke') && !page.includes('/blog/buchbare-beratungswebsite-an-einem-tag'),
      serialize: (item) => ({
        ...item,
        lastmod: new Date().toISOString(),
      }),
    }),
  ],
});
