import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from lib.i18n import t, Language

# ---- App Header ----
st.set_page_config(page_title="Occupancy Loss Calculator", page_icon="💸", layout="wide")
# Language selection
language = st.sidebar.selectbox(t("language_selector", "en"), options=["en", "th"], format_func=lambda lang: t("language_english", lang) if lang == "en" else t("language_thai", lang))

st.title(t("title", language))
st.caption(t("app_caption", language))

# ---- Inputs ----
st.sidebar.header(t("sidebar_header_building", language))
building_name = st.sidebar.text_input(t("sidebar_building_name", language), placeholder='e.g. "Hill House"')
n_flats = st.sidebar.slider(t("flats", language), 1, 200, 30)
st.sidebar.header(t("sidebar_header_tenants", language))
contract_length = st.sidebar.number_input(t("contract_length", language), 1, 12, 12, step=3)
rent_per_month = st.sidebar.number_input(t("sidebar_rent_per_month", language), 1000, 50000, 5000, step=1000)
notice_period_months = st.sidebar.number_input(t("notice_period", language), 1, 12, 1)
tenants_renewing = st.sidebar.slider(t("renews", language), 1, n_flats - 1, int(n_flats * 0.7))

st.sidebar.header(t("sidebar_header_moving_out", language))

delay_find_new_tenant = st.sidebar.slider(t("sidebar_delay_find_new_tenant", language), notice_period_months * 30, notice_period_months * 30 * 4, notice_period_months * 30 * 2)
delay_viewing = st.sidebar.slider(t("sidebar_delay_viewing", language), 0, 14, 3)
delay_contract = st.sidebar.slider(t("sidebar_delay_contract", language), 0, 14, 3)
turnover_days = max(0, (delay_find_new_tenant + delay_viewing + delay_contract) - (notice_period_months * 30))

# Calculate churn rate and occupancy metrics
days_in_year = 365
rent_per_day = rent_per_month / 30
total_days = n_flats * days_in_year
churn_rate = ((n_flats - tenants_renewing) / n_flats) * 100

# Occupancy calculations
void_days = (churn_rate / 100) * turnover_days * n_flats
effective_occupancy_rate = 1 - (void_days / total_days)

# Revenue calculations
theoretical_revenue = total_days * rent_per_day
effective_revenue = effective_occupancy_rate * total_days * rent_per_day
revenue_loss = theoretical_revenue - effective_revenue
percentage_loss = (revenue_loss / theoretical_revenue) * 100

# ---- Visualization ----
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader(t("financial_summary_header", language))
    st.metric(t("metric_total_annual_loss", language), f"{t('currency_symbol', language)}{revenue_loss:,.0f}",
              f"{-percentage_loss:.1f}% of revenue")

    # Compounded Revenue Loss over 3 years
    span_duration = 3
    total_span_loss = revenue_loss * span_duration
    st.metric(t("total_span_loss", language), f"{t('currency_symbol', language)}{total_span_loss:,.0f}")

    st.markdown("""
    ### What This Means
    - Every vacant day costs you money
    - Reducing turnover time can significantly boost your revenue
    - Invest in tenant satisfaction and quick maintenance
    """)

with col2:
    st.subheader(t("detailed_metrics_header", language))

    # Pie chart of revenue
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Revenue Pie Chart
    revenue_data = [effective_revenue, revenue_loss]
    labels = [t("chart_annual_revenue_distribution_retained", language), t("chart_annual_revenue_distribution_lost", language)]
    colors = ['#2ecc71', '#e74c3c']

    ax1.pie(revenue_data, labels=labels, colors=colors, autopct='%1.1f%%',
            startangle=90, wedgeprops={'edgecolor': 'white', 'linewidth': 1})
    ax1.set_title(t("chart_annual_revenue_distribution", language))

    # Bar chart of occupancy
    occupancy_data = pd.DataFrame({
        'Scenario': ['Theoretical Occupancy', 'Effective Occupancy'],
        'Occupancy (%)': [100, effective_occupancy_rate * 100]
    })

    sns.barplot(x='Scenario', y='Occupancy (%)', data=occupancy_data, ax=ax2,
                palette=['#3498db', '#2980b9'])
    ax2.set_title(t("chart_occupancy_comparison", language))
    ax2.set_ylim(0, 100)

    plt.tight_layout()
    st.pyplot(fig)


# Detailed Metrics
st.subheader(t("results_header", language))
col3, col4, col5 = st.columns(3)

with col3:
    st.metric(t("metric_total_units", language), f"{n_flats}")
    st.metric(t("metric_tenants_renewing", language), f"{tenants_renewing}")

with col4:
    st.metric(t("metric_annual_churn_rate", language), f"{churn_rate:.1f}%")
    st.metric(t("metric_void_days_per_year", language), f"{void_days:.0f}")

with col5:
    st.metric(t("metric_monthly_rent", language), f"{t('currency_symbol', language)}{rent_per_month:,}")
    st.metric(t("metric_effective_occupancy", language), f"{effective_occupancy_rate * 100:.2f}%")
