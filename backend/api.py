"""
FastAPI server for Tamil Raasi Palan.

Endpoints:
  GET /api/reading/{raasi_index}?lang=en    — single raasi reading
  GET /api/readings?lang=en                 — all 12 raasi readings
  GET /api/positions                        — raw planetary positions (for debugging)
  GET /api/raasis                           — list of all 12 raasis with names

In production, also serves the built React frontend.
"""

from pathlib import Path

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from transit import get_planet_positions, RAASI_NAMES, RAASI_NAMES_TAMIL
from interpret import get_daily_reading, get_all_readings

app = FastAPI(title="Tamil Raasi Palan", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


# ── API routes ──

@app.get("/api/raasis")
def list_raasis():
    """Return all 12 raasis with English and Tamil names."""
    return [
        {"index": i, "name": RAASI_NAMES[i], "name_ta": RAASI_NAMES_TAMIL[i]}
        for i in range(12)
    ]


@app.get("/api/reading/{raasi_index}")
def single_reading(raasi_index: int, lang: str = Query("en", regex="^(en|ta)$")):
    """Return today's reading for a single raasi."""
    if raasi_index < 0 or raasi_index > 11:
        return {"error": "raasi_index must be 0-11"}
    return get_daily_reading(raasi_index, lang)


@app.get("/api/readings")
def all_readings(lang: str = Query("en", regex="^(en|ta)$")):
    """Return today's readings for all 12 raasis."""
    return get_all_readings(lang)


@app.get("/api/positions")
def positions():
    """Return raw planetary positions (useful for verification)."""
    return get_planet_positions()


# ── Serve frontend build in production ──

_DIST = Path(__file__).parent.parent / "frontend" / "dist"

if _DIST.exists():
    app.mount("/assets", StaticFiles(directory=_DIST / "assets"), name="assets")

    @app.get("/{full_path:path}")
    def serve_frontend(full_path: str):
        """SPA fallback — serve static files or index.html."""
        file_path = _DIST / full_path
        if full_path and file_path.exists() and file_path.is_file():
            return FileResponse(file_path)
        return FileResponse(_DIST / "index.html")
