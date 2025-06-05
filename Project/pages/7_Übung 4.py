"""
4. Übung: Stereotype in KI-Berufsvorschlägen

1. Teilnehmer geben eigene Berufsvorschläge ein
2. KI-Anfragen für verschiedene Geschlechter
3. Vergleich der Antworten und Bewertung von Stereotypen

"""

import streamlit as st
import openai
import hilfsdatei
import os



#Überschrift der Seite
titel_seite = "4. Übung"
hilfsdatei.seite(titel_seite)

#Verbindung zu OpenAI
openai_client1, openai_client2, gemini_client, api_key1, api_key2 = hilfsdatei.openai_verbindung()


#Sicherstellen, dass ein Zugriff der Seiten nur mit Passwort erfolgt, und dass User keine Navigationsseite sehen

hilfsdatei.teilnehmer_anmelden()

#Überschrift auf der Seite
ueberschrift_seite = "4. Übung"
st.markdown(f"<h4>{ueberschrift_seite}</h4>",unsafe_allow_html=True)
#Einleitung zur Übung
st.markdown("""
                In den Übungen zuvor hast du schon Erfahrungen mit ChatGPT und DALL E gesammelt.
                Jetzt nutzt du ChatGPT, um dir bei einer Aufgabe zu helfen.       
            """)  
#Trennungslinie
        
st.divider()
#Aufgabenstellung
text_einleitung =(
             """
                Du sollst in der Schule einen Aufsatz über deinen Berufswunsch schreiben. 
                Welchen Beruf würdest du gerne ausüben?        
                Schreibe deine Berufsvorschläge in das unten stehende Feld und bitte die KI weitere Berufsvorschläge für dich zu generieren, z. B. welche Berufe passen zu einer Frau / zu einem Mann.
                Hinweis: Bitte gib außer deinem Geschlecht keine persönlichen Daten wie z. B. deinen Namen an.
            """
)
st.markdown(text_einleitung)

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


