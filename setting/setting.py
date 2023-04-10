
import streamlit as st
class ConstParamatreApplication:
    TERMINAL = "terminale"
    WEB = "streamlit"
    DETECTION_AUTOMATIQUE  = True
    DEBUG = False
    EXPLAIN_WHY = True
    EXPLAIN_WHAT_MODEL = True
    INTERFACE  = WEB
    OPTION_CHOISI = ("distincable","Ordre et nombre de tirage","Entrainement")
    HASART_MAXIMUM = 10
    
    
class VariableObjetStreamlit:
    def __init__(self) -> None:
        self.colonne_gauche,self.colonne_centralle = st.columns(2)
        self.selecte_option_choice = None
        self.Select_box_distingable_type  = None
        self.write_reponse = None
        self.write_model_choix  = None
        self.write_raison_choix  = None
        self.PARTILEMENT = "Partiellement"
        self.TOTALEMENT = "Totalement"
        
        
        
        