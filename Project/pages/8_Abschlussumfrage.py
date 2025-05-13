import streamlit as st
from google.cloud import firestore
import json
import uuid
import datetime

st.set_page_config(
    page_title="Abschlussumfrage"
 )
st.markdown("<h4>Abschlussumfrage</h4>",unsafe_allow_html=True)

st.markdown("""
            In den Übungen die du durchgegangen bist hast du einiges gelernt.
            Zum Abschluss gibt es noch ein paar Fragen die du bitte beantworten sollst und dann bist du schon fertig
            """)
if "abschlussumfrage" not in st.session_state:
        st.session_state.abschlussumfrage = {}


# ATTENTION FRAGE
frageaufmerksamkeit ="Wähle die Antwort mit der Zahl 2"
aufmerksamkeit = st.radio (
                                frageaufmerksamkeit,
                                ("1",
                                "9",
                                "2",
                                "Keine Angabe"),
                                index=None
)
#Ausgabe der Antwort
if aufmerksamkeit is not None:
    

    st.session_state.abschlussumfrage["aufmerksamkeit"] = {
    "Bereich": "Abschlussumfrage",
    "Typ": "Aufmerksamkeit",
    "Frage":  frageaufmerksamkeit,
    "Antwort": aufmerksamkeit
     }
    st.write("Deine Antwort ist:", aufmerksamkeit)

st.divider()

#########################
# INFORMATIONEN ÜBER GELERNTES
fragewissengewonnen = "Was hast du in dieser Lerneinheit gelernt?"
wissen_gewonnen = st.multiselect(
                                fragewissengewonnen,
                                ("Wie echt KI-generierte Bilder aussehen können",
                                "Wie ich Stereotype in KI-Antworten erkenne", 
                                "Was KI ist",
                                "Wie ich keine persönlichen Daten in die KI übergebe",
                                "Wie Urheberrechtliche Daten angeblich verwendet werden",
                                "Keine Angabe"),
                                placeholder="Bitte wähle die Themen aus, über die du etwas gelernt hast"
)
#Anpassung, damit die Antworten nicht als Sequenz ausgegeben werden
if wissen_gewonnen:
    antwort_wissen = ", ".join(wissen_gewonnen)
    #Ausgabe der Antwort
    st.session_state.abschlussumfrage["wissen_gewonnen"]={
        "Bereich": "Abschlussumfrage",
        "Typ": "Wissen_gewonnen",
        "Frage":fragewissengewonnen,
        "Antwort":antwort_wissen
    }
    st.write("Deine Antwort ist:", antwort_wissen)


st.divider()


# DIREKTE FRAGE ZUR VERBESSERUNG DER ERKENNUNGSFÄHIGKEIT
frageerkennungsfaehigkeit_verbessert = "Hat sich deine Fähigkeit, KI-Inhalte zu erkennen, durch die Lerneinheit verbessert?"
erkennungsfaehigkeit_verbessert = st.radio(
                       frageerkennungsfaehigkeit_verbessert,
                       ("Ja, deutlich verbessert",
                        "Ja, etwas verbessert",
                        "Keine Veränderung",
                        "Nein, gar nicht verbessert"),
                       index=None
)
# Ausgabe der Antwort
if erkennungsfaehigkeit_verbessert is not None:

   st.session_state.abschlussumfrage["erkennungsfaehigkeit_verbessert"] = {
   "Bereich": "Abschlussumfrage",
   "Typ": "erkennungsfaehigkeit_verbessert",
   "Frage":   frageerkennungsfaehigkeit_verbessert,
   "Antwort": erkennungsfaehigkeit_verbessert
    }
   st.write("Deine Antwort ist:", erkennungsfaehigkeit_verbessert)

st.divider()
##############################

# KI generierte Inhalte hinterfragen?
fragehinterfragen = "Wirst du KI-generierte Inhalte in Zukunft mehr hinterfragen?"
hinterfragen = st.radio (
                                fragehinterfragen,
                                ("Ja, ich werde die Inhalte mehr hinterfragen",
                                "Neutral",
                                "Nein, ich werde die Inhalte nicht mehr hinterfragen"),
                                index=None
)
#Ausgabe der Antwort
if hinterfragen is not None:
 
    

    st.session_state.abschlussumfrage["hinterfragen"] = {
    "Bereich": "Abschlussumfrage",
    "Typ": "Hinterfragen",
    "Frage":   fragehinterfragen,
    "Antwort": hinterfragen
    }
    st.write("Deine Antwort ist:", hinterfragen)

frageprüfverhalten_nachher = "Wie genau wirst du KI-generierte Inhalte in Zukunft prüfen?"
prüfverhalten_nachher = st.radio(
    frageprüfverhalten_nachher,
    [
        "Sehr genau - ich werde alle Fakten prüfen",
        "Eher genau - ich werde wichtige Behauptungen hinterfragen",
        "Mittel - ich werde manchmal nachprüfen",
        "Eher oberflächlich - ich werde selten nachprüfen",
        "Gar nicht - ich werde den Inhalten vertrauen",
        "Keine Angabe"
    ],
    index=None
)

