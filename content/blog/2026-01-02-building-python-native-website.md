---
title: "Building a Python-Native Personal Website (and Why I Didn't Use React)"
date: 2026-01-02
tags: [ml-systems, career]
description: "I'm an ML engineer, not a frontend developer. Here's how I built this site entirely in Python with FastHTML, and why that matters."
draft: false
---

When I decided to build a personal website, my first instinct was to reach for Next.js or Gatsby. That's what everyone uses, right? Markdown-based blog, React components, deploy to Vercel. Simple enough.

Then I remembered: I don't write JavaScript. Not professionally, not for fun, not at all if I can help it. My entire career is Python — PyTorch, scikit-learn, FastAPI, pandas. Why would I context-switch into an entirely different ecosystem just to build a blog?

## Enter FastHTML

FastHTML is a Python framework from the Answer.ai team (Jeremy Howard's shop) that lets you build full-stack web apps in pure Python. No templates, no Jinja, no JSX. You write Python functions that return HTML components.

```python
def blog_post(title, content):
    return Article(
        H1(title),
        Div(NotStr(content), cls="prose"),
    )
```

That's it. No build step, no transpilation, no `node_modules` directory eating your disk space.

## The Stack

Here's what powers this site:

- **FastHTML** for routing and page composition
- **python-markdown** for rendering blog posts from `.md` files
- **python-frontmatter** for parsing post metadata (title, date, tags)
- **Plotly** for interactive data visualizations
- **PicoCSS-inspired custom CSS** for styling
- **Vercel** for deployment via serverless Python functions

The entire site is about 500 lines of Python and 300 lines of CSS. No JavaScript was written in the making of this website.

## Why This Matters

As an ML engineer, my tools are Python. My mental models are Python. When I want to add a new feature — say, an interactive visualization of model performance — I don't want to learn D3.js. I want to write a Plotly figure in a Jupyter notebook, copy it into a `.py` file, and have it show up in my blog post.

That's exactly what this setup lets me do. My visualizations are version-controlled Python code that lives next to my prose. Push a data update, Vercel rebuilds, blog post updates. No friction.

## Tradeoffs

I'm not going to pretend this is the right choice for everyone:

- **Ecosystem maturity**: React/Next.js has thousands of components and plugins. FastHTML is newer and smaller.
- **Hiring**: If you're building a team product, JavaScript developers are easier to find.
- **Interactivity**: For complex client-side interactions, you'll eventually need some JavaScript. HTMX covers 90% of cases, but not all.

For a personal site and blog? Python all the way.
