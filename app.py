import pandas as pd
import streamlit as st

st.set_page_config(page_title="CRM Bot", layout="wide")
st.title("Welcome to CRM Bot")

@st.cache_data
def load_data():
    file = "InterconnectedData_Hierarchical.xlsx"
    # Load all sheets you mentioned
    region = pd.read_excel(file, sheet_name="Region")
    customer = pd.read_excel(file, sheet_name="CustomerDetails")
    transaction = pd.read_excel(file, sheet_name="Transaction")
    store = pd.read_excel(file, sheet_name="StoreMaster")
    return region, customer, transaction, store

region_df, customer_df, transaction_df, store_df = load_data()

# Display loaded data summaries
st.header("Data Preview")

st.subheader("Region Sheet")
st.write(region_df.head())

st.subheader("CustomerDetails Sheet")
st.write(customer_df.head())

st.subheader("Transaction Sheet")
st.write(transaction_df.head())

st.subheader("StoreMaster Sheet")
st.write(store_df.head())





