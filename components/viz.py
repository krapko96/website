import importlib
from pathlib import Path

VIZ_DIR = Path(__file__).parent.parent / "visualizations"
RENDERED_DIR = VIZ_DIR / "_rendered"


def render_visualization(viz_name):
    """Import a visualization module and call its render() function."""
    module = importlib.import_module(f"visualizations.{viz_name}")
    return module.render()


def render_all():
    """Pre-render all visualization modules to _rendered/ directory."""
    RENDERED_DIR.mkdir(parents=True, exist_ok=True)
    viz_files = [f for f in VIZ_DIR.glob("*.py") if f.name != "__init__.py"]
    rendered = []
    for viz_file in viz_files:
        viz_name = viz_file.stem
        try:
            html = render_visualization(viz_name)
            output_path = RENDERED_DIR / f"{viz_name}.html"
            output_path.write_text(html)
            rendered.append(viz_name)
            print(f"  Rendered: {viz_name}")
        except Exception as e:
            print(f"  Error rendering {viz_name}: {e}")
    return rendered
