"""
Übung 1: Interaktion mit der KI-Schnittstelle
Aufbau der Seite mit den Übungen
1. KI-generierter Text
2. Vokalzählung
3. Vorgebene Fragen von der KI beantworten lassen
4. Eigene Fragen an die KI stellen, der Prompt ist manipuliert

Weitere Datenerfassung durch Fragen
"""

import streamlit as st
import openai
import hilfsdatei

#Verbindung zu OpenAI
try: 
    client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])
#Fehlermeldung bei fehlendem oder falschem  API-Schlüssel
except KeyError:
    st.error("Kein API Key für OpenAI vorhanden. Abfragen über OpenAI nicht möglich")
    
#Seitentitel
hilfsdatei.seite("1. Übung")
#Sicherstellen, dass ein Zugriff der Seiten nur mit Passwort erfolgt, und dass User keine Navigationsseite sehen
hilfsdatei.teilnehmer_anmelden()

#Überschrift auf der Seite
ueberschrift_seite ="1. Übung"
st.markdown(f"<h5>{ueberschrift_seite}</h5>",unsafe_allow_html=True)
#Einleitung der ersten Übung
einleitung_text =(
    """
            Beginne mit der ersten Übung :)

            Auf der vorherigen Seite hast du gelernt, was KI ist und was sie kann. 
            Zudem hast du den ersten Kontakt mit einer KI-Anwendung mit der Eingabe deiner Frage gehabt.
            Die KI-Anwendung war ein texgenerierendes System mit Methoden des Deep Learnings,
            das auf große Sprachmodelle Large Language Models (LLM) trainiert ist.  Diese KI-Anwendung ist ChatGPT.
            """)
st.markdown(einleitung_text)



st.markdown("Jetzt kannst du sehen, was ChatGPT kann und ob die Anwendung ihre Daten analysiert hat.")
st.markdown("""
                Du stellst ChatGPT einige Aufgaben und schaust dir Antworten an.
               
            """)
#Trennungslinie
st.divider()
#Lernziele bzw. Aufgaben auf der Seite
st.markdown("""
                    Dafür soll ChatGPT dich unterstützen und für dich ein paar Aufgaben erledigen, d. h.:
                    - einen kurzen Text schreiben
                    - die Vokale zählen
                    - eine aktuelle Frage beantworten
                    - eine Matheaufgabe lösen
               """)


st.markdown("")
#Trennungslinie
st.divider()

#Speichern aller Antworten der Teilnehmer für die Seite

if "uebung1" not in st.session_state:
    st.session_state.uebung1 ={}
#Speichern der vorgegebenen Fragen & Antworten 
if "zaehler_eingaben_vorgegeben" not in st.session_state:
    st.session_state.zaehler_eingaben_vorgegeben = 0
#Speichern eigener Fragen & Antworten (Prompt ist angepasst, sodass er immer falsche Antworten liefern soll)
if "zaehler_eingaben_eigene" not in st.session_state:
    st.session_state.zaehler_eingaben_eigene = 0

#######################################
#AUFGABE 1 - Vorgegebener Satz von ChatGPT
####################################


st.markdown("<h5>Aufgabe 1</h5>",unsafe_allow_html=True)
#Prompt in ChatGPT eingegeben wurde

st.markdown("""
            ***Prompt für ChatGPT:***
            "Schreibe mir einen oder zwei Sätze über einen Sommertag mit Erdbeereis."
        """)

#Antwort von ChatGPT auf den Prompt "Schreibe mir einen oder zwei Sätze über einen Sommertag mit Erdbeereis"
st.markdown("""
                ***ChatGPT Antwort:***
                "Die Sonne brannte vom wolkenlosen Himmel, während das süße Erdbeereis langsam in meiner Hand schmolz.
                Jeder Löffel war
                ein kleiner, kühler Moment des Glücks an diesem warmen Sommertag."
            """)
#Speichern der Antwort von ChatGPT
textdeutsch="Die Sonne brannte vom wolkenlosen Himmel, während das süße Erdbeereis langsam in meiner Hand schmolz. Jeder Löffel war ein kleiner, kühler Moment des Glücks an diesem warmen Sommertag"

