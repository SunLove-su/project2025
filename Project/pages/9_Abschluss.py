import streamlit as st
from google.cloud import firestore
import json
import uuid
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
    user_id = f"{uuid.uuid4()}"
    st.session_state["user_id"]=user_id

    
    
    
doc_ref = db.collection(u'users').document(user_id)
#Hinterher alle Umfrageergenisse
doc_ref.set({
    "Einstiegstumfrage":st.session_state.get("antworten_einstiegsumfrage"),
    "Antworten_Grundwissen_KI":st.session_state.get("antworten_grundwissen_ki"),
    "Uebung1":st.session_state.uebung1,
    "Uebung2":st.session_state.uebung2,
    

    "Abschlussumfrage":st.session_state.get("antworten_abschlussumfrage")
    

})
    
