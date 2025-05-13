import streamlit as st
from google.cloud import firestore
import json
import uuid
import datetime
from supabase import create_client
if not st.session_state.get("admin"):
    st.set_page_config(page_title="Abschluss",initial_sidebar_state="collapsed")
 
    st.markdown(
        """
    <style>
        [data-testid="stSidebarCollapsedControl"] {
            display: none
        }
    </style>
    """,
        unsafe_allow_html=True,

    )
else:

    st.set_page_config(page_title="Abschluss"
    
)
def login():
    st.write("Enter the secret code")
    code = st.text_input("Code")
    if st.button("Login"):
        password = code
        if password == st.secrets["survey_secret"]:
            st.session_state["logged_in"] = True
            st.rerun()
        elif password == st.secrets["admin_secret"]:
            st.session_state["logged_in"] = True
            st.session_state["admin"] = True
            st.rerun()
        else:
            st.error("Wrong secret code")
    st.stop()
 
 
if not st.session_state.get("logged_in"):
    login()

st.markdown("<h4>Abschluss</h4>",unsafe_allow_html=True)

st.markdown("""
            Vielen Dank für deine Teilnahme!
            Ich hoffe das Modul hat dir Spaß gemacht und du konntest einiges für dich mitnehmen.

            ***Wichtige Regeln im Umgang mit KI***
            1. Gebe keine sensiblen Daten in die KI (Keine Namen, Dokumente, Bilder u.a.)
            2. Prüfe und Hinterfrage die Ergebnisse der KI immer, die Ergebnisse können fehlerhaft sein.
            3. Achte auf potenzielle Vorurteile in KI-Antworten
            4. Beachte den Urheberrechte bei der Nutzung von KI
            5. Informiere dich über Entwicklungen und Änderungen\n\n
            ***Die Seite kannst du jetzt gerne schließen***

            
            """,unsafe_allow_html=True)
googlecredentials = json.loads(st.secrets["firestore"]["google_api_key"])
db=firestore.Client.from_service_account_info(googlecredentials)
user_id = f"{uuid.uuid4()}"
if "user_id" in st.session_state:
    user_id=st.session_state.user_id
else:
    user_id = f"{datetime.datetime.now().isoformat()[:19]}-{uuid.uuid4()}"
    st.session_state["user_id"]=user_id

endzeit = datetime.datetime.now()
startzeit = st.session_state.get("startzeit")
if startzeit:
   dauerUmfrage = endzeit - startzeit
   dauerUmfrageSekunden = int(dauerUmfrage.total_seconds())
   dauerUmfrageSekunden
else:
    dauerUmfrageSekunden = ""


user_data = {
    "dauerUmfrageSekunden": dauerUmfrageSekunden,
    "Einstiegstumfrage": st.session_state.get("einstiegsumfrage"),
    "Grundwissen_KI": st.session_state.get("grundwissen_ki"),
    "Uebung1": st.session_state.get("uebung1"),
    "Uebung2": st.session_state.get("uebung2"),
    "Uebung3": st.session_state.get("uebung3"),
    "Uebung4": st.session_state.get("uebung4"),
    "Abschlussumfrage": st.session_state.get("abschlussumfrage")
}

doc_ref = db.collection(u'users').document(user_id)
doc_ref.set(user_data)


try:
    # Supabase-Client erstellen
    supabase_url = st.secrets["supabase"]["url"]
    supabase_key = st.secrets["supabase"]["key"]
    supabase = create_client(supabase_url, supabase_key)
   
    # Daten für Supabase vorbereiten
    supabase_data = {
        "user_id": user_id,
        "data": user_data
    }
   
    
    # Tabelle in Supabase erstellt mit dem Namen "umfrage_antworten"
    response = supabase.table("umfrage_antworten").insert(supabase_data).execute()
   
except Exception as error:
    st.error("Es ist ein Fehler aufgetreten")

st.write("Supabase-Ergebnis:", response)
    
