import streamlit as st
st.set_page_config(
    page_title="5. Übung"
 )
st.markdown("<h4>5. Übung</h4>",unsafe_allow_html=True)

st.markdown("""
            In den Übungen die wir durchgegangen sind haben wir einiges gelernt.
            Zum Abschluss gibt es noch ein paar Fragen die ich dir stellen möchte und dann sind wir schon fertig
            """)
if "antworten_abschlussumfrage" not in st.session_state:
        st.session_state.antworten_abschlussumfrage = {}
