"""
Einstiegsumfragen (Pre-Tests)
Erfragung von KI-Kenntnissen, Nutzung usw.
"""

import streamlit as st
import hilfsdatei
 
#Überschrift der Seite
titel_seite = "Einstiegsumfrage"
hilfsdatei.seite(titel_seite)
#Alle Seiten mit PW versehen, dass weiterhin die Teilnehmer die Navigation nicht sehen
hilfsdatei.teilnehmer_anmelden()

ueberschrift_seite = "Einstiegsumfrage"
#Überschrift der Sektion
st.markdown(f"<h4>{ueberschrift_seite}</h4>",unsafe_allow_html=True)

#Einleitung der Sektion
einleitung_text = (
            """
                Die Umfrage erfasst deine persönliche Erfahrung und Einschätzung
                von KI.
                Die Antworten werden nur im Rahmen dieser Arbeit ausgewertet.           
           """)
st.markdown(einleitung_text)
##########################################################################################
#Trennungslinie
st.divider()
#########################################################################################

if "einstiegsumfrage" not in st.session_state:
    st.session_state.einstiegsumfrage ={}

#Zur Speicherung der Anzahl der Auswahlmögochkeit
if "anzahl_alter" not in st.session_state:
    st.session_state.anzahl_alter = 0
if "anzahl_geschlecht" not in st.session_state:
    st.session_state.anzahl_geschlecht = 0
if "anzahl_ki_wissen" not in st.session_state:
    st.session_state.anzahl_ki_wissen = 0
if "anzahl_erkennung_ki" not in st.session_state:
    st.session_state.anzahl_erkennung_ki = 0
if "anzahl_nutzung_ki" not in st.session_state:
    st.session_state.anzahl_nutzung_ki = 0
if "anzahl_vertrauen_ki" not in st.session_state:
    st.session_state.anzahl_vertrauen_ki = 0
if "anzahl_pruefung_ki" not in st.session_state:
    st.session_state.anzahl_pruefung_ki = 0

# Demografische Daten

