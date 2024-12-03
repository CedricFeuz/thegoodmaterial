import streamlit as st
import requests
import pandas as pd

# API-Daten abrufen
def get_materials():
    response = requests.get("http://backend:5000/api/materials")
    if response.status_code == 200:
        return pd.DataFrame(response.json(), columns=["Material", "Kategorie"])
    return pd.DataFrame()

st.title("Materialien Filter")
materials_df = get_materials()

if not materials_df.empty:
    categories = st.multiselect("Kategorie auswählen", materials_df["Kategorie"].unique())
    if categories:
        filtered = materials_df[materials_df["Kategorie"].isin(categories)]
    else:
        filtered = materials_df
    st.write(filtered)
else:
    st.error("Keine Daten verfügbar.")
