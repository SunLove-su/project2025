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
import os
import replicate

#Überschrift der Seite
titel_seite = "3. Übung"
hilfsdatei.seite(titel_seite)

#API-Verbindung zu OpenAI und zu Gemini aufbauen
openai_client1, openai_client2, gemini_client, api_key1, api_key2 = hilfsdatei.openai_verbindung()

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


if "uebung3" not in st.session_state:
    st.session_state.uebung3 ={}

######################################################################
frage_bild_realistisch="Wie realistisch fandest du das Bild von der vorherigen Übung?"
antwort_bild_realistisch=st.radio(frage_bild_realistisch,
                                (
                                    "Sehr realistisch",        
                                    "Eher realistisch",
                                    "Mittelmäßig realistisch", 
                                    "Eher unrealistisch",
                                    "Sehr unrealistisch"
                                    ),
                                    index=None
                        )
if "anzahl_bild_realistisch" not in st.session_state:
    st.session_state.anzahl_bild_realistisch = 0
if "bild_realistisch_alt" not in st.session_state:
    st.session_state.bild_realistisch_alt = None
if "bild_realistisch_historie" not in st.session_state.uebung3:
    st.session_state.uebung3["bild_realistisch_historie"] = []

# Speicherung nur bei Änderung der Antwort
if antwort_bild_realistisch is not None and antwort_bild_realistisch != st.session_state.bild_realistisch_alt:
    st.session_state.anzahl_bild_realistisch += 1
    
    bild_realistisch_data = {
        "Bereich": "Übung3",
        "Typ": "KI Bild Realistisch",
        "Frage": frage_bild_realistisch,
        "Antwort": antwort_bild_realistisch,
        "Anzahl_Aenderungen": st.session_state.anzahl_bild_realistisch
    }
    
    st.session_state.uebung3["bild_realistisch_historie"].append(bild_realistisch_data)
    st.session_state.uebung3["bild_realistisch"] = bild_realistisch_data
    # Aktuelle Antwort merken
    st.session_state.bild_realistisch_alt = antwort_bild_realistisch
    
    st.markdown(f"Deine Antwort ist: {antwort_bild_realistisch}.")


##############################################
st.divider()

#Aufgabenstellung Teilnehmer
#Beispiel eines KI-generierten Bildes im Disney-Stil
st.markdown("""
                Jetzt erstellst du selbst Bilder mit der KI-Anwendung DALL E.
                Mit KI-Anwendungen haben Nutzer von sich Bilder in unterschiedlichen bekannten Stilen, z. B. sich als Anime oder Disneyfigur erstellt.
                Anstatt ein persönliches Bild hochzuladen, wird das Bild mithilfe eines Prompts erzeugt.

                ***Prompt:*** \"Erstelle mir ein Bild von Cinderella im Disney-Stil mit kurzen Haaren, einem Business-Outfit und einem Kaffee in der Hand."\n\n
                Erzeugte mir das unten aufgeführte Bild. Es gab Anpassungen bei der KI-Anwendung ChatGPT, sodass jetzt die Bilder nicht mehr in berühmten Stilen z. B. im Disney-Stil erzeugt werden.\n\n
                
            """)
#Anzeigen des generierten Bildes im Disney-Stil            
try:
    #Das Bild muss im Root Folder des Git-Repositories liegen, damit das so funktioniert         
    st.image("Cinderella.png",width=200)
except FileNotFoundError:
    st.error("Das Bild ist nicht verfügbar, bitte mach weiter mit der Übung.")

st.markdown("Versuche es selbst, kriegst du kein Bild, dann musst du deinen Prompt anpassen.")

