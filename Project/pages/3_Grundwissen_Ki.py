import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(
    page_title="Grundwissen über Künstliche Intelligenz (KI)"
)

st.markdown("<h4>Grundwissen über Künstliche Intelligenz (KI)</h4>",unsafe_allow_html=True)
st.markdown("""
            Auf dieser Seite lernen wir etwas über die Grundlagen der KI.
            Es sind neue oder schon für dich bekannte Informationen.
            """)
st.divider()

with st.expander("Was ist KI?",icon=":material/double_arrow:"):
     st.markdown("""
                    Stell dir ein Computer Fußballspiel vor:
                    - Bei normaler Programmierung bekommt der Computer genaue Befehle, z. B. "Steuer den Fußballspieler nach vorne, vorne rechts liegt der Ball. Lass ihn aufs
                      Tor schießen." Wird eine Möglichkeit nicht in einem Befehl erfasst, z. B. der Ball liegt an einer anderen Position, bleibt das Programm stehen.
                      
                    - Bei der KI ist es anders. Sie analysiert mehr als 1.000.000 unterschiedliche Fußballspiele und erfasst dabei Muster und Merkmale.
                      Liegt der Ball an einer anderen Stelle, trifft sie eine Entscheidung und steuert den Spieler dorthin.
                    
                    - Bei neuen Situationen, z. B. wenn der Ball im Zuschauerblock landet, kann sie falsche Entscheidungen treffen und den Spieler dorthin leiten.
                    
                    - Während du das Spielprinzip meist nach ein, zwei Versuchen verstehst, braucht die KI dafür tausende Spiele.
                     Sie lernt durch Auswertung der bereitgestellten Daten und kann dadurch selbst Entscheidungen treffen. Damit ahmt sie die Intelligenz eines Menschen nach.
                    

                      """
     )

with st.expander("Wie funktioniert KI?",icon=":material/double_arrow:"):
     st.markdown("""
                 Beim Fußballspiel haben wir gesehen, dass die KI:
                 1. Viele Daten braucht, um Erfahrungen aus vielen unterschiedlichen Fußballspielen zu sammeln
                 2. Muster erkennt, sodass der Spieler dem Ball im Feld hinterher läuft.
                 3. Erlerntes anwendet und daraus Entscheidungen trifft, z. B. der Spieler läuft zum Ball, obwohl er vorne links liegt
                 4. Fehler machen kann und z. B. der Spieler zum Zuschauerblock läuft
                """)

with st.expander("KI-Begriffe",icon=":material/double_arrow:"):
     st.markdown("""
                - Algorithmus: Schritt-für-Schritt Anleitung z. B. wie bei einem Computerprogramm
                - Machine Learning: Teilbereich der KI, der viele Daten nutzt, um Muster zu erkennen.
                   - Überwachtes Lernen: Unterstützung der KI, indem Daten mit Erklärungen und Informationen zur Verfügung gestellt werden.
                   - Unüberwachtes Lernen: Keine Unterstützung, die KI analysiert die Daten ohne zusätzliche Informationen.
                   - Künstliche Neuronale Netze (KNN): Ahmen den Aufbau und die Funktionsweise eines Gehirns nach.
                                                       Beispiel: Jeder Spieler ist ein Neuron, der Ball ist eine Information.                                                    
                                                       Der linke Torwart schießt den Ball zum Verteidiger, dieser zum Mittelfeldspieler, dieser zum Stürmer.
                                                       Jeder Spieler entscheidet, zu wem er den Ball spielt. 
                                                       Die Spieler und ihre Möglichkeiten den Ball zu spielen stellen ein Netz dar und mit dem Training werden sie besser.
                                                    
                   - Deep Learning: Komplexeres Netz, mit mehreren Spielerebenen auf dem Feld und bestimmten Aufgaben:
                                    Erste Reihe erkennt Ballposition, zweite findet freie Räume, dritte plant Laufwege und letzte macht den Torschuss.
                - Prompt: Befehle bzw. Eingaben, die wir schriftlich oder gesprochen der  KI-Anwendung übergeben
                - Generative KI (Gen-KI): KI-Anwendungen, die durch das gelernte neue Inhalte erzeugen
                    """)
