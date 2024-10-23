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
    utilisateur2()
utilisateur()

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



winorlose()




        








