import math
from setting.setting import ConstParamatreApplication,VariableObjetStreamlit
import streamlit as st


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
        self.resultat = valeur

    def p_liste(self):
        self.model_selectionnner = "le model chois est P_liste"
        self.set_resultat(self.cardinale_n**self.nb_tirage_p) 

    def arrangement(self):
        self.model_selectionnner = "le model chois est arrangement"
        dividende = self.factoriels(self.cardinale_n)
        diviseur =  self.factoriels(self.cardinale_n-self.nb_tirage_p)
        self.set_resultat(dividende/diviseur) 
    
    def combinaison(self):
        self.model_selectionnner = "le model chois est combinaison"
        dividende = self.factoriels(self.cardinale_n)
        diviseur = self.factoriels(self.nb_tirage_p)*self.factoriels(self.cardinale_n-self.nb_tirage_p)
        self.set_resultat(dividende/diviseur)
    
    def p_suite(self):
        self.model_selectionnner = "le model chois est p_suite"
        dividende =  self.factoriels(self.cardinale_n+self.nb_tirage_p-1)
        diviseur = self.factoriels(self.nb_tirage_p)*self.factoriels(self.cardinale_n-1)
        self.set_resultat(dividende/diviseur)
    
    def permutation_total(self):
        self.model_selectionnner = "le model chois est permutation total"
        self.set_resultat(self.factoriels(self.cardinale_n))
           
    def permutation_partiel(self):
        self.model_selectionnner = "le model chois est permutation partiel"
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
    def converte_True_False_to_str(variable,message_si_vrais,message_si_faut,si_vrais=True,_si_faut=False):
        if variable == si_vrais:
            return message_si_vrais
            
        if variable == _si_faut:
            return message_si_faut

    @staticmethod
    def conv_string_true_or_false(Choix_1: str,choix_2: str,input_value: str,Return_1=True,Return_2=False):
        input_value =  input(input_value)
        input_value = input_value.lower()
        if input_value == Choix_1:
            if Return_1 ==True:
                return Return_1
            else:
                return Return_1.lower()
        elif input_value == choix_2:
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
              

    def condition_pour_choisir_liste(self):
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
                st.write(f"-le model choisi: {self.model_selectionnner}")
                st.write(f"-il y : {self.resultat} possibilité.")
   
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
                with self.s.colonne_centralle:
                    st.write(self.model_selectionnner)
                    
            
    
    def run_programme(self):
        if  ConstParamatreApplication.DEBUG:
            self.init_test()
        elif ConstParamatreApplication.INTERFACE == ConstParamatreApplication.TERMINAL: 
            self.init_get_user_info()
        elif ConstParamatreApplication.INTERFACE == ConstParamatreApplication.WEB:
            self.init_streamlit()
        self.condition_pour_choisir_liste()
        self.Print_explain_what_model()
        # print()
        self.print_explain_why()
        self.print_resultat()

    def init_streamlit(self):
        with self.s.colonne_gauche:
            self.s.selecte_option_choice = st.selectbox("Options a choisir",("distincable","Ordre et nombre de tirage",))
            if self.s.selecte_option_choice =="distincable":
                self.s.Select_box_distingable_type = st.selectbox("les objet sont distingable :",(f"{self.s.PARTILEMENT}",f"{self.s.TOTALEMENT}"))
                if self.s.Select_box_distingable_type == self.s.PARTILEMENT:
                    self.distingable ="p"
                    nb_n_distingable = st.number_input("Nombre de groupe :",step=1)
                    for i in range(0,nb_n_distingable):
                        self.list_n_permutation_partiel.append(st.number_input(f"nombre d'objet du groupe n{i+1}: ",step=1))
                    self.cardinale_n = sum(self.list_n_permutation_partiel)
                elif self.s.Select_box_distingable_type == self.s.TOTALEMENT:
                    self.distingable ="t"
                    self.cardinale_n =st.number_input("Nombre d'objet au total :",step=1)
                
            elif self.s.selecte_option_choice =="Ordre et nombre de tirage":
                self.remise = st.checkbox("Remise")
                self.ordre= st.checkbox("ordre")
                self.cardinale_n = st.number_input("Nombre d'élement dana la liste (cardinale_n) :",step=1)
                self.nb_tirage_p = st.number_input("Nombre de tirage :",step=1)
        

