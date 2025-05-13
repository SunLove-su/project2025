import streamlit as st
import datetime


 
if not st.session_state.get("admin"):
    st.set_page_config(page_title="Lerneinheit zur Sensibilisierung von KI-generierten Inhalten",initial_sidebar_state="collapsed")
 
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

    st.set_page_config(page_title="Lerneinheit zur Sensibilisierung von KI-generierten Inhalten"
    
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

st.markdown("<h4>Willkommen zum Lerneinheit zur Sensibilisierung KI-generierter Inhalte</h4>", unsafe_allow_html=True)
st.markdown("""Diese Lerneinheit soll die Risiken von KI-generierten Inhalten aufzeigen und dich für diese sensibilisieren.
Künstliche Intelligenz (KI) findet heute überall Einsatz und bietet uns viele Chancen.
Es gibt aber auch einige Risiken beim Umgang mit KI, z. B. das die generierten Informationen falsch sind u.a. Diese werden in der Lerneinheit exemplarisch aufgezeigt,
damit du bewusster mit KI-Anwendungen umgehen kannst!""")
st.markdown("""
***Dich erwarten:***
- Umfragen zu deinem Nutzungsverhalten im privaten und schulischen Umfeld und zu deinem Vertrauen in KI
- Interaktive Übungen zur Erkennung von KI-generierten Inhalten
 """)

#Abtrennung -> Hinweise         
st.divider()
st.markdown("***Hinweise zur Lerneinheit:***")
st.markdown("""
- Dauer: ca. 40 - 45 Minuten
- Teilnahme: anonym
- Freiwilligkeit: freiwillige Teilnahme
- Datenschutz: Demografische Daten (Alter, Geschlecht) werden vertraulich behandelt.
  Es wird sichergestellt, dass eine Zurückverfolgung auf die teilnehmende Person nicht erfolgt.
  Die Daten werden ausschließlich für mein Forschungsprojekt verwendet.

""")

# funktioniert nur bei großen Layout, bei Handys werden col immer untereinander dargestellt
#Anpassung mit CSS funktionieren nicht, da diese überschrieben werden
#st.button hat seine eigenen Positionen, die können nur mit CSS-Hijacking geändert werden
# d.h. entsprechendes Element untersuchen mit den Entwickler-Modus und den entsprechenden div-container raussuchen
# bei Änderungen der Streamlit version kann es aber zu veränderungen kommen, die Hichaking version ist nicht offiziell

st.divider()
st.markdown("Um mit der Lerneinheit zu beginnen, klicke auf \"Start\" ")
col1, col2 = st.columns([8,2])
with col2:

    if st.button("Start"):
      startzeit = datetime.datetime.now()
      st.session_state["startzeit"] =startzeit
      st.switch_page("pages/2_Umfrage.py")