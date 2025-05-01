import streamlit as st


st.set_page_config(
    page_title="Schulmodul zur Sensibilisierung von KI-generierten Inhalten"
)

st.markdown("<h4>Willkommen zum Schulmodul zur Sensibilisierung KI-generierter Inhalte</h4>", unsafe_allow_html=True)
st.markdown("""Dieses Modul soll die Risiken von KI-generierten Inhalten aufzeigen und auf diese sensibilisieren.
KI findet heute überall Einsatz und bietet uns viele Chancen.
Es gibt aber auch einige Risiken beim Umgang mit KI, z. B. das die generierten Informationen falsch sind und weitere. Diese werden in dem Modul exemplarisch aufgezeigt,
damit ein bewusster Umgang mit KI-Anwendungen erfolgt""")
st.markdown("""
Was Dich erwartet:
- Umfragen zu deinem Nutzungsverhalten und zu deinem Vertrauen zu KI
- Interaktive Übungen zur Erkennung von KI-generierten Inhalten
 """)

#Abtrennung -> Hinweise         
st.divider()
st.markdown("Hinweise zum Modul:")
st.markdown("""
- Dauer: ca. 40 - 45 Minuten
- Teilnahme: anonym
- Freiwilligkeit: freiwillige Teilnahme
- Datenschutz: Demografische Daten (Alter, Geschlecht) werden vertraulich behandelt.
  Es wird sichergestellt, dass eine Zurückverfolgung auf die teilnehmende Person nicht erfolgt.
  Die Daten werden ausschließlich für ein Forschungsprojekt verwendet.

""")
#Abtrennung -> zur nächstem Thema
st.divider()

# funktioniert nur bei großen Layout, bei Handys werden col immer untereinander dargestellt
#Anpassung mit CSS funktionieren nicht, da diese überschrieben werden
#st.button hat seine eigenen Positionen, die können nur mit CSS-Hijacking geändert werden
# d.h. entsprechendes Element untersuchen mit den Entwickler-Modus und den entsprechenden div-container raussuchen
# bei Änderungen der Streamlit version kann es aber zu veränderungen kommen, die Hichaking version ist nicht offiziell
st.markdown("Um mit dem Schulmodul zu beginnen, klicke auf \"Start\" ")
col1, col2 = st.columns([8,2])
with col2:

    if st.button("Start"):
        st.switch_page("Grundwissen über Künstliche Intelligenz (KI)")