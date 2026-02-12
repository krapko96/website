from fasthtml.common import *


def page_head(title="Ken Rapko"):
    return Head(
        Meta(charset="utf-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1"),
        Meta(name="description", content="Ken Rapko - Sr. AI/ML Engineer. Blog, projects, and thoughts on ML systems, prediction markets, and computer vision."),
        Meta(property="og:title", content=title),
        Meta(property="og:type", content="website"),
        Meta(property="og:description", content="Sr. AI/ML Engineer - ML systems, prediction markets, computer vision"),
        Link(rel="stylesheet", href="/static/css/style.css"),
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;600;700&display=swap"),
        Title(title),
    )


def nav():
    return Nav(
        Div(
            A("~/kenrapko", href="/", cls="nav-logo"),
            Div(
                A("blog", href="/blog", cls="nav-link"),
                A("projects", href="/projects", cls="nav-link"),
                A("about", href="/about", cls="nav-link"),
                cls="nav-links",
            ),
            cls="nav-inner",
        ),
        cls="site-nav",
    )


def footer():
    return Footer(
        Div(
            P(
                "Built with ",
                A("FastHTML", href="https://fastht.ml", target="_blank"),
                " + Python. No JavaScript frameworks were harmed.",
            ),
            P(
                A("GitHub", href="https://github.com/kenrapko", target="_blank"),
                " · ",
                A("LinkedIn", href="https://linkedin.com/in/kenrapko", target="_blank"),
                " · ",
                A("Email", href="mailto:ken@kenrapko.dev"),
            ),
            cls="footer-inner",
        ),
        cls="site-footer",
    )


def page(title, *content):
    return Html(
        page_head(title=f"{title} — Ken Rapko" if title != "Ken Rapko" else title),
        Body(
            nav(),
            Main(*content, cls="content"),
            footer(),
        ),
        lang="en",
    )
