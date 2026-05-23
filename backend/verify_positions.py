"""
Verification script: prints today's planetary positions in a clear table
so you can compare against a published Tamil Panchangam or astrology site.
"""

from datetime import date
from transit import get_planet_positions, RAASI_NAMES

def print_positions(d=None):
    if d is None:
        d = date.today()

    positions = get_planet_positions(d)

    print(f"{'='*65}")
    print(f"  PLANETARY POSITIONS — {d.strftime('%A, %d %B %Y')}")
    print(f"  Ayanamsa: Lahiri (Chitrapaksha) | Sidereal / Nirayana")
    print(f"{'='*65}")
    print(f"  {'Planet':<12} {'Raasi (Sign)':<18} {'Degree':<12} {'Tamil'}")
    print(f"  {'-'*10:<12} {'-'*16:<18} {'-'*10:<12} {'-'*10}")

    for p in positions:
        deg = p['degree_in_sign']
        deg_d = int(deg)
        deg_m = int((deg - deg_d) * 60)
        deg_s = int(((deg - deg_d) * 60 - deg_m) * 60)
        dms = f"{deg_d}°{deg_m:02d}'{deg_s:02d}\""

        print(f"  {p['name']:<12} {p['raasi']:<18} {dms:<12} {p['raasi_ta']}")

    print(f"{'='*65}")
    print()

    print("  SATURN SPECIAL TRANSITS:")
    print(f"  Saturn is in {positions[6]['raasi']} ({positions[6]['raasi_ta']})")
    print()

    saturn_idx = positions[6]['raasi_index']
    specials = []
    for i in range(12):
        house = ((saturn_idx - i) % 12) + 1
        if house == 8:
            specials.append(f"    {RAASI_NAMES[i]:>12} — Ashtama Sani (Saturn in 8th house)")
        elif house in (12, 1, 2):
            phase = {12: "entering", 1: "peak", 2: "departing"}[house]
            specials.append(f"    {RAASI_NAMES[i]:>12} — Sade Sati ({phase} phase, Saturn in house {house})")
        elif house == 4:
            specials.append(f"    {RAASI_NAMES[i]:>12} — Kantaka Sani (Saturn in 4th house)")

    for s in specials:
        print(s)
    print()


if __name__ == "__main__":
    print_positions()
