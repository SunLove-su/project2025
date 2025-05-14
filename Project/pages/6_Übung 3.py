import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

if not st.session_state.get("admin"):
    st.set_page_config(page_title="3. Übung",initial_sidebar_state="collapsed")
 
    st.markdown(
        """
    <style>
        [data-testid="stSidebarCollapsedControl"] {
            display: none
        }
    </style>
    """,
        unsafe_allow_html=True,

    )
else:

    st.set_page_config(page_title="3. Übung"
    
)
def login():
    st.write("Enter the secret code")
    code = st.text_input("Code")
    if st.button("Login"):
        password = code
        if password == st.secrets["survey_secret"]:
            st.session_state["logged_in"] = True
            st.rerun()
        elif password == st.secrets["admin_secret"]:
            st.session_state["logged_in"] = True
            st.session_state["admin"] = True
            st.rerun()
        else:
            st.error("Wrong secret code")
    st.stop()
 
 
if not st.session_state.get("logged_in"):
    login()



st.markdown("<h4>3. Übung</h4>",unsafe_allow_html=True)

st.markdown("""
            In der Übung zuvor hast du die Person gesehen, die das Eis isst.
            Bei dem Bild handelt es sich um ein KI-generiertes Bild von der Seite "thispersondoesnotexist.com", dass sehr echt aussieht.
            
            Für KI-generierte Bilder wird der Deep Learning Algorithmus Generative Adversarial Networks (GAN) verwendet.
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
if "uebung3" not in st.session_state:
    st.session_state.uebung3 = {}
if "ki_antwort" not in st.session_state:
    st.session_state.ki_antwort = ""
#tab1 = st.tabs(["Eingaben"])[0]

# Berufsvorschlag
#with tab1:
containerfokus = st.container()
with containerfokus:
    with st.expander("Berufsvorschlag", expanded=True):    
        st.markdown("Deine Berufsvorschläge:")
        frage_berufsvorschlag = "Welchen Beruf würdest du gerne ausüben?"
        with st.form("frage_formular3_1", clear_on_submit=True):     
            berufsvorschlag = st.text_input("Deine Berufsvorschläge:")
            
            speichern = st.form_submit_button("speichern")
            if speichern and berufsvorschlag:
                st.write(f"Deine Antwort ist: {berufsvorschlag}")
                st.session_state.uebung3["berufsvorschlag"] = {
                    "Bereich": "Übung3",
                    "Typ": "Eigener Berufsvorschlag",
                    "Frage": frage_berufsvorschlag,
                    "Antwort": berufsvorschlag
                }
                # Wenn bereits KI-Antwort vorhanden, zeige Vergleich
                if st.session_state.ki_antwort:
                    st.write("VERGLEICH DER ANTWORTEN:")
                    st.write(f"**Deine Vorschläge:** {berufsvorschlag}")
                    st.write(f"**KI-Vorschläge:** {st.session_state.ki_antwort}")


        st.markdown("""
        "Frage die KI nach Berufen für dein Geschlecht:
        """)
        # Erste KI-Anfrage
        with st.form("frage_formular3_2", clear_on_submit=True):
            frage1 = st.text_input("Deine Frage bitte",placeholder="z. B. Welcher Beruf passt zu einer Frau / einem Mann")
            senden1 = st.form_submit_button("senden")
            
            if senden1 and frage1:
                try:
                    with st.spinner(text="Erstelle Text, bitte warten..."):
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
                        st.session_state.ki_antwort = antwort_text
                        st.session_state.uebung3["ki_antwort_1"] = {
                            "Bereich": "Übung3",
                            "Typ": "Berufsvorschlag eigenes Geschlecht-KI-Interaktion 1",
                            "Frage": frage1,
                            "Antwort": antwort_text
                        }
                        
                        # # Vergleich anzeigen wenn Berufsvorschlag vorhanden
                        # if "berufsvorschlag" in st.session_state.uebung3:
                        #     st.write("VERGLEICH DER ANTWORTEN:")
                        #     st.write(f"**Deine Vorschläge:** {st.session_state.uebung3['berufsvorschlag']['Antwort']}")
                        #     st.write(f"**KI-Vorschläge:** {antwort_text}")
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


        st.markdown("""
                        "Frage die KI nach Berufen für das andere Geschlecht:""")
        # Zweite KI-Anfrage
        with st.form("frage_formular3_3", clear_on_submit=True):
            frage2 = st.text_input("Deine Frage bitte",placeholder="z. B. Welcher Beruf passt zu einer Frau / einem Mann")
            senden2 = st.form_submit_button("senden")
            
            if senden2 and frage2:
                try:
                    with st.spinner(text="Erstelle Text, bitte warten..."):
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
                        st.session_state.ki_antwort = antwort_text
                        st.session_state.uebung3["ki_antwort_2"] = {
                            "Bereich":"Übung3",
                            "Typ":"Berufsvorschlag anderes Geschlecht - KI-Interaktion 2",
                            "Frage": frage2,
                            "Antwort": antwort_text
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
        if ("berufsvorschlag" in st.session_state.uebung3 and 
            "ki_antwort_1" in st.session_state.uebung3 and
            "ki_antwort_2" in st.session_state.uebung3):
            st.write("VERGLEICH DER ANTWORTEN:")
            st.write(f"**Deine Vorschläge:** {st.session_state.uebung3['berufsvorschlag']['Antwort']}")
            st.write(f"**KI-Vorschläge für dein Geschlecht:** {st.session_state.uebung3['ki_antwort_1']['Antwort']}")
            st.write(f"**KI-Vorschläge für das andere Geschlecht:** {st.session_state.uebung3['ki_antwort_2']['Antwort']}") 
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
    st.session_state.uebung3["stereotyp"] = {
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
        unbeantwortet = (stereotyp is None or 
                        "berufsvorschlag" not in st.session_state.uebung3 or 
                        st.session_state.ki_antwort == "")
        if unbeantwortet:
            st.error("Bitte beantworte alle Fragen, um fortzufahren.")
        else:
            st.switch_page("pages/7_Übung 4.py")