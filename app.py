import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---- App Header ----
st.set_page_config(page_title="Occupancy Simulator", page_icon="🏠", layout="centered")
st.title("🏠 Occupancy Rate Simulator")
st.caption("Understand how small improvements in occupancy drive annual revenue.")

# ---- Inputs ----
st.sidebar.header("Your building")
n_flats = st.sidebar.slider("Number of units", 1, 200, 30)
rent_per_month = st.sidebar.number_input("Monthly rent per flat (฿)", 3000, 8000, 5000, step=1000)
turnover_days = st.sidebar.slider("Average days vacant per turnover", 0, 60, 15)
churn_rate = st.sidebar.slider("Tenant churn rate (%)", 0, 100, 30)

# ---- Calculations ----
days_in_year = 365
rent_per_day = rent_per_month / 30
total_days = n_flats * days_in_year

# Estimate effective occupancy
void_days = (churn_rate / 100) * turnover_days * n_flats
effective_occupancy_rate = 1 - (void_days / total_days)

revenue = effective_occupancy_rate * total_days * rent_per_day

# ---- Display ----
st.subheader("📊 Results")
st.markdown(f"""
- **Flats:** {n_flats}
- **Effective Occupancy:** {effective_occupancy_rate * 100:.2f}%
- **Void Days per Year:** {void_days:.0f}
- **Annual Revenue:** ฿{revenue:,.0f}
""")

# ---- Chart ----
scenarios = pd.DataFrame({
    "Scenario": ["Theoretical (100%)", "Effective"],
    "Occupancy (%)": [100, effective_occupancy_rate * 100],
    "Revenue (฿)": [total_days * rent_per_day, revenue]
})
sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(6,4))
sns.barplot(data=scenarios, x="Scenario", y="Revenue (฿)", ax=ax)
st.pyplot(fig)
