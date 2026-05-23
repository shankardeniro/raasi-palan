"""
Interpretation layer: connects transit positions to human-readable readings.

Loads interpretations from the editable JSON file and produces a flowing
narrative daily reading for any raasi.
"""

import json
import math
from pathlib import Path
from datetime import date
from typing import Optional

from transit import get_transit_report, RAASI_NAMES, RAASI_NAMES_TAMIL

_INTERP_PATH = Path(__file__).parent / "interpretations.json"

# Transition phrases to weave effects into a flowing narrative
_TRANSITIONS_EN = {
    "good_open": [
        "Today brings encouraging signs. ",
        "The day opens with promise. ",
        "Positive currents are at work today. ",
    ],
    "good_join": [" ", " Additionally, ", " Meanwhile, "],
    "pivot": [
        " However, some caution is also warranted. ",
        " That said, the day also calls for mindfulness. ",
        " At the same time, there are areas needing care. ",
    ],
    "bad_join": [" ", " Also, ", " Furthermore, "],
    "bad_open": [
        "The day calls for patience and caution. ",
        "Today requires a careful and measured approach. ",
        "Mindfulness is the watchword for the day. ",
    ],
    "close_good": [
        " Overall, a day that leans in your favour.",
        " On balance, the day holds more promise than challenge.",
    ],
    "close_mixed": [
        " A balanced day overall. Stay aware and make the most of what flows well.",
        " Navigate with awareness, and the day will serve you well.",
    ],
    "close_bad": [
        " A testing day, but patience and spiritual grounding will carry you through.",
        " Focus on what you can control, and let the rest pass.",
    ],
}

_TRANSITIONS_TA = {
    "good_open": [
        "இன்று ஊக்கமளிக்கும் அறிகுறிகள் தென்படுகின்றன. ",
        "நாள் நல்ல நம்பிக்கையுடன் தொடங்குகிறது. ",
        "இன்று நேர்மறையான ஓட்டங்கள் செயல்படுகின்றன. ",
    ],
    "good_join": [" ", " மேலும், ", " அதே நேரத்தில், "],
    "pivot": [
        " இருப்பினும், சில விஷயங்களில் எச்சரிக்கையும் தேவை. ",
        " அதே சமயம், கவனம் தேவைப்படும் விஷயங்களும் உள்ளன. ",
        " ஆனால், சில விஷயங்களில் கவனமாக இருக்க வேண்டும். ",
    ],
    "bad_join": [" ", " மேலும், ", " அத்துடன், "],
    "bad_open": [
        "இன்று பொறுமையும் எச்சரிக்கையும் தேவைப்படும் நாள். ",
        "இன்று கவனமான மற்றும் அளவான அணுகுமுறை தேவை. ",
        "இன்றைய நாளுக்கு விழிப்புணர்வே முக்கியம். ",
    ],
    "close_good": [
        " மொத்தத்தில், உங்களுக்கு சாதகமான நாள்.",
        " ஒட்டுமொத்தமாக, சவாலை விட நம்பிக்கை அதிகம் உள்ள நாள்.",
    ],
    "close_mixed": [
        " சமநிலையான நாள். விழிப்புடன் இருந்து நல்லவற்றைப் பயன்படுத்துங்கள்.",
        " விழிப்புடன் நகருங்கள், நாள் உங்களுக்கு நன்றாக அமையும்.",
    ],
    "close_bad": [
        " சோதனையான நாள், ஆனால் பொறுமையும் ஆன்மீக உறுதியும் உங்களைக் கரை சேர்க்கும்.",
        " உங்களால் கட்டுப்படுத்த முடிவதில் கவனம் செலுத்துங்கள், மற்றவற்றை கடந்து செல்ல விடுங்கள்.",
    ],
}


