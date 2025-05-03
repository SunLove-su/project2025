import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(
    page_title="5. Übung"
 )
st.markdown("<h4>5. Übung</h4>",unsafe_allow_html=True)

st.markdown("""
            In der Übung zuvor haben wir die Person gesehen, die das Eis isst.
            Bei dem Bild handelt es sich um ein Ki-generiertes Bild, dass sehr echt aussieht.
            KI-generierte Bilder können sehr real und echt aussehen.

            Für KI-generierte Bilder wird der Deep Learning Algorithmus Generative Adversarial Networks GAN verwendet.

            """)
        
st.divider()
st.markdown("""
                Jetzt erstellen wir selbst Bilder, dass machen wir genauso wie in der 1. Übung.
                Wir schreibenen in den Prompt, wass uns die KI-Anwendung generieren soll.

            """)

#Erstelle mir einen Satz mit einem schönen Sommertag und Erdbeereis. Der Satz soll keine ausschweifende Beschreibungen enthalten
st.markdown("""
               Ich möchte am Trend teilnehmen und mir ein Bild generieren lassen.
               Jedoch lade ich nicht mein Bild hoch sondern beschreibe im Prompt, wie das Bild aussehen soll.

                "Erstelle mir ein Bild von Cinderella im Disney-Stil mit kurzen Haaren, einem Business-Outfit und einem Kaffee in der Hand."
            """)


bildanzeigen_button=st.button("Zeige mir das Bild", key="bildanzeigenlassen")
#Erstelle mir ein Bild von Cinderella im Disney-Stil mit kurzen Haaren, einem Business-Outfit und einem Kaffee in der Hand.
# 
#
if bildanzeigen_button:
    st.image("Cinderella.png",width=200)
        
st.divider()
st.markdown(
    """Jetzt bist du an der Reihe, bitte beschreibe das Bild, dass DALL E für dich generieren soll.
        """)
#Speichern der Prompts:
if "alle_eingaben" not in st.session_state:
     st.session_state.alle_eingaben = []

# Eingabe und Button
eingabe = st.text_input("Bitte beschreibe, wie dein Bild generiert werden soll",placeholder="z. B. Erstelle mir ein Bild von einer jungen Frau mit braunen Haaren in einem Kleid im Disney-Stil")
beschreibung=(f"{eingabe} stelle immer nur eine Person oder Tier dar.")
if st.button("Bild erstellen") and beschreibung:
    with st.spinner(text="Generiere Bild, bitte warten..."):
    # Antwort holen
        antwort = client.images.generate(
        model="dall-e-3",
        prompt=beschreibung,
        n=1,
        size="1024x1024"

    )
    
    # Antwort zeigen
    st.write("Bild:")
        # Bild anzeigen
    generiertesBild = antwort.data[0].url
    st.image(generiertesBild)
    st.session_state.alle_eingaben.append(eingabe)
   
    st.session_state.alle_eingaben
  
    st.divider()


    st.markdown("""
                    Siehst du, du hast ein Bild generieren lassen.

                    """)
    st.divider()
#Speichern der Prompts:
if "antworten_uebung5" not in st.session_state:
        st.session_state.antworten_uebung5 = {}
datenschutz=st.radio("Würdest du von dir ein Bild im Disney-Stil generieren lassen, indem du ein Bild von dir hochlädst?",
    ["Ja, ich würde ein Bild von mir hochladen",
     "Neutral",
     "Nein, ich würde kein Bild von mir hochladen",
     "Keine Angabe"
    ], index=None
    )
        #Ausgabe der Antwort 

if datenschutz is not None:
        st.write("Deine Antwort ist:", datenschutz)
        st.session_state.antworten_uebung5["datenschutz"]=datenschutz
        st.session_state.antworten_uebung5
urheberrecht=st.radio("Findest du es in Orndung, dass Bilder im Stil von bekannten Firmen und Künstlern innerhalb von Minuten generiert werden, obwohl diese Jahre lang daran arbeiten?",
                                  ["Ja, ich finde es in Ordnung",
                                   "Neutral",
                                   "Nein, ich finde es nicht in Ordnung",
                                   "Keine Angabe"
                                   ], index=None
                        )
if urheberrecht is not None:
        st.write("Deine Antwort ist:",urheberrecht)
        st.session_state.antworten_uebung5["urheberrecht"]=urheberrecht
        st.session_state.antworten_uebung5
    
st.divider()
st.markdown("Um fortzufahren, klicke auf \"weiter\" ")
col1, col2 = st.columns([8,2])
with col2:

    if st.button("weiter"):
        st.switch_page("pages/9_Abschlussumfrage.py")
