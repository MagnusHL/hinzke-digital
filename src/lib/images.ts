import type { ImageMetadata } from 'astro';

const moduleImages = import.meta.glob<{ default: ImageMetadata }>(
  '../assets/images/module/*.png',
  { eager: true }
);

export function getModuleImage(slug: string, type: 'problem' | 'solution'): ImageMetadata {
  const key = Object.keys(moduleImages).find(k => k.endsWith(`/${slug}-${type}.png`));
  if (!key) throw new Error(`Modul-Bild nicht gefunden: ${slug}-${type}.png`);
  return moduleImages[key].default;
}
