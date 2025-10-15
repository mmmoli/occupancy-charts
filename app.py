import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from lib.i18n import t, Language

# ---- App Header ----
st.set_page_config(page_title="Occupancy Loss Calculator", page_icon="💸", layout="wide")
# Language selection
language = st.sidebar.selectbox("Select Language", options=["en", "th"], format_func=lambda lang: "English" if lang == "en" else "ไทย")

st.title(t("title", language))
st.caption(t("caption", language))

# ---- Inputs ----
st.sidebar.header(t("params_header", language))
n_flats = st.sidebar.slider(t("flats", language), 1, 200, 30)
rent_per_month = st.sidebar.number_input(t("rent", language), 3000, 50000, 5000, step=1000)

st.sidebar.header(t("params_header", language))
tenants_renewing = st.sidebar.slider(t("flats", language), 0, n_flats, int(n_flats * 0.7))
st.sidebar.markdown("#### " + t("turnover", language))
delay_inspection = st.sidebar.slider(t("turnover", language) + " - Inspection", 0, 7, 2)
delay_callout = st.sidebar.slider(t("turnover", language) + " - Maintenance", 0, 7, 1)
delay_job_completion = st.sidebar.slider(t("turnover", language) + " - Repairs", 0, 7, 1)
delay_find_new_tenant = st.sidebar.slider(t("turnover", language) + " - New Tenant", 1, 90, 30)
turnover_days = delay_inspection + delay_callout + delay_job_completion + delay_find_new_tenant

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
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(t("results_header", language))

    # Pie chart of revenue
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Revenue Pie Chart
    revenue_data = [effective_revenue, revenue_loss]
    labels = ['Retained Revenue', 'Lost Revenue']
    colors = ['#2ecc71', '#e74c3c']

    ax1.pie(revenue_data, labels=labels, colors=colors, autopct='%1.1f%%',
            startangle=90, wedgeprops={'edgecolor': 'white', 'linewidth': 1})
    ax1.set_title('Annual Revenue Distribution')

    # Bar chart of occupancy
    occupancy_data = pd.DataFrame({
        'Scenario': ['Theoretical Occupancy', 'Effective Occupancy'],
        'Occupancy (%)': [100, effective_occupancy_rate * 100]
    })

    sns.barplot(x='Scenario', y='Occupancy (%)', data=occupancy_data, ax=ax2,
                palette=['#3498db', '#2980b9'])
    ax2.set_title('Occupancy Comparison')
    ax2.set_ylim(0, 100)

    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.subheader("💸 Financial Summary")
    st.metric("Total Annual Revenue Loss", f"฿{revenue_loss:,.0f}",
              f"{percentage_loss:.1f}% of potential revenue")

    st.markdown("""
    ### What This Means
    - Every vacant day costs you money
    - Reducing turnover time can significantly boost your revenue
    - Invest in tenant satisfaction and quick maintenance
    """)

# Detailed Metrics
st.subheader(t("results_header", language))
col3, col4, col5 = st.columns(3)

with col3:
    st.metric(t("flats", language), f"{n_flats}")
    st.metric(t("churn", language), f"{tenants_renewing} out of {n_flats}")

with col4:
    st.metric(t("churn", language), f"{churn_rate:.1f}%")
    st.metric(t("void_days", language), f"{void_days:.0f}")

with col5:
    st.metric(t("rent", language), f"฿{rent_per_month:,}")
    st.metric(t("effective_occ", language), f"{effective_occupancy_rate * 100:.2f}%")
