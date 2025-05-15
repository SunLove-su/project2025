import streamlit as st
import openai
import hilfsdatei

try: 
    client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])
except KeyError:
    st.error("Kein API Key für OpenAI vorhanden. Abfragen über OpenAI nicht möglich")

hilfsdatei.seite("2. Übung")
hilfsdatei.login()
 

st.markdown("<h4>2. Übung</h4>",unsafe_allow_html=True)


if "uebung2" not in st.session_state:
    st.session_state.uebung2 ={}



frage_personecht = "Glaubst du die Person auf dem Bild ist echt?"

st.write("Hat die Person auf dem Foto an dem schönen Sommertag ein Erdbeereis gegessen?")
# st.image("https://thispersondoesnotexist.com/",width=200)
try:
    st.image("ErdbeereisMann.png", width=200)
except FileNotFoundError:
    st.error("Das Bild konnte nicht gefunden werden, die Übung kannst du trotzdem fortsetzen")
personecht=st.radio(frage_personecht,
                    ["Ja, ich glaube die Person auf dem Bild ist echt",
                     "Ich bin mir nicht sicher",
                     "Nein, es handelt sich um ein KI-generiertes Bild",
                     "Keine Angabe"],
                    index=None,
                    
                    )

             

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
st.markdown("Um fortzufahren, klicke auf \"weiter\" ")
col1, col2 = st.columns([8,2])
with col2:

    if st.button("weiter"):
        unbeantwortet = False
        if personecht is None:
            st.error("Bitte beantworte die Frage, ob die Person auf dem Bild echt ist.")
            unbeantwortet = True
        
        if not unbeantwortet:
            st.switch_page("pages/6_Übung 3.py")