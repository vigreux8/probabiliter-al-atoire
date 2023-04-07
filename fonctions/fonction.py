import math


class Calcule_probabiliter:
    def __init__(self) -> None:
        self.remise =None
        self.ordre = None
        self.cardinale_n = None
        self.nb_tirage = None
        self.resultat = None
    #p-liste  remise:True | ordre:True 
    #arrangement remise:False | ordre:True 
    #combinaison remise:False | ordre:False 
    #p-suite : remise:True | ordre:False 
    #permutation distinct : remise: None | ordre:True | distincable : True
    #permutation partiels : remise: None | ordre: None | distincable : False
    
    def init_get_user_info(self):
        self.remise =  self.conv__string_true_or_false("o","n",int(input("Avec remise o/n"))) 
        self.ordre =  self.conv__string_true_or_false("o","n",int(input("Avec ordre o/n")))
        int(input("saisir cardinale(n): "))
        int(input("saisir nb_tirage(p): "))
        
    @staticmethod
    def conv__string_true_or_false(si_vrais: str,si_non: str,valeur: str):
        valeur = valeur.lower()
        if valeur == si_vrais:
            return True
        elif valeur == si_non:
            return False
        
    def get_resultat(self,valeur):
        self.resultat = valeur
    
    def print_resultat(self):
        print(self.resultat)

    def p_liste(self):
        print("p_list_choisis")
        self.get_resultat(self.cardinale^self.nb_tirage) 
       
    def condition_pour_choisir_liste(self):
        if self.remise and self.cardinale_n:
            self.p_liste()
        
    def run_programme(self):
        self.init_get_user_info()
        self.condition_pour_choisir_liste()
        self.print_resultat()
        