#Frage ob die Teilnehmer den Satz ebenfalls so schreiben würden
frage_text_echt = "Würdest du die 1-2 Sätze über einen Sommertag auch so schreiben?"
antwort_text_echt=st.radio(frage_text_echt,
                 ("Sehr wahrscheinlich",
                  "Eher wahrscheinlich",
                  "Neutral",
                  "Eher unwahrscheinlich",
                  "Sehr unwahrscheinlich"
                  ),
                  index=None           
            
            )
#Antwort speichern
if antwort_text_echt is not None:    
    st.session_state.uebung1["text_echt"]={
    "Bereich": "Übung1",
    "Typ":"Texteinschätzung",
    "Frage": frage_text_echt,
    "Antwort": antwort_text_echt
     }
    st.markdown(f"Deine Antwort: {antwort_text_echt}.")
    st.markdown("Die Sätze klingen gut und als würden sie von einem Menschen stammen, aber sie wurden von einer KI geschrieben")

#Trennungslinie
st.divider()

#######################
#AUFGABE 2: Vokale zählen
############################

st.markdown("<h5>Aufgabe 2</h5>",unsafe_allow_html=True)

#Vokale zählen Teil integrieren
#Aufgabenstellung für die Teilnehmer
st.markdown("""
            In der nächsten Übung nutzt du den Satz: ***"An einem schönen Sommertag genieße ich ein kühles Erdbeereis."***
            Diesmal sollst du den Satz etwas genauer untersuchen.
            Zähle die Anzahl von mindestens 2 Vokalen (a ,e ,i ,o ,u ,ä ,ö  und ü).
            """)
#Speichern des Beispielsatzes für das Vokale zählen
beispielsatz = "An einem schönen Sommertag genieße ich ein kühles Erdbeereis."
st.markdown(beispielsatz)

#Bei Benutzung des Buttons, werden die Vokale des Satzes gezählt
if st.button("Vokale selbst zählen"):
    #Alle Wörter werden klein geschrieben
    satzklein = beispielsatz.lower()
    #Vokale
    vokale ="aeiouäöü"
    ausgabe = ""
    gesamtvokale = 0
    
    #Durchlaufen der Vokale, wenn ein Vokal vorkommt wird dieser aufaddiert
    for vokal in vokale:
        anzahl = satzklein.count(vokal)
        if anzahl > 0:
            #Ausgabe z. B: a: 2
            ausgabe += f"{vokal}: {anzahl} "
            #Zählen der gesamten Vokale im Satz
            gesamtvokale += anzahl
    
    # Die gesamte Ausgabe in einer Zeile anzeigen
    ausgabe += f"Gesamt: {gesamtvokale}"
    st.write(f"Selbstgezählte Antwort: {ausgabe}")
    #Speichern der Vokale für den Satz
    st.session_state.uebung1["vokale_selbst"]={
        "Bereich":"Übung1",
        "Typ":"Vokale selbst zählen",
        "Frage": beispielsatz,
        "Antwort": ausgabe       
        
        }


