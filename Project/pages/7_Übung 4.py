import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(
    page_title="4. Übung"
 )
st.markdown("<h4>4. Übung</h4>",unsafe_allow_html=True)

st.markdown("""
            In der vorigen Übung hast du gesehen, dass in den Ausgaben der KI mit den Berufen
            Vorurteile ausgegeben wurden. Das kann ab und zu geschehen, da die KI mit vielen Daten trainiert wurde
            und in diesen diese Vorurteile enthalten sind.

            Jetzt erstellst du selbst Bilder mit der KI-Anwendung DALL E.

            """)
        
st.divider()

st.markdown("""
               Mit KI-Anwendungen erstellen zur Zeit Nutzer von sich Bilder in unterschiedlichen bekannten Stilen, z. B. sich als Anime oder Disneyfigur.
               Anstatt ein ein persönliches Bild hochzuladen, wird das Bild mithilfe eines Prompts erzeugt.

                "***Prompt:*** Erstelle mir ein Bild von Cinderella im Disney-Stil mit kurzen Haaren, einem Business-Outfit und einem Kaffee in der Hand."
            """)
            
            
st.image("Cinderella.png",width=200)

# bildanzeigen_button=st.button("Zeige mir das Bild", key="bildanzeigenlassen")
# #Erstelle mir ein Bild von Cinderella im Disney-Stil mit kurzen Haaren, einem Business-Outfit und einem Kaffee in der Hand.
# # 
# #
# if bildanzeigen_button:
#     st.image("Cinderella.png",width=200)
        
st.divider()

#Speichern der Prompts:
if "alle_eingaben" not in st.session_state:
     st.session_state.alle_eingaben = []

# Eingabe und Button
with st.form("frage_formular4", clear_on_submit=True):
    st.markdown(
    """Jetzt bist du wieder dran! Du kannst dir nun ein Bild mithilfe der KI erstellen lassen. Anstatt ein Bild hochzuladen, beschreibe das Bild,
     was du erstellen lassen möchtest.
        """)
    eingabe = st.text_input("Bitte beschreibe, wie dein Bild generiert werden soll",placeholder="z. B. Erstelle mir ein Bild von einer jungen Frau mit braunen Haaren in einem Kleid im Disney-Stil")
    beschreibung=(f"Stelle nur eine Person/Tier darf{eingabe}")
    senden = st.form_submit_button("erstellen")
    # Antwort generierung erst wenn Button geklickt und Eingabe vorhanden
    if senden and eingabe:
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
        st.image(generiertesBild, width=200)
        st.session_state.alle_eingaben.append(eingabe)

        st.session_state.alle_eingaben




    st.markdown("""
                    Siehst du, du hast ein Bild generieren lassen.

                    """)
#Speichern der Prompts:
if "antworten_uebung5" not in st.session_state:
        st.session_state.antworten_uebung5 = {}
datenschutz=st.radio("Würdest du von dir ein Bild generieren lassen, indem du ein Bild von dir hochlädst?",
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
        unbeantwortet = (datenschutz is None or urheberrecht is None)
        if unbeantwortet:
            st. error("Bitte beantworte alle Fragen, um fortzufahren.")
        else: 
            st.switch_page("pages/8_Abschlussumfrage.py")
