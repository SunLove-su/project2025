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
#Ausgabe der Antwort
if antwort_aufmerksamkeit is not None:
    

    st.session_state.abschlussumfrage["aufmerksamkeit"] = {
    "Bereich": "Abschlussumfrage",
    "Typ": "Aufmerksamkeit",
    "Frage":  frage_aufmerksamkeit,
    "Antwort": antwort_aufmerksamkeit
     }
    st.write(f"Deine Antwort ist: {antwort_aufmerksamkeit}")

st.divider()
# IDENTISCHE FRAGE 1: VERTRAUEN
frage_vertrauen_post = "Wie vertrauenswürdig hältst du KI-generierte Inhalte?"
antwort_vertrauen_post = st.radio(frage_vertrauen_post, (
    "Sehr vertrauenswürdig",
    "Eher vertrauenswürdig", 
    "Neutral",
    "Eher nicht vertrauenswürdig",
    "Gar nicht vertrauenswürdig"
), index=None)

if antwort_vertrauen_post is not None:
    st.session_state.abschlussumfrage["vertrauen_post"] = {
        "Bereich": "Abschlussumfrage",
        "Typ": "Vertrauen_Post",
        "Frage": frage_vertrauen_post,
        "Antwort": antwort_vertrauen_post
    }
    st.markdown(f"Deine Antwort: {antwort_vertrauen_post}")

# IDENTISCHE FRAGE 2: ERKENNUNGSFÄHIGKEIT  
frage_erkennung_post = "Wie gut kannst du erkennen, ob ein Text oder Bild von einer KI stammt?"
antwort_erkennung_post = st.radio(frage_erkennung_post, (
    "Sehr gut",
    "Gut",
    "Mittelmäßig",
    "Eher schlecht", 
    "Schlecht"
), index=None)

if antwort_erkennung_post is not None:
    st.session_state.abschlussumfrage["erkennung_post"] = {
        "Bereich": "Abschlussumfrage", 
        "Typ": "Erkennung_Post",
        "Frage": frage_erkennung_post,
        "Antwort": antwort_erkennung_post
    }
    st.markdown(f"Deine Antwort: {antwort_erkennung_post}")

# IDENTISCHE FRAGE 3: PRÜFVERHALTEN
frage_pruefung_post = "Wie genau prüfst du KI-generierte Inhalte, bevor du ihnen vertraust?"
antwort_pruefung_post = st.radio(frage_pruefung_post, (
    "Sehr genau",
    "Eher genau",
    "Manchmal",
    "Eher selten",
    "Gar nicht"
), index=None)

if antwort_pruefung_post is not None:
    st.session_state.abschlussumfrage["pruefung_post"] = {
        "Bereich": "Abschlussumfrage",
        "Typ": "Pruefung_Post", 
        "Frage": frage_pruefung_post,
        "Antwort": antwort_pruefung_post
    }
    st.markdown(f"Deine Antwort: {antwort_pruefung_post}")

st.divider()


#########################
# INFORMATIONEN ÜBER GELERNTES
frage_wissen_gewonnen = "Was hast du in dieser Lerneinheit gelernt?"
wissen_gewonnen = st.multiselect(
                                frage_wissen_gewonnen,
                                ("Wie echt KI-generierte Bilder aussehen können",
                                "Wie ich Stereotype in KI-Antworten erkenne", 
                                "Was KI ist",
                                "Wie ich keine persönlichen Daten in die KI übergebe",
                                "Wie Urheberrechtliche Daten angeblich verwendet werden",
                                "Keine Angabe"),
                                placeholder="Bitte wähle die Themen aus, über die du etwas gelernt hast"
)
#Anpassung, damit die Antworten nicht als Sequenz ausgegeben werden
if wissen_gewonnen:
    antwort_wissen = ", ".join(wissen_gewonnen)
    #Ausgabe der Antwort
    st.session_state.abschlussumfrage["wissen_gewonnen"]={
        "Bereich": "Abschlussumfrage",
        "Typ": "Wissen_gewonnen",
        "Frage":frage_wissen_gewonnen,
        "Antwort":antwort_wissen
    }
    st.markdown(f"Deine Antwort ist: {antwort_wissen}")


st.divider()


