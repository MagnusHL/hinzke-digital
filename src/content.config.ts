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
      'target', 'trending-up', 'send', 'handshake', 'repeat',
    ]),
    techStack: z.array(z.string()),
    benefits: z.array(z.string()),
    useCases: z.array(z.string()).optional(),
    order: z.number(),
    relatedModules: z.array(z.string()).optional(),
    faq: z.array(z.object({ question: z.string(), answer: z.string() })).optional(),
    highlights: z.array(z.object({
      icon: z.string(),
      title: z.string(),
      text: z.string(),
    })).length(3),
    steps: z.array(z.object({
      title: z.string(),
      description: z.string(),
    })).min(3).max(4),
    problem: z.object({
      heading: z.string(),
      text: z.string(),
    }),
    solution: z.object({
      heading: z.string(),
      text: z.string(),
    }),
  }),
});

export const collections = { module };
