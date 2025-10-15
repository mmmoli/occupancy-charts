import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ---- App Header ----
st.set_page_config(page_title="Occupancy Loss Calculator", page_icon="💸", layout="wide")
st.title("💸 Revenue Loss Simulator")
st.caption("Understand the hidden cost of tenant turnover")

# ---- Inputs ----
st.sidebar.header("Building Details")
n_flats = st.sidebar.slider("Total number of rental units", 1, 200, 30)
rent_per_month = st.sidebar.number_input("Monthly rent per unit (฿)", 3000, 50000, 5000, step=1000)

st.sidebar.header("Tenant Turnover")
let_duration = st.sidebar.number_input("Average Contract Duration (months)", 1, 36, 12)
st.sidebar.markdown("#### Vacancy Breakdown")
delay_inspection = st.sidebar.slider("Days for inspection", 0, 7, 2)
delay_callout = st.sidebar.slider("Days waiting for maintenance", 0, 7, 1)
delay_job_completion = st.sidebar.slider("Days to complete repairs", 0, 7, 1)
delay_find_new_tenant = st.sidebar.slider("Days to find new tenant", 1, 90, 30)
turnover_days = delay_inspection + delay_callout + delay_job_completion + delay_find_new_tenant

# Calculate churn rate and occupancy metrics
days_in_year = 365
rent_per_day = rent_per_month / 30
total_days = n_flats * days_in_year
churn_rate = (12 / let_duration) * 100

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
    st.subheader("💰 Revenue Impact Visualization")

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
st.subheader("📊 Detailed Metrics")
col3, col4, col5 = st.columns(3)

with col3:
    st.metric("Total Units", f"{n_flats}")
    st.metric("Average Tenant Stay", f"{let_duration} months")

with col4:
    st.metric("Annual Churn Rate", f"{churn_rate:.1f}%")
    st.metric("Void Days per Year", f"{void_days:.0f}")

with col5:
    st.metric("Monthly Rent", f"฿{rent_per_month:,}")
    st.metric("Effective Occupancy", f"{effective_occupancy_rate * 100:.2f}%")
