"""Pre-render visualizations at build time.

Run during Vercel's buildCommand to generate static HTML for all
visualization modules. This avoids importing Plotly on every request.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from components.viz import render_all


def main():
    print("Building visualizations...")
    rendered = render_all()
    print(f"Done. Rendered {len(rendered)} visualization(s).")


if __name__ == "__main__":
    main()
