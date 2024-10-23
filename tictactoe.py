from algo import *

def utilisateur():
    symbole = ""
    X = ''
    O = ''
    while symbole == X and symbole == O :
        symbole = input("Choisissez joueur 1 votre symbole: ")
    def utilisateur2():
        symbole_joueur2 = ''
        X = ''
        O = ''
        while symbole_joueur2 == X and symbole_joueur2 == O :
            symbole_joueur2 = input(f"Choisissez joueur 2 votre symbole: ")
            if symbole_joueur2 == symbole :
                print(f"Le joueur 1 a deja choisis {symbole}. Choisissez l'autre symbole.")
        return symbole_joueur2




winorlose()








