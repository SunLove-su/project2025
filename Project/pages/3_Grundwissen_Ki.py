import streamlit as st
import openai
import hilfsdatei
import os


#Überschrift der Seite 
titel_seite = "Grundwissen über Künstliche Intelligenz (KI)" 
hilfsdatei.seite(titel_seite)

#Damit auf Render keine Fehlermeldung kommt, dass die st.secrets toml fehlt
api_key1 = os.getenv("OPENAI_API_KEY1")
api_key2 = os.getenv("OPENAI_API_KEY2")
gemini_key = os.getenv("GEMINI_API_KEY")

# st.secrets für das Deployment in StreamlitCloud
try:
    if not api_key1:
        api_key1=st.secrets["openai"]["api_key1"]
    if not api_key2:
        api_key2=st.secrets["openai"]["api_key2"]
    if not gemini_key:
        gemini_key = st.secrets["googleapigemini"]["gemini_api_key"]
except Exception:
        pass
st.write("🔍 DEBUG - Keys Status:")
st.write(f"api_key1 vorhanden: {bool(api_key1)}")
st.write(f"api_key2 vorhanden: {bool(api_key2)}")
st.write(f"gemini_key vorhanden: {bool(gemini_key)}")

# DEBUG: Secrets verfügbar?
try:
    st.write("**Secrets Check:**")
    st.write(f"st.secrets verfügbar: {hasattr(st, 'secrets')}")
    if hasattr(st, 'secrets'):
        st.write(f"secrets keys: {list(st.secrets.keys())}")
        st.write(f"'openai' section exists: {'openai' in st.secrets}")
        st.write(f"'googleapigemini' section exists: {'googleapigemini' in st.secrets}")
        
        if 'openai' in st.secrets:
            st.write(f"openai keys: {list(st.secrets['openai'].keys())}")
        if 'googleapigemini' in st.secrets:
            st.write(f"googleapigemini keys: {list(st.secrets['googleapigemini'].keys())}")
except Exception as e:
    st.write(f"Secrets error: {e}")

# Environment Variables Check
st.write("**Environment Variables:**")
st.write(f"OPENAI_API_KEY1 in env: {bool(os.getenv('OPENAI_API_KEY1'))}")
st.write(f"OPENAI_API_KEY2 in env: {bool(os.getenv('OPENAI_API_KEY2'))}")
st.write(f"GEMINI_API_KEY in env: {bool(os.getenv('GEMINI_API_KEY'))}")

# Prüfe ob mindestens ein Service verfügbar ist
if not api_key1 and not api_key2 and not gemini_key:
    st.error("Es gibt zur Zeit Probleme mit den API-Keys!")
    st.stop()

# Client nur erstellen wenn OpenAI Keys verfügbar
client = None
if api_key1:
    client = openai.OpenAI(api_key=api_key1)
elif api_key2:
    client = openai.OpenAI(api_key=api_key2)
# Wenn nur gemini_key verfügbar ist, bleibt client = None (das ist OK!)

#Sicherstellen, dass ein Zugriff der Seiten nur mit Passwort erfolgt, und dass User keine Navigationsseite sehen
hilfsdatei.teilnehmer_anmelden()

#Überschrift der Seite
ueberschrift_seite="Grundwissen über Künstliche Intelligenz (KI)"
st.markdown(f"<h4>{ueberschrift_seite}</h4>",unsafe_allow_html=True)
einleitung_text =(
            """
            Auf dieser Seite lernst du etwas über die Grundlagen der KI.
            Es sind neue oder schon für dich bekannte Informationen.
            """)
st.markdown(einleitung_text)
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
if "zaehler_eingaben_grundwissen" not in st.session_state:
    st.session_state.zaehler_eingaben_grundwissen = 0

