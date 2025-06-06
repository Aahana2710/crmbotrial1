import pandas as pd
import streamlit as st

st.set_page_config(page_title="CRM Bot", layout="wide")
st.title("Welcome to CRM Bot")

@st.cache_data
def load_data():
    file = "InterconnectedData_Hierarchical.xlsx"
    region = pd.read_excel(file, sheet_name="Region")
    customer = pd.read_excel(file, sheet_name="CustomerDetails")
    transaction = pd.read_excel(file, sheet_name="Transaction")
    store = pd.read_excel(file, sheet_name="StoreMaster")
    return region, customer, transaction, store

region_df, customer_df, transaction_df, store_df = load_data()

# Filter by Channel
st.sidebar.header("Filter by Channel")

# Check that 'channel' column exists
if "channel" in store_df.columns:
    channel_options = store_df["channel"].dropna().unique()
    selected_channels = st.sidebar.multiselect("Select Channel(s)", options=channel_options, default=channel_options)

    # Filter store data by selected channels
    filtered_store = store_df[store_df["channel"].isin(selected_channels)]

    st.subheader("Filtered StoreMaster by Channel")
    st.write(filtered_store.reset_index(drop=True))
else:
    st.error("⚠️ Column 'channel' not found in StoreMaster sheet. Please check the Excel file.")

# Optional: show other sheet previews
st.header("📋 Data Preview")
with st.expander("Region Sheet"):
    st.write(region_df.head())

with st.expander("CustomerDetails Sheet"):
    st.write(customer_df.head())

with st.expander("Transaction Sheet"):
    st.write(transaction_df.head())

