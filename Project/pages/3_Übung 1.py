import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

# st.set_page_config(
#     page_title="1. Übung"
# )
st.markdown("<h4>1. Übung</h4>",unsafe_allow_html=True)
st.markdown("""
            Beginnen wir mit der ersten Übung.
            Auf der Seite davor haben wir gelernt, was KI ist und was eine KI kann.
            Jetzt verwenden wir eine KI-Anwendung, eine generative KI, die dir vielleicht bekannt vorkommt
            ChatGPT.
            Bei ChatGPT handelt es sich um ein Large Language Modell (LLM).
            Mit ChatGPT können z. B. Texte erzeugt, Übersetzungen gestellt und Informationen eingeholt werden usw.
            """)
st.divider()

#Erstelle mir einen Satz mit einem schönen Sommertag und Erdbeereis. Der Satz soll keine ausschweifende Beschreibungen enthalten
st.markdown("""
               Ich möchte, dass ChatGPT mir einen Satz erzeugt, in dem es um einen schönen Sommertag geht
               in der die Sonne scheint und ich ein Erdbeereis esse. 
            """)

satzanzeigen_button=st.button("Satz anzeigen", key="satzanzeigenlassen")
#An einem schönen Sommertag genieße ich ein kühles Erdbeereis.
#
if satzanzeigen_button:
    st.write(
        """
            An einem schönen Sommertag genieße ich ein kühles Erdbeereis.
        """)

st.divider()
st.markdown(
    """Jetzt bist du an der Reihe, bitte ChatGPT auch dir einen Satz über einen schönen Sommertag mit einem Erdbeereis zu erstellen.
        """)
#Speichern der Prompts:
if "alle_saetze" not in st.session_state:
     st.session_state.alle_saetze = []

# Eingabe und Button
satz = st.text_input("Dein Satz bitte",placeholder="z. B. Erstelle mir einen Satz mit schönen Sommertag und Erdbeereis")
if st.button("Satz erstellen") and satz:
    # Antwort holen
    antwort = client.chat.completions.create(
        model="gpt-3.5-turbo",

        messages=[
                  {"role": "system", "content": "Du gibst Antworten aus ohne ausschweifende Beschreibungen."},
                  {"role": "user", "content": satz}
                 ]
    )
    
    # Antwort zeigen
    st.write("Antwort:")
    antwort_text=antwort.choices[0].message.content
    st.write(antwort_text)
  
    st.divider()
    st.markdown("""
                Siehst du, du hast einen komplett anderen Satz erhalten!
                Frage nochmal nach.

                 """)
    
    satzvoneinemmenschen=st.radio("Ist es wahrscheinlich, dass ein Mensch den Satz auch so schreiben würde?",
                                  ["Ja, sehr wahrscheinlich",
                                   "Ja, wahrscheinlich",
                                   "Neutral",
                                   "Nein, unwahrscheinlich",
                                   "Nein, sehr unwahrscheinlich",
                                   "Keine Angabe"
                                   ], index=None
    )

#                Mein Satz oben ändert sich nicht, weil ich die Anfrage einmal an ChatGPT gestellt habe
#                und sie fest als Beispiel in unsere Übung aufgenommen habe.

    # Alle Sätze anzeigen
    st.write("Dein Satz:")
    st.write(satz)
    st.session_state.alle_saetze.append(satz)
   
    st.session_state.alle_saetze 
    
st.divider()
st.markdown("Um fortzufahren, klicke auf \"weiter\" ")
col1, col2 = st.columns([8,2])
with col2:

    if st.button("weiter"):
        st.switch_page("pages/4_Datei.py")

# st.markdown("""
#             In der ersten Übung hast du gerlernt, dass
#             - bei jedem Prompt ein neuer Text generiert wir
#             - dass es schwer ist den generierten Text von einer Maschine zu unterscheiden.
#             """)

