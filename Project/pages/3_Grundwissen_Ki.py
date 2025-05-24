import streamlit as st
import openai
import hilfsdatei

#Verbindung zu OpenAI
try: 
    client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])
#Fehlermeldung, falls der API-Schlüssel falsch ist
except KeyError:
    st.error("Kein API Key für OpenAI vorhanden. Abfragen über OpenAI nicht möglich")
#Überschrift der Seite    
hilfsdatei.seite("Grundwissen über Künstliche Intelligenz (KI)")
#Sicherstellen, dass ein Zugriff der Seiten nur mit Passwort erfolgt, und dass User keine Navigationsseite sehen
hilfsdatei.login()

#Überschrift der Seite
st.markdown("<h4>Grundwissen über Künstliche Intelligenz (KI)</h4>",unsafe_allow_html=True)
st.markdown("""
            Auf dieser Seite lernst du etwas über die Grundlagen der KI.
            Es sind neue oder schon für dich bekannte Informationen.
            """)
#Trennungslinie
st.divider()
#Expander um Wissen von der Darstellung optimiert für die Teilnehmer zur Verfügung zu stellen
#Interaktion, der Teilnehmer. Expander müssen aktiv geöffnet werden.

#Expander zum Thema "Was ist KI"
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

#Expander zum Thema "Wie funktioniert KI"
with st.expander("Wie funktioniert KI?",icon=":material/double_arrow:"):
     st.markdown("""
                 Beim Fußballspiel hast du gesehen, dass die KI:
                 1. Viele Daten braucht, um Erfahrungen aus vielen unterschiedlichen Fußballspielen zu sammeln
                 2. Muster erkennt, sodass der Spieler dem Ball im Feld hinterher läuft.
                 3. Erlerntes anwendet und daraus Entscheidungen trifft, z. B. der Spieler läuft zum Ball, obwohl er vorne links liegt
                 4. Fehler machen kann und z. B. der Spieler zum Zuschauerblock läuft
                """)
#Expander zum Thema "Definition KI-Begriffe"
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

#Expander zum Thema was kann KI
with st.expander("Was kann KI?",icon=":material/double_arrow:"):
     st.markdown("""
                    KI kann unterschiedliche Aufgaben ausführen:
                    - Bilder erkennen/erstellen: KI generiert Bilder nach deinen Vorgaben im Prompt, z. B. DALL E, Midjourney etc.
                    - Text erkennen/erstellen/übersetzen: KI antwortet auf deine Prompts, generiert Texte und übersetzt Texte, z. B. ChatGPT, Perplexity
                    - Sprache verstehen/antworten: KI empfängt und versteht deine  Sprache und antwortet, z. B. Alexa und Siri
                    - Muster/Merkmale erkennen: KI analysiert Muster und unterstützt bei Diagnosen oder Vorhersagen, z. B. bei Krankheiten oder zur Gefahrenabwehr
                      usw...
               """)
#Speichern aller Antworten der Teilnehmer für die Seite
if "grundwissen_ki" not in st.session_state:
    st.session_state.grundwissen_ki = {}


#Speichern der Anzahl der Prompts
if "anzahleingaben_grundwissen" not in st.session_state:
    st.session_state.anzahleingaben_grundwissen = 0

