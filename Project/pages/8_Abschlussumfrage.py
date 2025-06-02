"""
Abschlussumfrage


Speicherung der Daten mit Ausführen des Buttons. Speicherung erfolgt nur, wenn keine Fehler in der 
Datenbank vorhanden sind.
"""
import streamlit as st
from google.cloud import firestore
import json
import uuid
import datetime
from supabase import create_client
from google.api_core import exceptions as google_exceptions
import hilfsdatei
import os

#Überschrift der Seite
titel_seite = "Abschlussumfrage"
hilfsdatei.seite(titel_seite)
#Sicherstellen, dass ein Zugriff der Seiten nur mit Passwort erfolgt, und dass User keine Navigationsseite sehen

hilfsdatei.teilnehmer_anmelden()

#Überschrift der Seite
ueberschrift_seite = "Abschlussumfrage"
st.markdown(f"<h4>{ueberschrift_seite}</h4>",unsafe_allow_html=True)
#Einleitung der Abschlussumfrage
einleitung_text =("""
            In den Übungen die du durchgegangen bist hast du einiges gelernt.
            Zum Abschluss gibt es noch ein paar Fragen die du bitte beantworten sollst und dann bist du schon fertig
            """)
st.markdown(einleitung_text)

#Speichern Antworten
if "abschlussumfrage" not in st.session_state:
        st.session_state.abschlussumfrage = {}

############################################################################
# ATTENTION FRAGE
frage_aufmerksamkeit ="Wähle die Antwort mit der Zahl 2"
antwort_aufmerksamkeit = st.radio (
                                frage_aufmerksamkeit,
                                ("1",
                                "9",
                                "2",
                                "Keine Angabe"),
                                index=None
)
#Speichern der Antworten
if "anzahl_aufmerksamkeit" not in st.session_state:
    st.session_state.anzahl_aufmerksamkeit = 0
if "aufmerksamkeit_alt" not in st.session_state:
    st.session_state.aufmerksamkeit_alt = None
if "aufmerksamkeit_historie" not in st.session_state.abschlussumfrage:
    st.session_state.abschlussumfrage["aufmerksamkeit_historie"] = []

# Speicherung nur bei Änderung der Antwort
if antwort_aufmerksamkeit is not None and antwort_aufmerksamkeit != st.session_state.aufmerksamkeit_alt:
    st.session_state.anzahl_aufmerksamkeit += 1
    
    aufmerksamkeit = {
        "Bereich": "Abschlussumfrage",
        "Typ": "Aufmerksamkeit",
        "Frage": frage_aufmerksamkeit,
        "Antwort": antwort_aufmerksamkeit,
        "Anzahl_Aenderungen": st.session_state.anzahl_aufmerksamkeit
    }
    
    st.session_state.abschlussumfrage["aufmerksamkeit_historie"].append(aufmerksamkeit)
    st.session_state.abschlussumfrage["aufmerksamkeit"] = aufmerksamkeit
    # Aktuelle Antwort merken
    st.session_state.aufmerksamkeit_alt = antwort_aufmerksamkeit
    
    st.write(f"Deine Antwort ist: {antwort_aufmerksamkeit}")
########################################################################
st.divider()
########################################################################


#Identische Frage wie in der Umfrage am Anfang des Moduls
#Frage: Erkennungsfähigkeit, ob ein Text oder Bild von der KI generiert wurde

frage_erkennung_ki = "Wie gut kannst du erkennen, ob ein Text oder Bild von einer KI stammt?"
antwort_erkennung_ki = st.radio(frage_erkennung_ki, (
    "Sehr gut",
    "Gut",
    "Mittelmäßig",
    "Eher schlecht", 
    "Schlecht"
), index=None)


if "anzahl_erkennung_ki" not in st.session_state:
    st.session_state.anzahl_erkennung_ki = 0
if "erkennung_ki_alt" not in st.session_state: 
    st.session_state.erkennung_ki_alt = None 
if "erkennung_ki_historie" not in st.session_state.abschlussumfrage:
    st.session_state.abschlussumfrage["erkennung_ki_historie"] = []