if prüfverhalten_nachher is not None:
    

    st.session_state.abschlussumfrage["prüfverhalten_nachher"] = {
        "Bereich": "Abschlussumfrage",
        "Typ": "Prüfverhalten Nachher",
        "Frage": frageprüfverhalten_nachher,
        "Antwort": prüfverhalten_nachher
    }
    st.write("Deine Antwort ist:", prüfverhalten_nachher)

frageprüfstrategien = "Welche Strategien wirst du in Zukunft nutzen, um KI-generierte Inhalte kritisch zu bewerten?"
prüfstrategien = st.multiselect(
    frageprüfstrategien,
    [
        "Mehrere Quellen vergleichen",
        "Nach typischen KI-Formulierungen suchen",
        "Angaben mit seriösen Quellen gegenprüfen",
        "Auf Stereotypen und Vorurteile achten",
        "Bei Bildern auf unnatürliche Details achten",
        "Die Authentizität des Erstellers überprüfen",
        "Nach Quellenangaben suchen",
        "Keine besonderen Strategien",
        "Sonstiges"
    ],
    placeholder="Wähle alle Strategien aus, die du verwenden würdest"
)

if prüfstrategien:
    antwort_prüfstrategien = ", ".join(prüfstrategien)
    

    st.session_state.abschlussumfrage["prüfstrategien"] = {
        "Bereich": "Abschlussumfrage",
        "Typ":"Prüfstrategie",
        "Frage": frageprüfstrategien,
        "Antwort": antwort_prüfstrategien
    }
    st.write("Deine Antwort ist:", antwort_prüfstrategien)
fragevertrauensveränderung = "Hat sich dein Vertrauen in KI-generierte Inhalte durch die Lerneinheit verändert?"
vertrauensveränderung = st.radio(
    fragevertrauensveränderung,
    [
        "Ja, ich vertraue KI-Inhalten jetzt mehr",
        "Ja, ich vertraue KI-Inhalten jetzt weniger",
        "Nein, mein Vertrauen ist unverändert",
        "Keine Angabe"
    ],
    index=None
)

if vertrauensveränderung is not None:
    

    st.session_state.abschlussumfrage["vertrauensveränderung"] = {
        "Bereich":"Abschlussumfrage",
        "Typ":"Vertrauensveränderung",
        "Frage": fragevertrauensveränderung,
        "Antwort": vertrauensveränderung
    }
    st.write("Deine Antwort ist:", vertrauensveränderung)
st.divider()

#########################
# FEEDBACK ZUM MODUL
fragemodul = "Wie hilfreich fandest du diese Lerneinheit?"
modul_bewertung = st.radio(
                         fragemodul,
                        ("Sehr hilfreich",
                        "Hilfreich",
                        "Neutral",
                        "Weniger hilfreich",
                        "Nicht hilfreich"),
                        index=None
)
#Ausgabe der Antwort
if modul_bewertung is not None:
    st.session_state.abschlussumfrage["modul_bewertung"] = {
    "Bereich":"Abschlussumfrage",
    "Typ":"Modul Bewertung",
    "Frage":   fragemodul,
    "Antwort": modul_bewertung
    }
    st.write("Deine Antwort ist:", modul_bewertung)

frageverbesserung = "Was kann an der Lerneinheit verbessert werden? (optional)"
verbesserung = st.text_area(frageverbesserung, height=100)
if verbesserung:
   

    st.session_state.abschlussumfrage["verbesserung"] = {
    "Bereich": "Abschlussumfrage",
    "Typ": "Verbesserung",
    "Frage":   frageverbesserung,
    "Antwort": verbesserung
    }

#############################################
#############################################
#############################################

if st.button("Abschluss"):

    unbeantwortet = (aufmerksamkeit is None or wissen_gewonnen is None or 
                     erkennungsfaehigkeit_verbessert is None or modul_bewertung is None or
                     prüfverhalten_nachher is None or prüfstrategien is None or
                     vertrauensveränderung is None)
    if unbeantwortet:
        st. error("Bitte beantworte alle Fragen, um fortzufahren.")
    else:
        
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
        try: 
            doc_ref.set({
                    
                    "dauerUmfrageSekunden": dauerUmfrageSekunden,
                    "Einstiegstumfrage":st.session_state.get("einstiegsumfrage"),
                    "Antworten_Grundwissen_KI":st.session_state.get("antworten_grundwissen_ki"),
                    "Uebung1":st.session_state.get("uebung1"),
                    "Uebung2":st.session_state.get("uebung2"),
                    "Uebung3":st.session_state.get("uebung3"),
                    "Uebung4":st.session_state.get("uebung4"),
                
                #endzeit
                    "Abschlussumfrage":st.session_state.get("abschlussumfrage")
        
                

        })
        except Exception as error:
                st.write("Es ist bei der Speicherung ein Fehler aufgetreten.")
        
    
        st.switch_page("pages/9_Abschluss.py")

