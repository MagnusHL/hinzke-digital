import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import node from '@astrojs/node';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://hinzke.digital',
  security: { checkOrigin: false },
  image: {
    service: { entrypoint: 'astro/assets/services/sharp' },
  },
  adapter: node({ mode: 'standalone' }),
  integrations: [
    tailwind(),
    sitemap({
      customPages: ['https://hinzke.digital/kontakt/'],
      filter: (page) => !page.includes('/danke'),
    }),
  ],
});
