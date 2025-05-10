import inspect
import openai
from google.api_core import exceptions as gexc
import streamlit as st

def list_errors(module):
    return sorted(
        n for n, _ in inspect.getmembers(module)
        if n.endswith("Error") or (n[0].isupper() and "Error" in n)
    )

print("OpenAI  :", list_errors(openai))
print("Firestore:", list_errors(gexc))
print("Streamlit:", list_errors(st.errors))