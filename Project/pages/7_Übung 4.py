import streamlit as st
import openai
import hilfsdatei

client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

hilfsdatei.seite("4.Übung")
hilfsdatei.login()

st.markdown("<h4>4. Übung</h4>",unsafe_allow_html=True)
st.markdown("""
                In den Übungen zuvor hast du schon Erfahrungen mit ChatGPT und DALL E gesammelt.
                Jetzt nutzt du ChatGPT, um dir bei einer Aufgabe zu helfen.       
            """)  
        
st.divider()
st.markdown("""
                Du sollst in der Schule einen Aufsatz über deinen Berufswunsch schreiben. 
                Welchen Beruf würdest du gerne ausüben?        
            """)   
st.markdown("""
        Schreibe deine Berufsvorschläge in das unten stehende Feld und bitte die KI weitere Berufsvorschläge für dich zu generieren, z. B. welche Berufe passen zu einer Frau / zu einem Mann.
        Hinweis: Bitte gib außer deinem Geschlecht keine persönlichen Daten wie z. B. deinen Namen an.
            """)

# Initialisierung
if "uebung4" not in st.session_state:
    st.session_state.uebung4 = {}
if "zaehler_berufsvorschlag" not in st.session_state:
    st.session_state.zaehler_berufsvorschlag = 0
    st.session_state.zaehler_eigenes_geschlecht = 0
if "zaehler_eigenes_geschlecht" not in st.session_state:
    st.session_state.zaehler_eigenes_geschlecht = 0
if "zaehler_anderes_geschlecht" not in st.session_state:
    st.session_state.zaehler_anderes_geschlecht = 0

