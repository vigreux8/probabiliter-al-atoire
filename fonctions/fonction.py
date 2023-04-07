import math
from setting.setting import ConstParamatreApplication



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
    
    def get_resultat(self,valeur):
        self.resultat = valeur

    def p_liste(self):
        self.model_selectionnner = "le model chois est P_liste"
        self.get_resultat(self.cardinale_n**self.nb_tirage_p) 

    def arrangement(self):
        self.model_selectionnner = "le model chois est arrangement"
        dividende = self.factoriels(self.cardinale_n)
        diviseur =  self.factoriels(self.cardinale_n-self.nb_tirage_p)
        self.get_resultat(dividende/diviseur) 
    
    def combinaison(self):
        self.model_selectionnner = "le model chois est combinaison"
        dividende = self.factoriels(self.cardinale_n)
        diviseur = self.factoriels(self.nb_tirage_p)*self.factoriels(self.cardinale_n-self.nb_tirage_p)
        self.get_resultat(dividende/diviseur)
    
    def p_suite(self):
        self.model_selectionnner = "le model chois est p_suite"
        dividende =  self.factoriels(self.cardinale_n+self.nb_tirage_p-1)
        diviseur = self.factoriels(self.nb_tirage_p)*self.factoriels(self.cardinale_n-1)
        self.get_resultat(dividende/diviseur)
    
    def permutation_total(self):
        self.model_selectionnner = "le model chois est permutation total"
        print(self.factoriels(self.cardinale_n))
        self.get_resultat(self.factoriels(self.cardinale_n))
        
        
    def permutation_partiel(self):
        self.model_selectionnner = "le model chois est permutation partiel"
        dividende = self.factoriels(self.cardinale_n)
        diviseur = 1
        for i in self.list_n_permutation_partiel:
            diviseur *= self.factoriels(i)
        self.get_resultat= dividende/diviseur
        
    
   
class Calcule_probabiliter(TypeProbabiliter):
    def __init__(self) -> None:
        self.remise =None
        #distingable prend False = non, 1 = partiellement,2 = distingable
        self.distingable = False
        self.ordre = None
        self.model_selectionnner = None
   
   
    
    def init_get_user_info(self):
        self.distingable =  self.conv_string_true_or_false("o","n","se sont des object distincable O/N : ?") 
        if self.distingable:
            self.distingable =  self.conv_string_true_or_false("t","p","totalement/partiellement ? T/P : ","T","P")
            if self.distingable.lower() == "p":
                nb_n_distingable = int(input("combiens d'élément distingable ? "))
                for i in range(0,nb_n_distingable):
                    self.list_n_permutation_partiel.append(int(input("valeur de n",i)))
        elif self.distingable.lower() =="t":
            pass     
        else:
            self.remise =  self.conv_string_true_or_false("o","n",("Avec remise o/n : "))
            self.ordre =  self.conv_string_true_or_false("o","n",("Avec ordre o/n : "))
            self.cardinale_n= int(input("saisir cardinale(n): "))
            self.nb_tirage_p = int(input("saisir nb_tirage(p): "))
    
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
        
            
    @staticmethod
    def conv_string_true_or_false(Choix_1: str,choix_2: str,input_value: str,Return_1=True,Return_2=False):
        input_value =  input(input_value)
        input_value = input_value.lower()
        if input_value == Choix_1:
            return Return_1
        elif input_value == choix_2:
            return Return_2
    
    def condition_pour_choisir_liste(self):
        #p-liste  remise:True | ordre:True 
        #arrangement remise:False | ordre:True 
        #combinaison remise:False | ordre:False 
        #p-suite : remise:True | ordre:False 
        #permutation distinct : remise: None | ordre:True | distincable : True
        #permutation partiels : remise: None | ordre: None | distincable : False
        if self.remise and self.ordre:
            self.p_liste()
            
        elif  self.remise ==False and self.ordre and self.distingable ==None:
            self.arrangement()
            
        elif not self.remise and not self.ordre and self.distingable ==None:
            self.combinaison()
    
        elif self.remise and not self.ordre and self.distingable ==None:
            self.p_suite()
            
        elif self.distingable == "t":
            self.permutation_total()
            
        elif self.distingable == "p":
            self.permutation_partiel()
    
    
    
       
    def print_resultat(self):
        print("-le model choisi:",self.model_selectionnner,"\n-il y :",self.resultat,"possibilité.")
  
    def run_programme(self):
        if  ConstParamatreApplication.DEBUG:
            self.init_test()
        else : 
            self.init_get_user_info()
            
        self.condition_pour_choisir_liste()
        self.print_resultat()
    