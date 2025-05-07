import streamlit as st

st.set_page_config(
    page_title="Abschlussumfrage"
 )
st.markdown("<h4>Abschlussumfrage</h4>",unsafe_allow_html=True)

st.markdown("""
            In den Übungen die du durchgegangen bist hast du einiges gelernt.
            Zum Abschluss gibt es noch ein paar Fragen die du bitte beantworten sollst und dann bist du schon fertig
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
                                "Was hast du in dieser Lerneinheit gelernt?",
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
                       "Hat sich deine Fähigkeit, KI-Inhalte zu erkennen, durch die Lerneinheit verbessert?",
                       ("Ja, deutlich verbessert",
                        "Ja, etwas verbessert",
                        "Keine Veränderung",
                        "Nein, gar nicht verbessert"),
                       index=None
)
# Ausgabe der Antwort
if erkennungsfaehigkeit_verbessert is not None:
   st.write("Deine Antwort ist:", erkennungsfaehigkeit_verbessert)
   st.session_state.antworten_abschlussumfrage["erkennungsfaehigkeit_verbessert"] = erkennungsfaehigkeit_verbessert

st.divider()
##############################

# KI generierte Inhalte hinterfragen?
hinterfragen = st.radio (
                                "Wirst du KI-generierte Inhalte in Zukunft mehr hinterfragen?",
                                ("Ja, ich werde die Inhalte mehr hinterfragen",
                                "Neutral",
                                "Nein, ich werde die Inhalte nicht mehr hinterfragen"),
                                index=None
)
#Ausgabe der Antwort
if aufmerksamkeit is not None:
    st.write("Deine Antwort ist:", aufmerksamkeit)
    st.session_state.antworten_abschlussumfrage["aufmerksamkeit"] = aufmerksamkeit




#########################
# FEEDBACK ZUM MODUL

modul_bewertung = st.radio(
                        "Wie hilfreich fandest du diese Lerneinheit?",
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
    st.session_state.antworten_abschlussumfrage["modul_bewertung"] = modul_bewertung

verbesserung = st.text_area("Was kann an der Lerneinheit verbessert werden? (optional)", height=100)
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
