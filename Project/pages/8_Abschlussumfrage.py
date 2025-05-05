import streamlit as st

st.set_page_config(
    page_title="Abschlussumfrage"
 )
st.markdown("<h4>Abschlussumfrage</h4>",unsafe_allow_html=True)

st.markdown("""
            In den Übungen die wir durchgegangen sind haben wir einiges gelernt.
            Zum Abschluss gibt es noch ein paar Fragen die ich dir stellen möchte und dann sind wir schon fertig
            """)
if "antworten_abschlussumfrage" not in st.session_state:
        st.session_state.antworten_abschlussumfrage = {}
# ATTENTION FRAGE
aufmerksamkeit = st.radio (
                                "Wähle die Antwort mit der Zahl 2",
                                ("1",
                                "9",
                                "2",
                                "Keine Angabe"),
                                index=None
)
#Ausgabe der Antwort
if aufmerksamkeit is not None:
    st.write("Deine Antwort ist:", aufmerksamkeit)
    st.session_state.antworten_abschlussumfrage["aufmerksamkeit"] = aufmerksamkeit


st.divider()

#########################
# INFORMATIONEN ÜBER GELERNTES

wissen_gewonnen = st.multiselect(
                                "Was hast du im Modul gelernt?",
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
    st.session_state.antworten_abschlussumfrage["antwort_wissen"] = antwort_wissen

st.divider()


# DIREKTE FRAGE ZUR VERBESSERUNG DER ERKENNUNGSFÄHIGKEIT
erkennungsfaehigkeit_verbessert = st.radio(
                       "Hat sich deine Fähigkeit, KI-Inhalte zu erkennen, durch das Modul verbessert?",
                       ("Ja, deutlich verbessert",
                        "Ja, etwas verbessert",
                        "Keine Veränderung",
                        "Nein, gar nicht verbessert",
                        "Keine Angabe"),
                       index=None
)
# Ausgabe der Antwort
if erkennungsfaehigkeit_verbessert is not None:
   st.write("Deine Antwort ist:", erkennungsfaehigkeit_verbessert)
   st.session_state.antworten_abschlussumfrage["erkennungsfaehigkeit_verbessert"] = erkennungsfaehigkeit_verbessert

st.divider()
#########################
# FEEDBACK ZUM MODUL

modul_bewertung = st.radio(
                        "Wie hilfreich fandest du dieses Modul?",
                        ("Sehr hilfreich",
                        "Hilfreich",
                        "Neutral",
                        "Weniger hilfreich",
                        "Nicht hilfreich",
                        "Keine Angabe"),
                        index=None
)
#Ausgabe der Antwort
if modul_bewertung is not None:
    st.write("Deine Antwort ist:", modul_bewertung)
    st.session_state.antworten_abschlussumfrage["modul_bewertung"] = modul_bewertung

verbesserung = st.text_area("Was können wir verbessern? (optional)", height=100)
if verbesserung:
    st.session_state.antworten_abschlussumfrage["verbesserung"] = verbesserung

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
