# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal learning blog (blog.manas-mishra.com) built with **Hugo** static site generator, using the **hugo-theme-relearn** theme (git submodule), deployed on **Firebase Hosting**.

## Commands

```bash
# Local development
hugo server                        # Preview at localhost:1313

# Build
hugo                               # Output to public/

# Clean build
rm -rf public/ resources/ && hugo

# Deploy (interactive: git commit + hugo build + firebase deploy)
./deploy.sh
```

There is no test suite or linter configured.

## Architecture

### Content Structure

All content is Markdown with **TOML frontmatter** (`+++` delimiters). Content lives in `content/` organized hierarchically:

- `content/book_summaries/` — Book summary notes
- `content/course_summaries/` — Course notes, can be nested (e.g., `course_summaries/acadamy_jun25_advance_by_scaler/dsa/`)
- `content/_index.md` — Homepage

Each directory with sub-pages has an `_index.md`. Page ordering uses `weight` in frontmatter. Set `math = true` in frontmatter to enable KaTeX rendering on a page.

### Theme Customization

Base theme is a git submodule at `themes/hugo-theme-relearn`. Customizations are in `layouts/` which override the theme:

- `layouts/partials/custom-header.html` — KaTeX math support
- `layouts/partials/custom-footer.html` — Firebase analytics
- `layouts/partials/custom-comments.html` — Giscus comments (GitHub Discussions)
- `layouts/partials/logo.html` — Custom site logo

### Custom Shortcodes (`layouts/shortcodes/`)

Key shortcodes used in content:
- `{{< listsubpages >}}` — Auto-generates child page cards
- `{{< showimage "id" "caption" "dims" >}}` — Lazy-loaded images with captions
- `{{< ytvideo "videoid" >}}` — Privacy-friendly YouTube embeds
- `{{< define "term" "definition" >}}` — Glossary definitions
- `{{< toc >}}` — Table of contents
- `{{% notice type %}}...{{% /notice %}}` — Alert boxes (note, info, tip, warning)

### Configuration

- `hugo.toml` — Main Hugo config (base URL, theme settings, output formats, menu)
- `firebase.json` — Firebase hosting config (serves from `public/`)
- `.firebaserc` — Firebase project: testweb-1122, site: my-first-hugo-22

### VS Code Snippets

`.vscode/hugo.code-snippets` provides quick-insert templates: `high` (code highlight), `image`, `note`, `shortcode`.

### Content Archetypes

`archetypes/` contains templates for new content pages (`default.md`, `chapter.md`). Use `hugo new` to create content from these.
