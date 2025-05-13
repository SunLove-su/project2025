import streamlit as st
from google.cloud import firestore
import json
import uuid
import datetime

st.set_page_config(
    page_title="Abschluss"
 )
st.markdown("<h4>Abschluss</h4>",unsafe_allow_html=True)

st.markdown("""
            Vielen Dank für deine Teilnahme!
            Ich hoffe das Modul hat dir Spaß gemacht und du konntest einiges für dich mitnehmen.

            ***Die Seite kannst du jetzt gerne schließen***
            
            """)
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

    
doc_ref = db.collection(u'users').document(user_id)
#Hinterher alle Umfrageergenisse
doc_ref.set({
    
    "dauerUmfrageSekunden": dauerUmfrageSekunden,
    "Einstiegstumfrage":st.session_state.get("einstiegsumfrage"),
    "Grundwissen_KI":st.session_state.get("grundwissen_ki"),
    "Uebung1":st.session_state.get("uebung1"),
    "Uebung2":st.session_state.get("uebung2"),
    "Uebung3":st.session_state.get("uebung3"),
    "Uebung4":st.session_state.get("uebung4"),
   
#endzeit
    "Abschlussumfrage":st.session_state.get("abschlussumfrage")
    

})
    
