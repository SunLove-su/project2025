import streamlit as st

st.set_page_config(
    page_title="Grundwissen über Künstliche Intelligenz (KI)"
)
st.markdown("<h4>Grundwissen über Künstliche Intelligenz (KI)</h4>",unsafe_allow_html=True)
st.write("Auf dieser Seite erfährst du einiges spannendes über KI, mach dich bereit." \
"Wir erforschen gemeinsam KI und frischen entweder bereits vorhandes Wissen auf oder lernen" \
"was neues.")
with st.expander("Was ist KI"):
     st.write("Stellt euch ein Labyrinth vor mit Sackgassen und mit vielen unterschiedlichen Wegen bei dem nur einer führt" \
     "zum Ausgang." \
     "Vor der KI musste ich einem Computerprogramm genaue Angaben geben" \
     "Gehe zwei Schritte nach vorne, einen nach links, drei nach vorne. Gibt es Hindernisse wie eine Mauer" \
     "dann bleibt das Programm stehen, da es dazu keine Angeben erhalten hat." \
     "Beim Programmieren muss jede Möglichkeit, jedes Hinderniss und jeder Schritt beschrieben sein, ansonsten bleibt " \
     "das Programm an der Stelle mit dem Hinterniss stehen" \
     "" \

     
     "Mit KI ist es anders. Die KI geht 1.000.000 in unterschiedliche Labyrinthe und merkt sich," \
     "wie ein Hindernis aussieht, dass sie nicht weiter kann und merkt sich den besten Weg zum Ausgang." \
     "Anhand von Mustern hat die KI gelernt, dass wenn links eine Wand ist, sie rechts weiter gehen kann."
     "oder das bei 3 Wegen der mittlere meistens zum Ziel geführt hat." \
     "Bei Labyrithen die die KI noch nie gegangen ist, kann es passieren dass sie sich verläuft, den falschen Weg geht und in einer Sackgasse endet")
      
     "Während Du und ich beim ersten Mal in einem Labyrinth im Gegensatz zur KI, wissen, wie wir aus einer Sackgasse kommen, und uns den Ausgang" \
     "ersuchen, braucht eien KI 1.000.0000 Übungen. Mit diesen Übungen versucht sie unsere Intelligenz, die Kombinationen, Schlussfolgerungen und"
     "Entscheidungen die wir treffen nachzuahmen."

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

