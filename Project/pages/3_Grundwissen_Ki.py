import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

st.set_page_config(
    page_title="Grundwissen über Künstliche Intelligenz (KI)"
)

st.markdown("<h4>Grundwissen über Künstliche Intelligenz (KI)</h4>",unsafe_allow_html=True)
st.markdown("""
            Auf dieser Seite erfährst du einiges spannendes über KI, mach dich bereit. 
            Wir erforschen gemeinsam KI und frischen entweder bereits vorhandenes Wissen 
            auf oder lernen was neues
            """)
st.divider()

with st.expander("Was ist KI?",icon=":material/double_arrow:"):
     st.markdown("""
                    Stellt euch ein Labyrinth mit Sackgassen und mit vielen unterschiedlichen Wegen vor,
                    bei dem nur einer führt zum Ausgang.
                 
                    Vor der KI musste ich einem Computerprogramm genaue Angaben geben Gehe zwei Schritte
                    nach vorne, einen nach links, drei nach vorne. Gibt es Hindernisse wie eine Mauer dann
                    bleibt das Programm stehen, da es dazu keine Angeben erhalten hat. Beim Programmieren
                    muss jede Möglichkeit, jedes Hinderniss und jeder Schritt beschrieben sein,
                    ansonsten bleibt das Programm an der Stelle mit dem Hinterniss stehen.
                 
                    Mit KI ist es anders. Die KI geht 1.000.000 in unterschiedliche Labyrinthe und merkt sich,
                    wie ein Hindernis aussieht, dass sie nicht weiter kann und merkt sich den besten Weg zum
                    Ausgang.Anhand von Mustern hat die KI gelernt, dass wenn links eine Wand ist, sie rechts
                    weiter gehen kann.oder das bei 3 Wegen der mittlere meistens zum Ziel geführt hat. Bei
                    Labyrithen die die KI noch nie gegangen ist, kann es passieren dass sie sich verläuft,
                    den falschen Weg geht und in einer Sackgasse endet

                    Während Du und ich beim ersten Mal in einem Labyrinth im Gegensatz zur KI wissen, wie wir
                    aus einer Sackgasse kommen und uns den Ausgang ersuchen, braucht eien KI 1.000.0000 Übungen.
                    Mit diesen Übungen versucht sie unsere Intelligenz, die Kombinationen, Schlussfolgerungen
                    und Entscheidungen die wir treffen nachzuahmen."""
     )

with st.expander("Wie funktioniert KI?",icon=":material/double_arrow:"):
     st.markdown("""
                 Wir haben mit dem Labyrinth gesehen, dass die KI:
                 1. viele Daten braucht: 1.000.000 ist die KI die unterschiedlichen Labyrithen durchgegangen
                 2. sich Muster merkt: wenn links eine Wand ist, sie rechts weiter geht und das bei 3 Wegen der
                    mittlere meistens ins Ziel führt 
                 3. erlerntes anwendet und daraus vorhersagen trifft: die KI begeht ein Labyrinth, die sie noch nie gegangen ist und gelangt
                    an den Ausgang
                 4. fehler macht: die KI verläuft sich, geht den falschen Weg und steckt in einer Sackgasse fest 
                """)

with st.expander("Welche Risiken hat KI",icon=":material/double_arrow:"):
     st.markdown("""
                 Wir haben mit dem Labyrinth gesehen, dass die KI:
                 1. viele Daten braucht: 1.000.000 ist die KI die unterschiedlichen Labyrithen durchgegangen
                 2. sich Muster merkt: wenn links eine Wand ist, sie rechts weiter geht und das bei 3 Wegen der
                    mittlere meistens ins Ziel führt 
                 3. erlerntes anwendet und daraus vorhersagen trifft: die KI begeht ein Labyrinth, die sie noch nie gegangen ist und gelangt
                    an den Ausgang
                 4. fehler macht: die KI verläuft sich, geht den falschen Weg und steckt in einer Sackgasse fest 
                """)

