import streamlit as st
import openai
import hilfsdatei


try: 
    client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])
except KeyError:
    st.error("Kein API Key für OpenAI vorhanden. Abfragen über OpenAI nicht möglich")
    
hilfsdatei.seite("Grundwissen über Künstliche Intelligenz (KI)")
hilfsdatei.login()


st.markdown("<h4>Grundwissen über Künstliche Intelligenz (KI)</h4>",unsafe_allow_html=True)
st.markdown("""
            Auf dieser Seite lernst du etwas über die Grundlagen der KI.
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
                 Beim Fußballspiel hast du gesehen, dass die KI:
                 1. Viele Daten braucht, um Erfahrungen aus vielen unterschiedlichen Fußballspielen zu sammeln
                 2. Muster erkennt, sodass der Spieler dem Ball im Feld hinterher läuft.
                 3. Erlerntes anwendet und daraus Entscheidungen trifft, z. B. der Spieler läuft zum Ball, obwohl er vorne links liegt
                 4. Fehler machen kann und z. B. der Spieler zum Zuschauerblock läuft
                """)

with st.expander("Definition KI-Begriffe",icon=":material/double_arrow:"):
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
                                    Erste Reihe erkennt Ballposition, zweite findet freie Räume, dritte plant Laufwege und die letzte macht den Torschuss.
                - Prompt: Befehle bzw. Eingaben, die du schriftlich oder gesprochen der  KI-Anwendung übergeben
                - Generative KI (Gen-KI): KI-Anwendungen, die durch das Gelernte neue Inhalte erzeugen
                    """)
with st.expander("Was kann KI?",icon=":material/double_arrow:"):
     st.markdown("""
                    KI kann unterschiedliche Aufgaben ausführen:
                    - Bilder erkennen/erstellen: KI generiert Bilder nach deinen Vorgaben im Prompt, z. B. DALL E, Midjourney etc.
                    - Text erkennen/erstellen/übersetzen: KI antwortet auf deine Prompts, generiert Texte und übersetzt Texte, z. B. ChatGPT, Perplexity
                    - Sprache verstehen/antworten: KI empfängt und versteht deine  Sprache und antwortet, z. B. Alexa und Siri
                    - Muster/Merkmale erkennen: KI analysiert Muster und unterstützt bei Diagnosen oder Vorhersagen, z. B. bei Krankheiten oder zur Gefahrenabwehr
                      usw...
               """)
#Speichern aller Daten auf der Seite
if "grundwissen_ki" not in st.session_state:
    st.session_state.grundwissen_ki = []


#Speichern der Anzahl der Prompts ohne Session.State-Befehl wird durch neu eingeben einer Frage wieder 0 gesetzt
if "anzahleingaben_grundwissen" not in st.session_state:
    st.session_state.anzahleingaben_grundwissen = 0
#tab1 = st.tabs(["Fragen an die KI"])[0]
#st.text_input hat Bugs
# Eingabe und Button
containerfokus = st.container()
with containerfokus:
    with st.expander("Fragen an die KI", expanded=True):
    #with tab1:
        with st.form("frage_formular", clear_on_submit=True):
            frage = st.text_input("Falls du noch mehr Wissen möchtest, frag die KI!", 
                                placeholder="Du kannst mehrere Fragen stellen")
            senden = st.form_submit_button("Fragen")

            st.markdown("Wenn du keine Fragen mehr hast, scrolle bitte weiter nach unten")
            # Antwort generierung erst wenn Button geklickt und Eingabe vorhanden
            try:
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
                        # Frage anzeigen
                        st.write("Deine Frage:")
                        st.write(frage)


                        # Antwort anzeigen
                        st.write("Antwort:")
                        st.write(antwort_text)

            
                        # Frage und  Antwort speichern
                        st.session_state.grundwissen_ki.append({
                            "Bereich": "Grundwissen KI",
                            "Typ": "Grundwissen-KI-Interaktion",
                            "Frage": frage,
                            "Antwort": antwort_text,
                            "Anzahl Prompts": anzahleingaben
                        })
                st.session_state.grundwissen_ki
            except Exception as error:
                    hilfsdatei.openai_fehlerbehandlung(error)
                
            st.write("")
#Überprüfungsfrage: Sicherstellung, dass die Textbausteine gelesen wurden
st.divider()
if "anzahl_ueberpruefungsfrage" not in st.session_state:
    st.session_state.anzahl_ueberpruefungsfrage = 0

def zaehle_aenderung():
    st.session_state.anzahl_ueberpruefungsfrage +=1

st.write ("Nachdem du jetzt ein paar Informationen über KI erhalten hast, beantworte bitte die folgende Frage:")
frageueberpruefung="Welche Aussage über KI trifft zu?"
ueberpruefungsfrage=st.radio(frageueberpruefung,
                            ("KI braucht Schritt für Schritt-Anweisungen",
                             "KI kann jede Aufgabe lösen und macht keine Fehler",
                             "KI braucht sehr viele Daten um zu lernen und macht trotzdem Fehler",
                             "Keine der Dargestellten Fragen ist richtig"),
                             index=None,
                             on_change=zaehle_aenderung
)


if ueberpruefungsfrage is not None:
    st.session_state.grundwissen_ki.append({
    "Bereich": "Grundwissen KI",
    "Typ": "Ueberpruefungsfrage",
    "Frage":   frageueberpruefung,
    "Antwort": ueberpruefungsfrage
    })
    st.write(f"Du hast die Antwort gegeben: {ueberpruefungsfrage}.")


   
richtigeAntwort="KI braucht sehr viele Daten um zu lernen und macht trotzdem Fehler"



st.divider()
st.markdown("Um fortzufahren, klicke auf \"weiter\" ")
col1, col2 = st.columns([8,2])
with col2:

    if st.button("weiter"):
        unbeantwortet = False

        if ueberpruefungsfrage is None:
            st.error("Bitte Beantworte die Überprüfungsfrage.")
            unbeantwortet = True 
        elif ueberpruefungsfrage != richtigeAntwort:
            st.error("Deine Antwort ist leider falsch. Bitte lies den Inhalt nochmal und versuche es erneut.")
            unbeantwortet = True

        if not unbeantwortet and ueberpruefungsfrage==richtigeAntwort:
            st.info("Deine Antwort war richtig!")
              
            st.switch_page("pages/4_Übung 1.py")