container_fokus = st.container()
#Container für besseren Fokus
with container_fokus:
    with st.expander("Berufsvorschlag", expanded=True): 
        #Teilnehmer geben eigenen Berufsvorschlag ein   
        st.markdown("Deine Berufsvorschläge:")
        frage_berufsvorschlag = "Welchen Beruf würdest du gerne ausüben?"
        with st.form("frage_formular3_1", clear_on_submit=True):     
            berufsvorschlag_eingabe = st.text_input("Deine Berufsvorschläge:")
            
            speichern = st.form_submit_button("Speichern")
            if speichern and berufsvorschlag_eingabe:
                #Anzahl an eigenen Berufsvorschlägen erhöhen
                st.session_state.zaehler_berufsvorschlag += 1
                zaehler_berufsvorschlag = st.session_state.zaehler_berufsvorschlag
                #Ausgabe des eigenen Berufvorschlags
                st.markdown(f"Deine Antwort ist: {berufsvorschlag_eingabe}")
                
                
                 # Initialisiere die Historie-Liste, falls sie nicht existiert
                if "berufsvorschlag_historie" not in st.session_state.uebung4:
                    st.session_state.uebung4["berufsvorschlag_historie"] = []

                berufsvorschlag = {
                    "Bereich": "Übung4",
                    "Typ": "Eigener Berufsvorschlag",
                    "Frage": frage_berufsvorschlag,
                    "Antwort": berufsvorschlag_eingabe,
                    "Anzahl_Aenderungen": zaehler_berufsvorschlag

                }
                
                # Füge zur Historie hinzu
                st.session_state.uebung4["berufsvorschlag_historie"].append(berufsvorschlag)
                
                # Speichern der aktuellen Antworten
                st.session_state.uebung4["berufsvorschlag"]= berufsvorschlag
                
                
                # Wenn bereits KI-Antwort für das eigene Geschlecht vorhanden, zeige Vergleich
                if "antwort_ki_1" in st.session_state.uebung4:
                    st.markdown("VERGLEICH DER ANTWORTEN:")
                    st.markdown(f"**Deine Antwort:** {berufsvorschlag_eingabe}")
                    st.markdown(f"**ChatGPT Antwort:** {st.session_state.uebung4['antwort_ki_1']['Antwort']}")


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
                        
                        antwort_text = None

                        if openai_client1:
                            try:
                                antwort = openai_client1.chat.completions.create(
                                model="gpt-3.5-turbo",
                                messages=[
                                    {"role": "system", "content": prompt+frage1}
                                ]
                                )   
                            
                                antwort_text = antwort.choices[0].message.content
                            except:
                                pass

                        if openai_client2 and antwort_text is None:
                            try:
                                antwort = openai_client2.chat.completions.create(
                                    model="gpt-3.5-turbo",
                                    messages=[
                                        {"role": "system", "content": prompt+frage1}
                                    ]
                                    )   
                        
                                antwort_text = antwort.choices[0].message.content
                            except:
                                pass
                            
                        if gemini_client and antwort_text is None:
                            try:
                                antwort = gemini_client.generate_content(prompt+frage1)
                                antwort_text = antwort.text
                            except:
                                pass
                        
                        if antwort_text is None:
                            if "frau" in frage1.lower():
                                antwort_text = "Krankenschwester, Erzieherin, Sekretärin"
                            elif "mann" in frage1.lower():
                                antwort_text = "Ingenieur, Mechaniker, Programmierer"
                            else:
                                antwort_text = "Entschuldigung, ich kann diese Frage nicht beantworten."

                        st.write("Antwort:")
                        st.write(antwort_text)

                        if "antwort_ki_1_historie" not in st.session_state.uebung4:
                            st.session_state.uebung4["antwort_ki_1_historie"] = []

                        antwort_ki_1 ={
                            "Bereich": "Übung4",
                            "Typ": "Berufsvorschlag_Eigenes_Geschlecht_KI_Interaktion_1",
                            "Frage": frage1,
                            "Antwort": antwort_text,
                            "Anzahl_Aenderungen": zaehler_eigenes_geschlecht
                        }

                        # Füge zur Historie hinzu
                        st.session_state.uebung4["antwort_ki_1_historie"].append(antwort_ki_1)

                        
                        # Speichere aktuellen Eintrag
                        st.session_state.uebung4["antwort_ki_1"] = antwort_ki_1

                        

                        


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
            
                        antwort_text = None

                        if openai_client1:
                            try:
                                antwort = openai_client1.chat.completions.create(
                                model="gpt-3.5-turbo",
                                messages=[
                                    {"role": "system", "content": prompt+frage2}
                                ]
                                )   
                            
                                antwort_text = antwort.choices[0].message.content
                            except:
                                pass

                        if openai_client2 and antwort_text is None:
                            try:
                                antwort = openai_client2.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": prompt+frage2}
                            ]
                            )   
                        
                            antwort_text = antwort.choices[0].message.content
                        except:
                            pass
                            
                        if gemini_client and antwort_text is None:
                            try:
                                antwort = gemini_client.generate_content(prompt+frage2)
                                antwort_text = antwort.text
                            except:
                                pass
                        
                        if antwort_text is None:
                            if "frau" in frage2.lower():
                                antwort_text = "Krankenschwester, Erzieherin, Sekretärin"
                            elif "mann" in frage2.lower():
                                antwort_text = "Ingenieur, Mechaniker, Programmierer"
                            else:
                                antwort_text = "Entschuldigung, ich kann diese Frage nicht beantworten."

                        st.write("Antwort:")
                        st.write(antwort_text)


                        # Initialisiere die Historie-Liste, falls sie nicht existiert
                        if "antwort_ki_2_historie" not in st.session_state.uebung4:
                            st.session_state.uebung4["antwort_ki_2_historie"] = []
                            
                        antwort_ki_2 = {
                            "Bereich":"Übung4",
                            "Typ":"Berufsvorschlag_Anderes_Geschlecht_KI_Interaktion_2",
                            "Frage": frage2,
                            "Antwort": antwort_text,
                            "Anzahl_Aenderungen": zaehler_anderes_geschlecht
                        }
                        # Füge zur Historie hinzu
                        st.session_state.uebung4["antwort_ki_2_historie"].append(antwort_ki_2)
                        
                        # Speichere aktuellen Eintrag
                        st.session_state.uebung4["antwort_ki_2"] =antwort_ki_2


                except Exception as error:
                    hilfsdatei.openai_fehlerbehandlung(error)


    with st.expander("Vergleich der Eingabe und der KI-Ausgaben", expanded=True):             
        # Vergleich anzeigen wenn alle Daten vorhanden sind
        if ("berufsvorschlag" in st.session_state.uebung4 and 
            "antwort_ki_1" in st.session_state.uebung4 and
            "antwort_ki_2" in st.session_state.uebung4):
            st.markdown("VERGLEICH DER ANTWORTEN:")
            st.markdown(f"**Deine Vorschläge:** {st.session_state.uebung4['berufsvorschlag']['Antwort']}")
            st.markdown(f"**KI-Vorschläge für dein Geschlecht:** {st.session_state.uebung4['antwort_ki_1']['Antwort']}")
            st.markdown(f"**KI-Vorschläge für das andere Geschlecht:** {st.session_state.uebung4['antwort_ki_2']['Antwort']}") 
        else:
            st.info("Fülle bitte oben alle Felder aus!")

