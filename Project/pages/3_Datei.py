import streamlit as st

# st.set_page_config(
#     page_title="Sensibilisierungs Modul für KI-generierte Inhalte"
# )

import requests
import socket

def check_network():
    st.write("Netzwerkverbindung wird überprüft...")
    
    # DNS-Test
    try:
        socket.gethostbyname("api.openai.com")
        st.success("DNS-Auflösung für api.openai.com erfolgreich")
    except socket.gaierror:
        st.error("DNS-Auflösung für api.openai.com fehlgeschlagen")
    
    # Konnektivitätstest
    try:
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            st.success("Internetverbindung ist aktiv")
    except requests.exceptions.RequestException:
        st.error("Internetverbindung scheint nicht zu funktionieren")
    
    # OpenAI API-Test
    try:
        response = requests.get("https://api.openai.com/v1/models", 
                              headers={"Authorization": f"Bearer {st.secrets['openai']['api_key']}"},
                              timeout=10)
        if response.status_code == 200:
            st.success("Verbindung zur OpenAI API erfolgreich")
        else:
            st.error(f"OpenAI API-Verbindung fehlgeschlagen: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"OpenAI API-Verbindung fehlgeschlagen: {e}")

if st.button("Netzwerk testen"):
    check_network()