import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(
    page_title="1. Übung"
)
st.markdown("<h4>1. Übung</h4>",unsafe_allow_html=True)

st.markdown("""
            Beginne mit der ersten Übung :)

            Auf der vorherigen Seite hast du gelernt, was KI ist und was sie kann. 
            Zudem hast du den ersten Kontakt mit einer KI-Anwendung mit der Eingabe deiner Frage gehabt.
            Die KI-Anwendung war ein texgenerierendes System mit Methoden des Deep Learnings,
            das auf große Sprachmodelle Large Language Models (LLM) trainiert ist.  Diese KI-Anwendung ist ChatGPT.
            """)



st.markdown("Jetzt kannst du, was ChatGPT kann und ob die Anwendung ihre Daten analysiert hat.")
st.markdown("""
                Du stellst ChatGPT einige Aufgaben und schaust dir Antworten an.
               
            """)
st.divider()
st.markdown("""
                    Dafür soll ChatGPT dich unterstützen und für dich ein paar Aufgaben erledigen, d. h.:
                    - einen kurzen Text schreiben
                    - die Vokale zählen
                    - eine aktuelle Frage beantworten
                    - eine Matheaufgabe lösen
               """)


st.markdown("")

if "uebung1" not in st.session_state:
    st.session_state.uebung1 ={}
if "anzahleingaben_uebung1_vorgegeben" not in st.session_state:
    st.session_state.anzahleingaben_uebung1_vorgegeben = 0
if "anzahleingaben_uebung1_eigene" not in st.session_state:
    st.session_state.anzahleingaben_uebung1_eigene = 0

st.markdown("""
            ***Prompt für ChatGPT:***
            "Schreibe mir einen oder zwei Sätze über einen Sommertag mit Erdbeereis."
        """)

st.markdown("""
                ***ChatGPT Antwort:***
                "Die Sonne brannte vom wolkenlosen Himmel, während das süße Erdbeereis langsam in meiner Hand schmolz.
                Jeder Löffel war
                ein kleiner, kühler Moment des Glücks an diesem warmen Sommertag."
            """)
textdeutsch="Die Sonne brannte vom wolkenlosen Himmel, während das süße Erdbeereis langsam in meiner Hand schmolz. Jeder Löffel war ein kleiner, kühler Moment des Glücks an diesem warmen Sommertag"
fragetextecht = "Würdest du die 1-2 Sätze über einen Sommertag auch so schreiben?"
textecht=st.radio(fragetextecht,
                 ("Ja, sehr wahrscheinlich",
                  "Ja, eher wahrscheinlich",
                 "Nein, eher unwahrscheinlich",
                 "Nein, sehr unwahrscheinlich",
                 "Keine Angabe"
                  ),
                  index=None           
            
            )
if textecht:
    
    st.session_state.uebung1["texteinschaetzung"]={
    "Bereich": "Übung1",
    "Typ":"Texteinschätzung",
    "Frage":   fragetextecht,
    "Antwort": textecht
     }
    st.markdown("Die Sätze klingen gut und menschlich– aber sie wurden von einer KI geschrieben")
    



st.divider()

# Vokale zählen Teil integrieren
st.markdown("""
            In der nächsten Übung nutzt du den Satz: ***"An einem schönen Sommertag genieße ich ein kühles Erdbeereis."***
            Diesmal sollst du den Satz etwas genauer untersuchen.
            Zähle die Anzahl von mindestens 2 Vokalen (a ,e ,i ,o ,u ,ä ,ö  und ü).
            """)

beispielsatz = "An einem schönen Sommertag genieße ich ein kühles Erdbeereis."
st.markdown(beispielsatz)

if st.button("Vokale selbst zählen"):
    satzklein = beispielsatz.lower()
    vokale ="aeiouäöü"
    ausgabe = ""
    gesamtvokale = 0
        
    for vokal in vokale:
        anzahl = satzklein.count(vokal)
        if anzahl > 0:
            ausgabe += f"{vokal}: {anzahl} "
            gesamtvokale += anzahl
    
    # Die gesamte Ausgabe in einer Zeile anzeigen
    ausgabe += f"Gesamt: {gesamtvokale}"
    st.write(f"Selbstgezählte Antwort: {ausgabe}")
    st.session_state.uebung1["vokale_selbst"]={
        "Bereich":"Übung1",
        "Typ":"Vokale selbst zählen",
        "Frage": beispielsatz,
        "Antwort": ausgabe       
        
        }