#ChatGPT zählen lassen
if st.button("ChatGPT nach Vokalen fragen"):
    #Speichern der Vokale, die ChatGPT zählt
    if "anzahl_vokalabfrage_chatgpt" not in st.session_state:
        #Speichern, wie oft Teilnehmer das Ergebnis des Vokale zählens von ChatGPT ausführen
        st.session_state.anzahl_vokalabfrage_chatgpt = 0

    #Bei erneuten ausführen des Buttons, wird die Anzahl hochgezählt
    st.session_state.anzahl_vokalabfrage_chatgpt += 1
    anzahl_vokal_versuch=st.session_state.anzahl_vokalabfrage_chatgpt
    
    #Alle gezählten Versuche von ChatGPT speichern, für jedes Aussführen
    if "vokale_chatgpt_historie" not in st.session_state.uebung1:
        st.session_state.uebung1["vokale_chatgpt_historie"] = []
    prompt_vokale=("Zähle alle Vokale (a,e,i,o,u,ä,ö,ü) in dem Satz."+
                  "Liefer die Antwort genau in dem Format wie in dem Beispiel: 'a: 4 e: 6 i: 2 o: 3 u: 1 ä: 2 ö: 1 ü: 1 Gesamt: 20'"+
                  "In einer Zeile und ohne Kommentar."
                )
                  
    try:
        #Nutzung eines Spinners, damit die User sehen, dass ein Hintergrundprozess durchgeführt wird
        with st.spinner(text="Erstelle Text, bitte warten..."):
            #API-Aufruf an OpenAI
            antwort = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                      {"role": "user", "content": prompt_vokale+beispielsatz}
                     ]  )
       
        #Antwort in der Variable speichern
        antwort_text=antwort.choices[0].message.content

        #Falls ChatGPT 3.5 Turbo doch richtig Vokale zählt, soll trotzdem eine falsche Antwort ausgegeben werden
        if "Gesamt: 23" in antwort_text.lower() and "a: 2" in antwort_text.lower():
            antwort_text = "a: 4 e: 6 i: 2 o: 3 u: 1 ä: 2 ö: 1 ü: 1 Gesamt: 20"
            
    except Exception as error:
        # Fallback bei Verbindungsproblemen
        antwort_text = "a: 4 e: 6 i: 2 o: 3 u: 1 ä: 2 ö: 1 ü: 1 Gesamt: 20"

    #Antwort für die Teilnehmer anzeigen
    st.markdown(f"Antwort von ChatGPT: {antwort_text}")

    #Speichern aller Vokal-Zählungen von ChatGPT
    st.session_state.uebung1["vokale_chatgpt_historie"].append({
            "Bereich": "Übung1",
            "Typ": "Vokale zählen ChatGPT",
            "Frage" : beispielsatz,
            "Antwort": antwort_text,
            "Vokalabfrage_Anzahl": anzahl_vokal_versuch
        })
    #Speichern der letzten Vokal-Zählung
    st.session_state.uebung1["vokale_chatgpt"] = {
        "Bereich": "Übung1",
        "Typ": "Vokale zählen ChatGPT",
        "Frage": beispielsatz,
        "Antwort": antwort_text,
        "Vokalabfrage_Anzahl": anzahl_vokal_versuch
    }
    
    #Den Teilenhmern das Ergebnis der Übung 2 "Vokale zählen" anzeigen, da in Streamlit beim nächsten Widget, dass darüber schließt

    with st.expander("***VERGLEICH DER ERGEBNISSE:***",icon=":material/double_arrow:"):
        #Sicherstellen, dass der Vergleich die Übung durchgeführt wurde und anzeigen der letzten Ergebnisse
        if "vokale_chatgpt" in st.session_state.uebung1 and "vokale_selbst" in st.session_state.uebung1:
            st.markdown(f"""
                        ***Selbstgezählte Antwort:*** {st.session_state.uebung1["vokale_selbst"]["Antwort"]}\n
                        ***ChatGPT´s Antwort:*** {st.session_state.uebung1["vokale_chatgpt"]["Antwort"]}
                    """)
            #Hinweis, dass die KI Fehler machen kann
            st.markdown("""
                        Wie du siehst macht die KI-Anwendung auch Fehler. Sie kann gut Texte erzeugen, Fragen beantworten
                        aber nicht alles ist richtig! Sie kann sich auch vertun, deshalb ist es wichtig, dass Ergebnis immer zu prüfen!
                       """)
        #Fall der Vergleich nicht durchgeführt wird, dann den Teilnehmer darauf hinweisen
        else:
            st.info("Bitte klicke zuerst auf 'ChatGPT nach Vokalen fragen', um die Ergebnisse vergleichen zu können.")

        
#Trennungslinie
st.divider()

#############################
#AUFGABE 3 - Interaktion KI - vorgegebene Fragen stellen
###############################
st.markdown("<h5>Aufgabe 3</h5>",unsafe_allow_html=True)

#Prompt enthält mehrfach die Anweisung das die Antwort falsch sein soll,
#weil sonst bei der Frage: Was ist die Hauptstadt der Niederlande die Antwort Amsterdam wiedergibt.


#Expander im Container, da sonst nach Betätigung des Buttons der Fokus ans Ende der Seite springt
#Fokusverlust vorwiegend bei Interaktion mit KI, d.h. bei Eingabe von Prompts und Ausgabe der Antworten

