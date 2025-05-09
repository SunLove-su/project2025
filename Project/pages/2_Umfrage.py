import streamlit as st

st.set_page_config(
    page_title="Einstiegsumfrage"
 )
st.markdown("<h4>Einstiegsumfrage</h4>",unsafe_allow_html=True)

st.markdown("""
            Die Umfrage erfasst deine persönliche Erfahrung und Einschätzung
            von KI.
            Die Antworten werden nur im Rahmen dieser Arbeit ausgewertet.           
           """)
st.divider()

if "fragen_einstiegsumfrage" not in st.session_state:
    st.session_state.fragen_einstiegsumfrage ={}
if "antworten_einstiegsumfrage" not in st.session_state:
    st.session_state.antworten_einstiegsumfrage = {}
if "einstiegsumfrage" not in st.session_state:
    st.session_state.einstiegsumfrage ={}

fragen   = st.session_state.fragen_einstiegsumfrage    
antworten = st.session_state.antworten_einstiegsumfrage

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
     fragen["alter"] = fragealter 
     antworten["alter"] = alter
     st.session_state.einstiegsumfrage["alter"] = {
    "Frage":   fragealter,
    "Antwort": alter
     }
     st.write(f"Du bist: {alter} Jahre alt.")

     st.session_state.einstiegsumfrage
   

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
 fragen["geschlecht"] = fragegeschlecht
 antworten["geschlecht"]=geschlecht
 st.session_state.einstiegsumfrage["geschlecht"]={
    "Frage": fragegeschlecht,
    "Antwort": geschlecht,
 }
st.write(f"Du fühlst dich dem {geschlecht} zugehörig.")
st.session_state.einstiegsumfrage
st.divider()

#########################
# Nutzunghäufigkeit (Vodafone2024) S. 11 , Gerlich Studie 2025
fragehaeufigkeitkinutzung = "Wie oft nutzt du KI-Tools?"
haeufigkeitkinutzung = st.radio(
                                fragehaeufigkeitkinutzung,
                                ("Täglich",
                                "Wöchentlich",
                                "Monatlich",
                                "Selten",
                                "Nie",
                                "Keine Antwort"),
                                 index=None,
)
if haeufigkeitkinutzung is not None:
    fragen["haeufigkeitkinutzung"]=fragehaeufigkeitkinutzung
    antworten["haeufigkeitkinutzung"]=haeufigkeitkinutzung
    st.session_state.einstiegsumfrage["haeufigkeitkinutzung"]={

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
    fragen["vertrauenkiinhalten"]=fragevertrauenkiinhalte
    antworten["vertrauenkiinhalten"]=vertrauenkiinhalten
    st.write(f"Du hälst KI-generierte Inhalte für {vertrauenkiinhalten}")
    st.session_state.einstiegsumfrage["vertrauenkiinhalten"]={

    "Frage": fragevertrauenkiinhalte,
    "Antwort": vertrauenkiinhalten,
    }

frageprüfungvorher = "Wie genau prüfst du KI-generierte Inhalte, bevor du ihnen vertraust?"
prüfungvorher = st.radio(
                frageprüfungvorher,
                ("Sehr genau - ich prüfe alle Fakten",
                 "Eher genau - ich hinterfrage wichtige Behauptungen",
                 "Mittel - manchmal prüfe ich nach",
                 "Eher oberflächlich - selten prüfe ich nach",
                 "Gar nicht - ich vertraue den Inhalten",
                 "Keine Angabe"),
                index=None
)

if prüfungvorher is not None:
    fragen["prüfungvorher"] = frageprüfungvorher
    antworten["prüfungvorher"] = prüfungvorher
    st.session_state.einstiegsumfrage["prüfungvorher"] = {
        "Frage": frageprüfungvorher,
        "Antwort": prüfungvorher
    }
    st.write(f"Dein Prüfverhalten: {prüfungvorher}")
    



st.divider()
st.markdown("Um fortzufahren, klicke auf \"Weiter\" ")
col1, col2 = st.columns([8,2])
with col2:

    if st.button("Weiter"):
        unbeantwortet =(alter is None or geschlecht is None or
                        haeufigkeitkinutzung is None or vertrauenkiinhalten is None
                        or  prüfungvorher is None  )
        if unbeantwortet:
            st.error("Bitte beantworte alle Fragen, um fortzufahren.")
        else: 
            st.switch_page("pages/3_Grundwissen_Ki.py")