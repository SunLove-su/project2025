"""
Startseite des Schulmoduls zur Sensibilisierung KI-generierter Inhalte
Beschreibung des Schulmoduls und Hinweise
"""

# Importieren der notwendigen Module

import streamlit as st
#datetime zur Erfassung der Startzeit bei der Umfrage
import datetime
#Hilfsdatei mit Funktionen die Mehrfach auftreten, z. B. die Anmeldung mit dem Passwort und die st.Page-config.
import hilfsdatei

#Überschrift der Seite
seiten_titel = "Lerneinheit zur Sensibilisierung von KI-generierten Inhalten"
hilfsdatei.titel_seite(titel_seite)
#Anmeldung mit Passwort, weil bei StreamlitCloud jeder Zugriff hätte
hilfsdatei.teilnehmer_anmelden()

#Überschrift des Schulmoduls
ueberschrift_seite = "Willkommen zur Lerneinheit zur Sensibilisierung KI-generierter Inhalte"
st.markdown(f"<h4>{ueberschrift_seite}</h4>", unsafe_allow_html=True)

#Einleitung des Schulmoduls
einleitung_text ="""
                  Diese Lerneinheit soll die Risiken von KI-generierten Inhalten aufzeigen und
                  dich für diese sensibilisieren. Künstliche Intelligenz (KI) findet heute überall
                  Einsatz und bietet uns viele Chancen. Es gibtaber auch einige Risiken beim Umgang
                  mit KI, z. B. dass die generierten Informationen falsch sind u.a. Diese werden in
                  der Lerneinheit exemplarisch aufgezeigt, damit du bewusster mit KI-Anwendungen
                  umgehen kannst!"""
st.markdown(einleitung_text)

#Trennungslinie
st.divider()

#Aufbau des Schulmoduls
schulmodul_aufbau="""
                  ***Dich erwarten:***
                  - ***Einstieg***: Beantworte Fragen zu deinem Nutzungsverhalten und denem Vertrauen zu KI-generierten Inhalten.
                  - ***Grundwissen***: Lerne etwas über die KI und die Anwendungsbereiche.
                  - ***Übungen***: Erkenne KI-generierte Inhalte und interagiere mit KI-Anwendungen.
                  - ***Abschluss***: Beantworte erneut Fragen und reflektiere das Gelernte.
            """
st.markdown(schulmodul_aufbau)

#Trennungslinie       
st.divider()

#Hinweise zum Modul
modul_hinweise=(
            """
                ***Hinweise zur Lerneinheit:***
                - Dauer: ca. 40 - 45 Minuten
                - Teilnahme: anonym
                - Freiwilligkeit: freiwillige Teilnahme
                - Datenschutz: Demografische Daten (Alter, Geschlecht) werden vertraulich behandelt.
                  Es wird sichergestellt, dass eine Zurückverfolgung auf die teilnehmende Person nicht
                  erfolgt. Die Daten werden ausschließlich für mein Forschungsprojekt verwendet.
            """)
st.markdown(modul_hinweise)

#Trennungslinie
st.divider()

#Text zum Start des Schulmoduls
start_text=("""
               Bist du Bereit mit der Lerneinheit zu beginnen und über KI zu lernen,
               dann klicke auf \"Start\"
            """)
st.markdown(start_text)


#Abfrage zur nächsten Seite.
if st.button("Start"):
#Beginn der Messung der Startzeit der Umfrage.
      start_zeit = datetime.datetime.now()
#Speichern der Startzeit.
      st.session_state["start_zeit"] = start_zeit
#Weiterleitung zur nächsten Seite.
      naechste_seite ="pages/2_Umfrage.py"
      st.switch_page(naechste_seite)