container_fokus1 = st.container()
with container_fokus1:
    #Expander soll offen sein, damit die Teilnehmer die Aufgabe direkt sehen
    with st.expander("Vorgegebene Fragen", expanded=True):
        textzuaufgaben=st.markdown("""
                    Wähle eine der beiden folgenden Fragen aus und gib sie in das untenstehende Textfeld ein:
                    1. Wer ist der aktuelle Präsident der USA
                    2. Was das Ergebnis der Aufgabe 482 * 739 (Gerne kannst du den Taschenrechner benutzen und die Ergebnisse zu prüfen)
                """)
        #Clear_on_submit damit die Teilnehmer direkt dazu verleitet werden in das Textfeld neue Fragen zu stellen
        with st.form("frage_formular_vorgegeben", clear_on_submit=True):
            frage = st.text_input("Stelle eine der oben vorgegebenen Fragen")
            senden = st.form_submit_button("Fragen")
            #Hinweis an den Teilnehmer, damit er weiterscrollt.
            #Fokus sollte auf dieser Übung verbleiben, bis der Teilnehmer alle Fragen gestellt hat
            st.markdown("Wenn du fertig bist, dann scrolle bitte weiter nach unten")
            # Antwort generierung erst wenn Button geklickt und Eingabe vorhanden
            
            if senden and frage:
                try:
                        #Nutzung eines Spinners, damit die User sehen, dass ein Hintergrundprozess durchgeführt wird
                        with st.spinner(text="Erstelle Text, bitte warten..."):
                            #API-Aufruf an OpenAI
                            antwort = client.chat.completions.create(
                                #GPT 3.5 Turbo Nutzung, da es KI-Grenzen aufzeigt und keine Manipulation durch Anpassung des Prompts erfolgen muss(Rechenfehler bei höheren Zahlen, veraltete Daten)
                                #Ansonsten Empfehlung Nutung von gpt-4omini
                                model="gpt-4-turbo",
                                #Übergabe der "Frage" aus dem Form
                                messages=[{"role": "user", "content":"Beantworte die Frage nur auf Deutsch"+frage}]
                            )
                            if antwort and antwort.choices:
                                antwort_text = antwort.choices[0].message.content
                            else:
                                antwort_text = "Keine Antwort erhalten."
                            falscheantworten=("Antworte nur auf Deutsch. Gib bitte falsche Antworten für die Frage:")

                            #Sicherstellen, dass die Antworten falsch bleiben
                            if "präsident" in frage.lower() and "usa" in frage.lower():
                                if "trump" in antwort_text.lower():
                                    try:
                                        #API-Aufruf an OpenAI
                                        antwort = client.chat.completions.create(
                                            model="gpt-4-turbo",
                                            messages=[{"role": "user", "content":falscheantworten+frage}]
                                        )
                                        if antwort and antwort.choices:
                                            antwort_text = antwort.choices[0].message.content
                                        else:
                                            antwort_text = "Joe Biden ist der aktuelle Präsident der USA."
                                    #Hier soll die Aufgabe auch ohne Verbindung zu OpenAI funktionieren
                                    except Exception as error:
                                        antwort_text = "Joe Biden ist der aktuelle Präsident der USA."

                            elif "482" in frage and "739" in frage:  # Alle Rechenarten abfangen
                                if "356198" in antwort_text or "356.198" in antwort_text:
                                    try:
                                        #API-Aufruf an OpenAI
                                        antwort = client.chat.completions.create(
                                            model="gpt-4-turbo",
                                            messages=[{"role": "user", "content":falscheantworten+frage}]
                                        )
                                        if antwort and antwort.choices:
                                            antwort_text = antwort.choices[0].message.content
                                        else:
                                            antwort_text = "482 x 739 = 355.420"
                                    except Exception as error:
                                        antwort_text = "482 x 739 = 355.420"


                            # Zählen der Teilnehmereingaben bei den vorgegebenen Fragen
                            st.session_state.zaehler_eingaben_vorgegeben+= 1
                            anzahl_eingaben_vorgegeben = st.session_state.zaehler_eingaben_vorgegeben


                            #Vorgegebene Fragen anzeigen, die die Teilnehmer eingeben
                            st.markdown(f"Deine Frage: {frage}")
                            
                            
                            #ChatGPTs Antworten anzeigen
                            st.markdown(f"Antwort: {antwort_text}")
                            

                        #Speicherung der vorgegebenen Fragen + Antworten 
                        if "vorgegebene_fragen" not in st.session_state.uebung1:
                            st.session_state.uebung1["vorgegebene_fragen"] = []
                        
                        st.session_state.uebung1["vorgegebene_fragen"].append({
                                "Bereich": "Übung1",
                                "Typ": "Vorgegebene Frage - KI-Interaktion",
                                "Frage": frage,
                                "Antwort": antwort_text,
                                "Anzahl Prompts": anzahl_eingaben_vorgegeben
                            })

                #Fehlerbehandlung von OpenAI (z. B. zu viele Anfragen, keine Verbindung zu OpenAI-Schnittstelle)         
                except Exception as error:
                    hilfsdatei.openai_fehlerbehandlung(error)
