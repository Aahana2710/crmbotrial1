import pandas as pd
import streamlit as st

st.set_page_config(page_title="CRM Dashboard", layout="wide")
st.title("📊 CRM Data Dashboard")

@st.cache_data
def load_data():
    file = "InterconnectedData_Hierarchical.xlsx"
    customer = pd.read_excel(file, sheet_name="CustomerDetails")
    store = pd.read_excel(file, sheet_name="StoreMaster")
    return customer, store

customer_df, store_df = load_data()

# Merge customer and store data on locationcode and old store code
merged_df = customer_df.merge(store_df, left_on="locationcode", right_on="old store code", how="left")

# Filters in sidebar
st.sidebar.header("🔍 Filter Data")

selected_brand = st.sidebar.multiselect(
    "Brand", options=store_df["brand"].dropna().unique(), default=store_df["brand"].dropna().unique()
)

selected_state = st.sidebar.multiselect(
    "State", options=store_df["state"].dropna().unique(), default=store_df["state"].dropna().unique()
)

selected_city = st.sidebar.multiselect(
    "City", options=store_df["city"].dropna().unique(), default=store_df["city"].dropna().unique()
)

selected_region = st.sidebar.multiselect(
    "Region", options=store_df["region"].dropna().unique(), default=store_df["region"].dropna().unique()
)

selected_pincode = st.sidebar.multiselect(
    "Pincode", options=store_df["pincode"].dropna().unique(), default=store_df["pincode"].dropna().unique()
)

# Filter dataframe
filtered_df = merged_df[
    (merged_df["brand"].isin(selected_brand)) &
    (merged_df["state"].isin(selected_state)) &
    (merged_df["city"].isin(selected_city)) &
    (merged_df["region"].isin(selected_region)) &
    (merged_df["pincode"].isin(selected_pincode))
]

# Display filtered data
st.subheader("📋 Filtered Customer Data")
st.dataframe(filtered_df.reset_index(drop=True))

# Summary
st.markdown("### 📌 Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", filtered_df.shape[0])
col2.metric("Unique Cities", filtered_df['city'].nunique())
col3.metric("Unique Brands", filtered_df['brand'].nunique())


