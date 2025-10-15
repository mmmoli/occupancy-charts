from typing import Literal

Language = Literal["en", "th"]

_translations = {
    "en": {
        "title": "🏠 Occupancy Rate Simulator",
        "caption": "Explore how small improvements in occupancy impact annual revenue.",
        "params_header": "Simulation Parameters",
        "results_header": "Results",
        "flats": "Number of flats",
        "rent": "Monthly rent per flat (£)",
        "turnover": "Average days vacant per turnover",
        "churn": "Tenant churn rate (%)",
        "effective_occ": "Effective Occupancy",
        "void_days": "Void Days per Year",
        "revenue": "Annual Revenue",
    },
    "th": {
        "title": "🏠 เครื่องจำลองอัตราการเข้าพัก",
        "caption": "สำรวจว่าการเพิ่มอัตราการเข้าพักเพียงเล็กน้อยส่งผลต่อรายได้ต่อปีอย่างไร",
        "params_header": "ตั้งค่าการจำลอง",
        "results_header": "ผลลัพธ์",
        "flats": "จำนวนยูนิต",
        "rent": "ค่าเช่าต่อเดือน (บาท)",
        "turnover": "จำนวนวันที่ว่างต่อการเปลี่ยนผู้เช่า",
        "churn": "อัตราการเปลี่ยนผู้เช่า (%)",
        # missing some keys intentionally to demonstrate fallback
    },
}


def t(key: str, lang: Language = "en") -> str:
    """
    Translate a key for the selected language.
    Falls back to English or a readable placeholder if missing.
    """
    if key in _translations.get(lang, {}):
        return _translations[lang][key]
    elif key in _translations["en"]:
        # fallback to English
        return _translations["en"][key]
    else:
        # fallback placeholder for missing keys
        return f"[{key}]"