# Speicherung nur bei Änderung der Antwort
if antwort_erkennung_ki is not None and antwort_erkennung_ki != st.session_state.erkennung_ki_alt:
    st.session_state.anzahl_erkennung_ki += 1
    
    erkennung_ki = {
        "Bereich": "Abschlussumfrage",
        "Typ": "Erkennung_KI",
        "Frage": frage_erkennung_ki,
        "Antwort": antwort_erkennung_ki,
        "Anzahl_Aenderungen": st.session_state.anzahl_erkennung_ki
    }
    
    st.session_state.abschlussumfrage["erkennung_ki_historie"].append(erkennung_ki)
    st.session_state.abschlussumfrage["erkennung_ki"] = erkennung_ki
    # Aktuelle Antwort merken
    st.session_state.erkennung_ki_alt = antwort_erkennung_ki
    
    st.markdown(f"Deine Antwort: {antwort_erkennung_ki}")



##################################################################
#Identische Frage wie in der Umfrage am Anfang des Moduls
frage_vertrauen_ki = "Wie vertrauenswürdig hältst du KI-generierte Inhalte?"
antwort_vertrauen_ki = st.radio(frage_vertrauen_ki, (
    "Sehr vertrauenswürdig",
    "Eher vertrauenswürdig", 
    "Neutral",
    "Eher nicht vertrauenswürdig",
    "Gar nicht vertrauenswürdig"
), index=None)

if "anzahl_vertrauen_ki" not in st.session_state:
    st.session_state.anzahl_vertrauen_ki = 0
if "vertrauen_ki_alt" not in st.session_state:
    st.session_state.vertrauen_ki_alt = None   
if "vertrauen_ki_historie" not in st.session_state.abschlussumfrage:
    st.session_state.abschlussumfrage["vertrauen_ki_historie"] = []

# Speicherung nur bei Änderung der Antwort
if antwort_vertrauen_ki is not None and antwort_vertrauen_ki != st.session_state.vertrauen_ki_alt:
    st.session_state.anzahl_vertrauen_ki += 1
    
    vertrauen_ki = {
        "Bereich": "Abschlussumfrage",
        "Typ": "Vertrauen_KI_Inhalte",
        "Frage": frage_vertrauen_ki,
        "Antwort": antwort_vertrauen_ki,
        "Anzahl_Aenderungen": st.session_state.anzahl_vertrauen_ki
    }
    
    st.session_state.abschlussumfrage["vertrauen_ki_historie"].append(vertrauen_ki)
    st.session_state.abschlussumfrage["vertrauen_ki"] = vertrauen_ki
    # Aktuelle Antwort merken
    st.session_state.vertrauen_ki_alt = antwort_vertrauen_ki
    
    st.markdown(f"Deine Antwort: {antwort_vertrauen_ki}")
############################################################################


#Identische Frage wie am Anfang des Moduls
#Frage ob KI-generierte Inhalte geprüft werden

frage_pruefung_ki = "Wie genau prüfst du KI-generierte Inhalte, bevor du ihnen vertraust?"
antwort_pruefung_ki = st.radio(frage_pruefung_ki, (
    "Sehr genau",
    "Eher genau",
    "Manchmal",
    "Eher selten",
    "Gar nicht"
), index=None)

if "anzahl_pruefung_ki" not in st.session_state:
    st.session_state.anzahl_pruefung_ki = 0
if "pruefung_ki_alt" not in st.session_state: 
    st.session_state.pruefung_ki_alt = None    
if "pruefung_ki_historie" not in st.session_state.abschlussumfrage:
    st.session_state.abschlussumfrage["pruefung_ki_historie"] = []

