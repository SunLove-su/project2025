import streamlit as st

st.set_page_config(
    page_title="Grundwissen über Künstliche Intelligenz (KI)"
)
st.markdown("<h4>Grundwissen über Künstliche Intelligenz (KI)</h4>",unsafe_allow_html=True)
st.markdown("""
            Auf dieser Seite erfährst du einiges spannendes über KI, mach dich bereit. 
            Wir erforschen gemeinsam KI und frischen entweder bereits vorhandenes Wissen 
            auf oder lernen was neues
            """)
with st.expander("Was ist KI"):
     st.markdown("""
                    Stellt euch ein Labyrinth mit vielen Wegen und Sackgassen vor.

                    Vor der KI musste ich einem Computerprogramm exakte Anweisungen
                    geben: "Gehe einen Schritte nach vorne, dann zwei nach links, dann
                    einen nach rechts." Trifft es auf eine Mauer, bleibt das Programm stehen,
                    weil es keine Anweisung für diesen Fall hat. Jede Situation muss vorprogrammiert sein.

                    KI funktioniert anders: Sie geht durch tausende Labyrinthe und lernt daraus.
                    Sie merkt sich Muster: "Bei einer Wand links gehe rechts" oder "Bei drei Wegen
                    führt meist der mittlere zum Ziel". Trifft die KI auf ein völlig unbekanntes Labyrinth,
                    kann sie dennoch in Sackgassen enden.

                    **Der Unterschied: Wir Menschen können schon beim ersten Labyrinth intuitiv Probleme lösen. KI braucht Millionen Übungen, um unsere Fähigkeit zum Kombinieren und Entscheiden nachzuahmen.""", unsafe_allow_html=True
     )

with st.expander("Wie funktioniert KI"):
     st.write("Wir haben mit dem Labyrinth gesehen, dass die KI:" \
               "1. viele Daten braucht: 1.000.000 ist die KI die unterschiedlichen Labyrithen durchgegangen"
               "2. sich Muster merkt: wenn links eine Wand ist, sie rechts weiter geht und das bei 3 Wegen der mittlere meistens ins Ziel führt" \
               "3. erlerntes anwendet: die KI begeht ein Labyrinth, die sie noch nie gegangen ist und gelangt an den Ausgang" \
               "4. fehler macht: die KI verläuft sich, geht den falschen Weg und steckt in einer Sackgasse fest ")

with st.expander("KI-Begriffe"):
     st.write( " - Algorithmus: Schritt für Schritt Anleitung, wie das Computer-Programm, dem ich sagen musste gehe zwei Schritte nach vorne, einen nach links."
               " - Machine Learning: "
               "2. sich Muster merkt: wenn links eine Wand ist, sie rechts weiter geht und das bei 3 Wegen der mittlere meistens ins Ziel führt" \
               "3. erlerntes anwendet: die KI begeht ein Labyrinth, die sie noch nie gegangen ist und gelangt an den Ausgang" \
               "4. fehler macht: die KI verläuft sich, geht den falschen Weg und steckt in einer Sackgasse fest ")


with st.expander("Was kann KI"):
     st.write("")

#Fragen die du selbst über KI-beantworten haben willst

