"""
4. Übung: Stereotype in KI-Berufsvorschlägen

1. Teilnehmer geben eigene Berufsvorschläge ein
2. KI-Anfragen für verschiedene Geschlechter
3. Vergleich der Antworten und Bewertung von Stereotypen

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
hilfsdatei.seite("4.Übung")

#Sicherstellen, dass ein Zugriff der Seiten nur mit Passwort erfolgt, und dass User keine Navigationsseite sehen

hilfsdatei.login()

#Überschrift auf der Seite
st.markdown("<h4>4. Übung</h4>",unsafe_allow_html=True)
#Einleitung zur Übung
st.markdown("""
                In den Übungen zuvor hast du schon Erfahrungen mit ChatGPT und DALL E gesammelt.
                Jetzt nutzt du ChatGPT, um dir bei einer Aufgabe zu helfen.       
            """)  
#Trennungslinie
        
st.divider()
#Aufgabenstellung
st.markdown("""
                Du sollst in der Schule einen Aufsatz über deinen Berufswunsch schreiben. 
                Welchen Beruf würdest du gerne ausüben?        
                Schreibe deine Berufsvorschläge in das unten stehende Feld und bitte die KI weitere Berufsvorschläge für dich zu generieren, z. B. welche Berufe passen zu einer Frau / zu einem Mann.
                Hinweis: Bitte gib außer deinem Geschlecht keine persönlichen Daten wie z. B. deinen Namen an.
            """)

# Speicherung der Daten
if "uebung4" not in st.session_state:
    st.session_state.uebung4 = {}
if "zaehler_berufsvorschlag" not in st.session_state:
    st.session_state.zaehler_berufsvorschlag = 0
    st.session_state.zaehler_eigenes_geschlecht = 0
if "zaehler_eigenes_geschlecht" not in st.session_state:
    st.session_state.zaehler_eigenes_geschlecht = 0
if "zaehler_anderes_geschlecht" not in st.session_state:
    st.session_state.zaehler_anderes_geschlecht = 0


containerfokus = st.container()
#Container für besseren Fokus
with containerfokus:
    with st.expander("Berufsvorschlag", expanded=True): 
        #Teilnehmer geben eigenen Berufsvorschlag ein   
        st.markdown("Deine Berufsvorschläge:")
        frage_berufsvorschlag = "Welchen Beruf würdest du gerne ausüben?"
        with st.form("frage_formular3_1", clear_on_submit=True):     
            berufsvorschlag = st.text_input("Deine Berufsvorschläge:")
            
            speichern = st.form_submit_button("Speichern")
            if speichern and berufsvorschlag:
                #Anzahl an eigenen Berufsvorschlägen erhöhen
                st.session_state.zaehler_berufsvorschlag += 1
                zaehler_berufsvorschlag = st.session_state.zaehler_berufsvorschlag
                #Ausgabe des eigenen Berufvorschlags
                st.markdown(f"Deine Antwort ist: {berufsvorschlag}")
                
                
                 # Initialisiere die Historie-Liste, falls sie nicht existiert
                if "berufsvorschlag_historie" not in st.session_state.uebung4:
                    st.session_state.uebung4["berufsvorschlag_historie"] = []
                
                # Füge zur Historie hinzu
                st.session_state.uebung4["berufsvorschlag_historie"].append({
                    "Bereich": "Übung4",
                    "Typ": "Eigener Berufsvorschlag",
                    "Frage": frage_berufsvorschlag,
                    "Antwort": berufsvorschlag,
                    "Anzahl": zaehler_berufsvorschlag
                })
                
                # Speichere aktuellen Eintrag
                st.session_state.uebung4["berufsvorschlag"] = {
                    "Bereich": "Übung4",
                    "Typ": "Eigener Berufsvorschlag",
                    "Frage": frage_berufsvorschlag,
                    "Antwort": berufsvorschlag,
                    "Anzahl": zaehler_berufsvorschlag
                }
                # Wenn bereits KI-Antwort für das eigene Geschlecht vorhanden, zeige Vergleich
                if "ki_antwort_1" in st.session_state.uebung4:
                    st.markdown("VERGLEICH DER ANTWORTEN:")
                    st.markdown(f"**Deine Antwort:** {berufsvorschlag}")
                    st.markdown(f"**ChatGPT Antwort:** {st.session_state.uebung4['ki_antwort_1']['Antwort']}")


        st.markdown("""
                        Frage die KI nach Berufen für dein Geschlecht:
                    """)
        prompt="Nur 3-4 Vorschläge. In der Form Beruf, Beruf . Keine Beschreibung nur die Berufe. Berufe die nur stereotypisch sind"
        # Erste KI-Anfrage: Anfrage Berufsvorschlag einges Geschlecht
        with st.form("frage_formular3_2", clear_on_submit=True):
            frage1 = st.text_input("Deine Frage bitte",placeholder="z. B. Welcher Beruf passt zu einer Frau / einem Mann")
            senden1 = st.form_submit_button("Senden")
            
            if senden1 and frage1:
                try:
                    #Nutzung eines Spinners, damit die Teilnehmer sehen, dass ein Hintergrundprozess durchgeführt wird
                    with st.spinner(text="Erstelle Text, bitte warten..."):
                        #Zählen falls mehr Anfragen vom Teilnehmer erstellt werden
                        st.session_state.zaehler_eigenes_geschlecht += 1
                        zaehler_eigenes_geschlecht = st.session_state.zaehler_eigenes_geschlecht
                        
                        antwort = client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": prompt+frage1}
                            ]
                        )
                        antwort_text = antwort.choices[0].message.content
                        st.write("Antwort:")
                        st.write(antwort_text)

                        if "ki_antwort_1_historie" not in st.session_state.uebung4:
                            st.session_state.uebung4["ki_antwort_1_historie"] = []

                        # Füge zur Historie hinzu
                        st.session_state.uebung4["ki_antwort_1_historie"].append({
                            "Bereich": "Übung4",
                            "Typ": "Berufsvorschlag_Eigenes_Geschlecht_KI_Interaktion_1",
                            "Frage": frage1,
                            "Antwort": antwort_text,
                            "Anzahl": zaehler_eigenes_geschlecht
                        })
                        
                        # Speichere aktuellen Eintrag
                        st.session_state.uebung4["ki_antwort_1"] = {
                            "Bereich": "Übung4",
                            "Typ": "Berufsvorschlag_Eigenes_Geschlecht_KI_Interaktion_1",
                            "Frage": frage1,
                            "Antwort": antwort_text,
                            "Anzahl": zaehler_eigenes_geschlecht
                        }

                except Exception as error:
                    hilfsdatei.openai_fehlerbehandlung(error)




        st.markdown("""
                        "Frage die KI nach Berufen für das andere Geschlecht:""")
        # Zweite KI-Anfrage
        with st.form("frage_formular3_3", clear_on_submit=True):
            frage2 = st.text_input("Deine Frage bitte",placeholder="z. B. Welcher Beruf passt zu einer Frau / einem Mann")
            senden2 = st.form_submit_button("Senden")
            
            if senden2 and frage2:
                try:
                    #Nutzung eines Spinners, damit die Teilnehmer sehen, dass ein Hintergrundprozess durchgeführt wird
                    with st.spinner(text="Erstelle Text, bitte warten..."):
                        #Zählen wie oft die KI-Anfrage für das andere Geschlecht erstellt wird
                        st.session_state.zaehler_anderes_geschlecht += 1
                        zaehler_anderes_geschlecht = st.session_state.zaehler_anderes_geschlecht
            
                        antwort = client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": prompt+frage2}
                            ]
                        )
                        antwort_text = antwort.choices[0].message.content
                        st.write("Antwort:")
                        st.write(antwort_text)


                        # Initialisiere die Historie-Liste, falls sie nicht existiert
                        if "ki_antwort_2_historie" not in st.session_state.uebung4:
                            st.session_state.uebung4["ki_antwort_2_historie"] = []
                            
                        # Füge zur Historie hinzu
                        st.session_state.uebung4["ki_antwort_2_historie"].append({
                            "Bereich":"Übung4",
                            "Typ":"Berufsvorschlag_Anderes_Geschlecht_KI_Interaktion_2",
                            "Frage": frage2,
                            "Antwort": antwort_text,
                            "Anzahl": zaehler_anderes_geschlecht
                        })
                        
                        # Speichere aktuellen Eintrag
                        st.session_state.uebung4["ki_antwort_2"] = {
                            "Bereich":"Übung4",
                            "Typ":"Berufsvorschlag_Anderes_Geschlecht_KI_Interaktion_2",
                            "Frage": frage2,
                            "Antwort": antwort_text,
                            "Anzahl": zaehler_anderes_geschlecht
                        }


                except Exception as error:
                    hilfsdatei.openai_fehlerbehandlung(error)


    with st.expander("Vergleich der Eingabe und der KI-Ausgaben", expanded=True):             
        # Vergleich anzeigen wenn alle Daten vorhanden sind
        if ("berufsvorschlag" in st.session_state.uebung4 and 
            "ki_antwort_1" in st.session_state.uebung4 and
            "ki_antwort_2" in st.session_state.uebung4):
            st.write("VERGLEICH DER ANTWORTEN:")
            st.write(f"**Deine Vorschläge:** {st.session_state.uebung4['berufsvorschlag']['Antwort']}")
            st.write(f"**KI-Vorschläge für dein Geschlecht:** {st.session_state.uebung4['ki_antwort_1']['Antwort']}")
            st.write(f"**KI-Vorschläge für das andere Geschlecht:** {st.session_state.uebung4['ki_antwort_2']['Antwort']}") 
        else:
            st.info("Fülle bitte oben alle Felder aus!")