##########################################################################        
st.divider()
####################################################################

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

            eingabe = st.text_input("Bitte beschreibe, wie dein Bild generiert werden soll",placeholder="z. B. Junge Frau mit blonden Haaren im Disney-Stil.")
            einePerson=("Stelle nur eine Person oder nur ein Tier dar. Stelle keine weiteren Tiere oder Personen dar.")
            beschreibung=(einePerson+eingabe)
            senden = st.form_submit_button("Erstellen")
            #Bildgenerierung, wenn Button geklickt und Eingabe vorhanden
        
    
            if senden and eingabe:
                try:
                    #Nutzung eines Spinners, damit die User sehen, dass ein Hintergrundprozess durchgeführt wird
                    with st.spinner(text="Generiere Bild, bitte warten..."):
                    
                        #Zählen wie oft der Teilnehmer Bilder generiert
                        
                        if "zaehler_bildgenerierung" not in st.session_state:
                             st.session_state.zaehler_bildgenerierung = 0
                             
                        st.session_state.zaehler_bildgenerierung += 1
                        aktuelle_anzahl = st.session_state.zaehler_bildgenerierung
                        
                        generiertesBild = None
                        #DALL-E API Aufruf
                        if openai_client1:
                            try:
                                antwort = openai_client1.images.generate(
                                    model="dall-e-3",
                                    prompt=beschreibung,
                                    n=1,
                                    size="1024x1024"
                                )
                                generiertesBild = antwort.data[0].url
                            except:
                                pass

                        #2 Key falls erster Key nicht funktioniert

                        if openai_client2 and generiertesBild is None:
                            try:
                                antwort = openai_client2.images.generate(
                                    model="dall-e-3",
                                    prompt=beschreibung,
                                    n=1,
                                    size="1024x
                                )
                                generiertesBild = antwort.data[0].url
                            except:
                                pass

                        if replicate_client and generiertesBild is None:
                            try:
                                antwort = replicate.run("stability-ai/stable-diffusion",
                                input={
                                    prompt = beschreibung,
                                }
                                )
                                st.image(antwort)
                            except:
                                pass
                        
                        if generiertesBild is None:
                            st.error("Leider konnte kein Bild generiert werden")

                    
                        # Generiertes Bild
                        st.markdown("Bild:")
                        # Bild anzeigen
                        generiertesBild = antwort.data[0].url
                        #Anpassung des Bildes mit width, da size im API Aufruf nicht verkleindert werden kann
                        st.image(generiertesBild, width=200)
                        
                        #Speichern der Daten
                        if "bild_generierung_ki_historie" not in st.session_state.uebung3:
                            st.session_state.uebung3["bild_generierung_ki_historie"] = []

                        bild_generierung_ki = {
                            "Bereich": "Übung3",
                            "Typ": "DALL-E Bilderstellung",
                            "Frage": "Bitte beschreibe, wie dein Bild generiert werden soll",
                            "Antwort": eingabe,
                            "Anzahl_Aenderungen": aktuelle_anzahl

                        }
                        
                        st.session_state.uebung3["bild_generierung_ki_historie"].append(bild_generierung_ki)
                        st.session_state.uebung3["bild_generierung_ki"] = bild_generierung_ki

                           
                        st.markdown(f"Deine Antwort: {eingabe}.")

                        # st.session_state.uebung3["bild_generierung_ki"]

                except Exception as error:
                    hilfsdatei.openai_fehlerbehandlung(error)


    st.markdown("""
                    Siehst du, du hast ein Bild generieren lassen.

                    """)
############################################################################
#Frage ob Teilnehmer Bilder von sich hochladen würden, um Bilder generieren zu lassen
frage_datenschutz = "Würdest du von dir ein Bild generieren lassen, indem du ein Bild von dir hochlädst?"
antwort_datenschutz=st.radio(frage_datenschutz,
    (
                                    "Sehr wahrscheinlich",
                                    "Eher wahrscheinlich", 
                                    "Neutral",
                                    "Eher unwahrscheinlich",
                                    "Sehr unwahrscheinlich"
    ), index=None
    )
#Speichern der Antwort
if "anzahl_datenschutz" not in st.session_state:
    st.session_state.anzahl_datenschutz = 0
if "datenschutz_alt" not in st.session_state:
    st.session_state.datenschutz_alt = None
if "datenschutz_historie" not in st.session_state.uebung3:
    st.session_state.uebung3["datenschutz_historie"] = []

