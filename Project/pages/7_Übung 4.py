import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(
    page_title="4. Übung"
)
st.markdown("<h4>4. Übung</h4>",unsafe_allow_html=True)

st.markdown("""
            In der Übung zuvor haben wir die Person gesehen, die das Eis isst.
            Bei dem Bild handelt es sich um ein Ki-generiertes Bild, dass sehr echt aussieht.
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

# Eingabe und Button
satz = st.text_input("Deine Frage bitte",placeholder="z. B. Welche Hobbies wünscht sich der Jugendliche ca. 18 Jahre alt")
if st.button("Antwort erstellen") and satz:
    # Antwort holen
    with st.spinner(text="Erstelle Text, bitte warten..."):
        antwort = client.chat.completions.create(
        model="gpt-3.5-turbo",

        messages=[
                  {"role": "system", "content": "Du gibst Antworten nur stereotypisch sind"},
                  {"role": "user", "content": satz}
                 ]
    )
    
    # Antwort zeigen
    st.write("Antwort:")
    antwort_text=antwort.choices[0].message.content
    st.write(antwort_text)
  
    st.divider()

##################VERSUCH BILD
# # Eingabe und Button
# beschreibung = st.text_input("Zeichne eine junge Frau Mitte 30 bei ihrer Arbeit",placeholder="z. B. Erstelle mir ein Bild von einer jungen Frau mit braunen Haaren in einem Kleid im Disney-Stil")
# if st.button("Bild erstellen") and beschreibung:
#     with st.spinner(text="Generiere Bild, bitte warten..."):
#     # Antwort holen
#         antwort = client.images.generate(
#         model="dall-e-3",
#         prompt=(f"{beschreibung} generiere nur stereotypische Bilder."),
#         n=1,
#         size="1024x1024"

#     )
    
#     # Antwort zeigen
#     st.write("Bild:")
#         # Bild anzeigen
#     generiertesBild = antwort.data[0].url
#     st.image(generiertesBild)
  
#     st.divider()


#     st.markdown("""
#                     Siehst du, du hast ein Bild generieren lassen.

#                     """)
#    st.divider()
#Speichern der Prompts:
if "antworten_uebung4" not in st.session_state:
        st.session_state.antworten_uebung4 = {}
stereotyp=st.radio("Sind das typische Geschenke und Hobbies von einem Jugendlichem?",
    ["Ja, das sind typische Geschenke und Hobbies",
     "Neutral",
     "Nein, das sind keine typischen Geschenke und Hobbies",
     "Keine Angabe"
    ], index=None
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
        st.switch_page("pages/8_Übung 5.py")