# Speicherung nur bei Änderung der Antwort
if antwort_pruefung_ki is not None and antwort_pruefung_ki != st.session_state.pruefung_ki_alt:
    st.session_state.anzahl_pruefung_ki += 1
    
    pruefung_ki = {
        "Bereich": "Abschlussumfrage",
        "Typ": "Pruefung_KI",
        "Frage": frage_pruefung_ki,
        "Antwort": antwort_pruefung_ki,
        "Anzahl_Aenderungen": st.session_state.anzahl_pruefung_ki
    }
    
    st.session_state.abschlussumfrage["pruefung_ki_historie"].append(pruefung_ki)
    st.session_state.abschlussumfrage["pruefung_ki"] = pruefung_ki
    # Aktuelle Antwort merken
    st.session_state.pruefung_ki_alt = antwort_pruefung_ki
    
    st.markdown(f"Deine Antwort: {antwort_pruefung_ki}")

#################################################################################################
#Trennungslinie
st.divider()


#####################################################################################################
#Fragen über das gelernte im Modul
frage_wissen_gewonnen = "Was hast du in dieser Lerneinheit gelernt?"
#Kurze Antworten bei Multiselect, da sie nicht komplett auf einem Smartphone dargestellt werden
wissen_gewonnen = st.multiselect(
                                frage_wissen_gewonnen,
                                ("KI-Bilder erkennen",
                                "Stereotypen erkennen", 
                                "Was KI ist",
                                "Keine persönlichen Daten eingeben",
                                "Urheberrecht beachten",
                                "Keine Angabe"),
                                placeholder="Bitte wähle aus, was du gelernt hast"
)
#Anpassung, damit die Antworten nicht als Sequenz ausgegeben werden
if wissen_gewonnen:
    antwort_wissen = ", ".join(wissen_gewonnen)

    if "anzahl_wissen_gewonnen" not in st.session_state:
        st.session_state.anzahl_wissen_gewonnen = 0
    st.session_state.anzahl_wissen_gewonnen += 1
    
    if "wissen_gewonnen_historie" not in st.session_state.abschlussumfrage:
        st.session_state.abschlussumfrage["wissen_gewonnen_historie"] = []
    
    wissen_gewonnen = {
        "Bereich": "Abschlussumfrage",
        "Typ": "Wissen_gewonnen",
        "Frage": frage_wissen_gewonnen,
        "Antwort": antwort_wissen,
        "Anzahl_Aenderungen": st.session_state.anzahl_wissen_gewonnen
    }
    
    st.session_state.abschlussumfrage["wissen_gewonnen_historie"].append(wissen_gewonnen)
    st.session_state.abschlussumfrage["wissen_gewonnen"] = wissen_gewonnen
    st.markdown(f"Deine Antwort ist: {antwort_wissen}")

################################################################################

st.divider()

################################################################################
#Frage zur Verbesserung der Erkennungsfähigkeit vom Einsatz von KI

frage_erkennung_verbessert = "Hat sich deine Fähigkeit, KI-Inhalte zu erkennen, durch die Lerneinheit verbessert?"
antwort_erkennung_verbessert = st.radio(
                       frage_erkennung_verbessert,
                       ("Ja, deutlich verbessert",
                        "Ja, etwas verbessert",
                        "Keine Veränderung",
                        "Nein, gar nicht verbessert"),
                       index=None
)
# Speichern der Antwort
if "anzahl_erkennung_verbessert" not in st.session_state:
    st.session_state.anzahl_erkennung_verbessert = 0
if "erkennung_verbessert_alt" not in st.session_state:
    st.session_state.erkennung_verbessert_alt = None  
if "erkennung_verbessert_historie" not in st.session_state.abschlussumfrage:
    st.session_state.abschlussumfrage["erkennung_verbessert_historie"] = []

# Speicherung nur bei Änderung der Antwort
if antwort_erkennung_verbessert is not None and antwort_erkennung_verbessert != st.session_state.erkennung_verbessert_alt:
    st.session_state.anzahl_erkennung_verbessert += 1
    
    erkennung_verbessert = {
        "Bereich": "Abschlussumfrage",
        "Typ": "Erkennungsfaehigkeit_verbessert",
        "Frage": frage_erkennung_verbessert,
        "Antwort": antwort_erkennung_verbessert,
        "Anzahl_Aenderungen": st.session_state.anzahl_erkennung_verbessert
    }
    
    st.session_state.abschlussumfrage["erkennung_verbessert_historie"].append(erkennung_verbessert)
    st.session_state.abschlussumfrage["erkennung_verbessert"] = erkennung_verbessert
    # Aktuelle Antwort merken
    st.session_state.erkennung_verbessert_alt = antwort_erkennung_verbessert
    
    st.markdown(f"Deine Antwort ist: {antwort_erkennung_verbessert}")
