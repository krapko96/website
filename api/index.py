import sys
from pathlib import Path

# Ensure the project root is on the path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import app

# Vercel expects a handler; FastHTML exposes an ASGI app
handler = app
