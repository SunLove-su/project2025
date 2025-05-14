import streamlit as st

 
if not st.session_state.get("admin"):
    st.set_page_config(page_title="Einstiegsumfrage",initial_sidebar_state="collapsed")
 
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

    st.set_page_config(page_title="Einstiegsumfrage"
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


st.markdown("<h4>Einstiegsumfrage</h4>",unsafe_allow_html=True)

st.markdown("""
            Die Umfrage erfasst deine persönliche Erfahrung und Einschätzung
            von KI.
            Die Antworten werden nur im Rahmen dieser Arbeit ausgewertet.           
           """)
st.divider()

if "einstiegsumfrage" not in st.session_state:
    st.session_state.einstiegsumfrage ={}


# Demografische Daten

#Frage Alter: Wie alt bist du
#Alter der Jugendlichen in den Studien Vodafone(2024) = 14-20, Sinus (2024) = 14-17
fragealter = "Wie alt bist du?"
alter = st.radio (fragealter,
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
    st.session_state.einstiegsumfrage["alter"]={
    "Bereich": "Einstiegsumfrage",
    "Typ": "Alter",
    "Frage":   fragealter,
    "Antwort": alter
    }
    st.write(f"Du bist: {alter} Jahre alt.")


   

# Frage Geschlecht:
fragegeschlecht = "Welchem Geschlecht fühlst du dich zugehörig?"
geschlecht = st.radio(fragegeschlecht,
                                  ("Weiblich",
                                   "Männlich",
                                   "Divers",
                                   "Keine Angabe"
                                   ),
                                   index=None
)
if geschlecht is not None:
 st.session_state.einstiegsumfrage["geschlecht"]={
    "Bereich":"Einstiegsumfrage",
    "Typ":"Geschlecht",
    "Frage": fragegeschlecht,
    "Antwort": geschlecht
 
 }

 st.write(f"Du fühlst dich dem {geschlecht} zugehörig.")

st.divider()
##############

# Frage KI-Wissen (Selbsteinschätzung)
frage_kiwissen = "Wie gut kennst du dich mit Künstlicher Intelligenz (KI) aus?"
kiwissen = st.radio(
                    frage_kiwissen,
                    ("Sehr gut",
                     "Gut",
                     "Ein wenig",
                     "Kaum",
                     "Gar nicht",
                     "Keine Angabe"),
    index=None
)

if kiwissen is not None:
    st.session_state.einstiegsumfrage["kiwissen"]={
        "Bereich":"Einstiegsumfrage",
        "Typ": "KI-Wissen",
        "Frage": frage_kiwissen,
        "Antwort": kiwissen
    
    }

frage_erkennungsfaehigkeit = "Wie gut kannst du erkennen, ob ein Text oder Bild von einer KI stammt?"
erkennungsfaehigkeit = st.radio(
    frage_erkennungsfaehigkeit,
    [
        "Sehr gut",
        "Gut", 
        "Mittelmäßig",
        "Nicht so gut",
        "Gar nicht gut",
        "Keine Angabe"
    ],
    index=None
)

if erkennungsfaehigkeit is not None:
    st.session_state.einstiegsumfrage["erkennungsfaehigkeit"] = {
        "Bereich": "Einstiegsumfrage",
        "Typ": "Erkennungsfähigkeit",
        "Frage": frage_erkennungsfaehigkeit,
        "Antwort": erkennungsfaehigkeit
    }
    st.write("Deine Antwort ist:", erkennungsfaehigkeit)

#########################
# Nutzunghäufigkeit (Vodafone2024) S. 11 , Gerlich Studie 2025
fragehaeufigkeitkinutzung = "Wie oft nutzt du KI-Tools?"
haeufigkeitkinutzung = st.radio(
                                fragehaeufigkeitkinutzung,
                                ("Täglich",
                                "Mehrmals die Woche",
                                "Einmal pro Woche",
                                "Einmal pro Monat",
                                "Seltener als einmal pro Monat",
                                "Nie",
                                "Keine Antwort"),
                                 index=None,
)
if haeufigkeitkinutzung is not None:
    st.session_state.einstiegsumfrage["haeufigkeitsnutzung"]={
    "Bereich": "Einstiegsumfrage",
    "Typ": "Häufigkeitsnutzung",
    "Frage": fragehaeufigkeitkinutzung,
    "Antwort": haeufigkeitkinutzung,
    
    }
    st.write(f"Du nutzt KI: {haeufigkeitkinutzung}")
   

st.divider()

fragevertrauenkiinhalte = "Für wie vertrauenswürdig hältst du KI-generierte Inhalte?"
vertrauenkiinhalten = st.radio(
                               fragevertrauenkiinhalte,
                                ("Sehr vertrauenswürdig",
                                "Eher vertrauenswürdig",
                                "Neutral",
                                "Eher nicht vertrauenswürdig",
                                "Gar nicht vertrauenswürdig",
                                "Keine Angabe"),
                               index=None
)

if vertrauenkiinhalten is not None:


    st.session_state.einstiegsumfrage["vertrauenkiinhalten"]={

    "Bereich":"Einstiegsumfrage",
    "Typ": "Vertrauen KI Inhalte",
    "Frage": fragevertrauenkiinhalte,
    "Antwort": vertrauenkiinhalten,
    }
    st.write(f"Du hälst KI-generierte Inhalte für {vertrauenkiinhalten}")

fragepruefungvorher = "Wie genau prüfst du KI-generierte Inhalte, bevor du ihnen vertraust?"
pruefungvorher = st.radio(
                fragepruefungvorher,
                ("Sehr genau - ich prüfe alle Fakten",
                 "Eher genau - ich prüfe wichtige Behauptungen",
                 "Manchmal - ich prüfe je nach Thema",
                 "Eher ungenau - ich prüfe selten nach",
                 "Gar nicht - ich prüfe die Inhalte nicht",
                 "Keine Angabe"),
                index=None
)

if pruefungvorher is not None:
    st.session_state.einstiegsumfrage["pruefungvorher"]={
        "Bereich": "Einstiegsumfrage",
        "Typ": "Prüfung KI",
        "Frage": fragepruefungvorher,
        "Antwort": pruefungvorher
    
    }
    st.write(f"Dein Prüfverhalten: {pruefungvorher}")
    

st.session_state.einstiegsumfrage




st.divider()
st.markdown("Um fortzufahren, klicke auf \"Weiter\" ")
col1, col2 = st.columns([8,2])
with col2:

    if st.button("Weiter"):
        unbeantwortet = False

        if alter is None:
            st.error("Bitte gebe dein Alter an.")
            unbeantwortet = True
        if geschlecht is None:
            st.error("Bitte gebe dein Geschlecht an.")
            unbeantwortet = True
        if kiwissen is None:
            st.error("Bitte gebe dein Wissensstand an.")
            unbeantwortet = True
        if erkennungsfaehigkeit is None:
            st.error ("Bitte gebe deine Erkennungsfähigkeit an.")
            unbeantwortet = True
        if haeufigkeitkinutzung is None:
            st.error ("Bitte gebe an wie häufig du KI nutzt.")
            unbeantwortet = True
        if vertrauenkiinhalten is None:
            st.error ("Bitte gebe an wie sehr du KI generierten Inhalten vertraust")
            unbeantwortet = True
        if pruefungvorher is None:
            st.error ("Bitte gebe an, ob du KI prüfst.")
            unbeantwortet = True
 
        if not unbeantwortet: 
            st.switch_page("pages/3_Grundwissen_Ki.py")