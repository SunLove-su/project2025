import streamlit as st

st.set_page_config(
    page_title="Einstiegsumfrage"
 )
st.markdown("<h4>Einstiegsumfrage</h4>",unsafe_allow_html=True)

st.markdown("""
            Die Umfrage erfasst deine persönliche Erfahrung und Einschätzung
            mit Künstlicher Intelligenz.
            Die Antworten werden nur im Rahmen dieser Arbeit ausgewertet.           
           """)
st.divider()

if "antworten_einstiegsumfrage" not in st.session_state:
        st.session_state.antworten_einstiegsumfrage = {}
# Demografische Daten

#Frage Alter: Wie alt bist du
#Alter der Jugendlichen in den Studien Vodafone(2024) = 14-20, Sinus (2024) = 14-17
alter = st.radio ("Wie alt bist du?",
                                ("unter 15",
                                "15-16",
                                "16-17",
                                "17-18",
                                "18-19",
                                "über 19",
                                "Keine Angabe"
                                ),
                                index=None
)
if alter is not None:
    st.session_state.antworten_einstiegsumfrage["alter"]=alter
    st.write(f"Deine Antwort ist {alter}")
    st.session_state.antworten_einstiegsumfrage

# Frage Geschlecht:
geschlecht = st.radio("Welches Geschlecht hast du?",
                                  ("Weiblich",
                                   "Männlich",
                                   "Divers",
                                   "Keine Angabe"
                                   ),
                                   index=None
)
if geschlecht is not None:
    st.session_state.antworten_einstiegsumfrage["geschlecht"]=geschlecht
    st.write(f"Du bist {geschlecht}")
    st.session_state.antworten_einstiegsumfrage

st.divider()

#########################
# Nutzunghäufigkeit (Vodafone2024) S. 11 , Gerlich Studie 2025
haeufigkeitkinutzung = st.radio(
                                "Wie oft nutzt du KI-Tools?",
                                ("Täglich",
                                "Wöchentlich",
                                "Monatlich",
                                "Selten",
                                "Nie",
                                "Keine Antwort"),
                                 index=None,
)
if haeufigkeitkinutzung is not None:
    st.session_state.antworten_einstiegsumfrage["haeufigkeitkinutzung"]=haeufigkeitkinutzung
    st.write(f"Du nutzt KI: {haeufigkeitkinutzung}")
    st.session_state.antworten_einstiegsumfrage

st.divider()
vertrauenkiinhalten = st.radio(
                               "Für wie vertrauenswürdig hältst du KI-generierte Inhalte?",
                                ("Sehr vertrauenswürdig",
                                "Eher vertrauenswürdig",
                                "Neutral",
                                "Eher nicht vertrauenswürdig",
                                "Gar nicht vertrauenswürdig",
                                "Keine Angabe"),
                               index=None
)

if vertrauenkiinhalten is not None:
    st.session_state.antworten_einstiegsumfrage["vertrauenkiinhalten"]=vertrauenkiinhalten
    st.write(f"Du hälst KI für: {vertrauenkiinhalten}")
    st.session_state.antworten_einstiegsumfrage



st.divider()
st.markdown("Um forzufahren, klicke auf \"weiter\" ")
col1, col2 = st.columns([8,2])
with col2:

    if st.button("weiter"):
        unbeantwortet =(alter is None or geschlecht is None or
                        haeufigkeitkinutzung is None or vertrauenkiinhalten is None
                       )
        if unbeantwortet:
            st. error("Bitte beantworte alle Fragen, um fortzufahren.")
        else: 
            st.switch_page("pages/3_Grundwissen_Ki.py")