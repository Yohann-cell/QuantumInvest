import streamlit as st
import json
import yfinance as yf

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
