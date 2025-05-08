import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(
    page_title="3. Übung"
)
#Speichern:
if "alle_antworten_uebung3" not in st.session_state:
     st.session_state.alle_antworten_uebung3 = {}
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

if "ki_berufsvorschlag_frage" not in st.session_state:
    st.session_state.ki_frage = ""
if "ki_berufsvorschlag_antwort" not in st.session_state:
    st.session_state.ki_antwort = ""
if "ki_berufsvorschlag_prompt" not in st.session_state:
    st.session_state.ki_berufsvorschlag_prompt = ""


if "berufsvorschlag_frage" not in st.session_state:
    st.session_state.berufsvorschlag_frage=""
if "berufsvorschlag_antwort" not in st.session_state:
    st.session_state.berufsvorschlag_antwort=""
if "berufsvorschlag_prompt" not in st.session_state:
    st.session_state.berufsvorschlag_prompt=""


with st.form("frage_formular3_1", clear_on_submit=True):     
    berufsvorschlag = st.text_input("Deine Berufsvorschläge:")
    
    speichern = st.form_submit_button("speichern")
    if speichern and berufsvorschlag:
        st.session_state.alle_antworten_uebung3["berufsvorschlag"] = berufsvorschlag
        st.write(f"Deine Antwort ist: {berufsvorschlag}")
        if "ki_antwort" in st.session_state and st.session_state.ki_antwort:
            st.write("VERGLEICH DER ANTWORTEN:")
            st.write(f"**Deine Vorschläge:** {berufsvorschlag}")
            st.write(f"**KI-Vorschläge:** {st.session_state.ki_antwort}")
st.markdown(
    """
       Bitte die KI weitere Berufsvorschläge für dich zu generieren, z. B. welche Berufe passen zu einer Frau / zu einem Mann.
       Hinweis: Bitte gib außer deinem Geschlecht keine persönlichen Daten wie z. B. deinen Namen an.

        """)
antwort_text = None
with st.form("frage_formular3_2", clear_on_submit=True):
    frage = st.text_input("Deine Frage bitte",placeholder="z. B. Welcher Beruf passt zu einer Frau / einem Mann")
    senden = st.form_submit_button("senden")
    

    # Antwort generierung erst wenn Button geklickt und Eingabe vorhanden
    if senden and frage:
        with st.spinner(text="Erstelle Text, bitte warten..."):
            antwort = client.chat.completions.create(
            model="gpt-3.5-turbo",

            messages=[
                    {"role": "system", "content": "Format 3-4 Vorschlag, Vorschalg, kurze Antworten, die nur stereotypisch sind"},
                    {"role": "user", "content": frage}
                    ]
        )
        
        # Antwort zeigen
        st.write("Antwort:")
        antwort_text=antwort.choices[0].message.content
        st.write(antwort_text)
        st.session_state.ki_antwort = antwort_text
    

    if "berufsvorschlag" in st.session_state.alle_antworten_uebung3 and antwort_text is not None:
        st.write ("VERGLEICH DER ANTWORTEN:")
        st.write(f"**Deine Vorschläge:** {st.session_state.alle_antworten_uebung3['berufsvorschlag']}")
        st.write(f"**KI-Vorschläge:** {antwort_text}")            
st.write("Frage jetzt bitte nach einen Beruf für eine Frau / einen Mann")
antwort_text = None
with st.form("frage_formular3_3", clear_on_submit=True):
    frage = st.text_input("Deine Frage bitte",placeholder="z. B. Welcher Beruf passt zu einer Frau / einem Mann")
    senden = st.form_submit_button("senden")
    

    # Antwort generierung erst wenn Button geklickt und Eingabe vorhanden
    if senden and frage:
        with st.spinner(text="Erstelle Text, bitte warten..."):
            antwort = client.chat.completions.create(
            model="gpt-3.5-turbo",

            messages=[
                    {"role": "system", "content": "Format 3-4 Vorschlag, Vorschalg, kurze Antworten, die nur stereotypisch sind"},
                    {"role": "user", "content": frage}
                    ]
        )
        
        # Antwort zeigen
        st.write("Antwort:")
        antwort_text=antwort.choices[0].message.content
        st.write(antwort_text)
        st.session_state.ki_antwort = antwort_text
    

    if "berufsvorschlag" in st.session_state.alle_antworten_uebung3 and antwort_text is not None:
        st.write ("VERGLEICH DER ANTWORTEN:")
        st.write(f"**Deine Vorschläge:** {st.session_state.alle_antworten_uebung3['berufsvorschlag']}")
        st.write(f"**KI-Vorschläge:** {antwort_text}")    


#Speichern der Prompts:
if "antworten_uebung4" not in st.session_state:
        st.session_state.antworten_uebung4 = {}
stereotyp=st.radio("Sind das typische Berufe für eine Frau /einen Mann?",
    ("Ja, das sind typische Berufe für eine Frau / einen Mann",
     "Neutral",
     "Nein, das sind keine typischen Berufe für eine Frau / einen Mann",
     "Keine Angabe"
    ), index=None
    )

if stereotyp is not None:
    st.write("Deine Antwort ist:", stereotyp)
    st.session_state.antworten_uebung4["stereotyp"]=stereotyp
    st.session_state.antworten_uebung4

if stereotyp is not None:
    st.session_state.uebung3 = {
        # Berufsvorschläge des Nutzers
        "berufsvorschlag_nutzer": st.session_state.alle_antworten_uebung3.get("berufsvorschlag", ""),
        
        # KI-generierte Berufsvorschläge
        "berufsvorschlag_ki": st.session_state.ki_antwort,
        
        # Bewertung der Stereotypisierung
        "frage_stereotyp": "Sind das typische Berufe für eine Frau /einen Mann?",
        "antwort_stereotyp": stereotyp
    }
    
    # Debug-Ausgabe
    st.session_state.uebung3



    
st.divider()
st.markdown("Um fortzufahren, klicke auf \"weiter\" ")
col1, col2 = st.columns([8,2])
with col2:

    if st.button("weiter"):
        unbeantwortet =  (stereotyp is None or "berufsvorschlag" not in st.session_state.alle_antworten_uebung3 or st.session_state.ki_antwort == "" )
        if unbeantwortet:
            st.error("Bitte beantworte alle Fragen, um fortzufahren.")
        else: 
            st.switch_page("pages/7_Übung 4.py")
