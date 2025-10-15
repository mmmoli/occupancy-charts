from typing import Literal

Language = Literal["en", "th"]

_translations = {
    "en": {
        "title": "🏠 Occupancy Rate Simulator",
        "caption": "Explore how small improvements in occupancy impact annual revenue.",
        "results_header": "Results",
        "flats": "Number of units",
        "rent": "Monthly rent per flat (£)",
        "delay_inspection": "Days to inspect",
        "delay_maintenance": "Days waiting for maintenance",
        "delay_repairs": "Days to complete repairs",
        "delay_new_tenant": "Days to find new tenant",
        "delay_viewing": "Days for tenant viewing",
        "delay_contract": "Days to sign contract",
        "churn": "Tenant churn rate (%)",
        "effective_occ": "Effective Occupancy",
        "void_days": "Void Days per Year",
        "revenue": "Annual Revenue",
        "building_name": "Building Name/Address",
        "currency_symbol": "£",
        "renews": "Total no. of contract renewals",
        "language_selector": "Select Language",
        "language_english": "English",
        "language_thai": "English",
        "notice_period": "Notice Period (months)",
        "contract_length": "Contract Length (months)",
        "sidebar_header_building": "Building Details",
        "sidebar_header_tenants": "Tenancies",
        "sidebar_building_name": "Building Name",
        "sidebar_rent_per_month": "Rent per month (avg. £)",
        "sidebar_header_delay": "Repairs",
        "sidebar_delay_find_new_tenant": "Days to find a new tenant",
        "sidebar_delay_viewing": "Days to book viewing",
        "sidebar_delay_contract": "Days to sign contract",
        "sidebar_header_moving_out": "Turnover",
        "sidebar_header_replace": "New Tenant",
        "financial_summary_header": "💸 Lost Cash",
        "metric_total_annual_loss": "per year",
        "total_span_loss": "Over 3 years",
        "detailed_metrics_header": "Breakdown",
        "chart_annual_revenue_distribution": "Total Revenue",
        "chart_annual_revenue_distribution_lost": "Lost",
        "chart_annual_revenue_distribution_retained": "Retained",
        "metric_total_units": "Units",
        "metric_tenants_renewing": "Renewing Tenants",
        "metric_annual_churn_rate": "Churn Rate",
        "metric_void_days_per_year": "Void days per year",
        "metric_monthly_rent": "Monthly Rent (£)",
        "metric_effective_occupancy": "Effective Occupancy"
    },
    "th": {
        "building_name": "Building Name/Address",
        "caption": "สำรวจว่าการปรับปรุงอัตราการเข้าพักเล็กน้อยสามารถเพิ่มรายได้ต่อปีได้อย่างไร",
        "chart_annual_revenue_distribution": "Total Revenue",
        "chart_annual_revenue_distribution_lost": "Lost",
        "chart_annual_revenue_distribution_retained": "Retained",
        "churn": "อัตราการย้ายออกของผู้เช่า (%)",
        "contract_length": "Contract Length (months)",
        "currency_symbol": "฿",
        "delay_contract": "ระยะเวลาในการเซ็นสัญญา (วัน)",
        "delay_inspection": "ระยะเวลาในการตรวจสอบ (วัน)",
        "delay_maintenance": "ระยะเวลารอการซ่อมบำรุง (วัน)",
        "delay_new_tenant": "ระยะเวลาในการหาผู้เช่าใหม่ (วัน)",
        "delay_repairs": "ระยะเวลาในการซ่อมแซม (วัน)",
        "delay_viewing": "ระยะเวลาในการนัดดูห้อง (วัน)",
        "detailed_metrics_header": "Breakdown",
        "effective_occ": "Effective Occupancy",
        "financial_summary_header": "💸 Lost Cash",
        "flats": "จำนวนห้องพัก",
        "language_english": "English",
        "language_selector": "Select Language",
        "language_thai": "ไทย",
        "metric_annual_churn_rate": "Churn Rate",
        "metric_effective_occupancy": "Effective Occupancy",
        "metric_monthly_rent": "Monthly Rent (£)",
        "metric_tenants_renewing": "Renewing Tenants",
        "metric_total_annual_loss": "per year",
        "metric_total_units": "Units",
        "metric_void_days_per_year": "Void days per year",
        "notice_period": "Notice Period (months)",
        "params_header": "ตั้งค่าการจำลอง",
        "renews": "Total no. of contract renewals",
        "rent": "ค่าเช่ารายเดือน (บาท)",
        "results_header": "ผลลัพธ์",
        "revenue": "Annual Revenue",
        "sidebar_building_name": "Building Name",
        "sidebar_delay_contract": "Days to sign contract",
        "sidebar_delay_find_new_tenant": "Days to find a new tenant",
        "sidebar_delay_viewing": "Days to book viewing",
        "sidebar_header_building": "Building Details",
        "sidebar_header_delay": "Repairs",
        "sidebar_header_moving_out": "Turnover",
        "sidebar_header_replace": "New Tenant",
        "sidebar_header_tenants": "Tenancies",
        "sidebar_rent_per_month": "Rent per month (avg. £)",
        "title": "🏠 เครื่องจำลองอัตราการเข้าพัก",
        "total_span_loss": "Over 3 years",
        "void_days": "Void Days per Year",
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
