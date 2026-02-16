import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const module = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/module' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    icon: z.enum([
      'message-circle', 'ticket', 'calendar', 'receipt', 'bar-chart-3',
      'mail', 'star', 'share-2', 'file-scan', 'clipboard-list',
      'target', 'trending-up', 'send', 'handshake',
    ]),
    techStack: z.array(z.string()),
    benefits: z.array(z.string()),
    useCases: z.array(z.string()),
    order: z.number(),
    relatedModules: z.array(z.string()).optional(),
    faq: z.array(z.object({ question: z.string(), answer: z.string() })).optional(),
  }),
});

export const collections = { module };
