import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(
    page_title="4. Übung"
)
st.markdown("<h4>4. Übung</h4>",unsafe_allow_html=True)

st.markdown("""
            In der Übung zuvor haben wir die Person gesehen, die das Eis isst.
            Bei dem Bild handelt es sich um ein Ki-generiertes Bild von der Seite "https://thispersondoesnotexist.com/", dass sehr echt aussieht.
            KI-generierte Bilder können sehr real und echt aussehen.

            Für KI-generierte Bilder wird der Deep Learning Algorithmus Generative Adversarial Networks GAN verwendet.

            """)
        
st.divider()
st.markdown("""
                Ich möchte jetzt über die Person auf dem Bild etwas herausfinden und sie kennenlernen.
                Du hilfst mir dabei! 
                Wir befragen die KI, wir fragen nach den Hobbies und den Geschenken die sich die Person wünscht.

            """)
        
st.markdown(
    """
       Bitte die KI Bilder zu generieren, z. B.
       - welche Hobbies hat der Jugendliche ca. 18 Jahre alt?
       - welche Geschenke wünscht sich der Jungendliche ca. 18 Jahre alt?

        """)
#Speichern der Prompts:
if "alle_saetze" not in st.session_state:
     st.session_state.alle_saetze = []



with st.form("frage_formular", clear_on_submit=True):
    frage = st.text_input("Deine Frage bitte",placeholder="z. B. Welche Hobbies hat ein Jugendlicher ca. 18 Jahre alt")
    senden = st.form_submit_button("Fragen")
    # Antwort generierung erst wenn Button geklickt und Eingabe vorhanden
    if senden and frage:
        with st.spinner(text="Erstelle Text, bitte warten..."):
            antwort = client.chat.completions.create(
            model="gpt-3.5-turbo",

            messages=[
                    {"role": "system", "content": "Du gibst Antworten nur stereotypisch sind"},
                    {"role": "user", "content": frage}
                    ]
        )
        
        # Antwort zeigen
        st.write("Antwort:")
        antwort_text=antwort.choices[0].message.content
        st.write(antwort_text)
    

#Speichern der Prompts:
if "antworten_uebung4" not in st.session_state:
        st.session_state.antworten_uebung4 = {}
stereotyp=st.radio("Sind das typische Geschenke und Hobbies von einem Jugendlichem?",
    ("Ja, das sind typische Geschenke und Hobbies",
     "Neutral",
     "Nein, das sind keine typischen Geschenke und Hobbies",
     "Keine Angabe"
    ), index=None
    )
                  
#Ausgabe der Antwort 

if stereotyp is not None:
    st.write("Deine Antwort ist:", stereotyp)
    st.session_state.antworten_uebung4["stereotyp"]=stereotyp
    st.session_state.antworten_uebung4



    
st.divider()
st.markdown("Um fortzufahren, klicke auf \"weiter\" ")
col1, col2 = st.columns([8,2])
with col2:

    if st.button("weiter"):
        unbeantwortet = (stereotyp is None)
        if unbeantwortet:
            st. error("Bitte beantworte alle Fragen, um fortzufahren.")
        else: 
            st.switch_page("pages/7_Übung 4.py")