with st.expander("Was kann KI?",icon=":material/double_arrow:"):
     st.markdown("""
                    KI kann unterschiedliche Aufgaben ausführen:
                    - Bilder erkennen/erstellen: KI generiert Bilder nach deinen Vorgaben im Prompt, z. B. DALL E, Midjourney etc.
                    - Text erkennen/erstellen/übersetzen: KI antwortet auf deine Prompts, generiert Texte und übersetzt Texte, z. B. ChatGPT, Perplecity
                    - Sprache verstehen/antworten: KI versteht empfängt deine Sprache und antwortet, z. B. Alexa und Siri
                    - Muster/Merkmale erkennen: KI analysiert Muster und unterstützt bei Diagnosen oder Vorhersagen, z. B. bei Krankheiten oder zur Gefahrenabwehr
                      usw...
               """)

#Speichern der Prompts:
if "antworten_grundwissen" not in st.session_state:
    st.session_state.antworten_grundwissen = []
#Speichern der Anzahl der Prompts ohne Session.State-Befehl wird durch neu eingeben einer Frage wieder 0 gesetzt
if "anzahleingaben_grundwissen" not in st.session_state:
    st.session_state.anzahleingaben_grundwissen = 0

#st.text_input hat Bugs
# Eingabe und Button
with st.form("frage_formular", clear_on_submit=True):
    frage = st.text_input("Falls du noch mehr Wissen möchtest, frag die KI!", 
                          placeholder="Du kannst mehere Fragen stellen,")
    senden = st.form_submit_button("Fragen")

    st.markdown("Wenn du keine Fragen mehr hast, scrolle bitte weiter nach unten")
# Antwort generierung erst wenn Button geklickt und Eingabe vorhanden
if senden and frage:

    with st.spinner(text="Erstelle Text, bitte warten..."):
        antwort = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": frage}]
        )
        antwort_text = antwort.choices[0].message.content

    # Prompt-Zähler aktualisieren
    st.session_state.anzahleingaben_grundwissen += 1
    anzahleingaben = st.session_state.anzahleingaben_grundwissen

    # Antwort anzeigen
    st.write("Antwort:")
    st.write(antwort_text)

    # Frage anzeigen
    st.write("Deine Frage:")
    st.write(frage)

    # Frage + Antwort speichern
    st.session_state.antworten_grundwissen.append({
        "Frage": frage,
        "Antwort": antwort_text,
        "Anzahl Prompts": anzahleingaben
    })
st.write("")
#Überprüfungsfrage: Sicherstellung, dass die Textbausteine gelesen wurden
st.divider()
ueberpruefungsfrage=st.radio("Welche Aussage über KI trifft zu?",
                            ("KI braucht Schritt für Schritt-Anweisungen",
                             "KI kann jede Aufgabe lösen und macht keine Fehler",
                             "KI braucht sehr viele Daten um zu lernen und macht trotzdem Fehler",
                             "Keine der Dargestellten Fragen ist richtig"),
                             index=None,

)
richtigeAntwort="KI braucht sehr viele Daten um zu lernen und macht trotzdem Fehler"



st.divider()
st.markdown("Um fortzufahren, klicke auf \"weiter\" ")
col1, col2 = st.columns([8,2])
with col2:

    if st.button("weiter"):
        if ueberpruefungsfrage is not None:
            if ueberpruefungsfrage==richtigeAntwort:
               st.switch_page("pages/4_Übung 1.py")
            else:
                st.error("Die Antwort ist falsch. Bitte lies nochmal den Baustein Grundlagen")
        else:
            st.error("Bitte beantworte die Frage, um fortzufahren")