#Trennungslinie
st.divider()

# Frage ob es für die Geschlechter einen Stereotyp gibt
frage_stereotyp = "Sind das typische Berufe für eine Frau /einen Mann?"
stereotyp = st.radio(frage_stereotyp,
    ("Ja, das sind typische Berufe für eine Frau / einen Mann",
     "Neutral",
     "Nein, das sind keine typischen Berufe für eine Frau / einen Mann",
     "Keine Angabe"
    ), index=None
)
#Antwort speichern
if stereotyp is not None:
    st.write("Deine Antwort ist:", stereotyp)
    st.session_state.uebung4["stereotyp"] = {
        "Bereich":"Übung4",
        "Typ":"Stereotyp-Einschätzung",
        "Frage": frage_stereotyp,
        "Antwort": stereotyp
    }

# Weiter-Button
st.divider()
st.markdown("Um fortzufahren, klicke auf \"Weiter\"")
#Anzeigen wie weit der Teilnehmer in der gesamten Lerneinheit ist
st.markdown("Aktueller Fortschritt in der gesamten Lerneinheit: 6 von 8")
st.progress (6/8)

if st.button("Weiter"):
    unbeantwortet = False

    if "berufsvorschlag" not in st.session_state.uebung4:
        st.error("Bitte beantworte die Frage mit dem Berufsvorschlag.")
        unbeantwortet = True
    if "ki_antwort_1" not in st.session_state.uebung4:
        st.error("Bitte frage die KI nach Berufen für dein Geschlecht.")
        unbeantwortet = True
    if "ki_antwort_2" not in st.session_state.uebung4:
        st.error("Bitte frage die KI nach Berufen für das andere Geschlecht.")
        unbeantwortet = True
    if stereotyp is None:
        st.error("Bitte beantworte die Frage mit dem Stereotyp.")
        unbeantwortet= True 
    if not unbeantwortet:
        st.switch_page("pages/8_Abschlussumfrage.py")