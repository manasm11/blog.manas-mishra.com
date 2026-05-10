// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import { remarkMermaid } from './src/plugins/remark-mermaid.js';

export default defineConfig({
	site: 'https://blog.manas-mishra.com',
	output: 'static',
	integrations: [
		starlight({
			title: 'Manas Mishra',
			description: 'Random things I learn',
			social: [{ icon: 'youtube', label: 'YouTube', href: 'https://www.youtube.com/channel/UCcTM2rFfJbXiqTqYL7ts8Ew' }],
			sidebar: [
				{ label: 'Book Summaries', items: [{ autogenerate: { directory: 'book_summaries' } }] },
				{ label: 'Course Summaries', items: [{ autogenerate: { directory: 'course_summaries' } }] },
			],
			components: {
				Head: './src/components/overrides/Head.astro',
				Footer: './src/components/overrides/Footer.astro',
			},
			customCss: ['./src/styles/custom.css', 'katex/dist/katex.min.css'],
		}),
	],
	markdown: {
		remarkPlugins: [remarkMath, remarkMermaid],
		rehypePlugins: [rehypeKatex],
	},
});
