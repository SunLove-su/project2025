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
hilfsdatei.seite("2. Übung")
#Sicherstellen, dass ein Zugriff der Seiten nur mit Passwort erfolgt, und dass User keine Navigationsseite sehen
hilfsdatei.login()
 
#Überschrift auf der Seite
st.markdown("<h4>2. Übung</h4>",unsafe_allow_html=True)

#Einleitung zur Übung 2
st.markdown("""
                In dieser Übung sollst du ein Bild bewerten.
                Du siehst ein Bild einer Person und sollst angeben, ob das Bild
                von einer echten Person oder von einer KI generiert ist"""
            )

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
frage_personecht = "Glaubst du die Person auf dem Bild ist echt?"

personecht=st.radio(frage_personecht,
                    ["Ja, ich glaube die Person auf dem Bild ist echt",
                     "Ich bin mir nicht sicher",
                     "Nein, es handelt sich um ein KI-generiertes Bild",
                     "Keine Angabe"],
                    index=None,
                    
                    )
#Antworten speichern
if personecht is not None:
    st.session_state.uebung2["bildeinschaetzung"] = {
    "Bereich": "Übung2",
    "Typ": "Bild-Echt-Einschätzung",
    "Frage":   frage_personecht,
    "Antwort": personecht
     }
    st.write("Deine Antwort ist:", personecht)
    st.session_state.uebung2

st.divider()
st.markdown("Um fortzufahren, klicke auf \"Weiter\"")
st.markdown("Aktueller Fortschritt in der gesamten Lerneinheit: 4 von 7")
st.progress (4/7)


if st.button("Weiter"):
    unbeantwortet = False
    if personecht is None:
        st.error("Bitte beantworte die Frage, ob die Person auf dem Bild echt ist.")
        unbeantwortet = True
    
    if not unbeantwortet:
        st.switch_page("pages/6_Übung 3.py")