#Aufgabe 4
#Teilnehmer stellen ChatGPT selbst fragen, der Prompt ist jedoch manipuliert
container_fokus2 = st.container()
with container_fokus2:
    textzuaufgaben=st.markdown("""
                                    Jetzt bist du dran!
                                    Stelle ChatGPT eine Frage, die dich interessiert
            
                        	        """)

    with st.expander("Eigene Fragen", expanded=True):
        with st.form("frage_formular_eigene", clear_on_submit=True):
            frage_eigene = st.text_input("Stelle hier deine eigenen Fragen")

            falsch = "Antworte richtig, aber füge ein direkt kleines falsches Detail hinzu."
            prompt = (f"{frage_eigene}")
            senden = st.form_submit_button("Fragen")

            st.markdown("Wenn du fertig bist, dann scrolle bitte weiter nach unten")
            # Antwort generierung erst wenn Button geklickt und Eingabe vorhanden
            if senden and frage_eigene:
                try:

                    with st.spinner(text="Erstelle Text, bitte warten..."):
                        antwort = client.chat.completions.create(
                            model="gpt-4-turbo",
                            messages=[{"role": "user", "content":prompt+"nur 2-3 Sätze. Gebe Details an wie Jahre, Zahlen oder Eigenschaften"}],
                            
                        )
                        #antwort_text_eigene= antwort.choices[0].message.content
                        richtige_antwort= antwort.choices[0].message.content
                        falsche_antwort=("Nimm diese Antwort und ändere nur eine Kleinigkeit leicht ab, das 2 Prozent falsch sind, "+
                                         "die Antworten sollen plausibel sein und richtig klingen. "+
                                         "Die grundlegenden Informationen, die jeder kennt sollen richtig sein " +
                                         "Es sollen detaillierte Antworten sein mit Zahlen, dann bitte Zahlen, Eigenschaften oder "+
                                         "Details falsch sind")
                        #falsche_antwort =( "Passe die Antwort an, damit sie: glaubwürdige Fehler enthält, z. B. falsches Datum, "+
                                        #    "eine ungeaue Zahl, eine leicht abweichende Eigenschaft oder ein falsches Detail. "+
                                        #    "Die Fehler dürfen nicht sofort auffallen. "+
                                        #    "Vermeide absurde oder offensichtlich falsche Aussagen. "+
                                        #    "Die Antwort sollen glaubwürdig wirken." 
                                           
                        #)