with st.expander("KI-Begriffe",icon=":material/double_arrow:"):
     st.markdown("""
                - Algorithmus: Schritt für Schritt Anleitung, wie das Computer-Programm, dem ich sagen musste gehe zwei Schritte nach vorne, einen nach links."
                - Machine Learning: Ist die KI, die 1.000.000 mal durch die Labyrithen muss, sich die Muster und Merkmale merkt"
                   - Überwachtes Lernen: Ich begleite die KI bei einigen Labyrinthen und zeige ihr den richtigen Weg.
                   - Unüberwachtes Lernen: Die geht die 1.000.000 mal alleine durch die Labyrinthe und merkt sich die Muster
                   - Künstliche Neuronale Netze (KNN): Sollen den Aufbau und die Funktionsweise eines Gehirns nachahmen.
                                                       Beispiel Fußballspiel: Der linke Torwart schießt den Ball, einem freien Verteidiger,
                                                       dieser zum Mittelfeldspieler, dann zum Stürmer. Jeder Spieler entscheidet zu wem er den
                                                       Ball spielt.
                                                       Die Spieler stellen Neuronen dar, die den Ball also die Informationen erhalten, verarbeiten und weitergeben.
                                                       Als Gesamtbild stellt es ein Netz dar. 
                                                       Durch das Trainig wird ihr zusammenspiel besser, sodass sie in der Lage sind Titel zu holen oder
                                                       bei der KI komplexe Aufgaben zu lösen
                   - Deep Learning: Ist ein vielschichtigeres Netz, mit mehreren Ebenen.
                                    Beispiel es sind jetzt viel mehr Spieler zwischen den Positionen auf dem Feld, sodass ein tieferes Netz entsteht.
                                    Die Spieler jeder Ebene haben bestimmte Aufgaben. Die erste Reihe sucht die freien Räume, die zweite erkennt die Lücken in
                                    der Abwehr und die dritte Reihe machen den Laufweg, bevor die letzte Reihe den Torschuss macht.
                    - Prompt: Anweisungen die wir der KI gesprochen oder via Text
                    - Generative KI (Gen-KI): KI-Anwendungen, die durch das gelernte neue Inhalte generieren können
                    """)
with st.expander("Was kann KI?",icon=":material/double_arrow:"):
     st.markdown("""
                    KI kann unterschiedliche Aufgaben ausführen:
                    - Bilder erkennen und erstellen: KI kann die Motive auf den Bildern erkennen, mit Text lässt sich auch ein Bild erzeugen, z. B. DALL E
                    - Text erkennen und erstellen: KI erkennt Texte auch wenn sie nicht richtig geschrieben sind und kann auch Texte schreiben, z. B. ChatGPT
                    - Sprache verstehen und antworten: KI versteht deine Worte und Antwortet dir, z. B. Alexa und Siri
                    - Übersetzen verstehen und erzeugen: KI versteht andere Sprachen und kann auch Text in andere Sprachen übersetzen
                    - Muster erkennen: KI erkennt Muster die uns ggfls. nicht auffalen, z. B. bei Krankheiten oder zur Gefahrenabwehr
                      usw...
               """)

#Speichern der Prompts:
if "antworten_grundwissen" not in st.session_state:
    st.session_state.antworten_grundwissen = []
#Speichern der Anzahl der Prompts ohne Session.State-Befehl wird durch neu eingeben einer Frage wieder 0 gesetzt
if "anzahleingaben_grundwissen" not in st.session_state:
    st.session_state.anzahleingaben_grundwissen = 0
# Eingabe und Button
frage = st.text_input("Falls du noch mehr Wissen möchtest frag die KI")
if st.button("Fragen") and frage:
    # Antwort generieren
    
    with st.spinner(text="Erstelle Text, bitte warten..."):
        antwort = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": frage}]
    )
    st.session_state.anzahleingaben_grundwissen=st.session_state.anzahleingaben_grundwissen+1
    anzahleingaben=st.session_state.anzahleingaben_grundwissen
    # Antwort zeigen
    st.write("Antwort:")
    antwort_text=antwort.choices[0].message.content
    st.write(antwort_text)


    # Alle Fragen anzeigen
    st.write("Deine Fragen:")
    st.write(frage)

    #Speichern der Fragen, Antworten und Eingaben
    st.session_state.antworten_grundwissen.append({
        "Frage":frage,
        "Antwort":antwort_text,
        "Anzahl Prompts":anzahleingaben
        })
   
    st.session_state.antworten_grundwissen 
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