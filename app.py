import pandas as pd
import streamlit as st

st.set_page_config(page_title="CRM Bot", layout="wide")
st.title("Welcome to CRM Bot")

@st.cache_data
def load_data():
    file = "InterconnectedData_Hierarchical.xlsx"
    store_df = pd.read_excel(file, sheet_name="StoreMaster")
    customer_df = pd.read_excel(file, sheet_name="CustomerDetails")
    return store_df, customer_df

store_df, customer_df = load_data()

# Merge StoreMaster and CustomerDetails
merged_df = customer_df.merge(
    store_df,
    left_on="locationcode",
    right_on="old store code",
    how="left"
)

st.sidebar.header("Filters")

# Validate filter columns
required_cols = ["Channel", "State", "Region"]
missing_cols = [col for col in required_cols if col not in merged_df.columns]

if missing_cols:
    st.error(f"⚠️ Missing column(s): {', '.join(missing_cols)}")
    st.write("Available columns:", merged_df.columns.tolist())
else:
    # Channel filter
    channel_options = merged_df["Channel"].dropna().unique()
    selected_channels = st.sidebar.multiselect("Select Channel(s)", options=channel_options, default=channel_options)

    # Region filter
    region_options = merged_df["Region"].dropna().unique()
    selected_regions = st.sidebar.multiselect("Select Region(s)", options=region_options, default=region_options)

    # State filter
    state_options = merged_df["State"].dropna().unique()
    selected_states = st.sidebar.multiselect("Select State(s)", options=state_options, default=state_options)

    # Apply filters
    filtered_df = merged_df[
        (merged_df["Channel"].isin(selected_channels)) &
        (merged_df["Region"].isin(selected_regions)) &
        (merged_df["State"].isin(selected_states))
    ]

    st.subheader("Filtered Customer Data")
    st.write(filtered_df.reset_index(drop=True))