################################################################################################

st.divider()

################################################################################################

# Frage wie Teilnehmer KI generierte Inhalte hinterfragen?
frage_hinterfragen_ki = "Wirst du KI-generierte Inhalte in Zukunft mehr hinterfragen?"
antworten_hinterfragen_ki = st.radio (
                                frage_hinterfragen_ki,
                              ("Viel mehr",
                                "Etwas mehr", 
                                "Gleich",
                                "Etwas weniger",
                                "Viel weniger",),
                                index=None
)
#Speichern der Antwort
if "anzahl_hinterfragen_ki" not in st.session_state:
    st.session_state.anzahl_hinterfragen_ki = 0
if "hinterfragen_ki_alt" not in st.session_state:
    st.session_state.hinterfragen_ki_alt = None
if "hinterfragen_historie" not in st.session_state.abschlussumfrage:
    st.session_state.abschlussumfrage["hinterfragen_historie"] = []

# Speicherung nur bei Änderung der Antwort
if antworten_hinterfragen_ki is not None and antworten_hinterfragen_ki != st.session_state.hinterfragen_ki_alt:
    st.session_state.anzahl_hinterfragen_ki += 1
    
    hinterfragen = {
        "Bereich": "Abschlussumfrage",
        "Typ": "Hinterfragen",
        "Frage": frage_hinterfragen_ki,
        "Antwort": antworten_hinterfragen_ki,
        "Anzahl_Aenderungen": st.session_state.anzahl_hinterfragen_ki
    }
    
    st.session_state.abschlussumfrage["hinterfragen_historie"].append(hinterfragen)
    st.session_state.abschlussumfrage["hinterfragen"] = hinterfragen
    # Aktuelle Antwort merken
    st.session_state.hinterfragen_ki_alt = antworten_hinterfragen_ki
    
    st.write(f"Deine Antwort ist: {antworten_hinterfragen_ki}")

###################################################################################

#Frage wie Teilnehmer KI-generierte Inhalte in Zukunft prüfen

frage_pruefung = "Wie genau wirst du KI-generierte Inhalte in Zukunft prüfen?"
antwort_pruefung = st.radio(
    frage_pruefung,
    (
        "Sehr genau",
        "Eher genau",
        "Manchmal",
        "Eher oberflächlich",
        "Gar nicht",
        "Keine Angabe"
    ),
    index=None
)

if "anzahl_pruefung" not in st.session_state:
    st.session_state.anzahl_pruefung = 0
if "pruefung_alt" not in st.session_state:
    st.session_state.pruefung_alt = None
if "pruefung_historie" not in st.session_state.abschlussumfrage:
    st.session_state.abschlussumfrage["pruefung_historie"] = []

# Speicherung nur bei Änderung der Antwort
if antwort_pruefung is not None and antwort_pruefung != st.session_state.pruefung_alt:
    st.session_state.anzahl_pruefung += 1
    
    pruefung = {
        "Bereich": "Abschlussumfrage",
        "Typ": "Prüfverhalten_Nachher",
        "Frage": frage_pruefung,
        "Antwort": antwort_pruefung,
        "Anzahl_Aenderungen": st.session_state.anzahl_pruefung
    }
    
    st.session_state.abschlussumfrage["pruefung_historie"].append(pruefung)
    st.session_state.abschlussumfrage["prüfverhalten_nachher"] = pruefung
    # Aktuelle Antwort merken
    st.session_state.pruefung_alt = antwort_pruefung
    
    st.markdown(f"Deine Antwort ist: {antwort_pruefung}")


#####################################################################################
#Frage wie Teilnehmer die Antworten prüfen