#Frage nach dem Alter der Teilnehmenden
#Alter der Jugendlichen in den Studien Vodafone(2024) = 14-20, Sinus (2024) = 14-17
frage_alter = "Wie alt bist du?"
antwort_alter = st.radio (frage_alter,
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

#Speicherung der Antwort
if antwort_alter is not None:
    st.session_state.anzahl_alter +=1
    #Speicherung aller Antworten
    if "alter_historie" not in st.session_state.einstiegsumfrage:
        st.session_state.einstiegsumfrage["alter_historie"]=[]
    #Festlegung der Speichervariablen
    alter = {
        "Bereich": "Einstiegsumfrage",
        "Typ": "Alter",
        "Frage":   frage_alter,
        "Antwort": antwort_alter,
        "Anzahl_Aenderungen":st.session_state.anzahl_alter
    }
    #Hinzufügen aller Einträge
    st.session_state.einstiegsumfrage["alter_historie"].append(alter)
    #Speichern des letzten Eintrags
    st.session_state.einstiegsumfrage["alter"]= alter

st.markdown(f"Deine Antwort: {antwort_alter}.")

st.session_state.einstiegsumfrage

###############################################################################################

# Frage Geschlecht:
frage_geschlecht = "Welchem Geschlecht fühlst du dich zugehörig?"
antwort_geschlecht = st.radio(frage_geschlecht,
                                  ("Weiblich",
                                   "Männlich",
                                   "Divers",
                                   "Keine Angabe"
                                   ),
                                   index=None
)

#Speicherung der Antwort
if antwort_geschlecht is not None:
    st.session_state.anzahl_geschlecht += 1
    if "geschlecht_historie" not in st.session_state.einstiegsumfrage:
        st.session_state.einstiegsumfrage["geschlecht_historie"]=[]
    geschlecht = {
        "Bereich":"Einstiegsumfrage",
        "Typ":"Geschlecht",
        "Frage": frage_geschlecht,
        "Antwort": antwort_geschlecht,
        "Anzahl_Aenderungen": st.session_state.anzahl_geschlecht 
    }
    st.session_state.einstiegsumfrage["geschlecht_historie"].append(geschlecht)
    st.session_state.einstiegsumfrage["geschlecht"]=geschlecht
    st.markdown(f"Deine Antwort: {antwort_geschlecht}.")

################################################################################
#Trennungslinie
st.divider()
################################################################################

# Frage KI-Wissen (Selbsteinschätzung)
frage_ki_wissen = "Wie gut kennst du dich mit Künstlicher Intelligenz (KI) aus?"
antwort_ki_wissen = st.radio(
                    frage_ki_wissen,
                    ("Sehr gut",
                     "Gut",
                     "Mittelmäßig",
                     "Eher schlecht",
                     "Schlecht",
                     "Keine Angabe"),
    index=None
)

#Speicherung der Antwort
if antwort_ki_wissen is not None:
    st.session_state.anzahl_ki_wissen += 1
    if "ki_wissen_historie" not in st.session_state.einstiegsumfrage:
        st.session_state.einstiegsumfrage["ki_wissen_historie"] = []
    ki_wissen = {
        "Bereich":"Einstiegsumfrage",
        "Typ": "KI-Wissen",
        "Frage": frage_ki_wissen,
        "Antwort": antwort_ki_wissen,
        "Anzahl_Aenderungen": st.session_state.anzahl_ki_wissen
    }
    st.session_state.einstiegsumfrage["ki_wissen_historie"].append(ki_wissen)
    st.session_state.einstiegsumfrage["ki_wissen"] = ki_wissen
    st.markdown (f"Deine Antwort: {antwort_ki_wissen}.")

#########################################################################################

#Frage: Erkennungsfähigkeit, ob ein Text oder Bild von der KI generiert wurde
frage_erkennung_ki = "Wie gut kannst du erkennen, ob ein Text oder Bild von einer KI stammt?"
antwort_erkennung_ki = st.radio(frage_erkennung_ki,
                        (
                            "Sehr gut",
                            "Gut", 
                            "Mittelmäßig",
                            "Eher schlecht",
                            "Schlecht",
                            "Keine Angabe"
                        ),
                        index=None
                    )

#Speicherung der Antwort
if antwort_erkennung_ki is not None:
    st.session_state.anzahl_erkennung_ki += 1
    if "erkennung_ki_historie" not in st.session_state.einstiegsumfrage:
        st.session_state.einstiegsumfrage["erkennung_ki_historie"] = []
    erkennung_ki = {
        "Bereich": "Einstiegsumfrage",
        "Typ": "Erkennungsfähigkeit",
        "Frage": frage_erkennung_ki,
        "Antwort": antwort_erkennung_ki,
        "Anzahl_Aenderungen": st.session_state.anzahl_erkennung_ki
    }
    st.session_state.einstiegsumfrage["erkennung_ki_historie"].append(erkennung_ki)
    st.session_state.einstiegsumfrage["erkennung_ki"] = erkennung_ki
    st.markdown(f"Deine Antwort: {antwort_erkennung_ki}.")

##################################################################################

# Nutzunghäufigkeit (Vodafone2024) S. 11 , Gerlich Studie 2025
#Frage, wie oft KI-Anwendungen genutzt werden
frage_nutzung_ki = "Wie oft nutzt du KI-Anwendungen (z. B. ChatGPT, DALL·E, Perplexity usw.)?"
antwort_nutzung_ki = st.radio(
                                frage_nutzung_ki,
                                ("Täglich",
                                "Mehrmals pro Woche",
                                "Einmal pro Woche",
                                "Einmal pro Monat",
                                "Seltener",
                                "Nie"),
                                 index=None,
)

# Speicherung der Antwort
if antwort_nutzung_ki is not None:
    st.session_state.anzahl_nutzung_ki += 1
    if "nutzung_ki_historie" not in st.session_state.einstiegsumfrage:
        st.session_state.einstiegsumfrage["nutzung_ki_historie"] = []
    nutzung_ki = {
        "Bereich": "Einstiegsumfrage",
        "Typ": "Häufigkeitsnutzung",
        "Frage": frage_nutzung_ki,
        "Antwort": antwort_nutzung_ki,
        "Anzahl_Aenderungen": st.session_state.anzahl_nutzung_ki
    }
    st.session_state.einstiegsumfrage["nutzung_ki_historie"].append(nutzung_ki)
    st.session_state.einstiegsumfrage["nutzung_ki"] = nutzung_ki
    st.markdown(f"Deine Antwort: {antwort_nutzung_ki}")

#############################################################################
#Trennungslinie
st.divider()
############################################################################

#Frage für wie sehr KI Inhalten vertraut wird
frage_vertrauen_ki = "Wie vertrauenswürdig hältst du KI-generierte Inhalte?"
antwort_vertrauen_ki = st.radio(
                                 frage_vertrauen_ki,
                                ("Sehr vertrauenswürdig",
                                "Eher vertrauenswürdig",
                                "Neutral",
                                "Eher nicht vertrauenswürdig",
                                "Gar nicht vertrauenswürdig"
                                ),
                               index=None
)

# Speicherung der Antwort
if antwort_vertrauen_ki is not None:
    st.session_state.anzahl_vertrauen_ki += 1
    if "vertrauen_ki_historie" not in st.session_state.einstiegsumfrage:
        st.session_state.einstiegsumfrage["vertrauen_ki_historie"] = []
    vertrauen_ki = {
        "Bereich": "Einstiegsumfrage",
        "Typ": "Vertrauen KI Inhalte",
        "Frage": frage_vertrauen_ki,
        "Antwort": antwort_vertrauen_ki,
        "Anzahl_Aenderungen": st.session_state.anzahl_vertrauen_ki
    }
    st.session_state.einstiegsumfrage["vertrauen_ki_historie"].append(vertrauen_ki)
    st.session_state.einstiegsumfrage["vertrauen_ki"] = vertrauen_ki
    st.markdown(f"Deine Antwort: {antwort_vertrauen_ki}")

###################################################################

#Frage ob KI-generierte Inhalte geprüft werden
frage_pruefung_ki = "Wie genau prüfst du KI-generierte Inhalte, bevor du ihnen vertraust?"
antwort_pruefung_ki = st.radio(
                frage_pruefung_ki,
                ("Sehr genau",
                 "Eher genau",
                 "Manchmal",
                 "Eher selten",
                 "Gar nicht"
                 ),
                index=None
)

# Speicherung der Antwort
if antwort_pruefung_ki is not None:
    st.session_state.anzahl_pruefung_ki += 1
    if "pruefung_ki_historie" not in st.session_state.einstiegsumfrage:
        st.session_state.einstiegsumfrage["pruefung_ki_historie"] = []
    pruefung_ki = {
        "Bereich": "Einstiegsumfrage",
        "Typ": "Prüfung KI",
        "Frage": frage_pruefung_ki,
        "Antwort": antwort_pruefung_ki,
        "Anzahl_Aenderungen": st.session_state.anzahl_pruefung_ki
    }
    st.session_state.einstiegsumfrage["pruefung_ki_historie"].append(pruefung_ki)
    st.session_state.einstiegsumfrage["pruefung_ki"] = pruefung_ki
    st.markdown(f"Deine Antwort: {antwort_pruefung_ki}")

####################################################################################################
#Anzeigen der gespeicherten Eingaben, zur Überprüfung
#st.session_state.einstiegsumfrage
#####################################################################################################
#Trennungslinie
st.divider()
#####################################################################################################

#Button zur nächsten Seite
st.markdown("Um fortzufahren, klicke auf \"Weiter\"")
st.markdown("Aktueller Fortschritt in der gesamten Lerneinheit: 1 von 8")
st.progress (1/8)

if st.button("Weiter"):
    unbeantwortet = False
#Prüfung, ob alle Eingaben erfolgt sind
    if antwort_alter is None:
        st.error("Bitte gib dein Alter an.")
        unbeantwortet = True
    if antwort_geschlecht is None:
        st.error("Bitte gib dein Geschlecht an.")
        unbeantwortet = True
    if antwort_ki_wissen is None:
        st.error("Bitte gib deinen Wissensstand an.")
        unbeantwortet = True
    if antwort_erkennung_ki is None:
        st.error ("Bitte gib deine Einschätzung zur Erkennung von KI-generierten Inhalten an.")
        unbeantwortet = True
    if antwort_nutzung_ki is None:
        st.error ("Bitte gib an, wie häufig du KI nutzt.")
        unbeantwortet = True
    if antwort_vertrauen_ki is None:
        st.error ("Bitte gib an, wie sehr du KI-generierten Inhalten vertraust")
        unbeantwortet = True
    if antwort_pruefung_ki is None:
        st.error ("Bitte gib an, ob du KI prüfst.")
        unbeantwortet = True
#Wenn alle Pflichtfelder beantwortet sind, dann kann der Teilnehmer auf die nächste Seite
    if not unbeantwortet:
        naechste_seite ="pages/3_Grundwissen_Ki.py"
        st.switch_page(naechste_seite)