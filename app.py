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

st.sidebar.header("Tenants")
let_duration = st.sidebar.number_input("Contract Duration (months)", 1, 36, 12)
st.sidebar.markdown(
'''
#### Tenant Turnover
Once the tenant moves out…
''')
delay_inspection = st.sidebar.slider("Average days to conduct inspection", 0, 7, 2)
delay_callout = st.sidebar.slider("Average days to wait for callout", 0, 7, 1)
delay_job_completion = st.sidebar.slider("Average days to complete repair work", 0, 7, 1)
delay_find_new_tenant = st.sidebar.slider("Average days to find new tenant", 1, 30 * 3, 30)
turnover_days = delay_inspection + delay_callout + delay_job_completion + delay_find_new_tenant

# Calculate churn rate based on tenant stay
churn_rate = (12 / let_duration) * 100

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
- **Average Tenant Stay:** {let_duration} months
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