#Einsatz von Container, damit der Fokus bleibt und nicht nach unten auf die Seite gesprungen wird
container_fokus = st.container()
with container_fokus:
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

            #Antwort generierung erst wenn Button geklickt und Eingabe vorhanden
            try:
                #Sobald eine Frage im Feld ist, soll diese an die Schnittstelle übermittelt werden.
                if senden and frage:
                    #Nutzung eines Spinners, damit die User sehen, dass ein Hintergrundprozess durchgeführt wird
                    with st.spinner(text="Erstelle Text, bitte warten..."):
                       
                        #API-Aufruf an OpenAI (wenn es zu einem RateLimit kommt, soll der 2.te API-Schlüssel zum Einsatz kommen)
                        antwort_text = None

                        try:
                            # Szenario 1: OpenAI Key 1 verwenden
                            if client:
                                antwort = client.chat.completions.create(
                                    model="gpt-3.5-turbo",
                                    messages=[{"role": "user", "content": f"Beantworte die Frage nur auf Deutsch: {frage}"}]
                                )
                                antwort_text = antwort.choices[0].message.content
                                
                            # Szenario 2: Kein Key 1, aber Key 2 verfügbar
                            elif api_key2:
                                client = openai.OpenAI(api_key=api_key2)
                                antwort = client.chat.completions.create(
                                    model="gpt-3.5-turbo",
                                    messages=[{"role": "user", "content": f"Beantworte die Frage nur auf Deutsch: {frage}"}]
                                )
                                antwort_text = antwort.choices[0].message.content
                                
                            # Szenario 3: Nur Gemini verfügbar
                            elif gemini_key:
                                gemini_client = openai.OpenAI(
                                    api_key=gemini_key,
                                    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
                                )
                                antwort = gemini_client.chat.completions.create(
                                    model="gemini-2.0-flash",
                                    messages=[{"role": "user", "content": f"Beantworte die Frage nur auf Deutsch: {frage}"}]
                                )
                                antwort_text = antwort.choices[0].message.content
                                
                            else:
                                antwort_text = "Keine API-Services verfügbar"

                        except openai.RateLimitError:
                            # Fallback: Key 1 RateLimit → Key 2
                            try:
                                if api_key2:
                                    client = openai.OpenAI(api_key=api_key2)
                                    antwort = client.chat.completions.create(
                                        model="gpt-3.5-turbo",
                                        messages=[{"role": "user", "content": f"Beantworte die Frage nur auf Deutsch: {frage}"}]
                                    )
                                    antwort_text = antwort.choices[0].message.content
                                else:
                                    raise Exception("Kein Key 2 für RateLimit Fallback")
                            except Exception:
                                # Key 2 auch nicht verfügbar → Gemini
                                if gemini_key:
                                    gemini_client = openai.OpenAI(
                                        api_key=gemini_key,
                                        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
                                    )
                                    antwort = gemini_client.chat.completions.create(
                                        model="gemini-2.0-flash",
                                        messages=[{"role": "user", "content": f"Beantworte die Frage nur auf Deutsch: {frage}"}]
                                    )
                                    antwort_text = antwort.choices[0].message.content
                                else:
                                    antwort_text = "Alle API-Services sind momentan nicht verfügbar"

                        except Exception:
                            # OpenAI komplett down → Gemini Fallback
                            try:
                                if gemini_key:
                                    gemini_client = openai.OpenAI(
                                        api_key=gemini_key,
                                        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
                                    )
                                    antwort = gemini_client.chat.completions.create(
                                        model="gemini-2.0-flash",
                                        messages=[{"role": "user", "content": f"Beantworte die Frage nur auf Deutsch: {frage}"}]
                                    )
                                    antwort_text = antwort.choices[0].message.content
                                else:
                                    antwort_text = "Alle API-Services sind momentan nicht verfügbar"
                            except Exception:
                                antwort_text = "Alle API-Services sind momentan nicht verfügbar"

                        # Prompt-Zähler aktualisieren
                        st.session_state.zaehler_eingaben_grundwissen += 1
                        anzahl_eingaben = st.session_state.zaehler_eingaben_grundwissen
                        # Frage anzeigen
                        st.markdown(f"Deine Frage: {frage}")
               
                        # Antwort anzeigen
                        st.markdown(f"Antwort: {antwort_text}")
                     
                        # Frage und  Antwort speichern
                        if "ki_interaktion_historie" not in st.session_state.grundwissen_ki:
                            st.session_state.grundwissen_ki["ki_interaktion_historie"]=[]
                        ki_interaktion = {
                            "Bereich": "Grundwissen KI",
                            "Typ": "Grundwissen-KI-Interaktion",
                            "Frage": frage,
                            "Antwort": antwort_text,
                            "Anzahl Prompts": anzahl_eingaben
                        }
                        st.session_state.grundwissen_ki["ki_interaktion_historie"].append(ki_interaktion)
                        st.session_state.grundwissen_ki["ki_interaktion"]=ki_interaktion

            # #Abfangen von anderen Problemen
            except Exception as error:
                    hilfsdatei.openai_fehlerbehandlung(error)
   
