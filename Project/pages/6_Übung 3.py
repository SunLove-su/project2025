import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(
    page_title="4. Übung"
)
#Speichern:
if "alle_antworten_uebung3" not in st.session_state:
     st.session_state.alle_antworten_uebung3 = {}
st.markdown("<h4>4. Übung</h4>",unsafe_allow_html=True)

st.markdown("""
            In der Übung zuvor haben wir die Person gesehen, die das Eis isst.
            Bei dem Bild handelt es sich um ein KI-generiertes Bild von der Seite "https://thispersondoesnotexist.com/", dass sehr echt aussieht.
            
            Für KI-generierte Bilder wird der Deep Learning Algorithmus Generative Adversarial Networks (GAN) verwendet.

            """)
        
st.divider()
st.markdown("""
                Ich möchte der Person auf dem Bild ein Geschenk kaufen und du hilfst mir dabei.
                Was wäre passend für einen 18-jährigen Mann?            
            """)
with st.form("frage_formular3_1", clear_on_submit=True):     
    geschenkempfehlung = st.text_input("Deine Geschenkideen:")
    speichern = st.form_submit_button("speichern")
if geschenkempfehlung:
    st.session_state.alle_antworten_uebung3["geschenkempfehlung"] = geschenkempfehlung
    st.write(f"Deine Antwort ist: {geschenkempfehlung}")
st.markdown(
    """
       Bitte die KI weitere Geschenkideen zu generieren, z. B. was kann ich einen 18 Jährigen schenken

        """)
antwort_text = None
with st.form("frage_formular3_2", clear_on_submit=True):
    frage = st.text_input("Deine Frage bitte",placeholder="z. B. Was kann ich einem 18 Jährigen schenken")
    senden = st.form_submit_button("fragen")
    # Antwort generierung erst wenn Button geklickt und Eingabe vorhanden
    if senden and frage:
        with st.spinner(text="Erstelle Text, bitte warten..."):
            antwort = client.chat.completions.create(
            model="gpt-3.5-turbo",

            messages=[
                    {"role": "system", "content": "Du gibst kurze Antworten, die nur stereotypisch sind"},
                    {"role": "user", "content": frage}
                    ]
        )
        
        # Antwort zeigen
        st.write("Antwort:")
        antwort_text=antwort.choices[0].message.content
        st.write(antwort_text)
    

if geschenkempfehlung is None or antwort_text:
    st.markdown(f"""
                    ***Antworten:***\n
                    ***Deine Vorschläge:*** {geschenkempfehlung},\n
                    ***KI:*** {antwort_text} 
                """)     

#Speichern der Prompts:
if "antworten_uebung4" not in st.session_state:
        st.session_state.antworten_uebung4 = {}
stereotyp=st.radio("Sind das typische Geschenke für einen Jugendlichen?",
    ("Ja, das sind typische Geschenke",
     "Neutral",
     "Nein, das sind keine typischen Geschenke",
     "Keine Angabe"
    ), index=None
    )

if stereotyp is not None:
    st.write("Deine Antwort ist:", stereotyp)
    st.session_state.antworten_uebung4["stereotyp"]=stereotyp
    st.session_state.antworten_uebung4



    
st.divider()
st.markdown("Um fortzufahren, klicke auf \"weiter\" ")
col1, col2 = st.columns([8,2])
with col2:

    if st.button("weiter"):
        unbeantwortet = (stereotyp is None or geschenkempfehlung is None)
        if unbeantwortet:
            st. error("Bitte beantworte alle Fragen, um fortzufahren.")
        else: 
            st.switch_page("pages/7_Übung 4.py")
