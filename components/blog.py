import os
import math
from pathlib import Path

import frontmatter
import markdown
from pymdownx import superfences, highlight, inlinehilite
from fasthtml.common import *

BLOG_DIR = Path(__file__).parent.parent / "content" / "blog"
VIZ_RENDERED_DIR = Path(__file__).parent.parent / "visualizations" / "_rendered"


def _md_extensions():
    return [
        "pymdownx.superfences",
        "pymdownx.highlight",
        "pymdownx.inlinehilite",
        "tables",
        "footnotes",
        "toc",
        "smarty",
    ]


def _md_extension_configs():
    return {
        "pymdownx.highlight": {
            "use_pygments": True,
            "pygments_style": "monokai",
            "css_class": "highlight",
            "linenums": False,
        },
    }


def _reading_time(text):
    words = len(text.split())
    minutes = max(1, math.ceil(words / 250))
    return f"{minutes} min read"


def _inject_visualizations(html_content, viz_list):
    if not viz_list:
        return html_content
    for viz_name in viz_list:
        placeholder = f"{{{{viz:{viz_name}}}}}"
        rendered_path = VIZ_RENDERED_DIR / f"{viz_name}.html"
        if rendered_path.exists():
            viz_html = rendered_path.read_text()
            replacement = f'<div class="viz-container">{viz_html}</div>'
        else:
            replacement = f'<div class="viz-container viz-placeholder"><p>Visualization: {viz_name} (not yet rendered)</p></div>'
        html_content = html_content.replace(placeholder, replacement)
    return html_content


def load_posts():
    posts = []
    if not BLOG_DIR.exists():
        return posts
    for md_file in sorted(BLOG_DIR.glob("*.md"), reverse=True):
        post = frontmatter.load(md_file)
        if post.get("draft", False):
            continue
        posts.append({
            "title": post.get("title", "Untitled"),
            "date": str(post.get("date", "")),
            "tags": post.get("tags", []),
            "description": post.get("description", ""),
            "slug": md_file.stem,
            "reading_time": _reading_time(post.content),
            "content": post.content,
            "viz": post.get("viz", []),
        })
    return posts


def get_post(slug):
    md_file = BLOG_DIR / f"{slug}.md"
    if not md_file.exists():
        return None
    post = frontmatter.load(md_file)
    md_renderer = markdown.Markdown(
        extensions=_md_extensions(),
        extension_configs=_md_extension_configs(),
    )
    html_content = md_renderer.convert(post.content)
    viz_list = post.get("viz", [])
    html_content = _inject_visualizations(html_content, viz_list)
    return {
        "title": post.get("title", "Untitled"),
        "date": str(post.get("date", "")),
        "tags": post.get("tags", []),
        "description": post.get("description", ""),
        "slug": slug,
        "reading_time": _reading_time(post.content),
        "html": html_content,
        "viz": viz_list,
    }


def blog_list_page(posts, active_tag=None):
    if active_tag:
        posts = [p for p in posts if active_tag in p["tags"]]

    all_tags = sorted(set(tag for p in posts for tag in p["tags"]))
    tag_links = [
        A(
            tag,
            href=f"/blog?tag={tag}",
            cls=f"tag {'tag-active' if tag == active_tag else ''}",
        )
        for tag in all_tags
    ]
    if active_tag:
        tag_links.insert(0, A("all", href="/blog", cls="tag"))

    tag_bar = Div(*tag_links, cls="tag-bar") if tag_links else ""

    post_items = []
    for p in posts:
        tags = Span(*[Span(t, cls="post-tag") for t in p["tags"]], cls="post-tags")
        post_items.append(
            Article(
                A(H2(p["title"], cls="post-title"), href=f"/blog/{p['slug']}"),
                Div(
                    Span(p["date"], cls="post-date"),
                    Span(" · "),
                    Span(p["reading_time"], cls="post-reading-time"),
                    cls="post-meta",
                ),
                P(p["description"], cls="post-description"),
                tags,
                cls="post-card",
            )
        )

    if not post_items:
        post_items = [P("No posts yet. Check back soon.", cls="empty-state")]

    return (
        Section(
            H1("Blog", cls="page-title"),
            tag_bar,
            *post_items,
            cls="blog-list",
        ),
    )


def blog_post_page(post):
    if not post:
        return Section(H1("Post not found"), P("Sorry, that post doesn't exist."))

    tags = Span(*[Span(t, cls="post-tag") for t in post["tags"]], cls="post-tags")

    needs_katex = "\\(" in post["html"] or "\\[" in post["html"] or "$$" in post["html"]
    katex_includes = ()
    if needs_katex:
        katex_includes = (
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css"),
            Script(src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"),
            Script(src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"),
            Script("document.addEventListener('DOMContentLoaded',function(){renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}]})})"),
        )

    return (
        *katex_includes,
        Article(
            Header(
                A("← Back to blog", href="/blog", cls="back-link"),
                H1(post["title"], cls="post-title"),
                Div(
                    Span(post["date"], cls="post-date"),
                    Span(" · "),
                    Span(post["reading_time"], cls="post-reading-time"),
                    cls="post-meta",
                ),
                tags,
                cls="post-header",
            ),
            Div(NotStr(post["html"]), cls="prose"),
            cls="blog-post",
        ),
    )
