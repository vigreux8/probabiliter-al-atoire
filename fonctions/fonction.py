import math
from setting.setting import ConstParamatreApplication,VariableObjetStreamlit
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
            print(diviseur)
        print(dividende/diviseur)
        self.set_resultat(round(dividende/diviseur))
     
class CalculeProbabiliter(TypeProbabiliter):
    def __init__(self) -> None:
        super().__init__()
        self.remise =None
        #distingable prend False = non, 1 = partiellement,2 = distingable
        self.distingable = False
        self.distingable_mot_complet = None
        self.ordre = None
        self.model_selectionnner = None
        self.s = VariableObjetStreamlit()
        self.reponse_utilisateur = True
        self.bool_reponse = None
        
    def init_get_user_info(self):
        self.distingable =  self.conv_string_true_or_false("o","n","se sont des object distincable O/N : ?") 
        if self.distingable:
            self.distingable =  self.conv_string_true_or_false("t","p","la Totaliter/artiellement ? T/P : ","T","P") 
            if self.distingable == "p":
                self.distingable_mot_complet = "partielement"
                nb_n_distingable = int(input("Nombre de groupe : "))
                for i in range(0,nb_n_distingable):
                    self.list_n_permutation_partiel.append(int(input(f"nombre d'objet du groupe n{i+1}: ")))
                self.cardinale_n = sum(self.list_n_permutation_partiel)
            else :
                self.distingable_mot_complet = "totalement"
                self.cardinale_n = int(input("combiens d'élement au totals ? "))   
        else:
            self.remise =  self.conv_string_true_or_false("o","n",("Avec remise o/n : "))
            self.ordre =  self.conv_string_true_or_false("o","n",("Avec ordre o/n : "))
            self.cardinale_n= int(input("saisir cardinale(n): "))
            self.nb_tirage_p = int(input("saisir nb_tirage(p): "))
    
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
    

    def init_test(self):
        print("-------------test_actifs-------------")
        self.distingable = True
        if self.distingable:
            self.distingable = "p"
            self.list_n_permutation_partiel = [3,4,2]
            self.cardinale_n = sum(self.list_n_permutation_partiel)
            
        else:
            self.remise = True
            self.ordre = False
            self.nb_tirage_p = 3
            self.cardinale_n = 9
    
    def init_variable_globale_streamlite(self):
        if "reponse" not in st.session_state:
            st.session_state.reponse =  int(self.resultat)      

    def mise_a_jour_resultat(self):
        st.session_state.reponse =  int(self.resultat)
        st.session_state.model = self.model_selectionnner
    
    def affichage_reponse(self):
        st.write(st.session_state.reponse)
        
    
    def get_resultat_et_choisis_liste(self):
        #p-liste  remise:True | ordre:True 
        #arrangement remise:False | ordre:True 
        #combinaison remise:False | ordre:False 
        #p-suite : remise:True | ordre:False 
        #permutation distinct : remise: None | ordre:True | distincable : True
        #permutation partiels : remise: None | ordre: None | distincable : False
        if self.remise and self.ordre and self.distingable ==False:
            self.p_liste()
            
        elif  self.remise ==False and self.ordre and self.distingable ==False:
            self.arrangement()
            
        elif not self.remise and not self.ordre and self.distingable ==False:
            self.combinaison()
    
        elif self.remise and not self.ordre and self.distingable ==False:
            self.p_suite()
            
        elif self.distingable == "t":
            self.permutation_total()
            
        elif self.distingable == "p":
            self.permutation_partiel()

    def print_resultat(self):
        if ConstParamatreApplication.INTERFACE == ConstParamatreApplication.TERMINAL:
            print("-le model choisi:",self.model_selectionnner,"\n-il y :",self.resultat,"possibilité.")
        elif ConstParamatreApplication.INTERFACE == ConstParamatreApplication.WEB:
            with self.s.colonne_centralle:
                texte = f"-le model choisi: {self.model_selectionnner}"
                texte_html = re.sub(f'({self.model_selectionnner})', r'<span style="background-color: blue;">\1</span>', texte)
                st.write(texte_html, unsafe_allow_html=True)
                st.write(f"-il y : {self.resultat} possibilité.")
                if self.distingable =="p":
                    st.write(f"-la taille du groupe et de : {sum(self.list_n_permutation_partiel)}")
    
    def print_past_resultat(self):
        st.session_state
                 
    def print_explain_why(self):
        if ConstParamatreApplication.EXPLAIN_WHY:
            if self.distingable :
                print(f"_____pourquoi se choix ?______ \n les element sont distingable {self.distingable_mot_complet} les formule comprenne que la cardinaliter")
            else:
                remise=  self.converte_True_False_to_str(self.remise,"oui","non")
                ordre = self.converte_True_False_to_str(self.ordre,"oui","non")
                
                print(f"_____pourquoi se choix ?_____ \n-les element ne sont pas ditingable la remise et importante \n-remise = {remise} \n-l'ordre = {ordre}")
        
    def Print_explain_what_model(self):
        if ConstParamatreApplication.EXPLAIN_WHAT_MODEL:
            if ConstParamatreApplication.INTERFACE == ConstParamatreApplication.TERMINAL:
                print("_____pourquoi se model a était choisi :____")
                print(self.model_selectionnner ) 
            elif ConstParamatreApplication.INTERFACE == ConstParamatreApplication.WEB:
                pass
    
    def run_programme(self):
        if  ConstParamatreApplication.DEBUG:
            self.init_test()
        elif ConstParamatreApplication.INTERFACE == ConstParamatreApplication.TERMINAL: 
            self.init_get_user_info()
        elif ConstParamatreApplication.INTERFACE == ConstParamatreApplication.WEB:
            self.streamlit_choice_who_app_use()
        if not self.s.selecte_option_choice == ConstParamatreApplication.OPTION_CHOISI[2]:
            self.get_resultat_et_choisis_liste()
            self.streamlit_avertissement()
            self.Print_explain_what_model()
            self.print_explain_why()
            self.print_resultat()
        else:
            self.selection_aléatoire()
            self.get_resultat_et_choisis_liste()
            self.init_variable_globale_streamlite()
            self.streamlit_affichage_detaile()
            self.get_reponse_utilisateur()
            
    def streamlit_avertissement(self):
        with self.s.colonne_centralle:
                if not self.remise and not self.distingable :
                    st.write("<p style='color: red; font-weight: bold;'>nombre d'élement ne peut être supérieur au tirage !</p>", unsafe_allow_html=True)
            
    def streamlit_choice_who_app_use(self):
        with self.s.colonne_gauche:
            self.s.selecte_option_choice = st.selectbox("Options a choisir",ConstParamatreApplication.OPTION_CHOISI)
            if self.s.selecte_option_choice ==ConstParamatreApplication.OPTION_CHOISI[0]:
                if "reponse" in st.session_state:
                    self.del_save_varaible()
                self.streamlit_app_distingable()
                
            elif self.s.selecte_option_choice ==ConstParamatreApplication.OPTION_CHOISI[1]:
                if "reponse" in st.session_state:
                    self.del_save_varaible()
                self.streamlit_app_ordre_and_tirage()
            elif self.s.selecte_option_choice ==ConstParamatreApplication.OPTION_CHOISI[2]:
                self.Streamlit_app_entrainement()
                 
    def streamlit_affichage_detaile(self):
        with self.s.colonne_gauche:
            if self.distingable == False:
                st.write(f"remise : {self.converte_True_False_to_str(self.remise,'oui','non')}")
                st.write(f"ordre : {self.converte_True_False_to_str(self.ordre,'oui','non')}")
                st.write(f"distingable : non")
                st.write(f"nombre de tirage : {self.nb_tirage_p}")
                st.write(f"taille de la liste : {self.cardinale_n}")
                
            if self.distingable != False:
                st.write(f"remise : non")
                st.write(f"ordre :  non")
                st.write(f"distingable : {self.converte_True_False_to_str(self.distingable, si_vrais='t',si_faut='p',message_si_vrais= 'totalement',message_si_faut='partiellement')}")
                if self.distingable =="t":
                    st.write(f"taille du groupe : {self.cardinale_n}")
                # elif self.distingable =="p":
                #     st.write(f"taille total : {sum(self.list_n_permutation_partiel)}")
                    
            if self.distingable =="p":
                st.write(f"nombre de groupe distingable: {len(self.list_n_permutation_partiel)}")
                st.write(f"nombre de personne par groupe : {self.list_n_permutation_partiel}")  
    
    def del_save_varaible(self):
        del st.session_state.reponse
    def streamlit_app_distingable(self):
        with self.s.colonne_gauche:
                self.s.Select_box_distingable_type = st.selectbox("les objet sont distingable :",(f"{self.s.PARTILEMENT}",f"{self.s.TOTALEMENT}"))
                if self.s.Select_box_distingable_type == self.s.PARTILEMENT:
                    self.distingable ="p"
                    nb_n_distingable = st.number_input("Nombre de groupe :",step=1,min_value=2)
                    for i in range(0,nb_n_distingable):
                        self.list_n_permutation_partiel.append(st.number_input(f"nombre d'objet du groupe n{i+1}: ",step=1))
                    self.cardinale_n = sum(self.list_n_permutation_partiel)
                elif self.s.Select_box_distingable_type == self.s.TOTALEMENT:
                    self.distingable ="t"
                    self.cardinale_n =st.number_input("Nombre d'objet au total :",step=1,min_value=1)
    def streamlit_app_ordre_and_tirage(self):
        with self.s.colonne_gauche:
            self.remise = st.checkbox("Remise")
            self.ordre= st.checkbox("ordre")
            self.cardinale_n = st.number_input("Nombre d'élement dans la liste (cardinale_n) :",step=1,min_value=1)
            if not self.remise :
                self.nb_tirage_p = st.number_input("Nombre de tirage :",step=1,min_value=1,max_value=self.cardinale_n)
            else:
                self.nb_tirage_p = st.number_input("Nombre de tirage :",step=1,min_value=1)
    
    def Streamlit_app_entrainement(self):
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
        with self.s.colonne_centralle:
            st.write("Calculer le résultat :")
    
    def selection_aléatoire(self):
        """
        si la premier condition et respect on part sur :
            -distingable
        sinon :
            -ordre et remise
        """
        if self.random_1_ou_2():
            self.remise = self.random_1_ou_2()
            self.ordre = self.random_1_ou_2()
            print(self.remise)
            if not self.remise:
                self.cardinale_n = random.randint(1,ConstParamatreApplication.HASART_MAXIMUM)
                self.nb_tirage_p = random.randint(1,self.cardinale_n+1)
            else:
                self.cardinale_n = random.randint(1,ConstParamatreApplication.HASART_MAXIMUM)
                self.nb_tirage_p = random.randint(1,ConstParamatreApplication.HASART_MAXIMUM)
                
        else:
            self.distingable = self.random_1_ou_2("t","p")
            if self.distingable =="t":
                self.cardinale_n = random.randint(1,ConstParamatreApplication.HASART_MAXIMUM)
            elif self.distingable =="p":
                for i in range(0,random.randint(1,6)):
                    self.list_n_permutation_partiel.append(random.randint(1,5))
                self.cardinale_n = sum(self.list_n_permutation_partiel)
    
    def get_reponse_utilisateur(self):
        with self.s.colonne_centralle:
            if self.reponse_utilisateur:
                nombre = st.number_input("saisir le nombre de possibiliter",step=1,value=0)
                if st.button("valider la réponse") :
                    self.reponse_utilisateur = nombre
                    print("reponse utilisateur : ",self.reponse_utilisateur )
                    print("resultat : ", st.session_state.reponse)
                    print("condition : ", self.reponse_utilisateur == st.session_state.reponse)
                    if self.reponse_utilisateur == st.session_state.reponse:
                            st.write("reponse correcte")
                            self.mise_a_jour_resultat()
                            self.print_resultat()
                            
                    else:
                            st.write("reponse incorrect")
                            self.mise_a_jour_resultat()
                            self.print_resultat()
                            

        pass
    
    @staticmethod
    def random_1_ou_2(si_vraie=True,si_faut=False):
        if random.randint(0,2) == 0:
            return si_vraie
        else:
            return si_faut
        
        
        
