import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

# st.set_page_config(
#     page_title="3. Übung"
# )
st.markdown("<h4>3. Übung</h4>",unsafe_allow_html=True)

st.markdown("""
            In dieser Übung schauen wir uns an, wer an dem schönen Sommertag ein Erdbeereis gegessen hat

            """)
st.divider()
if "antworten_uebung3" not in st.session_state:
    antworten_uebung3 = {}
st.write("An den schönen Sommertag hat die  Person auf dem Foto ein Erdbeereis gegessen")
# st.image("https://thispersondoesnotexist.com/",width=200)
st.image("ErdbeereisMann.png", width=200)
personecht=st.radio("Glaubst du die Person auf dem Bild ist echt?",
                    ["Ja, ich glaube die Person auf dem Bild ist echt",
                     "Ich bin mir nicht sicher",
                     "Nein, es handelt sich um ein Ki-generiertes Bild",
                     "Keine Angabe"],
                    index=None,
                    
                    )

#Speichern der Prompts:
if "antworten_uebung3" not in st.session_state:
     st.session_state.antworten_uebung3 = {}                 
#Ausgabe der Antwort 

if personecht is not None:
    st.write("Deine Antwort ist:", personecht)
    st.session_state.antworten_uebung3["personecht"]=personecht
    st.session_state.antworten_uebung3

st.divider()
st.markdown("Um fortzufahren, klicke auf \"weiter\" ")
col1, col2 = st.columns([8,2])
with col2:

    if st.button("weiter"):
        st.switch_page("pages/6_Übung 4.py")