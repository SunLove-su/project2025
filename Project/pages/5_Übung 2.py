"""
Übung 2: Vorgegebenes KI-generiertes Bild
Bewertung der Teilnehmer, ob das Bild echt oder KI-generiert ist

"""
import streamlit as st
import openai
import hilfsdatei
import pathlib
import os


#Überschrift der Seite 
titel_seite = "2. Übung"
hilfsdatei.seite(titel_seite)
#Sicherstellen, dass ein Zugriff der Seiten nur mit Passwort erfolgt, und dass User keine Navigationsseite sehen
hilfsdatei.teilnehmer_anmelden()
 
#Überschrift auf der Seite
ueberschrift_seite ="2. Übung"
st.markdown(f"<h4>{ueberschrift_seite}</h4>",unsafe_allow_html=True)

#Einleitung zur Übung 2
einleitung_text =("""
                In dieser Übung sollst du ein Bild bewerten.
                Du siehst ein Bild einer Person und sollst angeben, ob das Bild
                von einer echten Person oder von einer KI generiert ist"""
                 )

st.markdown(einleitung_text)

#Trennungslinie
st.divider()
##Aufgabenstellung
st.markdown("""
                Schaue dir das Bild genau an! Hat die Person auf dem Foto an dem schönen Sommertag ein Erdbeereis gegessen?
            """)

#Sicherstellen, dass das Bild zur Verfügung steht

bilduebung_vorhanden = False
#Anzeigen des generierten Bildes im Disney-Stil            
try:
    #Das Bild muss im Root Folder des Git-Repositories liegen, damit das so funktioniert         
    st.image("ErdbeereisMann.png",width=200)
    bilduebung_vorhanden = True
except:
    pass

#Nur wenn das Bild nicht vorhanden ist, dann wird es aus der URL geladen.
if not bilduebung_vorhanden:
    try:
        #Alternativ wenn das Bild nicht im Root-Verzeichnis gefunden wird
        st.image("https://github.com/SunLove-su/project2025/raw/main/ErdbeereisMann.png", width=200) 
    except:
        #Falls kein Bild verfügbar sit
        st.error("Das Bild ist nicht verfügbar, bitte mach weiter mit der Übung.")


#Speichern der Antworten in Übung 2
if "uebung2" not in st.session_state:
    st.session_state.uebung2 = {}

#######################################################################
#Frage ob die Teilnehmer glauben, dass die Person auf dem Bild echt ist
frage_person_echt = "Wie wahrscheinlich ist es, dass die Person auf dem Bild echt ist?"

antwort_person_echt=st.radio(frage_person_echt,
                  ("Sehr wahrscheinlich echt",
                    "Eher wahrscheinlich echt",
                    "Unentschieden",
                    "Eher wahrscheinlich KI-generiert", 
                    "Sehr wahrscheinlich KI-generiert"),
                    index=None,
                    
                    )

if "anzahl_person_echt" not in st.session_state:
    st.session_state.anzahl_person_echt = 0
if "person_echt_alt" not in st.session_state:  
    st.session_state.person_echt_alt = None    
if "bildeinschaetzung_historie" not in st.session_state.uebung2:
    st.session_state.uebung2["bildeinschaetzung_historie"] = []

# Speicherung nur bei Änderung der Antwort
if antwort_person_echt is not None and antwort_person_echt != st.session_state.person_echt_alt:
    st.session_state.anzahl_person_echt += 1
    
    bildeinschaetzung = {
        "Bereich": "Übung2",
        "Typ": "Bild-Echt-Einschätzung",
        "Frage": frage_person_echt,
        "Antwort": antwort_person_echt,
        "Anzahl_Aenderungen": st.session_state.anzahl_person_echt
    }
    
    st.session_state.uebung2["bildeinschaetzung_historie"].append(bildeinschaetzung)
    st.session_state.uebung2["bildeinschaetzung"] = bildeinschaetzung
    # Aktuelle Antwort merken
    st.session_state.person_echt_alt = antwort_person_echt
    
    st.markdown(f"Deine Antwort ist: {antwort_person_echt}.")

###########################################################
#Frage wie sicher die Teilnehmer bei der Antwort sind
frage_sicherheit_bild = "Wie sicher bist du bei deiner Einschätzung?"
antwort_sicherheit_bild = st.radio(frage_sicherheit_bild,
                                        (
                                            "Sehr sicher",
                                            "Eher sicher",
                                            "Neutral", 
                                            "Eher unsicher",
                                            "Sehr unsicher"
                                        ),index=None
                                        )

if "anzahl_sicherheit" not in st.session_state:
    st.session_state.anzahl_sicherheit = 0
if "sicherheit_bild_alt" not in st.session_state:
    st.session_state.sicherheit_bild_alt = None
if "sicherheit_historie" not in st.session_state.uebung2:
    st.session_state.uebung2["sicherheit_historie"] = []

# Speicherung nur bei Änderung der Antwort
if antwort_sicherheit_bild is not None and antwort_sicherheit_bild != st.session_state.sicherheit_bild_alt:
    st.session_state.anzahl_sicherheit += 1
    
    sicherheit = {
        "Bereich": "Übung2", 
        "Typ": "Sicherheit-Einschätzung",
        "Frage": frage_sicherheit_bild,
        "Antwort": antwort_sicherheit_bild,
        "Anzahl_Aenderungen": st.session_state.anzahl_sicherheit
    }
    
    st.session_state.uebung2["sicherheit_historie"].append(sicherheit)
    st.session_state.uebung2["sicherheit_einschaetzung"] = sicherheit
    # Aktuelle Antwort merken
    st.session_state.sicherheit_bild_alt = antwort_sicherheit_bild
    
    st.markdown(f"Deine Antwort: {antwort_sicherheit_bild}.")
################################################################################################
st.divider()
##############################################################################################
st.markdown("Um fortzufahren, klicke auf \"Weiter\"")
st.markdown("Aktueller Fortschritt in der gesamten Lerneinheit: 4 von 8")
st.progress (4/8)


if st.button("Weiter"):
    unbeantwortet = False
    if antwort_person_echt is None:
        st.error("Bitte beantworte die Frage, ob die Person auf dem Bild echt ist.")
        unbeantwortet = True
    if antwort_sicherheit_bild is None:
        st.error("Bitte gib an, wie sicher du bei deiner Einschätzung bist.")
        unbeantwortet = True
    
    if not unbeantwortet:
        naechste_seite = "pages/6_Übung 3.py"
        st.switch_page(naechste_seite)