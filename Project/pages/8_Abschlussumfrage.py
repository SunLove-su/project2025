import streamlit as st

st.set_page_config(
    page_title="Abschlussumfrage"
 )
st.markdown("<h4>Abschlussumfrage</h4>",unsafe_allow_html=True)

st.markdown("""
            In den Übungen die du durchgegangen bist hast du einiges gelernt.
            Zum Abschluss gibt es noch ein paar Fragen die du bitte beantworten sollst und dann bist du schon fertig
            """)
if "fragen_abschlussumfrage" not in st.session_state:
    st.session_state.fragen_abschlussumfrage ={}
if "antworten_abschlussumfrage" not in st.session_state:
    st.session_state.antworten_abschlussumfrage = {}
if "abschlussumfrage" not in st.session_state:
        st.session_state.abschlussumfrage = {}

fragen = st.session_state.fragen_abschlussumfrage
antworten = st.session_state.antworten_abschlussumfrage
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
    st.write("Deine Antwort ist:", aufmerksamkeit)
    fragen["frageaufmerksamkeit"] = frageaufmerksamkeit 
    antworten["aufmerksamkeit"] = aufmerksamkeit
    st.session_state.abschlussumfrage["aufmerksamkeit"] = {
    "Frage":   frageaufmerksamkeit,
    "Antwort": aufmerksamkeit
     }

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
    st.write("Deine Antwort ist:", antwort_wissen)

    fragen["wissen_gewonnen"]=fragewissengewonnen
    antworten["wissen_gewonnen"]=antwort_wissen
    st.session_state.abschlussumfrage["wissen_gewonnen"]={
        "frage":fragewissengewonnen,
        "antwort":antwort_wissen
    }

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
   st.write("Deine Antwort ist:", erkennungsfaehigkeit_verbessert)
   fragen["erkennunsgfaehigkeit_verbessert"] = erkennungsfaehigkeit_verbessert 
   antworten["erkennungsfaehigkeit_verbessert"] = erkennungsfaehigkeit_verbessert
   st.session_state.abschlussumfrage["erkennungsfaehigkeit_verbessert"] = {
   "Frage":   frageerkennungsfaehigkeit_verbessert,
   "Antwort": erkennungsfaehigkeit_verbessert
    }

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
if aufmerksamkeit is not None:
    st.write("Deine Antwort ist:", aufmerksamkeit)
    
    fragen["fragehinterfragen"] = fragehinterfragen 
    antworten["hinterfragen"] = hinterfragen
    st.session_state.abschlussumfrage["hinterfragen"] = {
    "Frage":   fragehinterfragen,
    "Antwort": hinterfragen
    }




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
    st.write("Deine Antwort ist:", modul_bewertung)

   
    fragen["fragemodul"] = fragemodul 
    antworten["modul_bewertung"] = modul_bewertung
    st.session_state.abschlussumfrage["modul_bewertung"] = {
    "Frage":   fragemodul,
    "Antwort": modul_bewertung
    }

frageverbesserung = "Was kann an der Lerneinheit verbessert werden? (optional)"
verbesserung = st.text_area(frageverbesserung, height=100)
if verbesserung:
   
    fragen["frageverbesserung"] = frageverbesserung 
    antworten["verbesserung"] = verbesserung
    st.session_state.abschlussumfrage["verbesserung"] = {
    "Frage":   frageverbesserung,
    "Antwort": verbesserung
    }

#############################################
#############################################
#############################################

if st.button("Abschluss"):
    unbeantwortet = (aufmerksamkeit is None or wissen_gewonnen is None or 
                     erkennungsfaehigkeit_verbessert is None or modul_bewertung is None)
    if unbeantwortet:
        st. error("Bitte beantworte alle Fragen, um fortzufahren.")
    else: 
        st.switch_page("pages/9_Abschluss.py")
