from pathlib import Path

import yaml
from fasthtml.common import *

PROJECTS_DIR = (Path(__file__).parent.parent / "content" / "projects").resolve()

STATUS_COLORS = {
    "active": "status-active",
    "published": "status-published",
    "archived": "status-archived",
}


def load_projects():
    projects = []
    if not PROJECTS_DIR.exists():
        return projects
    for yaml_file in sorted(PROJECTS_DIR.glob("*.yaml")):
        with open(yaml_file) as f:
            data = yaml.safe_load(f)
            if data:
                projects.append(data)
    return projects


def project_card(project):
    links = []
    if project.get("github"):
        links.append(A("GitHub", href=project["github"], target="_blank", cls="project-link"))
    if project.get("demo"):
        links.append(A("Demo", href=project["demo"], target="_blank", cls="project-link"))
    if project.get("paper"):
        links.append(A("Paper", href=project["paper"], target="_blank", cls="project-link"))
    if project.get("blog"):
        links.append(A("Blog Post", href=project["blog"], cls="project-link"))

    status = project.get("status", "active")
    status_cls = STATUS_COLORS.get(status, "status-active")

    tech_tags = [Span(t, cls="tech-tag") for t in project.get("tech", [])]

    return Article(
        Div(
            Span(status, cls=f"status-badge {status_cls}"),
            H3(project.get("name", "Untitled"), cls="project-name"),
            P(project.get("description", ""), cls="project-description"),
            Div(*tech_tags, cls="tech-tags") if tech_tags else "",
            Div(*links, cls="project-links") if links else "",
            cls="project-card-inner",
        ),
        cls="project-card",
    )


def projects_page(projects):
    cards = [project_card(p) for p in projects]
    if not cards:
        cards = [P("No projects yet.", cls="empty-state")]

    return (
        Section(
            H1("Projects", cls="page-title"),
            P("Things I've built, contributed to, or researched.", cls="page-subtitle"),
            Div(*cards, cls="projects-grid"),
            cls="projects-section",
        ),
    )
