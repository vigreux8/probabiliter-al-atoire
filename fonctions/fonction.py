import math
from setting.setting import ConstParamatreApplication 
import streamlit as st
import re
from numpy import random

#demander si le paramétre et distinc partiellement disting si oui allez passer la demande si répétition et nombre de répétitions
# class DebugTest:
#     #toute les fonctione pour debug et tester


    
class CalculculeMathematique:
    
    @staticmethod
    def factoriels(n):
        if n == 0:
            return 1
        else:
           return n*CalculculeMathematique.factoriels(n-1)

class TypeProbabiliter(CalculculeMathematique):
    def __init__(self) -> None:
        super().__init__()
        self.cardinale_n = None
        self.nb_tirage_p = None
        self.resultat = None
        self.list_n_permutation_partiel = []
    
    def set_resultat(self,valeur):
        self.resultat = int(valeur)

    def p_liste(self):
        self.model_selectionnner = "P_liste"
        self.set_resultat(self.cardinale_n**self.nb_tirage_p) 

    def arrangement(self):
        self.model_selectionnner = "arrangement"
        dividende = self.factoriels(self.cardinale_n)
        diviseur =  self.factoriels(self.cardinale_n-self.nb_tirage_p)
        self.set_resultat(dividende/diviseur) 
    
    def combinaison(self):
        self.model_selectionnner = "combinaison"
        dividende = self.factoriels(self.cardinale_n)
        diviseur = self.factoriels(self.nb_tirage_p)*self.factoriels(self.cardinale_n-self.nb_tirage_p)
        self.set_resultat(dividende/diviseur)
    
    def p_suite(self):
        self.model_selectionnner = "P_suite"
        dividende =  self.factoriels(self.cardinale_n+self.nb_tirage_p-1)
        diviseur = self.factoriels(self.nb_tirage_p)*self.factoriels(self.cardinale_n-1)
        self.set_resultat(dividende/diviseur)
    
    def permutation_total(self):
        self.model_selectionnner = "permutation total"
        self.set_resultat(self.factoriels(self.cardinale_n))
           
    def permutation_partiel(self):
        self.model_selectionnner = "permutation partiel"
        dividende = self.factoriels(self.cardinale_n)
        diviseur = 1
        for i in self.list_n_permutation_partiel:
            diviseur *= self.factoriels(i)
        self.set_resultat(round(dividende/diviseur))

class WhatModelCalculeProbabiliter(TypeProbabiliter):
    #distingable prend False = non, 1 = partiellement,2 = distingable
    def __init__(self) -> None:
        super().__init__()
        self.bool_remise =None
        self.distingable = False
        self.distingable_mot_complet = None
        self.bool_distingable = None
        self.bool_ordre = None
        self.model_selectionnner = None
        self.reponse_utilisateur = None
        
    @staticmethod
    def converte_True_False_to_str(variable,message_si_vrais,message_si_faut,si_vrais=True,si_faut=False):
        if variable == si_vrais:
            return message_si_vrais
            
        if variable == si_faut:
            return message_si_faut

    @staticmethod
    def conv_string_true_or_false(condition_1: str,condition_2: str,input_value: str,Return_1=True,Return_2=False):
        input_value =  input(input_value)
        input_value = input_value.lower()
        if input_value == condition_1:
            if Return_1 ==True:
                return Return_1
            else:
                return Return_1.lower()
        elif input_value == condition_2:
            if  Return_2 == False:
                return Return_2
            else:
                return Return_2.lower()           
    
    def calcule_resultat(self):
        #p-liste  remise:True | ordre:True 
        #arrangement remise:False | ordre:True 
        #combinaison remise:False | ordre:False 
        #p-suite : remise:True | ordre:False 
        #permutation distinct : remise: None | ordre:True | distincable : True
        #permutation partiels : remise: None | ordre: None | distincable : False
        if self.bool_remise and self.bool_ordre and self.distingable ==False:
            self.p_liste()
            
        elif  self.bool_remise ==False and self.bool_ordre and self.distingable ==False:
            self.arrangement()
            
        elif not self.bool_remise and not self.bool_ordre and self.distingable ==False:
            self.combinaison()
    
        elif self.bool_remise and not self.bool_ordre and self.distingable ==False:
            self.p_suite()
            
        elif self.distingable == "t":
            self.permutation_total()
            
        elif self.distingable == "p":
            self.permutation_partiel()
  
    def set_random_parametre(self):
        """
        si la premier condition et respect on part sur :
            -distingable
        sinon :
            -ordre et remise
        """
        if self.random_1_ou_2():
            self.bool_distingable = False
            self.bool_remise = self.random_1_ou_2()
            self.bool_ordre = self.random_1_ou_2()
            print(self.bool_remise)
            if not self.bool_remise:
                self.cardinale_n = random.randint(1,ConstParamatreApplication.HASART_MAXIMUM)
                self.nb_tirage_p = random.randint(1,self.cardinale_n+1)
            else:
                self.cardinale_n = random.randint(1,ConstParamatreApplication.HASART_MAXIMUM)
                self.nb_tirage_p = random.randint(1,ConstParamatreApplication.HASART_MAXIMUM)
                
        else:
            self.bool_distingable= True
            self.bool_remise = False
            self.bool_ordre = False
            self.distingable = self.random_1_ou_2("t","p")
            if self.distingable =="t":
                self.cardinale_n = random.randint(1,ConstParamatreApplication.HASART_MAXIMUM)
            elif self.distingable =="p":
                for i in range(0,random.randint(1,6)):
                    self.list_n_permutation_partiel.append(random.randint(1,5))
                self.cardinale_n = sum(self.list_n_permutation_partiel)
    
    
        pass
    
    def bool_resultat_vs_utilisateur(self):
        return st.session_state.reponse == self.reponse_utilisateur

    @staticmethod
    def random_1_ou_2(si_vraie=True,si_faut=False):
        if random.randint(0,2) == 0:
            return si_vraie
        else:
            return si_faut


