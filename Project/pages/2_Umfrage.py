import streamlit as st
import hilfsdatei
 
#Überschrift der Seite
hilfsdatei.seite("Einstiegsumfrage")
#Alle Seiten mit PW versehen, dass weiterhin die Teilnehmer die Navigation nicht sehen
hilfsdatei.login()

#Überschrift der Sektion
st.markdown("<h4>Einstiegsumfrage</h4>",unsafe_allow_html=True)

#Einleitung der Sektion
st.markdown("""
            Die Umfrage erfasst deine persönliche Erfahrung und Einschätzung
            von KI.
            Die Antworten werden nur im Rahmen dieser Arbeit ausgewertet.           
           """)
#Trennungslinie
st.divider()
#Speicherung der Antworten in "einstiegsumfrage"
#Dictonary das die Antworten speichert, damit sie später im Abschluss an die Datenbank übergeben werden kann
if "einstiegsumfrage" not in st.session_state:
    st.session_state.einstiegsumfrage ={}


# Demografische Daten

#Frage nach dem Alter der Teilnehmenden
#Alter der Jugendlichen in den Studien Vodafone(2024) = 14-20, Sinus (2024) = 14-17
fragealter = "Wie alt bist du?"
alter = st.radio (fragealter,
                                (
                                    "Unter 15 Jahre",
                                    "15 - 16 Jahre",
                                    "17 - 18 Jahre",
                                    "19 Jahre",
                                    "Über 19 Jahre",
                                    "Keine Angabe"
    
                                ),
# index= None, damit nicht schon eine "Vorauswahl" besteht.
                                index=None
)
#sobald der Teilnehmer den Radio-Button bestätigt, dann soll die Eingabe unter den Schlüssel "alter" gespeichert werden
if alter is not None:
    st.session_state.einstiegsumfrage["alter"]={
    "Bereich": "Einstiegsumfrage",
    "Typ": "Alter",
    "Frage":   fragealter,
    "Antwort": alter
    }
    st.markdown(f"Deine Antwort: {alter}.")


   

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

 st.markdown(f"Deine Antwort: {geschlecht}.")
#Trennungslinie
st.divider()
##############

# Frage KI-Wissen (Selbsteinschätzung)
frage_kiwissen = "Wie gut kennst du dich mit Künstlicher Intelligenz (KI) aus?"
kiwissen = st.radio(
                    frage_kiwissen,
                    ("Sehr gut",
                     "Gut",
                     "Mittel",
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
    st.markdown (f"Deine Antwort: {kiwissen}.")

#Frage: Erkennungsfähigkeit, ob ein Text oder Bild von der KI generiert wurde

frage_erkennungsfaehigkeit = "Wie gut kannst du erkennen, ob ein Text oder Bild von einer KI stammt?"
erkennungsfaehigkeit = st.radio(
    frage_erkennungsfaehigkeit,
    [
        "Sehr gut",
        "Gut", 
        "Mittel",
        "Eher schlecht",
        "Schlecht",
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
    st.markdown(f"Deine Antwort: {erkennungsfaehigkeit}.")

#########################

# Nutzunghäufigkeit (Vodafone2024) S. 11 , Gerlich Studie 2025
#Frage, wie oft KI-Anwendungen genutzt werden
fragehaeufigkeitkinutzung = "Wie oft nutzt du KI-Anwendungen (z. B. ChatGPT, DALL·E, Perplexity usw.)?"
haeufigkeitkinutzung = st.radio(
                                fragehaeufigkeitkinutzung,
                                ("Täglich",
                                "Mehrmals die Woche",
                                "Einmal pro Woche",
                                "Einmal pro Monat",
                                "Seltener als einmal pro Monat",
                                "Nie",
                                "Keine Angabe"),
                                 index=None,
)
if haeufigkeitkinutzung is not None:
    st.session_state.einstiegsumfrage["haeufigkeitsnutzung"]={
    "Bereich": "Einstiegsumfrage",
    "Typ": "Häufigkeitsnutzung",
    "Frage": fragehaeufigkeitkinutzung,
    "Antwort": haeufigkeitkinutzung,
    
    }
    st.markdown(f"Deine Antwort: {haeufigkeitkinutzung}")
   
#Trennungslinie
st.divider()

#Frage für wie sehr KI Inhalten vertraut wird
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
    st.markdown(f"Deine Antwort: {vertrauenkiinhalten}")


#Frage ob KI-generierte Inhalte geprüft werden

fragepruefungvorher = "Wie genau prüfst du KI-generierte Inhalte, bevor du ihnen vertraust?"
pruefungvorher = st.radio(
                fragepruefungvorher,
                ("Sehr genau - ich prüfe alles, bis ins kleinste Detail",
                 "Eher genau - ich prüfe, aber nicht alles bis ins kleinste Detail",
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
    st.markdown(f"Deine Antwort: {pruefungvorher}")
    



#Anzeigen der gespeicherten Eingaben, zur Überprüfung
#st.session_state.einstiegsumfrage

#Trennungslinie
st.divider()

#Button zur nächsten Seite
st.markdown("Um fortzufahren, klicke auf \"Weiter\"")
st.markdown("Aktueller Fortschritt in der gesamten Lerneinheit: 1 von 7")
st.progress (1/7)

#Anpassung des Layouts des Buttons
col1, col2 = st.columns([8,2])
with col2:

    if st.button("Weiter"):
        unbeantwortet = False
#Prüfung, ob alle Eingaben erfolgt sind
        if alter is None:
            st.error("Bitte gib dein Alter an.")
            unbeantwortet = True
        if geschlecht is None:
            st.error("Bitte gib dein Geschlecht an.")
            unbeantwortet = True
        if kiwissen is None:
            st.error("Bitte gib deinen Wissensstand an.")
            unbeantwortet = True
        if erkennungsfaehigkeit is None:
            st.error ("Bitte gib deine Einschätzung zur Erkennung von KI-generierten Inhalten an.")
            unbeantwortet = True
        if haeufigkeitkinutzung is None:
            st.error ("Bitte gib an, wie häufig du KI nutzt.")
            unbeantwortet = True
        if vertrauenkiinhalten is None:
            st.error ("Bitte gib an, wie sehr du KI-generierten Inhalten vertraust")
            unbeantwortet = True
        if pruefungvorher is None:
            st.error ("Bitte gib an, ob du KI prüfst.")
            unbeantwortet = True
 #Wenn alle Pflichtfelder beantwortet sind, dann kann der Teilnehmer auf die nächste Seite
        if not unbeantwortet:
            st.switch_page("pages/3_Grundwissen_Ki.py")