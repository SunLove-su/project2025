import streamlit as st
#datetime zur Erfassung der Startzeit bei der Umfrage
import datetime
#Hilfsdatei mit Funktionen die Mehrfach auftreten, z. B. die Anmeldung mit dem Passwort und die st.Page-config.
import hilfsdatei

#Überschrift der Seite
hilfsdatei.seite("Lerneinheit zur Sensibilisierung von KI-generierten Inhalten")
#Anmeldung mit Passwort, weil bei StreamlitCloud jeder Zugriff hätte
hilfsdatei.login()

st.markdown("<h4>Willkommen zum Lerneinheit zur Sensibilisierung KI-generierter Inhalte</h4>", unsafe_allow_html=True)
st.markdown("""Diese Lerneinheit soll die Risiken von KI-generierten Inhalten aufzeigen und dich für diese sensibilisieren.
Künstliche Intelligenz (KI) findet heute überall Einsatz und bietet uns viele Chancen.
Es gibt aber auch einige Risiken beim Umgang mit KI, z. B. das die generierten Informationen falsch sind u.a. Diese werden in der Lerneinheit exemplarisch aufgezeigt,
damit du bewusster mit KI-Anwendungen umgehen kannst!""")

st.divider()

st.markdown("""
                    ***Dich erwarten:***
                      - ***Einstieg***: Beantworte Fragen zu deinem Nutzungsverhalten und denem Vertrauen zu KI-generierten Inhalten.
                      - ***Grundwissen***: Lerne etwas über die KI und die Anwendungsbereiche.
                      - ***Übungen***: Erkenne KI-generierte Inhalte und interagiere mit KI-Anwendungen.
                      - ***Abschluss***: Beantworte erneut Fragen und reflektiere das Gelernte.
            """)

#Grafische Trennung durch eine Linie       
st.divider()
#Inhalt über das Modul
st.markdown("***Hinweise zur Lerneinheit:***")
st.markdown("""
                - Dauer: ca. 40 - 45 Minuten
                - Teilnahme: anonym
                - Freiwilligkeit: freiwillige Teilnahme
                - Datenschutz: Demografische Daten (Alter, Geschlecht) werden vertraulich behandelt.
                  Es wird sichergestellt, dass eine Zurückverfolgung auf die teilnehmende Person nicht erfolgt.
                  Die Daten werden ausschließlich für mein Forschungsprojekt verwendet.
            """)
#Grafische Trennung durch eine Linie
st.divider()

st.markdown("Bist du Bereit mit der Lerneinheit zu beginnen und über KI zu lernen, dann klicke auf \"Start\" ")
#Anpassung der Position des Buttons, CSS funktioniert hier nicht nur durch Hijacking.
#Anpassung durch Spalten, wobei die erste 80% und die andere 20 % annimmt. 
#Bei entsprechender Auflösung und Gerät ist der Button rechts. Bei kleineren Seiten funktioniert das nicht
#Spalten werden bei kleinen Bildschirmen immer untereinander dargestellt.

col1, col2 = st.columns([8,2])
with col2:
#Abfrage zur nächsten Seite.
    if st.button("Start"):
#Beginn der Messung der Startzeit der Umfrage.
      startzeit = datetime.datetime.now()
#Speichern der Startzeit.
      st.session_state["startzeit"] =startzeit
#Weiterleitung zur nächsten Seite.
      st.switch_page("pages/2_Umfrage.py")