frage_vertrauen = "Hat sich dein Vertrauen in KI-generierte Inhalte durch die Lerneinheit verändert?"
antwort_vertrauen = st.radio(
    frage_vertrauen,
    (
        "Ja, ich vertraue KI-Inhalten jetzt mehr",
        "Ja, ich vertraue KI-Inhalten jetzt weniger",
        "Nein, mein Vertrauen ist unverändert",
        "Keine Angabe"
    ),
    index=None
)

if antwort_vertrauen is not None:
    

    st.session_state.abschlussumfrage["vertrauensveränderung"] = {
        "Bereich":"Abschlussumfrage",
        "Typ":"Vertrauensveränderung",
        "Frage": frage_vertrauen,
        "Antwort": antwort_vertrauen
    }
    st.markdown(f"Deine Antwort ist: {antwort_vertrauen}")


########################################################################
st.divider()

######################################################################
# Teilnehmerfeedback
frage_modul = "Wie hilfreich fandest du diese Lerneinheit?"
antwort_modul = st.radio(
                         frage_modul,
                        ("Sehr hilfreich",
                        "Hilfreich",
                        "Neutral",
                        "Weniger hilfreich",
                        "Nicht hilfreich"),
                        index=None
)
#Speichern der Antwort
if "anzahl_modul" not in st.session_state:
    st.session_state.anzahl_modul = 0
if "modul_alt" not in st.session_state:
    st.session_state.modul_alt = None
if "modul_bewertung_historie" not in st.session_state.abschlussumfrage:
    st.session_state.abschlussumfrage["modul_bewertung_historie"] = []

# Speicherung nur bei Änderung der Antwort
if antwort_modul is not None and antwort_modul != st.session_state.modul_alt:
    st.session_state.anzahl_modul += 1
    
    modul = {
        "Bereich": "Abschlussumfrage",
        "Typ": "Modul_Bewertung",
        "Frage": frage_modul,
        "Antwort": antwort_modul,
        "Anzahl_Aenderungen": st.session_state.anzahl_modul
    }
    
    st.session_state.abschlussumfrage["modul_bewertung_historie"].append(modul)
    st.session_state.abschlussumfrage["modul_bewertung"] = modul
    # Aktuelle Antwort merken
    st.session_state.modul_alt = antwort_modul
    
    st.markdown(f"Deine Antwort ist: {antwort_modul}")

#################################################################
#Frage zur Verbesserung des Moduls
frage_verbesserung = "Was kann an der Lerneinheit verbessert werden? (optional)"
antwort_verbesserung = st.text_area(frage_verbesserung, height=100)
#Speichern der Antworten
if antwort_verbesserung:
    if "anzahl_verbesserung" not in st.session_state:
        st.session_state.anzahl_verbesserung = 0
    st.session_state.anzahl_verbesserung += 1
    
    if "verbesserung_historie" not in st.session_state.abschlussumfrage:
        st.session_state.abschlussumfrage["verbesserung_historie"] = []
    
    verbesserung = {
        "Bereich": "Abschlussumfrage",
        "Typ": "Verbesserung",
        "Frage": frage_verbesserung,
        "Antwort": antwort_verbesserung,
        "Anzahl_Aenderungen": st.session_state.anzahl_verbesserung
    }
    
    st.session_state.abschlussumfrage["verbesserung_historie"].append(verbesserung)
    st.session_state.abschlussumfrage["verbesserung"] = verbesserung
    st.markdown(f"Deine Antwort ist: {antwort_verbesserung}")

st.session_state.abschlussumfrage
##################################################################################

st.divider()

#############################################################################