#Einsatz von Container, damit der Fokus bleibt und nicht nach unten auf die Seite gesprungen wird
containerfokus = st.container()
with containerfokus:
    with st.expander("Fragen an die KI", expanded=True):
        #Nutzung von Form in Kombination mit Textinput weil Textinput Probleme hat. 
        #"Press Enter" funktioniert nicht bei st.text_input, obwohl es angezeigt wird.
        with st.form("frage_formular", clear_on_submit=True):
            frage = st.text_input("Falls du noch mehr Wissen möchtest, frag die KI!", 
                                placeholder="Du kannst mehrere Fragen stellen")
            #Button zur besseren Nutzung
            senden = st.form_submit_button("Fragen")
            #Anweisung an den Teilnehmer, da es bei Streamlit Probleme mit dem Fokus gibt
            st.markdown("Wenn du keine Fragen mehr hast, scrolle bitte weiter nach unten")
            # Antwort generierung erst wenn Button geklickt und Eingabe vorhanden
            try:
                #Sobald eine Frage im Feld ist, soll diese an die Schnittstelle übermittelt werden.
                if senden and frage:
                    #Nutzung eines Spinners, damit die User sehen, dass ein Hintergrundprozess durchgeführt wird
                    with st.spinner(text="Erstelle Text, bitte warten..."):
                        
                        #API-Aufruf an OpenAI
                        antwort = client.chat.completions.create(
                            #GPT 3.5 Turbo Nutzung, da es KI-Grenzen aufzeigt (Rechenfehler bei höheren Zahlen, veraltete Daten)
                            #Ansonsten Empfehlung Nutung von gpt-4omini
                            model="gpt-3.5-turbo",
                            #Übergabe der "Frage" aus dem Form
                            messages=[{"role": "user", "content": frage}]
                        )
                        #Abfrage, ob eine Ermittlung erfolgt ist
                        if antwort and antwort.choices:
                            antwort_text = antwort.choices[0].message.content
                        else:
                            antwort_text = "Keine Antwort erhalten."
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
                        if "ki_interaktion_historie" not in st.session_state.grundwissen_ki:
                            st.session_state.grundwissen_ki["ki_interaktion_historie"]=[]
                        st.session_state.grundwissen_ki["ki_interaktion_historie"].append({
                            "Bereich": "Grundwissen KI",
                            "Typ": "Grundwissen-KI-Interaktion",
                            "Frage": frage,
                            "Antwort": antwort_text,
                            "Anzahl Prompts": anzahleingaben
                        })
                        st.session_state.grundwissen_ki["aktuelle_ki_antwort"]={
                                "Bereich": "Grundwissen KI",
                                "Typ": "Grundwissen-KI-Interaktion",
                                "Frage": frage,
                                "Antwort": antwort_text,
                                "Anzahl Prompts": anzahleingaben
                        }
                st.session_state.grundwissen_ki
#Abfangen von Problemen
            except Exception as error:
                    hilfsdatei.openai_fehlerbehandlung(error)
                
            st.write("")
#Überprüfungsfrage: Sicherstellung, dass die Textbausteine gelesen wurden
st.divider()

st.write ("Nachdem du jetzt ein paar Informationen über KI erhalten hast, beantworte bitte die folgende Frage:")


#Frage: Verständlichkeit der dargestellten Inhalte

frage_verstaendlichkeitki= "Wie verständlich waren die Erklärungen über KI?"
verstaendlichkeitki = st.radio(
    frage_verstaendlichkeitki,
    [
        "Sehr verständlich",
        "Gut verständlich", 
        "Teilweise verständlich",
        "Schwer verständlich",
        "Nicht verständlich",
        "Keine Angabe"
    ],
    index=None
)
# Speichern der Antwort
if verstaendlichkeitki is not None:
    st.session_state.grundwissen_ki["verstaendlichkeitki"] = {
        "Bereich": "Grundwissen KI",
        "Typ": "Verstaendlichkeit",
        "Frage": frage_verstaendlichkeitki,
        "Antwort": verstaendlichkeitki
    }


#Frage: Über neue Informationen über das Thema KI

frage_neueInformationenKI = "Wie viel Neues hast du über KI gelernt?"
neueInformationenKI  = st.radio(
    frage_neueInformationenKI ,
    [
        "Sehr viel Neues über KI gelernt",
        "Einiges über KI dazugelernt", 
        "Wenig Neues über KI gelernt",
        "Keine neuen Informationen über KI gelernt",
        "Keine Angabe"
    ],
    index=None
)

