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
if "fragen_uebung1" not in st.session_state:
    st.session_state.fragen_uebung1 = {}
if "antworten_uebung1" not in st.session_state:
    st.session_state.antworten_uebung1 = {}
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
textecht=st.radio("Würdest du die 1-2 Sätze über einen Sommertag auch so schreiben?",
                 ("Ja, sehr wahrscheinlich",
                  "Ja, eher wahrscheinlich",
                 "Nein, eher unwahrscheinlich",
                 "Nein, sehr unwahrscheinlich",
                 "Keine Angabe"
                  ),
                  index=None           
            
            )
if textecht:
    st.markdown("Die Sätze klingen gut und menschlich– aber sie wurden von einer KI geschrieben")
    st.session_state.fragen_uebung1["textdeutsch"]=textdeutsch
    st.session_state.antworten_uebung1["textecht"]=textecht
st.session_state.fragen_uebung1
st.session_state.antworten_uebung1

st.divider()
if "selbstgezaehlteantwort" not in st.session_state:
    st.session_state.selbstgezaehlteantwort = ""
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
    st.session_state.selbstgezaehlteantwort=ausgabe

# Speichern der generierten Ausgaben als Variable 
if "vokal_antwort_chatgpt" not in st.session_state:
    st.session_state.vokal_antwort_chatgpt = ""
antwort_text=""
if st.button("ChatGPT nach Vokalen fragen"):
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
    st.write(f"Antwort: {antwort_text}")
    st.session_state.vokal_antwort_chatgpt = antwort_text

    
   
    with st.expander("***VERGLEICH DER ERGEBNISSE:***",icon=":material/double_arrow:"):
        if st.session_state.vokal_antwort_chatgpt:
            st.markdown(f"""
                        ***Selbstgezählte Antwort:*** {st.session_state.selbstgezaehlteantwort}\n
                        ***ChatGPT´s Antwort:*** {st.session_state.vokal_antwort_chatgpt}
                    """)
            st.markdown("""
                        Wie du siehst macht die KI-Anwendung auch Fehler. Sie kann gut Texte erzeugen, Fragen beantworten
                        aber nicht alles ist richtig! Sie kann sich auch vertun, deshalb ist es wichtig, dass Ergebnis immer zu prüfen!
                        """)
        else:
            st.info("Bitte klicke zuerst auf 'ChatGPT nach Vokalen fragen', um die Ergebnisse vergleichen zu können.")

            st.session_state.vokal_antwort_chatgpt


st.divider()

#Speichern der Prompts:
if "antworten_uebung1antwortenzufragen_vorgegeben" not in st.session_state:
    st.session_state.antworten_uebung1antwortenzufragen_vorgegeben= []
if "anzahleingaben_uebung1_vorgegeben" not in st.session_state:
    st.session_state.anzahleingaben_uebung1_vorgegeben = 0
if "anzahleingaben_uebung1_eigene" not in st.session_state:
    st.session_state.anzahleingaben_uebung1_eigene = 0
#Speichern der Prompts:
if "antworten_uebung1antwortenzufragen_eigene" not in st.session_state:
    st.session_state.antworten_uebung1antwortenzufragen_eigene= []
#Speichern der Anzahl der Prompts ohne Session.State-Befehl wird durch neu eingeben einer Frage wieder 0 gesetzt


#st.text_input hat Bugs
# Eingabe und Button
textzuaufgaben=st.markdown("""
                Suche die eine der beiden hier angegebenen Fragen aus, die ChatGPT dir beantworten soll und gibt diese in das untenstehende leere
                Textfeld ein.
                1. Wer ist der aktuelle Präsident der USA ist
                2. Wie das Ergebnis der Aufgabe 482 * 739
            """)
with st.form("frage_formular_vorgegeben", clear_on_submit=True):
    frage = st.text_input("Stelle eine der oben vorgegebenen Fragen")
    senden = st.form_submit_button("Fragen")

    st.markdown("Wenn du fertig bist, dann scrolle bitte weiter nach unten")
    # Antwort generierung erst wenn Button geklickt und Eingabe vorhanden
    if senden and frage:

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
        st.session_state.antworten_uebung1antwortenzufragen_vorgegeben.append({
            "Frage": frage,
            "Antwort": antwort_text,
            "Anzahl Prompts": anzahleingaben_vorgegeben
        })
        st.session_state.antworten_uebung1antwortenzufragen_vorgegeben


# Eingabe und Button
textzuaufgaben=st.markdown("""
                Jetzt bist du dran!
                Stelle ChatGPT eine Frage, die dich interessiert
            """)
with st.form("frage_formular_eigene", clear_on_submit=True):
    frage_eigene = st.text_input("Stelle hier deine eigenen Fragen")
    senden = st.form_submit_button("Fragen")

    st.markdown("Wenn du fertig bist, dann scrolle bitte weiter nach unten")
    # Antwort generierung erst wenn Button geklickt und Eingabe vorhanden
    if senden and frage_eigene:

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
        st.session_state.antworten_uebung1antwortenzufragen_eigene.append({
            "Frage": frage_eigene,
            "Antwort": antwort_text_eigene,
            "Anzahl Prompts": anzahleingaben_eigene
        })
        st.session_state.antworten_uebung1antwortenzufragen_eigene
st.write("")




fragevertrauen="Glaubst du, dass diese Antworten richtig ist?"
antwortvertrauen = st.radio("Glaubst du, dass diese Antworent richtig ist?",
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
    st.session_state.fragen_uebung1["fragevertrauen"]=fragevertrauen
    st.session_state.antworten_uebung1["antwortvertrauen"]=antwortvertrauen
    st.session_state.fragen_uebung1
    st.session_state.antworten_uebung1

st.session_state.uebung1 = {
    ####Auswertefrage
    # Textübung
    "textdeutsch": st.session_state.fragen_uebung1.get("textdeutsch", ""),
    "textecht": st.session_state.antworten_uebung1.get("textecht", ""),
    
    #######Vokale zählen
    # Vokalzählen
    "selbstgezaehlt": st.session_state.get("selbstgezaehlteantwort", ""),
    "vokal_antwort_chatgpt": st.session_state.get("vokal_antwort_chatgpt", ""),
    
    ####Interaktion Schüler:innen mit ChatGPT
    # Vorgegebene Fragen
    "vorgegebene_fragen": st.session_state.get("antworten_uebung1antwortenzufragen_vorgegeben", []),
    "anzahl_vorgegebene": st.session_state.get("anzahleingaben_uebung1_vorgegeben", 0),
    
    # Eigene Fragen
    "eigene_fragen": st.session_state.get("antworten_uebung1antwortenzufragen_eigene", []),
    "anzahl_eigene": st.session_state.get("anzahleingaben_uebung1_eigene", 0),
    
    #########Frage beantworten
    # Vertrauensfrage
    "fragevertrauen": st.session_state.fragen_uebung1.get("fragevertrauen", ""),
    "antwortvertrauen": st.session_state.antworten_uebung1.get("antwortvertrauen", "")
}
st.session_state.uebung1
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