if st.button("Abschluss"):
    #Anzeigen wie weit der Teilnehmer in der gesamten Lerneinheit ist
    st.markdown("Aktueller Fortschritt in der gesamten Lerneinheit: 7 von 8")
    st.progress (7/8)

    unbeantwortet = False
    if antwort_aufmerksamkeit is None:
        st.error("Bitte beantworte die Frage mit der Aufmerksamkeit.")
        unbeantwortet = True
    if antwort_vertrauen_ki is None:
        st.error("Bitte beantworte die Frage zum Vertrauen.")
        unbeantwortet = True
    if antwort_erkennung_ki is None:
        st.error("Bitte beantworte die Frage zur Erkennungsfähigkeit.")
        unbeantwortet = True
    if antwort_pruefung_ki is None:
        st.error("Bitte beantworte die Frage zum Prüfverhalten.")
        unbeantwortet = True
    if not wissen_gewonnen:
        st.error("Bitte beantworte die Frage mit dem Wissen gewonnen.")
        unbeantwortet = True
    if antwort_erkennung_verbessert is None:
        st.error("Bitte beantworte die Frage mit der Erkennungsfähigkeit.")
        unbeantwortet = True
    if antwort_modul is None:
        st.error("Bitte bewerte das Modul.")
        unbeantwortet = True
    if antworten_hinterfragen_ki is None:
        st.error("Bitte gebe dein Vertrauen an KI-generierten Inhalten an.")
        unbeantwortet = True
    if antwort_pruefung is None:
        st.error("Bitte gebe dein Prüfverhalten an.")
        unbeantwortet = True
    if antwort_vertrauen is None:
        st.error("Bitte gebe deine Vertrauen in KI an.")
        unbeantwortet = True
    speicher_fehler_firestore = 0
    speicher_fehler_supabase = 0
    if not unbeantwortet:  
        
        
        firestore_key = os.getenv("FIRESTORE_GOOGLE_API_KEY")

        if not firestore_key:
            try:
                firestore_key = st.secrets["firestore"]["google_api_key"]

            except Exception:
                st.error ("Kein Google API Key für Firestore vorhanden.")   
                st.stop()

        try: 
            googlecredentials = json.loads(firestore_key)
            db = firestore.Client.from_service_account_info(googlecredentials)
        except Exception:
            st.error("Fehler bei den Google Credentials. Datenbank nicht verfügbar")
            st.stop()

        #uuid.uuid4 generiert eine zufällige UUID
        #user_id = f"{uuid.uuid4()}"
        #wenn der Teilnehmer keine user_id hat, wird eine neue erzeugt
        if "user_id" in st.session_state:
            user_id=st.session_state.user_id
        else:
            #
            teilnehmergruppe = st.session_state.get("teilnehmergruppe_info")
            zeitstempel = datetime.datetime.now().isoformat()[:19]
            uuid_generieren= uuid.uuid4()
            user_id = f"{zeitstempel}-{uuid_generieren}-{teilnehmergruppe}"
            st.session_state["user_id"]=user_id

        endzeit = datetime.datetime.now()
        startzeit = st.session_state.get("startzeit")
        if startzeit:
            dauerUmfrage = endzeit - startzeit
            dauerUmfrageSekunden = int(dauerUmfrage.total_seconds())
            dauerUmfrageSekunden
        else:
            dauerUmfrageSekunden = ""
        user_data = {
            "teilnehmergruppe": st.session_state.get("teilnehmergruppe_info"),
            "dauerUmfrageSekunden": dauerUmfrageSekunden,
            "Einstiegstumfrage": st.session_state.get("einstiegsumfrage"),
            "Grundwissen_KI": st.session_state.get("grundwissen_ki"),
            "Uebung1": st.session_state.get("uebung1"),
            "Uebung2": st.session_state.get("uebung2"),
            "Uebung3": st.session_state.get("uebung3"),
            "Uebung4": st.session_state.get("uebung4"),
            "Abschlussumfrage": st.session_state.get("abschlussumfrage")
        }
            
        #Hinterher alle Umfrageergebnisse
        try: 
            doc_ref = db.collection(u'users').document(user_id)
            doc_ref.set(user_data)
            st.success("Daten erfolgreich gespeichert!")

        except KeyError as error:
            speicher_fehler_firestore +=1
            st.error("Problem mit der Datenbankkonfiguration. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
        # https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types
        #https://cloud.google.com/firestore/docs/understand-error-codes?hl=de 
        except google_exceptions.ServiceUnavailable as error:
            speicher_fehler_firestore +=1
            st.error("Firestore: Problem mit der Verbindung zur Datenbank. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
            st.info(f"Google-Fehlermeldung: {str(error)}")
        except google_exceptions.DeadlineExceeded as error:
            speicher_fehler_firestore +=1
            st.error("Firestore: Problem mit der Verbindung zur Datenbank. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
            st.info(f"Google-Fehlermeldung: {str(error)}")
        except google_exceptions.ResourceExhausted as error:
            speicher_fehler_firestore +=1
            st.error("Firestore: Zu viele Anfragen. Das Kontingent oder die Rate wurde überschritten. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
            st.info(f"Google-Fehlermeldung: {str(error)}")
        except google_exceptions.NotFound as error:
            speicher_fehler_firestore +=1
            st.error("Firestore:Dokument nicht gefunden. Das gesuchte Dokument existiert nicht in der Datenbank. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
            st.info(f"Google-Fehlermeldung: {str(error)}")
        except google_exceptions.PermissionDenied as error:
            speicher_fehler_firestore +=1
            st.error("Firestore: Zugriff verweigert. Du hast keine Berechtigung für diese Operation. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
            st.info(f"Google-Fehlermeldung: {str(error)}")
        except Exception as error:
            st.error("Firestore: Es gibt ein Problem mit der Datenbank. Bitte melde dich, wenn du die Fehlermeldung siehst")
            st.info(f"Google-Fehlermeldung:{str(error)}")
             speicher_fehler_firestore +=1


        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")

        if not supabase_url or not supabase_key:
            try:

                supabase_url = st.secrets["supabase"]["url"]
                supabase_key = st.secrets["supabase"]["key"]

            except Exception:
                st.error("Keine Supabase-Konfiguration vorhanden.")
                st.stop()
        
        supabase = create_client(supabase_url, supabase_key)

        # Daten für Supabase vorbereiten
        supabase_data = {
            "user_id": user_id,
            "data": user_data
        }
        
        try:   
            # Tabelle in Supabase erstellt mit dem Namen "umfrage_antworten"
            response = supabase.table("umfrage_antworten").insert(supabase_data).execute()
            #st.write("Supabase-Ergebnis:", response) 
            
        #Errorcodes: https://supabase.com/docs/guides/storage/debugging/error-codes

        except Exception as error:
            speicher_fehler_supabase +=1
            error_text = str(error).lower()
                
            if "429" in error_text or "too many requests" in error_text:
                st.error("Supabase: Zu viele Anfragen. Das Kontingent oder die Rate wurde überschritten. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
                st.info(f"Supabase-Fehlermeldung: {str(error)}")
                
                
            elif "544" in error_text or "database_timeout" in error_text:
                st.error("Supabase: Zeitüberschreitung bei der Datenbankverbindung. Bitte versuche es später erneut. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
                st.info(f"Supabase-Fehlermeldung: {str(error)}")
                
                
            elif "500" in error_text or "internal_server_error" in error_text:
                st.error("Supabase: Interner Serverfehler bei Supabase. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
                st.info(f"Supabase-Fehlermeldung: {str(error)}")
                
            elif "403" in error_text or "unauthorized" in error_text:
                st.error("Supabase: Problem mit der Berechtigung. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
                st.info(f"Supabase-Fehlermeldung: {str(error)}")
                
            elif "404" in error_text or "not_found" in error_text:
                st.error("Supabase: Die Datei ist nicht vorhanden oder du hast nicht die Berechtigungen für den Zugriff. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
                st.info(f"Supabase-Fehlermeldung: {str(error)}")
                
            else:
                st.error("Supabase: Es gibt ein Problem mit der Datenbank. Bitte melde dich, wenn du die Fehlermeldung siehst.")
                st.info(f"Supabase-Fehlermeldung: {str(error)}")
    #Wenn es keine Fehler bei der Datenbank gibt, kann die Lerneinheit abgeschlossen werden
    if speicher_fehler_supabase==0 or  speicher_fehler_firestore==0:
        naechste_seite = "pages/9_Abschluss.py"
        st.switch_page(naechste_seite)
