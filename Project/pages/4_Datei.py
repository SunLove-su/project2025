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