####################################################################################################################
#Trennungslinie
st.divider()
###################################################################################################################
# Frage ob es für die Geschlechter einen Stereotyp gibt
frage_stereotyp = "Wie stereotypisch findest du die KI-Berufsvorschläge für Frauen und Männer"
antwort_stereotyp = st.radio(frage_stereotyp,
    (
    "Sehr stereotypisch",
    "Eher stereotypisch",
    "Mittelmäßig stereotypisch", 
    "Eher nicht stereotypisch",
    "Gar nicht stereotypisch"
    ), index=None
)
#Antwort speichern
if "anzahl_stereotyp" not in st.session_state:
    st.session_state.anzahl_stereotyp = 0
if "stereotyp_alt" not in st.session_state:
    st.session_state.stereotyp_alt = None 
if "stereotyp_historie" not in st.session_state.uebung4:
    st.session_state.uebung4["stereotyp_historie"] = []

# Speicherung nur bei Änderung der Antwort
if antwort_stereotyp is not None and antwort_stereotyp != st.session_state.stereotyp_alt:
    st.session_state.anzahl_stereotyp += 1
    
    stereotyp = {
        "Bereich": "Übung4",
        "Typ": "Stereotyp-Einschätzung",
        "Frage": frage_stereotyp,
        "Antwort": antwort_stereotyp,
        "Anzahl_Aenderungen": st.session_state.anzahl_stereotyp
    }
    
    st.session_state.uebung4["stereotyp_historie"].append(stereotyp)
    st.session_state.uebung4["stereotyp"] = stereotyp
    # Aktuelle Antwort merken
    st.session_state.stereotyp_alt = antwort_stereotyp
    
    st.markdown(f"Deine Antwort ist: {antwort_stereotyp}")


################################################################################################################################
st.divider()

################################################################################################################################
st.markdown("Um fortzufahren, klicke auf \"Weiter\"")
#Anzeigen wie weit der Teilnehmer in der gesamten Lerneinheit ist
st.markdown("Aktueller Fortschritt in der gesamten Lerneinheit: 6 von 8")
st.progress (6/8)

if st.button("Weiter"):
    unbeantwortet = False

    if "berufsvorschlag" not in st.session_state.uebung4:
        st.error("Bitte beantworte die Frage mit dem Berufsvorschlag.")
        unbeantwortet = True
    if "antwort_ki_1" not in st.session_state.uebung4:
        st.error("Bitte frage die KI nach Berufen für dein Geschlecht.")
        unbeantwortet = True
    if "antwort_ki_2" not in st.session_state.uebung4:
        st.error("Bitte frage die KI nach Berufen für das andere Geschlecht.")
        unbeantwortet = True
    if antwort_stereotyp is None:
        st.error("Bitte beantworte die Frage mit dem Stereotyp.")
        unbeantwortet= True 
    if not unbeantwortet:
        naechste_seite= ("pages/8_Abschlussumfrage.py")
        st.switch_page(naechste_seite)