# DIREKTE FRAGE ZUR VERBESSERUNG DER ERKENNUNGSFÄHIGKEIT
frage_erkennung_verbessert = "Hat sich deine Fähigkeit, KI-Inhalte zu erkennen, durch die Lerneinheit verbessert?"
antwort_erkennung_verbessert = st.radio(
                       frage_erkennung_verbessert,
                       ("Ja, deutlich verbessert",
                        "Ja, etwas verbessert",
                        "Keine Veränderung",
                        "Nein, gar nicht verbessert"),
                       index=None
)
# Ausgabe der Antwort
if antwort_erkennung_verbessert is not None:

   st.session_state.abschlussumfrage["erkennungsfaehigkeit_verbessert"] = {
   "Bereich": "Abschlussumfrage",
   "Typ": "erkennungsfaehigkeit_verbessert",
   "Frage":   frage_erkennung_verbessert,
   "Antwort": antwort_erkennung_verbessert
    }
   st.markdown(f"Deine Antwort ist: {antwort_erkennung_verbessert}")

st.divider()
##############################

# KI generierte Inhalte hinterfragen?
frage_hinterfragen_ki = "Wirst du KI-generierte Inhalte in Zukunft mehr hinterfragen?"
antworten_hinterfragen_ki = st.radio (
                                frage_hinterfragen_ki,
                                ("Ja, ich werde die Inhalte mehr hinterfragen",
                                "Neutral",
                                "Nein, ich werde die Inhalte nicht mehr hinterfragen"),
                                index=None
)
#Ausgabe der Antwort
if antworten_hinterfragen_ki is not None:
 
    

    st.session_state.abschlussumfrage["hinterfragen"] = {
    "Bereich": "Abschlussumfrage",
    "Typ": "Hinterfragen",
    "Frage":   frage_hinterfragen_ki,
    "Antwort": antworten_hinterfragen_ki
    }
    st.write(f"Deine Antwort ist: {antworten_hinterfragen_ki}")

frage_pruefung = "Wie genau wirst du KI-generierte Inhalte in Zukunft prüfen?"
antwort_pruefung = st.radio(
    frage_pruefung,
    (
        "Sehr genau - ich werde alle Fakten prüfen",
        "Eher genau - ich werde wichtige Behauptungen hinterfragen",
        "Mittel - ich werde manchmal nachprüfen",
        "Eher oberflächlich - ich werde selten nachprüfen",
        "Gar nicht - ich werde den Inhalten vertrauen",
        "Keine Angabe"
    ),
    index=None
)

if antwort_pruefung is not None:
    

    st.session_state.abschlussumfrage["prüfverhalten_nachher"] = {
        "Bereich": "Abschlussumfrage",
        "Typ": "Prüfverhalten Nachher",
        "Frage": frage_pruefung,
        "Antwort": antwort_pruefung
    }
    st.markdown(f"Deine Antwort ist: {antwort_pruefung}")

frage_pruef_strategie = "Welche Strategien wirst du in Zukunft nutzen, um KI-generierte Inhalte kritisch zu bewerten?"
antwort_pruef_strategie = st.multiselect(
    frage_pruef_strategie,
    (
        "Auf KI-Formulierungen achten",
        "Ausgaben gegenprüfen",
        "Auf Stereotypen und Vorurteile achten",
        "Bei Bildern auf unnatürliche Details achten",
        "Nach Quellenangaben suchen",
        "Keine besonderen Strategien",
        "Sonstiges"
    ),
    placeholder="Wähle alle Strategien aus, die du verwenden würdest"
)

if antwort_pruef_strategie:
    antwort_pruef_strategie_alle = ", ".join(antwort_pruef_strategie)
    

    st.session_state.abschlussumfrage["prüfstrategien"] = {
        "Bereich": "Abschlussumfrage",
        "Typ":"Prüfstrategie",
        "Frage": frage_pruef_strategie,
        "Antwort": antwort_pruef_strategie_alle
    }
    st.write(f"Deine Antwort ist: {antwort_pruef_strategie_alle}")
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
st.divider()

#########################
# FEEDBACK ZUM MODUL
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
#Ausgabe der Antwort
if antwort_modul is not None:
    st.session_state.abschlussumfrage["modul_bewertung"] = {
    "Bereich":"Abschlussumfrage",
    "Typ":"Modul Bewertung",
    "Frage":   frage_modul,
    "Antwort": antwort_modul
    }
    st.write(f"Deine Antwort ist: {antwort_modul}")

