import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(
    page_title="1. Übung"
)
st.markdown("<h4>1. Übung</h4>",unsafe_allow_html=True)

st.markdown("""
            Beginnen wir mit der ersten Übung!

            Auf vorherigen Seite haben wir gelernt, was KI ist und was sie kann. 
            Zudem hast du die erste Interaktion mit einer KI-Anwendung mit der Eingabe deiner Frage gehabt.
            Die KI-Anewndung war ein texgenerierendes System mit Methoden des Deep Learnings,
            das auf große Sprachmodelle Large Language Models (LLM) trainiert ist.
        
            Diese KI-Anwendung ist ChatGPT.
            """)



st.markdown("Jetzt überprüfen wir, was ChatGPT kann und ob die Anwendung fleißig ihre Daten analysiert hat.")
st.markdown("""
                Wir stellen ChatGPT einige Aufgaben und schauen uns die Antworten an.
               
            """)
st.divider()
st.markdown("""
                    Dafür soll ChatGPT mich unterstützen einige Aufgaben für mich erledigen, d. h.:
                    - einen Text
                    - mir diesen dann übersetzen
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
            "Schreibe mir einen zwei Sätze über einen Sommertag mit Erdbeereis."
        """)

st.markdown("""
                ***ChatGPT Antwort:***
                "Die Sonne brannte vom wolkenlosen Himmel, während das süße Erdbeereis langsam in meiner Hand schmolz.
                Jeder Löffel war
                ein kleiner, kühler Moment des Glücks an diesem warmen Sommertag."
            """)
textdeutsch="Die Sonne brannte vom wolkenlosen Himmel, während das süße Erdbeereis langsam in meiner Hand schmolz. Jeder Löffel war ein kleiner, kühler Moment des Glücks an diesem warmen Sommertag"
textecht=st.radio("Würdest du 1-2 Sätze über einen Sommertag auch so schreiben?",
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

st.divider()
st.markdown("""
            Aufgabe übersetzen des Textes:

        """)
st.markdown("""
            ***Prompt für ChatGPT:***
            "Übersetze mir den Text ins Englische."
        """)

st.markdown("""
                ***ChatGPT Antwort:***
                "The sun blazed in the cloudless sky as the sweet strawberry ice cream slowly melted in my hand.
                 Every spoonful was a small, cool moment of happiness on this warm summer day."
            """)

st.divider()
# Vokale zählen Teil integrieren
st.markdown("""
            In dieser Übung nutzen wir den Satz: ***"An einem schönen Sommertag genieße ich ein kühles Erdbeereis."***
            Diesmal untersuchen wir den Satz etwas genauer.
            Wir machen eine Aufgabe aus unserer Grundschulzeit. Wir haben damals gelernt was Vokale sind (a,e,i,o,u,ä,ö,ü).
            """)

beispielsatz="An einem schönen Sommertag genieße ich ein kühles Erdbeereis."
st.markdown(beispielsatz)
if st.button("ChatGPT nach Vokalen fragen"):
    # Lösung generieren
    with st.spinner(text="Erstelle Text, bitte warten..."):
        antwort = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
 #                 {"role": "system", "content": "Zähle die Vokale für den Satz und gebe sie so aus, dass ich sie gut lesen kann."},
                  {"role": "user", "content": f"Vokale zählen {beispielsatz} in jeder Zeile jeweils ein Vokal. In dem Format Buchstabe Kleinbuchstabe : zahl Leerzeile dann nächster Vokal am Ende die Summe der Vokale. Ohne einen Kommentar danach"}
                 ]  )
   
    # Antwort zeigen
    st.write("Antwort:")
    antwort_text=antwort.choices[0].message.content
    st.write(antwort_text)
st.write("Jetzt zählen wir selbst nach:")
if st.button("Vokale selbst zählen"):
    satzklein = beispielsatz.lower()
    vokale ="aeiouäöü"
    gesamtvokale = 0
    for vokal in vokale:
        anzahl=satzklein.count(vokal)
        if anzahl >0:
            st.write(f"{vokal} : {anzahl},")
            gesamtvokale=gesamtvokale+anzahl
    st.write(f"Gesamt: {gesamtvokale}")
    st.markdown("""
                    Wie du siehst macht die KI-Anwendung auch Fehler. Sie kann gut Texte erzeugen, Fragen beantworten
                    aber nicht alles ist richtig! Sie kann sich auch vertun, deshalb ist es wichtig, dass Ergebnis immer zu prüfen!
   
                """)


st.divider()

#Speichern der Prompts:
if "antworten_uebung1antwortenzufragen" not in st.session_state:
    st.session_state.antworten_uebung1antwortenzufragen= []
#Speichern der Anzahl der Prompts ohne Session.State-Befehl wird durch neu eingeben einer Frage wieder 0 gesetzt
if "anzahleingaben_uebung1" not in st.session_state:
    st.session_state.anzahleingaben_uebung1 = 0

#st.text_input hat Bugs
# Eingabe und Button
textzuaufgaben=st.markdown("""
                Jetzt unterstützt du mich dabei frag bitte nach:
                1. Wer der aktuelle Präsident der USA ist
                2. Wie die Lösung von 482 * 739 ist
                3. Bei Interesse kannst du selbst Aufgaben in ChatGPT testen

            """)
with st.form("frage_formular", clear_on_submit=True):
    frage = st.text_input("Stelle die Fragen hier")
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
    st.session_state.anzahleingaben_uebung1 += 1
    anzahleingaben = st.session_state.anzahleingaben_uebung1

    # Antwort anzeigen
    st.write("Antwort:")
    st.write(antwort_text)

    # Frage anzeigen
    st.write("Deine Frage:")
    st.write(frage)

    # Frage + Antwort speichern
    st.session_state.antworten_uebung1antwortenzufragen.append({
        "Frage": frage,
        "Antwort": antwort_text,
        "Anzahl Prompts": anzahleingaben
    })
    st.session_state.antworten_uebung1antwortenzufragen
st.write("")
fragevertrauen="Glaubst du, dass diese Antwort richtig ist?"
antwortvertrauen = st.radio("Glaubst du, dass diese Antwort richtig ist?",
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
