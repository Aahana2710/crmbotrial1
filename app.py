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

# Debug print to show columns
st.write("Customer columns:", customer_df.columns.tolist())
st.write("Store columns:", store_df.columns.tolist())

# You must replace these keys with correct names after you check the output above:
merged_df = customer_df.merge(store_df, left_on="YOUR_CUSTOMER_COLUMN", right_on="YOUR_STORE_COLUMN", how="left")

# Filters and rest of your code goes here...




