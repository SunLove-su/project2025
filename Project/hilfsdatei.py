import streamlit as st
import os
import openai
import google.generativeai as genai
import replicate

def seite(titel):
    #set_page muss immer am Anfang der Dateien definiert sein und darf nur einmal auftreten"""
    if not st.session_state.get("admin"):
        #Einstellung damit die Navigation nicht sichtbar ist für Teilnehmer
        st.set_page_config(page_title=titel, initial_sidebar_state="collapsed")
        # Sidebar ausblenden
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
        st.set_page_config(page_title=titel)

# Passwortschutz für die Umfrage/damit nicht jeder drauf zugreifen kann
def teilnehmer_anmelden():
   if not st.session_state.get("eingeloggt"): 
        st.markdown("Bitte gebe das Passwort ein, damit du teilnehmen kannst")
        with st.form("login_formular", clear_on_submit=True):
            eingabe = st.text_input("Passwort")
            anmelden = st.form_submit_button("Anmelden")
            if anmelden and eingabe:
                passwort = eingabe

                basis_passwort = os.getenv("UMFRAGE_PASSWORT")
                if not basis_passwort:
                    try:
                        basis_passwort = st.secrets["umfrage_passwort"]
                    except Exception:
                        st.error ("Kein Passwort vorhanden. Bitte wenden sie sich an den Administrator.")
                        st.stop()

                admin_pw = os.getenv("ADMIN_PASSWORT")
                if not admin_pw:
                    try:
                        admin_pw = st.secrets["admin_passwort"]
                    except Exception:
                        st.error("Kein Passwort vorhanden. Bitte wenden sie sich an den Administrator.")
                        st.stop()

                #Passwort prüfen
                if passwort.startswith(basis_passwort):
                    teilnehmergruppe_info = passwort.replace(basis_passwort, "")
                    
                        
                    if teilnehmergruppe_info is not None and teilnehmergruppe_info != "":
                        st.session_state["teilnehmergruppe_info"] = teilnehmergruppe_info
                    else:
                        
                        st.session_state["teilnehmergruppe_info"] =""
                    st.session_state["eingeloggt"] = True
                    st.rerun()
                # Admin-Passwort / Admin kann die Seitenleiste sehen und muss nicht bedingt alle Fragen ausfüllen, um auf
                # die entsprechenden Seiten im Modul zu kommen.
                elif passwort == admin_pw:
                    st.session_state["eingeloggt"] = True
                    st.session_state["admin"] = True
                    st.session_state["teilnehmergruppe_info"] ="admin"

                    st.rerun()
                else:
                    st.error("Das Passwort ist falsch")
            elif anmelden and not eingabe:
                st.error("Bitte gib ein Passwort ein.")
        st.stop()

#Verbindung der OpenAI Schnittstelle: API-Schlüssel
def openai_verbindung():
    #Damit auf Render keine Fehlermeldung kommt, dass die st.secrets toml fehlt
    api_key1 = os.getenv("OPENAI_API_KEY1")
    api_key2 = os.getenv("OPENAI_API_KEY2")
    gemini_key = os.getenv("GEMINI_API_KEY")


    # st.secrets für das Deployment in StreamlitCloud
    if not api_key1:
        try:
            api_key1 = st.secrets["openai"]["api_key1"]
        except:
            pass

    if not api_key2:
        try:
            api_key2 = st.secrets["openai"]["api_key2"]
        except:
            pass

    if not gemini_key:
        try:
            gemini_key = st.secrets["googleapigemini"]["gemini_api_key"]
        except:
            pass


        
        
    if not api_key1 and not api_key2 and not gemini_key:
        st.error("Es gibt zur Zeit Probleme mit den API-Keys!")
        st.stop()


            
    openai_client1 = None
    if api_key1:
        openai_client1 = openai.OpenAI(api_key=api_key1)
    
    openai_client2 = None
    if api_key2:
        openai_client2 = openai.OpenAI(api_key=api_key2)

    
   #https://www.linkedin.com/pulse/how-create-gemini-pro-chatbot-using-python-streamlit-hafiz-m-ahmed-pxscf 
    gemini_client = None
    if gemini_key:
        genai.configure(api_key=gemini_key)
        gemini_client = genai.GenerativeModel("gemini-1.5-flash")
        
    return openai_client1, openai_client2, gemini_client, api_key1, api_key2



    
#https://platform.openai.com/docs/guides/error-codes/api-errors.
       
def openai_fehlerbehandlung(error):
    error_text = str(error).lower()
    if "api_status_error" in error_text:
        st.error("OpenAI verarbeitet die Anfrage nicht, verändere den Prompt und versuche es erneut. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
    elif "api_connection_error" in error_text: 
        st.error("Problem mit der Verbindung zu OpenAI. Bitte versuche es erneut. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
    elif "rate_limit_error" in error_text:
        st.error("Zu viele Anfragen: Das Kontingent oder die Rate wurde überschritten. Bitte warte einen Moment und versuche es erneut. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
    elif "bad_request_error" in error_text:
        st.error("Ungültige Anfrage: Die Anfrage enthält fehlerhafte Daten. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
    elif "api_timeout_error" in error_text:
        st.error("Zeitüberschreitung bei der Verbindung zu OpenAI. Bitte versuche es später erneut. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
    else:
        st.error("Es ist ein Fehler bei der Kommunikation mit OpenAI aufgetreten. Bitte melde dich, wenn du die Fehlermeldung bekommst.")

    st.info(f"OpenAI-Fehlermeldung: {str(error)}")

#https://ai.google.dev/gemini-api/docs/troubleshooting?hl=de

def gemini_fehlerbehandlung(error):
    error_text = str(error).lower()
    if "400" in error_text or "invalid_argument" in error_text:
    st.error("400 INVALID_ARGUMENT: Die Anfrage enthält fehlerhafte Daten oder Pflichtfelder fehlen. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
    elif "400" in error_text or "failed_precondition" in error_text:
        st.error("400 FAILED_PRECONDITION: Die kostenlose Gemini API ist in deinem Land nicht verfügbar oder die Abrechnung ist nicht aktiviert. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
    elif "403" in error_text or "permission_denied" in error_text:
        st.error("403 PERMISSION_DENIED: Der API-Schlüssel ist ungültig oder hat keine Berechtigung. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
    elif "404" in error_text or "not_found" in error_text:
        st.error("404 NOT_FOUND: Eine angegebene Ressource konnte nicht gefunden werden. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
    elif "429" in error_text or "resource_exhausted" in error_text:
        st.error("429 RESOURCE_EXHAUSTED: Das Kontingent oder die Rate wurde überschritten. Bitte warte einen Moment und versuche es erneut. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
    elif "500" in error_text or "internal" in error_text:
        st.error("500 INTERNAL: Interner Fehler bei Google. Bitte versuche es später erneut. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
    elif "503" in error_text or "unavailable" in error_text:
        st.error("503 UNAVAILABLE: Der Dienst ist derzeit nicht verfügbar. Bitte versuche es später erneut. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
    elif "504" in error_text or "deadline_exceeded" in error_text:
        st.error("504 DEADLINE_EXCEEDED: Die Anfrage konnte nicht rechtzeitig verarbeitet werden. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
    else:
        st.error("Es ist ein Fehler bei der Kommunikation mit der Gemini API ist aufgetreten. Bitte melde dich, wenn du die Fehlermeldung bekommst.")