#Überprüfungsfrage: Sicherstellung, dass die Textbausteine gelesen wurden
st.divider()

st.markdown ("Nachdem du jetzt ein paar Informationen über KI erhalten hast, beantworte bitte die folgende Frage:")

#########################################################################

#Frage: Verständlichkeit der dargestellten Inhalte

frage_verstaendlichkeit_ki= "Wie verständlich waren die Erklärungen über KI?"
antwort_verstaendlichkeit_ki = st.radio(
    frage_verstaendlichkeit_ki,
    (
        "Sehr verständlich",
        "Gut verständlich", 
        "Mittelmäßig verständlich",
        "Eher unverständlich",
        "Unverständlich"
    ),
    index=None
)
# Speichern der Antwort
if "anzahl_verstaendlichkeit_ki" not in st.session_state:
    st.session_state.anzahl_verstaendlichkeit_ki = 0
if "verstaendlichkeit_ki_alt" not in st.session_state:
    st.session_state.verstaendlichkeit_ki_alt = None 
if "verstaendlichkeit_ki_historie" not in st.session_state.grundwissen_ki:
    st.session_state.grundwissen_ki["verstaendlichkeit_ki_historie"] = []

# Speicherung nur bei Änderung der Antwort
if antwort_verstaendlichkeit_ki is not None and antwort_verstaendlichkeit_ki != st.session_state.verstaendlichkeit_ki_alt:
    st.session_state.anzahl_verstaendlichkeit_ki += 1
    
    verstaendlichkeit_ki = {
        "Bereich": "Grundwissen KI",
        "Typ": "Verstaendlichkeit",
        "Frage": frage_verstaendlichkeit_ki,
        "Antwort": antwort_verstaendlichkeit_ki,
        "Anzahl_Aenderungen": st.session_state.anzahl_verstaendlichkeit_ki
    }
    
    st.session_state.grundwissen_ki["verstaendlichkeit_ki_historie"].append(verstaendlichkeit_ki)
    st.session_state.grundwissen_ki["verstaendlichkeit_ki"] = verstaendlichkeit_ki
    # Aktuelle Antwort merken
    st.session_state.verstaendlichkeit_ki_alt = antwort_verstaendlichkeit_ki
    
    st.markdown(f"Deine Antwort: {antwort_verstaendlichkeit_ki}.")

###############################################################################

#Frage: Über neue Informationen über das Thema KI

frage_neue_informationen_ki = "Wie viel Neues hast du über KI gelernt?"
antwort_neue_informationen_ki  = st.radio(
    frage_neue_informationen_ki ,
    (
        "Sehr viel Neues über KI gelernt",
        "Einiges über KI dazugelernt", 
        "Wenig Neues über KI gelernt",
        "Keine neuen Informationen über KI gelernt",
        "Keine Angabe"
    ),
    index=None
)

# Speichern der Antwort
if "anzahl_neue_informationen_ki" not in st.session_state:
    st.session_state.anzahl_neue_informationen_ki = 0
if "neue_informationen_ki_alt" not in st.session_state: 
    st.session_state.neue_informationen_ki_alt = None  
if "neue_informationen_ki_historie" not in st.session_state.grundwissen_ki:
    st.session_state.grundwissen_ki["neue_informationen_ki_historie"] = []

