import pandas as pd
import streamlit as st

st.set_page_config(page_title="CRM Dashboard", layout="wide")

st.title("📊 CRM Data Dashboard")

# Load data
@st.cache_data
def load_data():
    file = "InterconnectedData_Hierarchical.xlsx"
    region = pd.read_excel(file, sheet_name="Region")
    customer = pd.read_excel(file, sheet_name="CustomerDetails")
    transaction = pd.read_excel(file, sheet_name="Transaction")
    store = pd.read_excel(file, sheet_name="StoreMaster")
    return region, customer, transaction, store

region_df, customer_df, transaction_df, store_df = load_data()

# Debug: show columns to verify names
st.write("Store columns:", store_df.columns.tolist())
st.write("Customer columns:", customer_df.columns.tolist())

# Merge customer and store for filtering
merged_df = customer_df.merge(store_df, left_on="locationcode", right_on="old store code", how="left")

# Sidebar Filters
st.sidebar.header("🔍 Filter Data")

selected_channel = st.sidebar.multiselect(
    "Channel", options=store_df["channel"].unique(), default=store_df["channel"].unique()
)

selected_state = st.sidebar.multiselect(
    "State", options=store_df["state"].unique(), default=store_df["state"].unique()
)

selected_region = st.sidebar.multiselect(
    "Region", options=store_df["region"].unique(), default=store_df["region"].unique()
)

selected_city = st.sidebar.multiselect(
    "City", options=store_df["city"].unique(), default=store_df["city"].unique()
)

selected_pincode = st.sidebar.multiselect(
    "Pincode", options=store_df["pincode"].unique(), default=store_df["pincode"].unique()
)

# Apply filters
filtered_df = merged_df[
    (merged_df["channel"].isin(selected_channel)) &
    (merged_df["state"].isin(selected_state)) &
    (merged_df["region"].isin(selected_region)) &
    (merged_df["city"].isin(selected_city)) &
    (merged_df["pincode"].isin(selected_pincode))
]

# Display filtered data
st.subheader("📋 Filtered Customer Data")
st.dataframe(filtered_df.reset_index(drop=True))

# Summary Stats
st.markdown("### 📌 Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", filtered_df.shape[0])
col2.metric("Unique Cities", filtered_df['city'].nunique())
col3.metric("Channels Shown", len(selected_channel))

# Optional: Download filtered data
st.download_button(
    label="⬇ Download Filtered Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_customers.csv",
    mime="text/csv"
)