class UsingTerminal(WhatModelCalculeProbabiliter):
    """
    EN TRAVAUX La classe ne fonctionnne pas
    """
    def __init__(self) -> None:
        pass
    def terminal_resultat(self):
        print("-le model choisi:",self.model_selectionnner,"\n-il y :",self.resultat,"possibilité.")
                         
    def terminal_explain_why(self):
        if ConstParamatreApplication.EXPLAIN_WHY:
            if self.distingable :
                print(f"_____pourquoi se choix ?______ \n les element sont distingable {self.distingable_mot_complet} les formule comprenne que la cardinaliter")
            else:
                remise=  self.converte_True_False_to_str(self.bool_remise,"oui","non")
                ordre = self.converte_True_False_to_str(self.bool_ordre,"oui","non")
                
                print(f"_____pourquoi se choix ?_____ \n-les element ne sont pas ditingable la remise et importante \n-remise = {remise} \n-l'ordre = {ordre}")
        
    def terminale_explain_what_model(self):
        if ConstParamatreApplication.EXPLAIN_WHAT_MODEL:
            print("_____pourquoi se model a était choisi :____")
            print(self.model_selectionnner ) 

class UsingStreamlit(WhatModelCalculeProbabiliter):
    def __init__(self) -> None:
        super().__init__()
        self.colonne_gauche,self.colonne_centralle = st.columns(2)
        self.selecte_option_choice = None
        self.Select_box_distingable_type  = None
        self.write_reponse = None
        self.write_model_choix  = None
        self.write_raison_choix  = None
        self.PARTILEMENT = "Partiellement"
        self.TOTALEMENT = "Totalement"
        
    def display_streamlit_resultat(self):
        with self.colonne_centralle:
                texte = f"-le model choisi: {self.model_selectionnner}"
                texte_html = re.sub(f'({self.model_selectionnner})', r'<span style="background-color: blue;">\1</span>', texte)
                st.write(texte_html, unsafe_allow_html=True)
                st.write(f"-il y : {self.resultat} possibilité.")
                if self.distingable =="p":
                    st.write(f"-la taille du groupe et de : {sum(self.list_n_permutation_partiel)}")
    
    def display_streamlit_avertissement(self):
        with self.colonne_centralle:
            if not self.bool_remise and not self.bool_distingable :
                st.write("<p style='color: red; font-weight: bold;'>nombre d'élement ne peut être supérieur au tirage !</p>", unsafe_allow_html=True)
    
    def display_streamlit_information(self):
        with self.colonne_gauche:
            if self.distingable == False:
                st.write(f"remise : {self.converte_True_False_to_str(self.bool_remise,'oui','non')}")
                st.write(f"ordre : {self.converte_True_False_to_str(self.bool_ordre,'oui','non')}")
                st.write(f"distingable : non")
                st.write(f"nombre de tirage : {self.nb_tirage_p}")
                st.write(f"taille de la liste : {self.cardinale_n}")
                
            if self.distingable != False:
                st.write(f"remise : non")
                st.write(f"ordre :  non")
                st.write(f"distingable : {self.converte_True_False_to_str(self.distingable, si_vrais='t',si_faut='p',message_si_vrais= 'totalement',message_si_faut='partiellement')}")
                if self.distingable =="t":
                    st.write(f"taille du groupe : {self.cardinale_n}")
                elif self.distingable =="p":
                    #  st.write(f"taille total : {sum(self.list_n_permutation_partiel)}")
                    pass
                    
            if self.distingable =="p":
                st.write(f"nombre de groupe distingable: {len(self.list_n_permutation_partiel)}")
                st.write(f"nombre de personne par groupe : {self.list_n_permutation_partiel}") 
                pass
      
    def what_streamlit_app_choice(self):
        with self.colonne_gauche:
            selecte_option_choice = st.selectbox("Options a choisir",ConstParamatreApplication.OPTION_CHOISI)
            if selecte_option_choice ==ConstParamatreApplication.OPTION_CHOISI[0]:
                self.app_streamlit__distingable()
                self.display_calculator()
                  
            elif selecte_option_choice ==ConstParamatreApplication.OPTION_CHOISI[1]:
                self.app_streamlit_ordre_and_tirage()
                self.display_streamlit_avertissement()
                self.display_calculator()
                
            elif selecte_option_choice ==ConstParamatreApplication.OPTION_CHOISI[2]:
                self.app_Streamlit_entrainement()
                
    
    def display_calculator(self):
        self.calcule_resultat()
        self.display_streamlit_resultat()
                
    def app_streamlit__distingable(self):
        with self.colonne_gauche:
            Select_box_distingable_type =st.selectbox("les objet sont distingable :",("PARTIELEMENT","TOTALEMENT"))
            if Select_box_distingable_type == "PARTIELEMENT":
                self.distingable ="p"
                nb_n_distingable = st.number_input("Nombre de groupe :",step=1,min_value=2)
                for i in range(0,nb_n_distingable):
                    self.list_n_permutation_partiel.append(st.number_input(f"nombre d'objet du groupe n{i+1}: ",step=1))
                self.cardinale_n = sum(self.list_n_permutation_partiel)
            elif Select_box_distingable_type == "TOTALEMENT":
                self.distingable ="t"
                self.cardinale_n =st.number_input("Nombre d'objet au total :",step=1,min_value=1)
         
    def app_streamlit_ordre_and_tirage(self):
        with self.colonne_gauche:
            self.bool_remise = st.checkbox("Remise")
            self.bool_ordre= st.checkbox("ordre")
            self.cardinale_n = st.number_input("Nombre d'élement dans la liste (cardinale_n) :",step=1,min_value=1)
            if not self.bool_remise :
                self.nb_tirage_p = st.number_input("Nombre de tirage :",step=1,min_value=1,max_value=self.cardinale_n)
            else:
                self.nb_tirage_p = st.number_input("Nombre de tirage :",step=1,min_value=1)
                    
    def app_Streamlit_entrainement(self):
        """
        Detaille du jeux 
        selectionne des valeurs aléatoires 
            -remise  true / false
            -ordre   true / false
            -distingable
                -partiel
                -Total
            me donne les parametre 
            demande la réponse 
            compare la réponse
        """
        with self.colonne_centralle:
            st.write("Calculer le résultat :")
            self.set_random_parametre()
            self.calcule_resultat()
            self.display_streamlit_information()
            self.get_reponse_utilisateur_streamlit()
            
            
    def get_reponse_utilisateur_streamlit(self):
        with self.colonne_centralle:
                st.button("générer")
                with st.expander(f"afficher la réponse"):
                    st.write(f"le model chois est : {self.model_selectionnner}")
                    st.write(f"la réponse est : {self.resultat}")
                    
                    
 
    def run_streamlit(self):
        self.what_streamlit_app_choice()                    
                                
                            
    
class run_programme:
    def __init__(self) -> None:
        self.terminale = UsingTerminal()
        self.streamlit = UsingStreamlit()
        
    def run_streamlit(self):
        self.streamlit.run_streamlit()
    