# Speicherung nur bei Änderung der Antwort
if antwort_neue_informationen_ki is not None and antwort_neue_informationen_ki != st.session_state.neue_informationen_ki_alt:
    st.session_state.anzahl_neue_informationen_ki += 1
    
    neue_informationen_ki = {
        "Bereich": "Grundwissen KI",
        "Typ": "Neue Informationen",
        "Frage": frage_neue_informationen_ki,
        "Antwort": antwort_neue_informationen_ki,
        "Anzahl_Aenderungen": st.session_state.anzahl_neue_informationen_ki
    }
    
    st.session_state.grundwissen_ki["neue_informationen_ki_historie"].append(neue_informationen_ki)
    st.session_state.grundwissen_ki["neue_informationen_ki"] = neue_informationen_ki
    # Aktuelle Antwort merken
    st.session_state.neue_informationen_ki_alt = antwort_neue_informationen_ki
    
    st.markdown(f"Deine Antwort: {antwort_neue_informationen_ki}.")

##############################################################################################################

# Zählen, wie oft der Teilnehmer gebraucht hat, um die Überprüfungsfrage "richtig" zu beantworten

frage_ueberpruefung = "Welche Aussage über KI trifft zu?"
antwort_ueberpruefung=st.radio(frage_ueberpruefung,
                            (
                            "KI braucht Schritt für Schritt-Anweisungen",
                             "KI kann jede Aufgabe lösen und macht keine Fehler",
                             "KI braucht sehr viele Daten um zu lernen und macht trotzdem Fehler",
                             "Keine der dargestellten Aussagen ist richtig"
                             ),
                             index=None
)                          

# Speichern der Antwort
if "anzahl_ueberpruefung" not in st.session_state:
    st.session_state.anzahl_ueberpruefung = 0
if "ueberpruefung_alt" not in st.session_state:
    st.session_state.ueberpruefung_alt = None
if "ueberpruefung_historie" not in st.session_state.grundwissen_ki:
    st.session_state.grundwissen_ki["ueberpruefung_historie"] = []

# Speicherung nur bei Änderung der Antwort  
if antwort_ueberpruefung is not None and antwort_ueberpruefung != st.session_state.ueberpruefung_alt:
    st.session_state.anzahl_ueberpruefung += 1
    
    ueberpruefung = {
        "Bereich": "Grundwissen KI",
        "Typ": "Ueberpruefungsfrage",
        "Frage": frage_ueberpruefung,
        "Antwort": antwort_ueberpruefung,
        "Anzahl_Aenderungen": st.session_state.anzahl_ueberpruefung
    }
    
    st.session_state.grundwissen_ki["ueberpruefung_historie"].append(ueberpruefung)
    st.session_state.grundwissen_ki["ueberpruefung"] = ueberpruefung
    # Aktuelle Antwort merken 
    st.session_state.ueberpruefung_alt = antwort_ueberpruefung
    
    st.markdown(f"Deine Antwort: {antwort_ueberpruefung}.")

#Richtige Antwort für die Überprüfungsfrage 
richtige_antwort="KI braucht sehr viele Daten um zu lernen und macht trotzdem Fehler"

##############################################################################
#Trennungslinie

st.divider()

################################################################################

st.markdown("Um fortzufahren, klicke auf \"Weiter\"")
st.markdown("Aktueller Fortschritt in der gesamten Lerneinheit: 2 von 8")
st.progress (2/8)

#Überprüfung, ob alle Antworten vom Teilnehmer vorhanden sind, danach erfolgt die Möglichkeit auf die nächste Seite zu gelangen
if st.button("Weiter"):
    unbeantwortet = False
    
    if antwort_verstaendlichkeit_ki is None:
        st.error("Bitte bewerte die Verständlichkeit der Informationen.")
        unbeantwortet = True
    if antwort_neue_informationen_ki is None:
        st.error("Bitte beantworte, ob du neue Informationen erhalten hast.")
        unbeantwortet = True
    if antwort_ueberpruefung is None:
        st.error("Bitte beantworte die Überprüfungsfrage.")
        unbeantwortet = True 
    elif antwort_ueberpruefung != richtige_antwort:
        st.error("Deine Antwort ist leider falsch. Bitte lies den Inhalt nochmal und versuche es erneut.")
        unbeantwortet = True

    # Weiterleitung auf die nächste Seite nur bei richtiger Beantwortung der Frage und Ausfüllen aller Fragen
    if not unbeantwortet and antwort_ueberpruefung==richtige_antwort:    
        st.info("Deine Antwort ist richtig!")
        st.switch_page("pages/4_Übung 1.py")