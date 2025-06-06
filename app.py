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

# Show columns of StoreMaster to debug column name
st.write("StoreMaster columns:", store_df.columns.tolist())

# After checking the output, replace 'brand' below with the correct column name
brands = store_df["brand"].dropna().unique()  # <-- Replace 'brand' if needed

st.sidebar.header("Filter by Brand")
selected_brands = st.sidebar.multiselect("Select Brand(s)", options=brands, default=brands)

filtered_store = store_df[store_df["brand"].isin(selected_brands)]  # <-- Replace 'brand' if needed

st.header("Data Preview")

st.subheader("Region Sheet")
st.write(region_df.head())

st.subheader("CustomerDetails Sheet")
st.write(customer_df.head())

st.subheader("Transaction Sheet")
st.write(transaction_df.head())

st.subheader("Filtered StoreMaster Sheet by Brand")
st.write(filtered_store.reset_index(drop=True))
