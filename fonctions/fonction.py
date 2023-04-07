import math
from setting.setting import ConstParamatreApplication

# class DebugTest:
#     #toute les fonctione pour debug et tester

class TypeProbabiliter:
    def p_liste(self):
        self.model_selectionnner = "le model chois est P_liste"
        self.get_resultat(self.cardinale_n**self.nb_tirage) 
       
class Calcule_probabiliter(TypeProbabiliter):
    def __init__(self) -> None:
        self.remise =None
        self.ordre = None
        self.cardinale_n = None
        self.nb_tirage = None
        self.resultat = None
        self.model_selectionnner = None
    #p-liste  remise:True | ordre:True 
    #arrangement remise:False | ordre:True 
    #combinaison remise:False | ordre:False 
    #p-suite : remise:True | ordre:False 
    #permutation distinct : remise: None | ordre:True | distincable : True
    #permutation partiels : remise: None | ordre: None | distincable : False
    
    def init_get_user_info(self):
        self.remise =  self.conv__string_true_or_false("o","n",(input("Avec remise o/n : "))) 
        self.ordre =  self.conv__string_true_or_false("o","n",(input("Avec ordre o/n : ")))
        self.cardinale_n= int(input("saisir cardinale(n): "))
        self.nb_tirage = int(input("saisir nb_tirage(p): "))
        
    def init_test(self):
        print("-------------test_actifs-------------")
        self.remise = True
        self.ordre = True
        self.cardinale_n = 5
        self.nb_tirage = 3
            
    @staticmethod
    def conv__string_true_or_false(si_vrais: str,si_non: str,valeur: str):
        valeur = valeur.lower()
        if valeur == si_vrais:
            return True
        elif valeur == si_non:
            return False
        
    def get_resultat(self,valeur):
        self.resultat = valeur
    
    def condition_pour_choisir_liste(self):
        if self.remise and self.ordre:
            self.p_liste()
    
    def print_resultat(self):
        print("-le model choisi:",self.model_selectionnner,"\n-il y :",self.resultat,"possibilité.")
  
    def run_programme(self):
        if  ConstParamatreApplication.DEBUG:
            self.init_test()
        else : 
            self.init_get_user_info()
            
        self.condition_pour_choisir_liste()
        self.print_resultat()
    
