import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const module = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/module' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    icon: z.string(),
    techStack: z.array(z.string()),
    benefits: z.array(z.string()),
    useCases: z.array(z.string()),
    order: z.number(),
  }),
});

export const collections = { module };
