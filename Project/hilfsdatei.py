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
def login():
   if not st.session_state.get("eingeloggt"): 
        st.write("Bitte gebe das Passwort ein, damit du teilnehmen kannst")
        eingabe = st.text_input("Passwort")
        if st.button("Anmelden"):
            passwort = eingabe
            # Überprüfung ob das eingegebene Passwort mit dem gesetzten Passwort aus der secrets Datei übereinstimmt
            if passwort == st.secrets["umfrage_passwort"]:
                st.session_state["eingeloggt"] = True
                st.rerun()
            # Admin-Passwort / Admin kann die Seitenleiste sehen und muss nicht bedingt alle Fragen ausfüllen, um auf
            # die entsprechenden Seiten im Modul zu kommen.
            elif passwort == st.secrets["admin_passwort"]:
                st.session_state["eingeloggt"] = True
                st.session_state["admin"] = True
                st.rerun()
            else:
                st.error("Das Passwort ist falsch")
        st.stop()
 


