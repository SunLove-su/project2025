"""
Übung 2: Vorgegebenes KI-generiertes Bild
Bewertung der Teilnehmer, ob das Bild echt oder KI-generiert ist

"""
import streamlit as st
import openai
import hilfsdatei

#Verbindung zu OpenAI
try: 
    client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])
#Fehlermeldung, falls der API-Schlüssel falsch ist
except KeyError:
    st.error("Kein API Key für OpenAI vorhanden. Abfragen über OpenAI nicht möglich")
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

# st.image("https://thispersondoesnotexist.com/",width=200)
#Sicherstellen, dass das Bild zur Verfügung steht
try:
    st.image("ErdbeereisMann.png", width=200)
except FileNotFoundError:
    st.error("Das Bild konnte nicht gefunden werden, die Übung kannst du trotzdem fortsetzen")

#Speichern der Antworten in Übung 2
if "uebung2" not in st.session_state:
    st.session_state.uebung2 ={}

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
#Antworten speichern
if antwort_person_echt is not None:
    st.session_state.uebung2["bildeinschaetzung"] = {
    "Bereich": "Übung2",
    "Typ": "Bild-Echt-Einschätzung",
    "Frage":   frage_person_echt,
    "Antwort": antwort_person_echt
     }
    st.write(f"Deine Antwort ist: {antwort_person_echt}.")
    st.session_state.uebung2

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

if antwort_sicherheit_bild is not None:
    st.session_state.uebung2["sicherheit_einschaetzung"] = {
        "Bereich": "Übung2",
        "Typ": "Sicherheit-Einschätzung", 
        "Frage": frage_sicherheit_bild,
        "Antwort": antwort_sicherheit_bild
    }
    st.markdown(f"Deine Antwort: {antwort_sicherheit_bild}.")

st.divider()
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