if st.button("ChatGPT nach Vokalen fragen"):
    if "anzahl_uebung1_vokalabfrage_chatgpt" not in st.session_state:
        st.session_state.anzahl_uebung1_vokalabfrage_chatgpt = 0

 
    st.session_state.anzahl_uebung1_vokalabfrage_chatgpt += 1
    anzahlergebnisseanzeigen=st.session_state.anzahl_uebung1_vokalabfrage_chatgpt
    

    
    if "vokale_chatgpt_antworten" not in st.session_state.uebung1:
        st.session_state.uebung1["vokale_chatgpt_antworten"] = []

    # Lösung generieren
    with st.spinner(text="Erstelle Text, bitte warten..."):
        antwort = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
 #                 {"role": "system", "content": "Zähle die Vokale für den Satz und gebe sie so aus, dass ich sie gut lesen kann."},
                  {"role": "user", "content": f"Vokale zählen {beispielsatz}. In dem Format Buchstabe Kleinbuchstabe : zahl dann nächster Vokal am Ende die Gesamzahl der Vokale. Alles in einer Zeile. Ohne einen Kommentar danach"}
                 ]  )
   
    # Antwort zeigen
    antwort_text=antwort.choices[0].message.content
    st.write(f"Antwort von ChatGPT: {antwort_text}")

    st.session_state.uebung1["vokale_chatgpt_antworten"].append({
            "Bereich": "Übung1",
            "Typ": "Vokale zählen ChatGPT",
            "Frage" : beispielsatz,
            "Antwort": antwort_text,
            "Vokalabfrage_Anzahl": anzahlergebnisseanzeigen
        })
    st.session_state.uebung1["vokale_chatgpt"] = {
        "Bereich": "Übung1",
        "Typ": "Vokale zählen ChatGPT",
        "Frage": beispielsatz,
        "Antwort": antwort_text,
        "Vokalabfrage_Anzahl": anzahlergebnisseanzeigen
    }
    
   
    with st.expander("***VERGLEICH DER ERGEBNISSE:***",icon=":material/double_arrow:"):
        if "vokale_chatgpt" in st.session_state.uebung1 and "vokale_selbst" in st.session_state.uebung1:
            st.markdown(f"""
                        ***Selbstgezählte Antwort:*** {st.session_state.uebung1["vokale_selbst"]["Antwort"]}\n
                        ***ChatGPT´s Antwort:*** {st.session_state.uebung1["vokale_chatgpt"]["Antwort"]}
                    """)
            st.markdown("""
                        Wie du siehst macht die KI-Anwendung auch Fehler. Sie kann gut Texte erzeugen, Fragen beantworten
                        aber nicht alles ist richtig! Sie kann sich auch vertun, deshalb ist es wichtig, dass Ergebnis immer zu prüfen!
                        """)
        else:
            st.info("Bitte klicke zuerst auf 'ChatGPT nach Vokalen fragen', um die Ergebnisse vergleichen zu können.")

           


st.divider()

tab1 = st.tabs(["Vorgegebene Fragen"])[0]