#                         falscher_prompt = (f"Hier ist eine sachlich korrekte Antwort:\n\n{richtige_antwort}\n\n"
#                                             "Ändere diese Antwort so, dass sie auf den ersten Blick korrekt klingt, "
#                                             "aber einen kleinen sachlichen Fehler enthält – z. B. ein leicht falsches Datum, "
#                                             "eine ungenaue Zahl oder ein Detail, das nicht sofort auffällt. "
#                                             "Die Antwort soll weiterhin professionell und glaubwürdig klingen."
# )
                        antwort = client.chat.completions.create(
                        model="gpt-4-turbo",
                        messages=[{"role": "user", "content": f"{falsche_antwort}:{richtige_antwort}"}]
        
                        )
                        antwort_text_eigene = antwort.choices[0].message.content
                        antwort_text_eigene= antwort.choices[0].message.content

                    # Prompt-Zähler aktualisieren
                    st.session_state.zaehler_eingaben_eigene += 1
                    anzahl_eingaben_eigene = st.session_state.zaehler_eingaben_eigene
                    


                    # Frage anzeigen
                    st.markdown(f"Deine Frage: {frage_eigene}")
                
                    
                    # Antwort anzeigen
                    st.markdown(f"Antwort: {antwort_text_eigene}")
                    



                    # Erzeugen einer Speicherliste, sofern keine Vorhanden ist
                    if "eigene_fragen" not in st.session_state.uebung1:
                        st.session_state.uebung1["eigene_fragen"] = []
                    
                    # Eigene Fragen & KI-Antworten speichern
                    st.session_state.uebung1["eigene_fragen"].append({
                        "Bereich": "Übung1",
                        "Typ": "Eigene Frage - KI-Interaktion",
                        "Frage": frage_eigene,
                        "Antwort": antwort_text_eigene,
                        "Anzahl Prompts": anzahl_eingaben_eigene
                    })
                #Fehlerbehandlung von OpenAI
                except Exception as error:
                    hilfsdatei.openai_fehlerbehandlung(error)
                

#Trennungslinie
st.divider()
#Frage ob die gestellten Antworten richtig sind
frage_vertrauen="Glaubst du, dass diese Antworten richtig sind?"
antwort_vertrauen = st.radio(frage_vertrauen,
        ( "Sehr wahrscheinlich",
          "Eher wahrscheinlich",
          "Mittelmäßig wahrscheinlich",
          "Eher unwahrscheinlich", 
          "Sehr unwahrscheinlich"
         
        ),
        index=None,
    )
#Speichern der Antworten
if antwort_vertrauen:
    st.write(f"Deine Antwort ist: {antwort_vertrauen}")
    st.session_state.uebung1["antwort_vertrauen"] = {
    "Bereich": "Übung1",
    "Typ" : "VertrauenKIAntworten",
    "Frage":   frage_vertrauen,
    "Antwort": antwort_vertrauen
     }

frage_unbefriedigend = "Wie zufrieden warst du mit ChatGPTs Antworten?"
antwort_unbefriedigend = st.radio(frage_unbefriedigend,
                         (  "Sehr zufrieden",
                            "Eher zufrieden",
                            "Neutral",
                            "Eher unzufrieden", 
                            "Sehr unzufrieden"
                         ), index=None, key="unbefriedigend"
                        )



if antwort_unbefriedigend is not None:
    st.session_state.uebung1["unbefriedigend"] = {
        "Bereich": "Übung1",
        "Typ": "ChatGPT Antworten unbefriedigend",
        "Frage": frage_unbefriedigend,
        "Antwort": antwort_unbefriedigend
    }
    st.markdown(f"Deine Antwort: {antwort_unbefriedigend}")


####################
#ENDE DER ÜBUNG
###################

#Trennungslinie
st.divider()
#Anweisung für den Teilnehmer, sobald er mit der Übung fertig ist
st.markdown("Um fortzufahren, klicke auf \"Weiter\"")
#Anzeigen wie weit der Teilnehmer in der gesamten Lerneinheit ist
st.markdown("Aktueller Fortschritt in der gesamten Lerneinheit: 3 von 8")
st.progress (3/8)

if st.button("Weiter"):
    unbeantwortet = False
    if antwort_text_echt is None:
        st.error ("Bitte beantworte die Frage, ob der Text echt ist.")
        unbeantwortet = True
    if antwort_vertrauen is None:
        st.error ("Bitte gebe an, ob du den Antworten der KI vertraust.")
        unbeantwortet = True
    if antwort_unbefriedigend is None:
        st.error ("Bitte gebe an, ob die Antworten von ChatGPT in Ordnung waren.")
        unbeantwortet = True 
    if not unbeantwortet:
        naechste_seite="pages/5_Übung 2.py"
        st.switch_page(naechste_seite)
