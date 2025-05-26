"""
Übung 3: Bildgenerierung mit DALL-E

Aufklärung,dass das vorherige Bild KI-generiert ist
Vorgegebenenes Beispiel eines generierten Bildes im Disney-Stil
Erwähnung, dass eine Anpassung vorgenommen wurde und die Bilder nicht mehr in dem Stil dargestellt werden
Teilnehmer generieren eigene Bilder
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
titel_seite = "3. Übung"
hilfsdatei.seite(titel_seite)
#Sicherstellen, dass ein Zugriff der Seiten nur mit Passwort erfolgt, und dass User keine Navigationsseite sehen
hilfsdatei.teilnehmer_anmelden() 

#Überschrift auf der Seite
ueberschrift_seite = "3. Übung"
st.markdown(f"<h4>{ueberschrift_seite}</h4>",unsafe_allow_html=True)

#Aufklärung über das vorherige Bild
einleitung_text =("""
            In der Übung zuvor hast du die Person gesehen, die das Eis isst.
            Bei dem Bild handelt es sich um ein KI-generiertes Bild von der Seite "thispersondoesnotexist.com", das sehr echt aussieht.
            
            Für KI-generierte Bilder wird der Deep Learning Algorithmus Generative Adversarial Networks (GAN) verwendet.
            """)
st.markdown(einleitung_text)

frage_bild_realistisch="Wie realistisch fandest du das Bild von der vorherigen Übung?"
antwort_bild_realistisch=st.radio(frage_bild_realistisch,
                                  ("Sehr realisitisch",
                                   "Eher realisitisch",
                                   "Mittelmäßig",
                                   "Eher unrealistisch",
                                   "Sehr unrealisitisch",
                                   "Keine Angabe"),
                                    index=None
                        )
if antwort_bild_realistisch is not None:
        
        st.session_state.uebung3["bild_realistisch"]={
            "Bereich":"Übung3",
            "Typ": "KI Bild Realistisch",
            "Frage": frage_bild_realistisch,
            "Antwort": antwort_bild_realistisch
        }
        st.write(f"Deine Antwort ist: {antwort_bild_realistisch}.")


#Aufgabenstellung für die Teilnehmer
st.markdown("""
            Jetzt erstellst du selbst Bilder mit der KI-Anwendung DALL E.

            """)
        
st.divider()
#Beispiel eines KI-generierten Bildes im Disney-Stil
st.markdown("""
               Mit KI-Anwendungen haben Nutzer von sich Bilder in unterschiedlichen bekannten Stilen, z. B. sich als Anime oder Disneyfigur erstellt.
               Anstatt ein ein persönliches Bild hochzuladen, wird das Bild mithilfe eines Prompts erzeugt.

                "***Prompt:*** Erstelle mir ein Bild von Cinderella im Disney-Stil mit kurzen Haaren, einem Business-Outfit und einem Kaffee in der Hand."
                Erzeugte mir das unten aufgeführte Bild. Es gab Anpassungen bei der KI-Anwendung und jetzt werden die Bilder nicht so identisch im Disney-Stil erzeugt.
                Versuche es selbst, kriegst du kein Bild, dann musst du deinen Prompt anpassen.
            """)
#Anzeigen des generierten Bildes im Disney-Stil            
try:         
    st.image("Cinderella.png",width=200)
except FileNotFoundError:
    st.error("Das Bild ist nicht verfügbar, bitte mach weiter mit der Übung.")

        
st.divider()

#Speichern der Eingaben und Antworten:

if "uebung3" not in st.session_state:
    st.session_state.uebung3 ={}

if "zaehler_bildgenerierung" not in st.session_state:
    st.session_state.zaehler_bildgenerierung = 0


#Container um den Fokus zu behalten
container_fokus = st.container()
with container_fokus:
    with st.expander("Bildgenerierung", expanded=True):    
        # Eingabe und Button
        with st.form("frage_formular4", clear_on_submit=True):
            #Aufgabenstellung
            st.markdown(
            """
                Jetzt bist du wieder dran! Du kannst dir nun ein Bild mithilfe der KI erstellen lassen. Anstatt ein Bild hochzuladen, beschreibe das Bild,
                was du erstellen lassen möchtest.
            """)

            eingabe = st.text_input("Bitte beschreibe, wie dein Bild generiert werden soll",placeholder="z. B. Erstelle mir ein Bild von einer jungen Frau mit braunen Haaren in einem Kleid im Disney-Stil")
            einePerson=("Stelle nur eine Person oder nur ein Tier dar. Stelle keine weiteren Tiere oder Personen dar.")
            beschreibung=(einePerson+eingabe)
            senden = st.form_submit_button("Erstellen")
            #Bildgenerierung, wenn Button geklickt und Eingabe vorhanden
        
    
            if senden and eingabe:
                try:
                    #Nutzung eines Spinners, damit die User sehen, dass ein Hintergrundprozess durchgeführt wird
                    with st.spinner(text="Generiere Bild, bitte warten..."):
                    
                        #Zählen wie oft der Teilnehmer Bilder generiert
                        st.session_state.zaehler_bildgenerierung += 1
                        aktuelle_anzahl = st.session_state.zaehler_bildgenerierung
                        
                        #DALL-E API Aufruf
                        antwort = client.images.generate(
                            model="dall-e-3",
                            prompt=beschreibung,
                            n=1,
                            size="1024x1024"
                        )

                        # Generiertes Bild
                        st.markdown("Bild:")
                        # Bild anzeigen
                        generiertesBild = antwort.data[0].url
                        #Anpassung des Bildes mit width, da size im API Aufruf nicht verkleindert werden kann
                        st.image(generiertesBild, width=200)
                        
                        #Speichern der Daten
                        if "bild_generierung_ki" not in st.session_state.uebung3:
                            st.session_state.uebung3["bild_generierung_ki"] = []
                        
                        st.session_state.uebung3["bild_generierung_ki"].append({
                            "Bereich": "Übung3",
                            "Typ": "DALL-E Bilderstellung",
                            "Frage": "Bitte beschreibe, wie dein Bild generiert werden soll",
                            "Antwort": eingabe,
                            "Anzahl Bildgenerierungen": aktuelle_anzahl
                        })
                        st.session_state.uebung3["bild_generierung_ki"]

                except Exception as error:
                    hilfsdatei.openai_fehlerbehandlung(error)


    st.markdown("""
                    Siehst du, du hast ein Bild generieren lassen.

                    """)
#Speichern der Prompts:
frage_datenschutz = "Würdest du von dir ein Bild generieren lassen, indem du ein Bild von dir hochlädst?"
antwort_datenschutz=st.radio(frage_datenschutz,
    ("Ja, ich würde ein Bild von mir hochladen",
     "Neutral",
     "Nein, ich würde kein Bild von mir hochladen",
     "Keine Angabe"
    ), index=None
    )
 #Ausgabe der Antwort
if antwort_datenschutz is not None:
    
    st.session_state.uebung3["datenschutz"] = {
        "Bereich":"Übung3",
        "Typ" : "Datenschutz",
        "Frage" : frage_datenschutz,
        "Antwort": antwort_datenschutz
    }
    st.markdown(f"Deine Antwort ist: {antwort_datenschutz}")

frage_urheberrecht="Findest du es in Ordnung, dass Bilder im Stil von bekannten Firmen und Künstlern innerhalb von Minuten generiert werden, obwohl diese Jahre lang daran arbeiten?"
antwort_urheberrecht=st.radio(frage_urheberrecht,
                                  ("Ja, ich finde es in Ordnung",
                                   "Neutral",
                                   "Nein, ich finde es nicht in Ordnung",
                                   "Keine Angabe"
                                  ), index=None
                        )
if antwort_urheberrecht is not None:
        
        st.session_state.uebung3["urheberrecht"]={
            "Bereich":"Übung3",
            "Typ": "Urheberrecht",
            "Frage": frage_urheberrecht,
            "Antwort": antwort_urheberrecht
        }
        st.markdown(f"Deine Antwort ist: {antwort_urheberrecht}")



frage_unterscheidung = "Wie einfach oder schwierig ist es deiner Meinung nach, KI-generierte Bilder von echten zu unterscheiden?"
antwort_unterscheidung = st.radio(frage_unterscheidung,
                                ["Sehr einfach",
                                "Eher einfach",
                                "Teils/teils", 
                                "Eher schwierig",
                                "Sehr schwierig",
                                "Keine Angabe"
                                ], index=None, key="unterscheidung"
                            )
    
if antwort_unterscheidung is not None:
    st.session_state.uebung3["unterscheidung"] = {
        "Bereich": "Übung3", 
        "Typ": "Bewertung",
        "Frage": frage_unterscheidung,
        "Antwort": antwort_unterscheidung
    }
    st.markdown(f"Deine Antwort ist: {antwort_unterscheidung}")


    
st.session_state.uebung3
st.divider()
st.markdown("Um fortzufahren, klicke auf \"Weiter\"")
#Anzeigen wie weit der Teilnehmer in der gesamten Lerneinheit ist
st.markdown("Aktueller Fortschritt in der gesamten Lerneinheit: 5 von 8")
st.progress (5/8)
if st.button("Weiter"):
    unbeantwortet = False
    if antwort_bild_realistisch is None:
        st.error("Bitte beantworte die Frage, ob das Bild realistisch wirkt.")
        unbeantwortet = True
    if antwort_datenschutz is None:
        st.error("Bitte beantworte die Frage mit dem Datenschutz.")
        unbeantwortet = True
    if antwort_unterscheidung is None:
        st.error("Bitte beantworte die Frage zur Unterscheidung von KI-Bildern.")
        unbeantwortet = True    
    if antwort_urheberrecht is None:
        st.error("Bitte beantworte die Frage mit dem Urheberrecht.")
        unbeantwortet = True
    if "bild_generierung_ki" not in st.session_state.uebung3:
        st.error("Bitte lass von der KI ein Bild generieren.")
        unbeantwortet = True
    
    if not unbeantwortet:
        naechste_seite=("pages/7_Übung 4.py")
        st.switch_page(naechste_seite)
