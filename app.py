import pandas as pd
import streamlit as st

st.set_page_config(page_title="CRM Bot", layout="wide")
st.title("Welcome to CRM Bot")

@st.cache_data
def load_data():
    file = "InterconnectedData_Hierarchical.xlsx"
    store = pd.read_excel(file, sheet_name="StoreMaster")
    return store

store_df = load_data()

# Sidebar filter for Channel
st.sidebar.header("Filter by Channel")

if "Channel" in store_df.columns:
    channel_options = store_df["Channel"].dropna().unique()
    selected_channels = st.sidebar.multiselect("Select Channel(s)", options=channel_options, default=channel_options)

    # Apply filter
    filtered_store = store_df[store_df["Channel"].isin(selected_channels)]

    st.subheader("Filtered StoreMaster by Channel")
    st.write(filtered_store.reset_index(drop=True))
else:
    st.error("⚠️ Column 'Channel' not found in StoreMaster sheet.")



