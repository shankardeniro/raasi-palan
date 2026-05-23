"""
Transit computation core for Tamil Raasi Palan.

Uses Swiss Ephemeris (pyswisseph) with Lahiri ayanamsa to compute
sidereal planetary positions. For each of the 12 raasis (moon signs),
calculates which house (1-12) each planet currently transits.
"""

import swisseph as swe
from datetime import date, datetime
from typing import Optional

RAASI_NAMES = [
    "Mesha",      # Aries
    "Rishabha",   # Taurus
    "Mithuna",    # Gemini
    "Kataka",     # Cancer
    "Simha",      # Leo
    "Kanni",      # Virgo
    "Thulam",     # Libra
    "Viruchigam", # Scorpio
    "Dhanus",     # Sagittarius
    "Makara",     # Capricorn
    "Kumbha",     # Aquarius
    "Meena",      # Pisces
]

RAASI_NAMES_TAMIL = [
    "மேஷம்",
    "ரிஷபம்",
    "மிதுனம்",
    "கடகம்",
    "சிம்மம்",
    "கன்னி",
    "துலாம்",
    "விருச்சிகம்",
    "தனுசு",
    "மகரம்",
    "கும்பம்",
    "மீனம்",
]

PLANETS = [
    {"id": swe.SUN,     "name": "Sun",     "name_ta": "சூரியன்"},
    {"id": swe.MOON,    "name": "Moon",    "name_ta": "சந்திரன்"},
    {"id": swe.MARS,    "name": "Mars",    "name_ta": "செவ்வாய்"},
    {"id": swe.MERCURY, "name": "Mercury", "name_ta": "புதன்"},
    {"id": swe.JUPITER, "name": "Jupiter", "name_ta": "குரு"},
    {"id": swe.VENUS,   "name": "Venus",   "name_ta": "சுக்கிரன்"},
    {"id": swe.SATURN,  "name": "Saturn",  "name_ta": "சனி"},
]

NODES = [
    {"id": swe.MEAN_NODE, "name": "Rahu",  "name_ta": "ராகு"},
    {"id": swe.MEAN_NODE, "name": "Ketu",  "name_ta": "கேது", "is_ketu": True},
]


def _date_to_jd(d: date) -> float:
    # 0:00 UT = 5:30 AM IST, close to Indian sunrise — our daily reference point
    return swe.julday(d.year, d.month, d.day, 0.0)


def _sidereal_longitude(planet_id: int, jd: float, is_ketu: bool = False) -> float:
    """
    Get sidereal longitude of a planet using Lahiri ayanamsa.
    For Ketu, we add 180° to Rahu's position (they are always opposite).
    """
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    flags = swe.FLG_SIDEREAL | swe.FLG_SPEED
    result, _ = swe.calc_ut(jd, planet_id, flags)
    longitude = result[0]
    if is_ketu:
        longitude = (longitude + 180.0) % 360.0
    return longitude


def _longitude_to_raasi_index(longitude: float) -> int:
    """Convert sidereal longitude (0-360) to raasi index (0-11)."""
    return int(longitude / 30.0) % 12


def _house_from_moon(planet_raasi_index: int, moon_sign_index: int) -> int:
    """
    Calculate which house (1-12) a planet occupies, counted from the moon sign.
    Moon sign itself = house 1, next sign = house 2, etc.
    """
    return ((planet_raasi_index - moon_sign_index) % 12) + 1


def get_planet_positions(d: Optional[date] = None) -> list[dict]:
    """
    For a given date, return each planet's sidereal longitude, degree within
    its sign, and which raasi it occupies.

    Returns a list like:
    [
        {"name": "Sun", "name_ta": "சூரியன்", "longitude": 37.5,
         "raasi_index": 1, "raasi": "Rishabha", "raasi_ta": "ரிஷபம்",
         "degree_in_sign": 7.5},
        ...
    ]
    """
    if d is None:
        d = date.today()
    jd = _date_to_jd(d)

    positions = []
    for planet in PLANETS + NODES:
        is_ketu = planet.get("is_ketu", False)
        lng = _sidereal_longitude(planet["id"], jd, is_ketu=is_ketu)
        raasi_idx = _longitude_to_raasi_index(lng)
        positions.append({
            "name": planet["name"],
            "name_ta": planet["name_ta"],
            "longitude": round(lng, 4),
            "raasi_index": raasi_idx,
            "raasi": RAASI_NAMES[raasi_idx],
            "raasi_ta": RAASI_NAMES_TAMIL[raasi_idx],
            "degree_in_sign": round(lng % 30.0, 4),
        })
    return positions


def get_transit_report(d: Optional[date] = None) -> dict:
    """
    Main function: for a given date, compute the full transit report.

    Returns:
    {
        "date": "2026-05-22",
        "planet_positions": [ ... ],   # where each planet is today
        "raasi_readings": {
            0: {  # Mesha
                "raasi": "Mesha", "raasi_ta": "மேஷம்",
                "transits": [
                    {"planet": "Sun", "planet_ta": "சூரியன்",
                     "house": 2, "raasi_of_planet": "Rishabha"},
                    ...
                ],
                "saturn_status": None or "Ashtama Sani" or "Sade Sati" or "Kantaka Sani"
            },
            ...
        }
    }
    """
    if d is None:
        d = date.today()

    positions = get_planet_positions(d)

    raasi_readings = {}
    for moon_idx in range(12):
        transits = []
        saturn_house = None

        for pos in positions:
            house = _house_from_moon(pos["raasi_index"], moon_idx)
            transits.append({
                "planet": pos["name"],
                "planet_ta": pos["name_ta"],
                "house": house,
                "raasi_of_planet": pos["raasi"],
                "raasi_of_planet_ta": pos["raasi_ta"],
            })
            if pos["name"] == "Saturn":
                saturn_house = house

        saturn_status = None
        saturn_status_ta = None
        if saturn_house == 8:
            saturn_status = "Ashtama Sani"
            saturn_status_ta = "அஷ்டம சனி"
        elif saturn_house in (12, 1, 2):
            saturn_status = "Sade Sati"
            saturn_status_ta = "சனிப்பெயர்ச்சி (ஏழரை சனி)"
        elif saturn_house == 4:
            saturn_status = "Kantaka Sani"
            saturn_status_ta = "கண்டக சனி"

        raasi_readings[moon_idx] = {
            "raasi": RAASI_NAMES[moon_idx],
            "raasi_ta": RAASI_NAMES_TAMIL[moon_idx],
            "transits": transits,
            "saturn_status": saturn_status,
            "saturn_status_ta": saturn_status_ta,
        }

    return {
        "date": d.isoformat(),
        "planet_positions": positions,
        "raasi_readings": raasi_readings,
    }


if __name__ == "__main__":
    import json
    report = get_transit_report()
    print(json.dumps(report, indent=2, ensure_ascii=False))
