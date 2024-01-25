import streamlit as st
import json
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(data)

formulaire = st.form(key = 'formulaire1')
secteur = formulaire.multiselect('Sector :',['Basic Materials', 'Communication Services', 'Consumer Cyclical', 'Consumer Defensive', 'Energy', 'Financial Services', 'Healthcare', 'Industrials','Real Estate','Technology','Utilities'])
industry = formulaire.multiselect('Industry :',['yohann'])
inst_type = formulaire.multiselect('Instrument type :', ['CRYPTOCURRENCY', 'EQUITY', 'ETF', 'MUTUALFUND', 'OPTION'])
region = formulaire.multiselect('Region :', ['United States','France'])
currency = formulaire.multiselect('currency : ', ['USD','EUR'])
exchange = formulaire.multiselect('exchange :', ['NYQ'])
esg_score = formulaire.number_input('ESG Score', value = 80, min_value = 0, max_value = 100)
submit_data = formulaire.form_submit_button("Enregistrer")

if submit_data:
    data = {'secteur' : secteur,
            'industry' : industry,
            'inst_type' : inst_type,
            'region' : region,
            'currency' : currency,
            'exchange' : exchange,
            'esg_score' : esg_score}

    donnees_json = json.dumps(data)
    # Enregistrer la chaîne JSON dans un fichier
    with open("donnees.json", "w") as fichier_json:
        fichier_json.write(donnees_json)

    st.success("Données enregistrées avec succès !")
