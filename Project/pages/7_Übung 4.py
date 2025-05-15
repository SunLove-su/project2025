import streamlit as st
import openai
import hilfsdatei

try: 
    client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])
except KeyError:
    st.error("Kein API Key für OpenAI vorhanden. Abfragen über OpenAI nicht möglich")

hilfsdatei.seite("4. Übung")
hilfsdatei.login()   


st.markdown("<h4>4. Übung</h4>",unsafe_allow_html=True)

st.markdown("""
            In der vorigen Übung hast du gesehen, dass in den Ausgaben der KI mit den Berufen
            Vorurteile ausgegeben wurden. Das kann ab und zu geschehen, da die KI mit vielen Daten trainiert wurde
            und in diesen diese Vorurteile enthalten sind.

            Jetzt erstellst du selbst Bilder mit der KI-Anwendung DALL E.

            """)
        
st.divider()

st.markdown("""
               Mit KI-Anwendungen haben Nutzer von sich Bilder in unterschiedlichen bekannten Stilen, z. B. sich als Anime oder Disneyfigur erstellt.
               Anstatt ein ein persönliches Bild hochzuladen, wird das Bild mithilfe eines Prompts erzeugt.

                "***Prompt:*** Erstelle mir ein Bild von Cinderella im Disney-Stil mit kurzen Haaren, einem Business-Outfit und einem Kaffee in der Hand."
                Erzeugte mir das unten aufgeführte Bild. Es gab Anpassungen bei der KI-Anwendung und jetzt werden die Bilder nicht so identisch im Disney-Stil erzeugt.
                Versuche es selbst, kriegst du kein Bild, dann musst du deinen Prompt anpassen.
            """)
            
try:         
    st.image("Cinderella.png",width=200)
except FileNotFoundError:
    st.error("Das Bild ist nicht verfügbar, bitte mach weiter mit der Übung.")

# bildanzeigen_button=st.button("Zeige mir das Bild", key="bildanzeigenlassen")
# #Erstelle mir ein Bild von Cinderella im Disney-Stil mit kurzen Haaren, einem Business-Outfit und einem Kaffee in der Hand.
# # 
# #
# if bildanzeigen_button:
#     st.image("Cinderella.png",width=200)
        
st.divider()

#Speichern der Prompts:

if "uebung4" not in st.session_state:
    st.session_state.uebung4 ={}

if "anzahl_bildgenerierungen" not in st.session_state:
    st.session_state.anzahl_bildgenerierungen = 0
#tab1 = st.tabs(["Bildgenerierung"])[0]
#with tab1:
containerfokus = st.container()
with containerfokus:
    with st.expander("Bildgenerierung", expanded=True):    
        # Eingabe und Button
        with st.form("frage_formular4", clear_on_submit=True):
            st.markdown(
            """Jetzt bist du wieder dran! Du kannst dir nun ein Bild mithilfe der KI erstellen lassen. Anstatt ein Bild hochzuladen, beschreibe das Bild,
            was du erstellen lassen möchtest.
                """)
            eingabe = st.text_input("Bitte beschreibe, wie dein Bild generiert werden soll",placeholder="z. B. Erstelle mir ein Bild von einer jungen Frau mit braunen Haaren in einem Kleid im Disney-Stil")
            beschreibung=(f"Stelle nur eine Person oder ein Tier dar: {eingabe}")
            senden = st.form_submit_button("erstellen")
            # Antwort generierung erst wenn Button geklickt und Eingabe vorhanden
            
        #https://platform.openai.com/docs/guides/error-codes/api-errors.
        try:
            if senden and eingabe:
                with st.spinner(text="Generiere Bild, bitte warten..."):
                    st.session_state.anzahl_bildgenerierungen += 1
                    aktuelle_anzahl = st.session_state.anzahl_bildgenerierungen
                    
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
                    
                    
                    if "BildgenerierenKI" not in st.session_state.uebung4:
                        st.session_state.uebung4["BildgenerierenKI"] = []
                    
                    st.session_state.uebung4["BildgenerierenKI"].append({
                        "Bereich": "Übung4",
                        "Typ": "DALL-E Bilderstellung",
                        "Frage": "Bitte beschreibe, wie dein Bild generiert werden soll",
                        "Antwort": eingabe,
                        "Anzahl Bildgenerierungen": aktuelle_anzahl
                    })
                    st.session_state.uebung4["BildgenerierenKI"]

        except Exception as error:
            hilfsdatei.openai_fehlerbehandlung(error)

                




    st.markdown("""
                    Siehst du, du hast ein Bild generieren lassen.

                    """)
#Speichern der Prompts:
fragedatenschutz = "Würdest du von dir ein Bild generieren lassen, indem du ein Bild von dir hochlädst?"
datenschutz=st.radio(fragedatenschutz,
    ["Ja, ich würde ein Bild von mir hochladen",
     "Neutral",
     "Nein, ich würde kein Bild von mir hochladen",
     "Keine Angabe"
    ], index=None
    )
 #Ausgabe der Antwort
if datenschutz is not None:
    
    st.session_state.uebung4["datenschutz"] = {
        "Bereich":"Übung4",
        "Typ" : "Datenschutz",
        "Frage" : fragedatenschutz,
        "Antwort": datenschutz
    }
    st.write("Deine Antwort ist:",datenschutz)
frageurheberrecht="Findest du es in Orndung, dass Bilder im Stil von bekannten Firmen und Künstlern innerhalb von Minuten generiert werden, obwohl diese Jahre lang daran arbeiten?"
urheberrecht=st.radio(frageurheberrecht,
                                  ["Ja, ich finde es in Ordnung",
                                   "Neutral",
                                   "Nein, ich finde es nicht in Ordnung",
                                   "Keine Angabe"
                                   ], index=None
                        )
if urheberrecht is not None:
        
        st.session_state.uebung4["urheberrecht"]={
            "Bereich":"Übung4",
            "Typ": "Urheberrecht",
            "Frage": frageurheberrecht,
            "Antwort": urheberrecht
        }
        st.write("Deine Antwort ist:",urheberrecht)
    
st.session_state.uebung4
st.divider()
st.markdown("Um fortzufahren, klicke auf \"weiter\" ")
col1, col2 = st.columns([8,2])
with col2:

    if st.button("weiter"):
        unbeantwortet = False
        if datenschutz is None:
            st.error("Bitte beantworte die Frage mit dem Datenschutz.")
            unbeantwortet = True
        if urheberrecht is None:
            st.error("Bitte beantworte die Frage mit dem Urheberrecht.")
            unbeantwortet = True
        if "BildgenerierenKI" not in st.session_state.uebung4:
            st.error("Bitte lass von der KI ein Bild generieren.")
            unbeantwortet = True
        
        if not unbeantwortet:
            st.switch_page("pages/8_Abschlussumfrage.py")