# Speichern der Antwort
if neueInformationenKI is not None:
    st.session_state.grundwissen_ki["neueInformationenKI"] = {
        "Bereich": "Grundwissen KI",
        "Typ": "NeueInformationen",
        "Frage": frage_neueInformationenKI ,
        "Antwort": neueInformationenKI 
    }

# Zählen, wie oft der Teilnehmer gebraucht hat, um die Überprüfungsfrage "richtig" zu beantworten

if "anzahl_ueberpruefungsfrage" not in st.session_state:
    st.session_state.anzahl_ueberpruefungsfrage = 0


frageueberpruefung="Welche Aussage über KI trifft zu?"
ueberpruefungsfrage=st.radio(frageueberpruefung,
                            ("KI braucht Schritt für Schritt-Anweisungen",
                             "KI kann jede Aufgabe lösen und macht keine Fehler",
                             "KI braucht sehr viele Daten um zu lernen und macht trotzdem Fehler",
                             "Keine der dargestellten Aussagen ist richtig"),
                             index=None
)


if ueberpruefungsfrage is not None:
    #Zählen der Änderungen bei der Überprüfungsfrage
    st.session_state.anzahl_ueberpruefungsfrage +=1

    #Alle Antworten der Teilnehmer speichern, die sie ausgewählt haben
    if "ueberpruefung_historie" not in st.session_state.grundwissen_ki:
        st.session_state.grundwissen_ki["ueberpruefung_historie"]=[]
    
    st.session_state.grundwissen_ki["ueberpruefung_historie"].append({
    "Bereich": "Grundwissen KI",
    "Typ": "Ueberpruefungsfrage_Versuch",
    "Versuch_Nr": st.session_state.anzahl_ueberpruefungsfrage,
    "Frage": frageueberpruefung,
    "Antwort": ueberpruefungsfrage
    })
    
    # Speichern der aktuellen Antworten
    st.session_state.grundwissen_ki["ueberpruefungsfrage"]={
    "Bereich": "Grundwissen KI",
    "Typ": "Ueberpruefungsfrage",
    "Frage":   frageueberpruefung,
    "Antwort": ueberpruefungsfrage,
    "Anzahl_Aenderungen": st.session_state.anzahl_ueberpruefungsfrage
    }
    st.write(f"Deine Antwort: {ueberpruefungsfrage}.")


#Richtige Antwort für die Überprüfungsfrage 
richtigeAntwort="KI braucht sehr viele Daten um zu lernen und macht trotzdem Fehler"


#Trennungslinie
st.divider()
st.markdown("Um fortzufahren, klicke auf \"Weiter\"")
st.markdown("Aktueller Fortschritt in der gesamten Lerneinheit: 2 von 7")
st.progress (2/7)

#Überprüfung, ob alle Antworten vom Teilnehmer vorhanden sind, danach erfolgt die Möglichkeit auf die nächste Seite zu gelangen
if st.button("Weiter"):
    unbeantwortet = False
    
    if verstaendlichkeitki is None:
        st.error("Bitte bewerte die Verständlichkeit der Informationen.")
        unbeantwortet = True
    if neueInformationenKI is None:
        st.error("Bitte beantworte, ob du neue Informationen erhalten hast.")
        unbeantwortet = True
    if ueberpruefungsfrage is None:
        st.error("Bitte beantworte die Überprüfungsfrage.")
        unbeantwortet = True 
    elif ueberpruefungsfrage != richtigeAntwort:
        st.error("Deine Antwort ist leider falsch. Bitte lies den Inhalt nochmal und versuche es erneut.")
        unbeantwortet = True

    # Weiterleitung auf die nächste Seite nur bei richtiger Beantwortung der Frage und Ausfüllen aller Fragen
    if not unbeantwortet and ueberpruefungsfrage==richtigeAntwort:    
        st.info("Deine Antwort ist richtig!")
        st.switch_page("pages/4_Übung 1.py")