# Speicherung nur bei Änderung der Antwort
if antwort_datenschutz is not None and antwort_datenschutz != st.session_state.datenschutz_alt:
    st.session_state.anzahl_datenschutz += 1
    
    datenschutz_data = {
        "Bereich": "Übung3",
        "Typ": "Datenschutz",
        "Frage": frage_datenschutz,
        "Antwort": antwort_datenschutz,
        "Anzahl_Aenderungen": st.session_state.anzahl_datenschutz
    }
    
    st.session_state.uebung3["datenschutz_historie"].append(datenschutz_data)
    st.session_state.uebung3["datenschutz"] = datenschutz_data
    # Aktuelle Antwort merken
    st.session_state.datenschutz_alt = antwort_datenschutz
    
    st.markdown(f"Deine Antwort ist: {antwort_datenschutz}")



######################################################

frage_urheberrecht="Findest du es in Ordnung, dass Bilder im Stil von bekannten Firmen und Künstlern innerhalb von Minuten generiert werden, obwohl diese Jahre lang daran arbeiten?"
antwort_urheberrecht=st.radio(frage_urheberrecht,
                                (
                                    "Völlig in Ordnung",
                                    "Eher in Ordnung",
                                    "Neutral", 
                                    "Eher nicht in Ordnung",
                                    "Gar nicht in Ordnung"
                                  ), index=None
                        )

if "anzahl_urheberrecht" not in st.session_state:
    st.session_state.anzahl_urheberrecht = 0
if "urheberrecht_alt" not in st.session_state:
    st.session_state.urheberrecht_alt = None
if "urheberrecht_historie" not in st.session_state.uebung3:
    st.session_state.uebung3["urheberrecht_historie"] = []

# Speicherung nur bei Änderung der Antwort
if antwort_urheberrecht is not None and antwort_urheberrecht != st.session_state.urheberrecht_alt:
    st.session_state.anzahl_urheberrecht += 1
    
    urheberrecht_data = {
        "Bereich": "Übung3",
        "Typ": "Urheberrecht",
        "Frage": frage_urheberrecht,
        "Antwort": antwort_urheberrecht,
        "Anzahl_Aenderungen": st.session_state.anzahl_urheberrecht
    }
    
    st.session_state.uebung3["urheberrecht_historie"].append(urheberrecht_data)
    st.session_state.uebung3["urheberrecht"] = urheberrecht_data
    # Aktuelle Antwort merken
    st.session_state.urheberrecht_alt = antwort_urheberrecht
    
    st.markdown(f"Deine Antwort ist: {antwort_urheberrecht}")

########################################################################

frage_unterscheidung = "Wie schwierig ist es deiner Meinung nach, KI-generierte Bilder von echten zu unterscheiden?"
antwort_unterscheidung = st.radio(frage_unterscheidung,
                                ("Sehr schwierig",
                                "Eher schwierig",
                                "Mittelmäßig schwierig", 
                                "Eher einfach",
                                "Sehr einfach",
                                
                                ), index=None, key="unterscheidung"
                            )
    
if "anzahl_unterscheidung" not in st.session_state:
    st.session_state.anzahl_unterscheidung = 0
if "unterscheidung_alt" not in st.session_state:
    st.session_state.unterscheidung_alt = None
if "unterscheidung_historie" not in st.session_state.uebung3:
    st.session_state.uebung3["unterscheidung_historie"] = []

# Speicherung nur bei Änderung der Antwort
if antwort_unterscheidung is not None and antwort_unterscheidung != st.session_state.unterscheidung_alt:
    st.session_state.anzahl_unterscheidung += 1
    
    unterscheidung_data = {
        "Bereich": "Übung3",
        "Typ": "Bewertung",
        "Frage": frage_unterscheidung,
        "Antwort": antwort_unterscheidung,
        "Anzahl_Aenderungen": st.session_state.anzahl_unterscheidung
    }
    
    st.session_state.uebung3["unterscheidung_historie"].append(unterscheidung_data)
    st.session_state.uebung3["unterscheidung"] = unterscheidung_data
    # Aktuelle Antwort merken
    st.session_state.unterscheidung_alt = antwort_unterscheidung
    
    st.markdown(f"Deine Antwort ist: {antwort_unterscheidung}")

#Anzeigen aller Speicherungen in der Datenbank auf der Seite
# st.session_state.uebung3
##########################################################################
st.divider()
############################################################################
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