frage_verbesserung = "Was kann an der Lerneinheit verbessert werden? (optional)"
antwort_verbesserung = st.text_area(frage_verbesserung, height=100)
if antwort_verbesserung:
   
    st.session_state.abschlussumfrage["verbesserung"] = {
    "Bereich": "Abschlussumfrage",
    "Typ": "Verbesserung",
    "Frage":   frage_verbesserung,
    "Antwort": antwort_verbesserung
    }

#############################################
#############################################
#############################################

if st.button("Abschluss"):
    #Anzeigen wie weit der Teilnehmer in der gesamten Lerneinheit ist
    st.markdown("Aktueller Fortschritt in der gesamten Lerneinheit: 7 von 8")
    st.progress (7/8)

    unbeantwortet = False
    if antwort_aufmerksamkeit is None:
        st.error("Bitte beantworte die Frage mit der Aufmerksamkeit.")
        unbeantwortet = True
    if antwort_vertrauen_post is None:
        st.error("Bitte beantworte die Frage zum Vertrauen.")
        unbeantwortet = True
    if antwort_erkennung_post is None:
        st.error("Bitte beantworte die Frage zur Erkennungsfähigkeit.")
        unbeantwortet = True
    if antwort_pruefung_post is None:
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
    if not antwort_pruef_strategie:
        st.error("Bitte gebe deine Prüfstrategien an.")
        unbeantwortet = True
    if antwort_vertrauen is None:
        st.error("Bitte gebe deine Vertrauen in KI an.")
        unbeantwortet = True
    speicher_fehler = 0
    if not unbeantwortet:   
        try:
            
            googlecredentials = json.loads(st.secrets["firestore"]["google_api_key"])
            db=firestore.Client.from_service_account_info(googlecredentials)

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
            except Exception as error:
                speicher_fehler +=1
                st.error("Es gab ein Problem mit der Speicherung der Daten")
                st.info(f"Google-Fehlermeldung:{str(error)}")

        except KeyError as error:
            speicher_fehler +=1
            st.error("Problem mit der Datenbankkonfiguration. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
        # https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/Error-Types
        #https://cloud.google.com/firestore/docs/understand-error-codes?hl=de 
        except google_exceptions.ServiceUnavailable as error:
            speicher_fehler +=1
            st.error("Firestore: Problem mit der Verbindung zur Datenbank. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
            st.info(f"Google-Fehlermeldung: {str(error)}")
        except google_exceptions.DeadlineExceeded as error:
            speicher_fehler +=1
            st.error("Firestore: Problem mit der Verbindung zur Datenbank. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
            st.info(f"Google-Fehlermeldung: {str(error)}")
        except google_exceptions.ResourceExhausted as error:
            speicher_fehler +=1
            st.error("Firestore: Zu viele Anfragen. Das Kontingent oder die Rate wurde überschritten. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
            st.info(f"Google-Fehlermeldung: {str(error)}")
        except google_exceptions.NotFound as error:
            speicher_fehler +=1
            st.error("Firestore:Dokument nicht gefunden. Das gesuchte Dokument existiert nicht in der Datenbank. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
            st.info(f"Google-Fehlermeldung: {str(error)}")
        except google_exceptions.PermissionDenied as error:
            speicher_fehler +=1
            st.error("Firestore: Zugriff verweigert. Du hast keine Berechtigung für diese Operation. Bitte melde dich, wenn du die Fehlermeldung bekommst.")
            st.info(f"Google-Fehlermeldung: {str(error)}")
        except Exception as error:
            st.error("Firestore: Es gibt ein Problem mit der Datenbank. Bitte melde dich, wenn du die Fehlermeldung siehst")
            st.info(f"Google-Fehlermeldung:{str(error)}")
            speicher_fehler +=1

    
        try:
            # Supabase-Client erstellen
            supabase_url = st.secrets["supabase"]["url"]
            supabase_key = st.secrets["supabase"]["key"]
            supabase = create_client(supabase_url, supabase_key)
        
            # Daten für Supabase vorbereiten
            supabase_data = {
                "user_id": user_id,
                "data": user_data
            }
        
            
            # Tabelle in Supabase erstellt mit dem Namen "umfrage_antworten"
            response = supabase.table("umfrage_antworten").insert(supabase_data).execute()
            st.write("Supabase-Ergebnis:", response) 
            
        #Errorcodes: https://supabase.com/docs/guides/storage/debugging/error-codes

        except Exception as error:
            speicher_fehler +=1
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
        if speicher_fehler==0:
            naechste_seite = "pages/9_Abschluss.py"
            st.switch_page(naechste_seite)
        
        

