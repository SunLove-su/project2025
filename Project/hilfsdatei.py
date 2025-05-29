import streamlit as st

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
                try:
                    basis_passwort = st.secrets["umfrage_passwort"]
                except:
                    basis_passwort = os.getenv("UMFRAGE_PASSWORT")
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
                else: 
                    try:
                        admin_pw  == st.secrets["admin_passwort"]:
                    except:
                        admin_pw  = os.getenv("ADMIN_PASSWORT")
                    if passwort == admin_pw:
                        st.session_state["eingeloggt"] = True
                        st.session_state["admin"] = True
                        st.session_state["teilnehmergruppe_info"] ="admin"

                        st.rerun()
                    else:
                        st.error("Das Passwort ist falsch")
            elif anmelden and not eingabe:
                st.error("Bitte gib ein Passwort ein.")
        st.stop()
    
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