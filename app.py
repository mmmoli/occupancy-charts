import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---- App Header ----
st.set_page_config(page_title="Occupancy Simulator", page_icon="🏠", layout="centered")
st.title("🏠 Occupancy Rate Simulator")
st.caption("Understand how tenant turnover impacts your annual building revenue.")

# ---- Inputs ----
st.sidebar.header("Your Building Details")
n_flats = st.sidebar.slider("Total number of rental units", 1, 200, 30)
rent_per_month = st.sidebar.number_input("Monthly rent per unit (฿)", 3000, 8000, 5000, step=1000)

# More intuitive churn rate inputs
st.sidebar.markdown("### Tenant Turnover")
avg_tenant_stay = st.sidebar.slider("Average tenant stay (months)", 6, 36, 12)
turnover_days = st.sidebar.slider("Average days to prepare unit between tenants", 0, 60, 15)

# Calculate churn rate based on tenant stay
churn_rate = (12 / avg_tenant_stay) * 100

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
- **Total Units:** {n_flats}
- **Average Tenant Stay:** {avg_tenant_stay} months
- **Estimated Annual Churn Rate:** {churn_rate:.1f}%
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