#st.text_input hat Bugs
# Eingabe und Button
with tab1:
    textzuaufgaben=st.markdown("""
                Suche die eine der beiden hier angegebenen Fragen aus, die ChatGPT dir beantworten soll und gibt diese in das untenstehende leere
                Textfeld ein.
                1. Wer ist der aktuelle Präsident der USA ist
                2. Wie das Ergebnis der Aufgabe 482 * 739 (Gerne kannst du den Taschenrechner benutzen und die Ergebnisse zu prüfen)
            """)
    with st.form("frage_formular_vorgegeben", clear_on_submit=True):
        frage = st.text_input("Stelle eine der oben vorgegebenen Fragen")
        senden = st.form_submit_button("Fragen")

        st.markdown("Wenn du fertig bist, dann scrolle bitte weiter nach unten")
        # Antwort generierung erst wenn Button geklickt und Eingabe vorhanden
        
        if senden and frage:
            try:
                    with st.spinner(text="Erstelle Text, bitte warten..."):
                        antwort = client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[{"role": "user", "content": frage}]
                        )
                        antwort_text = antwort.choices[0].message.content

                    # Prompt-Zähler aktualisieren
                    st.session_state.anzahleingaben_uebung1_vorgegeben+= 1
                    anzahleingaben_vorgegeben = st.session_state.anzahleingaben_uebung1_vorgegeben



                    # Frage anzeigen
                    st.write("Deine Frage:")
                    st.write(frage)
                    
                    # Antwort anzeigen
                    st.write("Antwort:")
                    st.write(antwort_text)



                    # Frage + Antwort speichern
                    if "vorgegebene_fragen" not in st.session_state.uebung1:
                        st.session_state.uebung1["vorgegebene_fragen"] = []
                    
                    st.session_state.uebung1["vorgegebene_fragen"].append({
                            "Bereich": "Übung1",
                            "Typ": "Vorgegebene Frage - KI-Interaktion",
                            "Frage": frage,
                            "Antwort": antwort_text,
                            "Anzahl Prompts": anzahleingaben_vorgegeben
                        })
            except openai.APIStatusError:
                st.error("OpenAI verarbeitet die Anfrage nicht, bitte versuche es erneut.")
            except openai.APIConnectionError:
                st.error("Verbindungsproblem mit OpenAI. Bitte versuche es später noch einmal.")
            except openai.RateLimitError:
                st.error("Zu viele Anfragen. Bitte warte einen Moment und versuche es dann erneut.")
            except Exception as e:
                st.error(f"Ein Fehler ist aufgetreten: {e}")
                        

                # Eingabe und Button
                textzuaufgaben=st.markdown("""
                                Jetzt bist du dran!
                                Stelle ChatGPT eine Frage, die dich interessiert
        
                """)
    tab2 = st.tabs(["Eigene Fragen"])[0]
    with tab2:
        with st.form("frage_formular_eigene", clear_on_submit=True):
            frage_eigene = st.text_input("Stelle hier deine eigenen Fragen")
            senden = st.form_submit_button("Fragen")

            st.markdown("Wenn du fertig bist, dann scrolle bitte weiter nach unten")
            # Antwort generierung erst wenn Button geklickt und Eingabe vorhanden
            if senden and frage_eigene:
                try:

                    with st.spinner(text="Erstelle Text, bitte warten..."):
                        antwort = client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[{"role": "user", "content": frage_eigene}]
                        )
                        antwort_text_eigene= antwort.choices[0].message.content

                    # Prompt-Zähler aktualisieren
                    st.session_state.anzahleingaben_uebung1_eigene += 1
                    anzahleingaben_eigene = st.session_state.anzahleingaben_uebung1_eigene
                    


                    # Frage anzeigen
                    st.write("Deine Frage:")
                    st.write(frage_eigene)
                    
                    # Antwort anzeigen
                    st.write("Antwort:")
                    st.write(antwort_text_eigene)



                    # Frage + Antwort speichern
                    if "eigene_fragen" not in st.session_state.uebung1:
                        st.session_state.uebung1["eigene_fragen"] = []
                    
                    st.session_state.uebung1["eigene_fragen"].append({
                        "Bereich": "Übung1",
                        "Typ": "Eigene Frage - KI-Interaktion",
                        "Frage": frage_eigene,
                        "Antwort": antwort_text_eigene,
                        "Anzahl Prompts": anzahleingaben_eigene
                    })
                except openai.APIStatusError:
                    st.error("OpenAI verarbeitet die Anfrage nicht, bitte versuche es erneut.")
                except openai.APIConnectionError:
                    st.error("Verbindungsproblem mit OpenAI. Bitte versuche es später noch einmal.")
                except openai.RateLimitError:
                    st.error("Zu viele Anfragen. Bitte warte einen Moment und versuche es dann erneut.")
                except Exception as e:
                    st.error(f"Ein Fehler ist aufgetreten: {e}")

st.write("")





fragevertrauen="Glaubst du, dass diese Antworten richtig ist?"
antwortvertrauen = st.radio(fragevertrauen,
        ("Ja, die Antworten waren richtig",
         "Ja, die Antworten sind wahrscheinlich richtig",
         "Ich bin unsicher",
         "Nein, die Antworten sind wahrscheinlich falsch",
         "Nein, die Antworten sind falsch",
         "Keine Angabe"
        ),
        index=None,
    )

if antwortvertrauen:
    st.write(f"Deine Antwort ist: {antwortvertrauen}")
    st.session_state.uebung1["antwortvertrauen"] = {
    "Bereich": "Übung1",
    "Typ" : "VertrauenKIAntworten",
    "Frage":   fragevertrauen,
    "Antwort": antwortvertrauen
     }


st.divider()

st.markdown("Um fortzufahren, klicke auf \"weiter\" ")
col1, col2 = st.columns([8,2])
with col2:
    if st.button("weiter"):
        # Prüft, ob eine der beiden Fragen NICHT beantwortet wurde
        unbeantwortet = (textecht is None or antwortvertrauen is None)
        if unbeantwortet:
            st.error("Bitte beantworte alle Fragen, um fortzufahren.")
        else:
            st.switch_page("pages/5_Übung 2.py")
