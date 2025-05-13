import streamlit as st
import json
from supabase import create_client

def save_data_to_supabase(user_data, user_id):
    """Speichert Daten in Supabase als zusätzliche Backup-Datenbank"""
    
    success = False
    error_message = None
    
    try:
        # Supabase-Client erstellen
        supabase_url = st.secrets["supabase"]["url"]
        supabase_key = st.secrets["supabase"]["key"]
        supabase = create_client(supabase_url, supabase_key)
        
        # Daten vorbereiten - user_id und data als JSON
        supabase_data = {
            "user_id": user_id,
            "data": user_data
        }
        
        # In Supabase speichern
        #Tabelle Lokal in Supabase erstellt mit den Namen "umfrage_antworten"
        response = supabase.table("umfrage_antworten").insert(supabase_data).execute()
      
        