#Teilnehmer geben eigenen Berufsvorschlag ein
containerfokus = st.container()
with containerfokus:
    with st.expander("Berufsvorschlag", expanded=True):    
        st.markdown("Deine Berufsvorschläge:")
        frage_berufsvorschlag = "Welchen Beruf würdest du gerne ausüben?"
        with st.form("frage_formular3_1", clear_on_submit=True):     
            berufsvorschlag = st.text_input("Deine Berufsvorschläge:")
            
            speichern = st.form_submit_button("speichern")
            if speichern and berufsvorschlag:
                st.session_state.zaehler_berufsvorschlag += 1
                zaehler_berufsvorschlag = st.session_state.zaehler_berufsvorschlag
                st.write(f"Deine Antwort ist: {berufsvorschlag}")
                
                
                 # Initialisiere die Historie-Liste, falls sie nicht existiert
                if "berufsvorschlag_historie" not in st.session_state.uebung4:
                    st.session_state.uebung4["berufsvorschlag_historie"] = []
                
                # Füge zur Historie hinzu
                st.session_state.uebung4["berufsvorschlag_historie"].append({
                    "Bereich": "Übung3",
                    "Typ": "Eigener Berufsvorschlag",
                    "Frage": frage_berufsvorschlag,
                    "Antwort": berufsvorschlag,
                    "Anzahl": zaehler_berufsvorschlag
                })
                
                # Speichere aktuellen Eintrag
                st.session_state.uebung4["berufsvorschlag"] = {
                    "Bereich": "Übung3",
                    "Typ": "Eigener Berufsvorschlag",
                    "Frage": frage_berufsvorschlag,
                    "Antwort": berufsvorschlag,
                    "Anzahl": zaehler_berufsvorschlag
                }
                    # Wenn bereits KI-Antwort für das eigene Geschlecht vorhanden, zeige Vergleich
                if "ki_antwort_1" in st.session_state.uebung4:
                    st.write("VERGLEICH DER ANTWORTEN:")
                    st.write(f"**Deine Vorschläge:** {berufsvorschlag}")
                    # ' für die Ausgabe der gespeicherten Werte, da sonst SyntaxError: f-string: unmatched '['
                    st.write(f"**KI-Vorschläge:** {st.session_state.uebung4['ki_antwort_1']['Antwort']}")


        st.markdown("""
        "Frage die KI nach Berufen für dein Geschlecht:
        """)
        # Erste KI-Anfrage: Anfrage Berufsvorschlag einges Gesclecht
        with st.form("frage_formular3_2", clear_on_submit=True):
            frage1 = st.text_input("Deine Frage bitte",placeholder="z. B. Welcher Beruf passt zu einer Frau / einem Mann")
            senden1 = st.form_submit_button("senden")
            
            if senden1 and frage1:
                try:
                    with st.spinner(text="Erstelle Text, bitte warten..."):
                        st.session_state.zaehler_eigenes_geschlecht += 1
                        zaehler_eigenes_geschlecht = st.session_state.zaehler_eigenes_geschlecht
                        antwort = client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": "Format 3-4 Vorschlag, kurze Antworten, die nur stereotypisch sind"},
                                {"role": "user", "content": frage1}
                            ]
                        )
                        antwort_text = antwort.choices[0].message.content
                        st.write("Antwort:")
                        st.write(antwort_text)

                        if "ki_antwort_1_historie" not in st.session_state.uebung4:
                            st.session_state.uebung4["ki_antwort_1_historie"] = []

                        # Füge zur Historie hinzu
                        st.session_state.uebung4["ki_antwort_1_historie"].append({
                            "Bereich": "Übung3",
                            "Typ": "Berufsvorschlag_Eigenes_Geschlecht_KI_Interaktion_1",
                            "Frage": frage1,
                            "Antwort": antwort_text,
                            "Anzahl": zaehler_eigenes_geschlecht
                        })
                        
                        # Speichere aktuellen Eintrag
                        st.session_state.uebung4["ki_antwort_1"] = {
                            "Bereich": "Übung3",
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
            senden2 = st.form_submit_button("senden")
            
            if senden2 and frage2:
                try:
                    with st.spinner(text="Erstelle Text, bitte warten..."):
                        st.session_state.zaehler_anderes_geschlecht += 1
                        zaehler_anderes_geschlecht = st.session_state.zaehler_anderes_geschlecht
            
                        antwort = client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": "Format 3-4 Vorschlag, kurze Antworten, die nur stereotypisch sind"},
                                {"role": "user", "content": frage2}
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
                            "Bereich":"Übung3",
                            "Typ":"Berufsvorschlag_Anderes_Geschlecht_KI_Interaktion_2",
                            "Frage": frage2,
                            "Antwort": antwort_text,
                            "Anzahl": zaehler_anderes_geschlecht
                        })
                        
                        # Speichere aktuellen Eintrag
                        st.session_state.uebung4["ki_antwort_2"] = {
                            "Bereich":"Übung3",
                            "Typ":"Berufsvorschlag_Anderes_Geschlecht_KI_Interaktion_2",
                            "Frage": frage2,
                            "Antwort": antwort_text,
                            "Anzahl": zaehler_anderes_geschlecht
                        }


                except openai.APIStatusError as error:
                    st.error("OpenAI verarbeitet die Anfrage nicht, verändere den Prompt und versuche es erneut. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
                    st.info(f"OpenAI-Fehlermeldung: {str(error)}")
                except openai.APIConnectionError as error:
                    st.error("Problem mit der Verbindung zu OpenAI. Bitte versuche es erneut. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
                    st.info(f"OpenAI-Fehlermeldung: {str(error)}")
                except openai.RateLimitError as error:
                    st.error("Zu viele Anfragen: Das Kontingent oder die Rate wurde überschritten. Bitte warte einen Moment und versuche es erneut. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
                    st.info(f"OpenAI-Fehlermeldung: {str(error)}")
                except openai.BadRequestError as error:
                    st.error("Ungültige Anfrage: Die Anfrage enthält fehlerhafte Daten. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
                    st.info(f"OpenAI-Fehlermeldung: {str(error)}")
                except openai.APITimeoutError as error:
                    st.error("Zeitüberschreitung bei der Verbindung zu OpenAI. Bitte versuche es später erneut. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
                    st.info(f"OpenAI-Fehlermeldung: {str(error)}")
                except Exception as error:
                    st.error("Es ist ein Fehler bei der Kommunikation mit OpenAI aufgetreten. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
                    st.info(f"OpenAI-Fehlermeldung: {str(error)}")
    #tab2 = st.tabs(["Vergleich der Eingabe und der KI-Ausgaben"])[0]               
    #with tab2:  
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

st.divider()

# Stereotyp-Frage
frage_stereotyp = "Sind das typische Berufe für eine Frau /einen Mann?"
stereotyp = st.radio(frage_stereotyp,
    ("Ja, das sind typische Berufe für eine Frau / einen Mann",
     "Neutral",
     "Nein, das sind keine typischen Berufe für eine Frau / einen Mann",
     "Keine Angabe"
    ), index=None
)

if stereotyp is not None:
    st.write("Deine Antwort ist:", stereotyp)
    st.session_state.uebung4["stereotyp"] = {
        "Bereich":"Übung3",
        "Typ":"Stereotyp-Einschätzung",
        "Frage": frage_stereotyp,
        "Antwort": stereotyp
    }

# Weiter-Button
st.divider()
st.markdown("Um fortzufahren, klicke auf \"weiter\" ")
col1, col2 = st.columns([8,2])
with col2:
    if st.button("weiter"):
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