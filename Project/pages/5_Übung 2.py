import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(
    page_title="2. Übung"
)
st.markdown("<h4>2. Übung</h4>",unsafe_allow_html=True)

if "fragen_uebung2" not in st.session_state:
    st.session_state.fragen_uebung2 = {}
if "antworten_uebung2" not in st.session_state:
    st.session_state.antworten_uebung2 = {}


if "uebung2" not in st.session_state:
    st.session_state.uebung2 ={}

fragen   = st.session_state.fragen_uebung2   
antworten = st.session_state.antworten_uebung2

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

             
#Ausgabe der Antwort 
st.session_state.fragen_uebung2["frage_personecht"] = frage_personecht

if personecht is not None:
    st.write("Deine Antwort ist:", personecht)
    fragen["personecht"]   = frage_personecht 
    antworten["personecht"] = personecht
    st.session_state.uebung2["personecht"] = {
    "Frage":   frage_personecht,
    "Antwort": personecht
     }

    st.session_state.uebung2

st.divider()
st.markdown("Um fortzufahren, klicke auf \"weiter\" ")
col1, col2 = st.columns([8,2])
with col2:

    if st.button("weiter"):
        unbeantwortet = (personecht is None)
        if unbeantwortet:
            st.error("Bitte beantworte alle Fragen, um fortzufahren.")
        else: 
                
            st.switch_page("pages/6_Übung 3.py")