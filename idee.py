


a=0
b=1
c=2
d=3
e=4
f=5
g=6
h=7
i=8
print("_____"*5)
print("|"+"___"+f"{a}"+"___"+"|"+"___"+f"{b}"+"___"+"|"+"___"+f"{c}"+"___"+"|")
print("|"+"___"+f"{d}"+"___"+"|"+"___"+f"{e}"+"___"+"|"+"___"+f"{f}"+"___"+"|")
print("|"+"___"+f"{g}"+"___"+"|"+"___"+f"{h}"+"___"+"|"+"___"+f"{i}"+"___"+"|")

from truc2 import *
 if matrice[0][c] == matrice[1][c] == matrice [2][c] == symbo:
                    print("o a gagné")


symbole = 'X'
symbole_joueur2 = 'O'
def utilisateur():
    X = ''
    O = ''
    while symbole == X and symbole == O :
        symbole = input("Choisissez joueur 1 votre symbole: ")
    def utilisateur2():
        X = ''
        O = ''
        while symbole_joueur2 == X and symbole_joueur2 == O :
            symbole_joueur2 = input(f"Choisissez joueur 2 votre symbole: ")
            if symbole_joueur2 == symbole :
                print(f"Le joueur 1 a deja choisis {symbole}. Choisissez l'autre symbole.")
        return symbole_joueur2
    utilisateur2()
utilisateur()