def _load_interpretations() -> dict:
    with open(_INTERP_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {k: v for k, v in data.items() if k != "_meta"}


def _pick(lst, seed):
    """Deterministic pick from a list based on a seed (so same date = same text)."""
    return lst[seed % len(lst)]


def _fit_case(effect, preceding, lang):
    """Lowercase first char only when English effect follows a comma-joiner."""
    if lang != "en" or not effect:
        return effect
    if preceding.endswith(", "):
        return effect[0].lower() + effect[1:]
    return effect


def get_daily_reading(raasi_index: int, lang: str = "en", d: Optional[date] = None) -> dict:
    """
    Produce a complete daily reading as a single flowing narrative.

    Returns:
        {
            "date": "2026-05-23",
            "raasi": "Mesha" or "மேஷம்",
            "raasi_index": 0,
            "score": 5,           # 1-10
            "saturn_status": ...,
            "narrative": "Today brings encouraging signs. ..."
        }
    """
    if d is None:
        d = date.today()

    report = get_transit_report(d)
    interp = _load_interpretations()
    raasi_data = report["raasi_readings"][raasi_index]

    # Gather effects
    good_effects = []
    bad_effects = []
    effect_key = f"effect_{lang}"

    for transit in raasi_data["transits"]:
        planet_name = transit["planet"]
        house = transit["house"]
        planet_interp = interp.get(planet_name, {}).get(str(house), {})
        tendency = planet_interp.get("tendency", "neutral")
        effect = planet_interp.get(effect_key, "")

        if not effect:
            continue

        if tendency == "favourable":
            good_effects.append(effect)
        else:
            bad_effects.append(effect)

    # Score: 1-10 based on ratio, with slight weighting
    total = len(good_effects) + len(bad_effects)
    if total == 0:
        score = 5
    else:
        raw = good_effects.__len__() / total
        score = max(1, min(10, round(raw * 9) + 1))

    # Seed for deterministic transition picks (same raasi + date = same narrative)
    seed = raasi_index + d.toordinal()
    tr = _TRANSITIONS_TA if lang == "ta" else _TRANSITIONS_EN

    # Compose narrative
    parts = []

    if good_effects and bad_effects:
        # Mixed day: good → pivot → challenging → close
        opener = _pick(tr["good_open"], seed)
        parts.append(opener)
        prev = opener
        for i, eff in enumerate(good_effects):
            if i > 0:
                joiner = _pick(tr["good_join"], seed + i)
                parts.append(joiner)
                prev = joiner
            parts.append(_fit_case(eff, prev, lang))
        pivot = _pick(tr["pivot"], seed + 10)
        parts.append(pivot)
        prev = pivot
        for i, eff in enumerate(bad_effects):
            if i > 0:
                joiner = _pick(tr["bad_join"], seed + 20 + i)
                parts.append(joiner)
                prev = joiner
            parts.append(_fit_case(eff, prev, lang))
        if score >= 6:
            parts.append(_pick(tr["close_good"], seed + 30))
        elif score >= 4:
            parts.append(_pick(tr["close_mixed"], seed + 30))
        else:
            parts.append(_pick(tr["close_bad"], seed + 30))

    elif good_effects:
        # All good
        opener = _pick(tr["good_open"], seed)
        parts.append(opener)
        prev = opener
        for i, eff in enumerate(good_effects):
            if i > 0:
                joiner = _pick(tr["good_join"], seed + i)
                parts.append(joiner)
                prev = joiner
            parts.append(_fit_case(eff, prev, lang))
        parts.append(_pick(tr["close_good"], seed + 30))

    else:
        # All challenging
        opener = _pick(tr["bad_open"], seed)
        parts.append(opener)
        prev = opener
        for i, eff in enumerate(bad_effects):
            if i > 0:
                joiner = _pick(tr["bad_join"], seed + 20 + i)
                parts.append(joiner)
                prev = joiner
            parts.append(_fit_case(eff, prev, lang))
        parts.append(_pick(tr["close_bad"], seed + 30))

    narrative = "".join(parts)

    # Short witty verdict phrase
    _VERDICTS_EN = {
        10: "Universe rolled out the red carpet",
        9: "Stars are basically flirting with you",
        8: "Green lights everywhere",
        7: "The cosmos approves",
        6: "One eye open, one eye winking",
        5: "The universe shrugged",
        4: "Maybe don't sign anything today",
        3: "Netflix and stay home",
        2: "Even your coffee will judge you",
        1: "Mercury called, it's personal",
    }
    _VERDICTS_TA = {
        10: "பிரபஞ்சமே சிவப்புக் கம்பளம் விரித்தது",
        9: "நட்சத்திரங்கள் உங்களுக்காகவே ஜொலிக்கின்றன",
        8: "எல்லா பச்சை விளக்கும் உங்களுக்கே",
        7: "கிரகங்கள் தலையாட்டுகின்றன",
        6: "ஒரு கண் திறந்து, ஒரு கண் சிமிட்டி",
        5: "பிரபஞ்சம் தோள் குலுக்கியது",
        4: "இன்று கையெழுத்து போடாதீர்கள்",
        3: "வீட்டிலேயே இருங்கள், பரவாயில்லை",
        2: "காபி கூட உங்களை முறைக்கும்",
        1: "கிரகங்கள் தனிப்பட்ட விரோதம் வைத்துள்ளன",
    }

    verdict = (_VERDICTS_TA if lang == "ta" else _VERDICTS_EN).get(score, "")

    return {
        "date": report["date"],
        "raasi": raasi_data["raasi_ta"] if lang == "ta" else raasi_data["raasi"],
        "raasi_index": raasi_index,
        "score": score,
        "verdict": verdict,
        "narrative": narrative,
    }


def get_all_readings(lang: str = "en", d: Optional[date] = None) -> list[dict]:
    """Get daily readings for all 12 raasis."""
    return [get_daily_reading(i, lang, d) for i in range(12)]


if __name__ == "__main__":
    reading = get_daily_reading(0, "en")
    print(f"{'=' * 70}")
    print(f"  {reading['raasi']} — Score: {reading['score']}/10")
    print(f"  {reading['date']}")
    if reading["saturn_status"]:
        print(f"  ⚠ {reading['saturn_status']}")
    print(f"{'=' * 70}")
    print()
    print(f"  {reading['narrative']}")
    print()

    reading_ta = get_daily_reading(0, "ta")
    print(f"{'=' * 70}")
    print(f"  {reading_ta['raasi']} — மதிப்பெண்: {reading_ta['score']}/10")
    print(f"{'=' * 70}")
    print()
    print(f"  {reading_ta['narrative']}")
