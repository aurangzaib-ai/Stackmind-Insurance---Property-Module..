import streamlit as st
import pandas as pd

st.set_page_config(page_title="Stackmind Insurance - Quote App", layout="wide")
st.title("🏠 Stackmind Insurance - Property Module")

# -------------------------------
# Session storage for properties
# -------------------------------
if "properties" not in st.session_state:
    st.session_state["properties"] = {}

# -------------------------------
# File Upload (Mock Extraction)
# -------------------------------
uploaded_files = st.file_uploader(
    "📂 Upload Insurance Documents",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        # Mock: Create new property id
        new_id = f"Property_{len(st.session_state['properties'])+1:03}"

        # Fake extracted attributes (25 fields fixed)
        st.session_state["properties"][new_id] = {
            "Property ID": new_id,
            "Address": f"{new_id} Demo Avenue, Quebec",
            "City": "Quebec City",
            "Province": "Quebec",
            "Postal Code": "H3Z 2Y7",
            "Country": "Canada",
            "Contact": "111-222-3333",
            "Email": "demo@example.com",
            "Size (sqft)": 2500,
            "Rooms": 5,
            "Bathrooms": 3,
            "Garage": "Yes",
            "Year Built": 2015,
            "Roof Type": "Metal",
            "Heating": "Gas",
            "Cooling": "Central",
            "Floors": 2,
            "Basement": "Unfinished",
            "Lot Size": "5000 sqft",
            "Insurance": "Covered",
            "Status": "Active",
            "Value": "$600,000",
            "Tax": "$3,800",
            "Notes": f"Extracted from {file.name}",
            "Extra Field": ""
        }

        st.success(f"✅ New property detected and added: {new_id}")

# -------------------------------
# Dropdown + Property Details
# -------------------------------
if st.session_state["properties"]:
    selected = st.selectbox("🏡 My Properties", list(st.session_state["properties"].keys()))

    if selected:
        st.subheader("📑 Extracted Property Data (25 Key Fields)")
        data = st.session_state["properties"][selected]
        df = pd.DataFrame([data])
        st.dataframe(df, use_container_width=True)
else:
    st.info("📌 No properties yet. Upload a document to get started.")
