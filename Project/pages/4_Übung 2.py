import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

# st.set_page_config(
#     page_title="1. Übung"
# )
st.markdown("<h4>2. Übung</h4>",unsafe_allow_html=True)

st.markdown("""
            In dieser Übung nutzen wir den Satz mit dem schönen Sommertag und dem Erdbeereis aus Übung 1 weiter.
            Diesmal untersuchen wir den Satz etwas genauer.
            Wir machen eine Aufgabe aus unserer Grundschulzeit. Wir haben damals gelernt was Vokale sind (a,e,i,o,u).
            """)
st.divider()
beispielsatz="An einem schönen Sommertag genieße ich ein kühles Erdbeereis."
st.markdown(beispielsatz)

if st.button("ChatGPT nach Vokalen fragen"):
    antwort = client.chat.completions.create(
        model="gpt-3.5-turbo",

        messages=[
 #                 {"role": "system", "content": "Zähle die Vokale für den Satz und gebe sie so aus, dass ich sie gut lesen kann."},
                  {"role": "user", "content": f"Zähle die Vokale für den Satz {beispielsatz} in dem format kleinbuchstabe : zahl und gebe die Vokale untereinander aus mit : und der Anzahl. Ohne einen Kommentar danach"}
                 ]  )
    
    # Antwort zeigen
    st.write("Antwort:")
    antwort_text=antwort.choices[0].message.content
    st.write(antwort_text)

st.write("Jetzt zählen wir selbst nach:")
if st.button("Vokale selbst zählen"):
    satzklein = beispielsatz.lower()
    vokale ="aeiouäöü"

    for vokal in vokale:
        anzahl=satzklein.count(vokal)
        if anzahl >0:
            st.write(f"Buchstabe {vokal} : {anzahl}")
    st.markdown("""
                    Wie du siehst macht die KI-Anwendung auch Fehler. Sie kann gut Texte erzeugen, Fragen beantworten
                    aber nicht alles ist richtig! Sie kann sich auch vertun, deshalb ist es wichtig, dass Ergebnis immer zu prüfen!

    
                """)




#Idee Schüler sollen in einem Prompt die KI bitten einen Text zu schreiben, eine spannende
#Geschichte erfinden. Dabei werden die Schüler gebeten, zu überlegen, was sie sich als Ergebnis
#vorstellen
#Das Ergebnis weicht von ihrer Vorstellung ab, sie geben ggfls einen neuen Prompt ein, um es
#nochmal zu versuchen, dasselbe Ergebnis
#beim dritten mal die KI den Text nicht als Text aus sondern als Stichpunkte oder komplett anderer
#Kontext
# 
#Danach aufzeigen, wie oft der User einen Prompt eingegeben hat, was er eingegeben hat
#und dann das die KI den Kontext nicht immer versteht, Fehler machen kann und die KI
#Texte nach wahrscheinlichkeiten generiert d.h. es folgt Wort für Wort. Während wir uns
#in unseren Gedanken schon ein Bild über den Inhalt des Textes machen
#
#
#