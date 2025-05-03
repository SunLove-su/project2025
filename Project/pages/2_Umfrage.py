import streamlit as st

st.set_page_config(
    page_title="Umfrage"
 )
st.markdown("<h4>Einstiegsumfrage</h4>",unsafe_allow_html=True)

st.markdown("""
            Die Umfrage erfasst deine persönliche Erfahrung und Einschätzung
            mit Künstlicher Intelligenz.
            Die Antworten werden nur im Rahmen dieser Arbeit ausgewertet.           
           """)


if "antworten_einstiegsumfrage" not in st.session_state:
        st.session_state.antworten_einstiegsumfrage = {}
# Demografische Daten

#Frage Alter: Wie alt bist du
alter = st.radio ("Wie alt bist du?",
                                (
                                "15-16",
                                "16-17",
                                "17-18",
                                "18-19",
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
# INFORMATIONEN ÜBER GELERNTES











st.divider()
st.markdown("Um forzufahren, klicke auf \"weiter\" ")
col1, col2 = st.columns([8,2])
with col2:

    if st.button("weiter"):
        unbeantwortet =(alter is None or geschlecht is None)
        if unbeantwortet:
            st. error("Bitte beantworte alle Fragen, um fortzufahren.")
        else: 
            st.switch_page("pages/3_Grundwissen_Ki.py")