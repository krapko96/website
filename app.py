from fasthtml.common import *

from components.layout import page
from components.blog import load_posts, get_post, blog_list_page, blog_post_page
from components.projects import load_projects, projects_page

app, rt = fast_app(
    live=True,
    hdrs=(
        Link(rel="stylesheet", href="/static/css/style.css"),
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        Link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;600;700&display=swap",
        ),
    ),
    pico=False,
)

app.static_route_exts(prefix="/static/", static_path="static")


# ── Home ────────────────────────────────────────────────────────────────────────


@rt("/")
def get():
    posts = load_posts()[:3]
    recent_items = []
    for p in posts:
        recent_items.append(
            A(
                Span("→ ", cls="arrow"),
                f"blog/{p['slug']}.md",
                href=f"/blog/{p['slug']}",
                cls="terminal-link",
            )
        )

    terminal = Div(
        Div(
            Div(
                Span(cls="dot dot-red"),
                Span(cls="dot dot-yellow"),
                Span(cls="dot dot-green"),
                cls="terminal-dots",
            ),
            Span("kenrapko — bash", cls="terminal-title"),
            cls="terminal-header",
        ),
        Div(
            Div(
                Span("$ ", cls="prompt"),
                Span("whoami", cls="cmd"),
                cls="terminal-line",
            ),
            Div(
                P("Ken Rapko — Sr. AI/ML Engineer", cls="terminal-output name-output"),
                cls="terminal-response",
            ),
            Div(
                Span("$ ", cls="prompt"),
                Span("cat interests.txt", cls="cmd"),
                cls="terminal-line",
            ),
            Div(
                P(
                    "prediction markets · computer vision · ML systems",
                    Br(),
                    "sports analytics · counter-factual reasoning",
                    cls="terminal-output",
                ),
                cls="terminal-response",
            ),
            Div(
                Span("$ ", cls="prompt"),
                Span("ls ./recent", cls="cmd"),
                cls="terminal-line",
            ),
            Div(
                *recent_items,
                cls="terminal-response recent-links",
            ),
            Div(
                Span("$ ", cls="prompt"),
                Span("_", cls="cursor"),
                cls="terminal-line",
            ),
            cls="terminal-body",
        ),
        cls="terminal",
    )

    return page("Ken Rapko", terminal)


# ── Blog ────────────────────────────────────────────────────────────────────────


@rt("/blog")
def get(tag: str = None):
    posts = load_posts()
    return page("Blog", *blog_list_page(posts, active_tag=tag))


@rt("/blog/{slug}")
def get(slug: str):
    post = get_post(slug)
    if not post:
        return page("Not Found", H1("Post not found"), P("Sorry, that post doesn't exist."))
    return page(post["title"], *blog_post_page(post))


# ── Projects ────────────────────────────────────────────────────────────────────


@rt("/projects")
def get():
    projects = load_projects()
    return page("Projects", *projects_page(projects))


# ── About ───────────────────────────────────────────────────────────────────────


@rt("/about")
def get():
    timeline = Div(
        Div(
            Div(
                Span("2014", cls="timeline-year"),
                Div(
                    H4("Virginia Tech"),
                    P("BS Mechanical Engineering — Robotics focus"),
                    cls="timeline-content",
                ),
                cls="timeline-item",
            ),
            Div(
                Span("2016", cls="timeline-year"),
                Div(
                    H4("Lockheed Martin"),
                    P("Computer Vision & ML R&D"),
                    cls="timeline-content",
                ),
                cls="timeline-item",
            ),
            Div(
                Span("2020", cls="timeline-year"),
                Div(
                    H4("Georgia Tech"),
                    P("MS Computational Perception & Robotics"),
                    cls="timeline-content",
                ),
                cls="timeline-item",
            ),
            Div(
                Span("2021", cls="timeline-year"),
                Div(
                    H4("Nike"),
                    P("Sr. AI/ML Engineer — ML systems at scale"),
                    cls="timeline-content",
                ),
                cls="timeline-item",
            ),
            Div(
                Span("Now", cls="timeline-year"),
                Div(
                    H4("What's next"),
                    P("Building, writing, exploring."),
                    cls="timeline-content",
                ),
                cls="timeline-item",
            ),
            cls="timeline",
        ),
        cls="timeline-wrapper",
    )

    return page(
        "About",
        Section(
            H1("About", cls="page-title"),
            Div(
                P(
                    "I'm Ken — a senior AI/ML engineer with a background that zigs where "
                    "others zag. I started in mechanical engineering, moved into computer "
                    "vision and robotics at Lockheed Martin, got a master's at Georgia Tech "
                    "in computational perception, and now build ML systems at scale."
                ),
                P(
                    "I'm interested in the places where rigorous engineering meets messy "
                    "real-world problems: prediction markets, sports analytics, "
                    "counter-factual reasoning, and making ML systems that actually work "
                    "in production."
                ),
                P(
                    "I built this site because I wanted a place to write long-form about "
                    "the things I'm learning — with real data, interactive visualizations, "
                    "and actual code. No hot takes, no threads. Just thoughtful analysis."
                ),
                cls="prose",
            ),
            H2("Career Timeline", cls="section-title"),
            timeline,
            H2("Get in touch", cls="section-title"),
            Div(
                P(
                    A("GitHub", href="https://github.com/kenrapko", target="_blank"),
                    " · ",
                    A("LinkedIn", href="https://linkedin.com/in/kenrapko", target="_blank"),
                    " · ",
                    A("Email", href="mailto:ken@kenrapko.dev"),
                ),
                cls="contact-links",
            ),
            cls="about-section",
        ),
    )


# ── Run ─────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    serve(port=5001)
