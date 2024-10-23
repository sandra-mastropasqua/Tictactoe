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

def winorlose():
    empty = '_'
    matrice = [
        [empty for i in range(3)],
        [empty for i in range(3)],
        [empty for i in range(3)]
    ]
    counter = 0
    
    for row in matrice:
        for case in row:
            c = 0
            while c < 3:
                if matrice[0][c] == matrice[1][c] == matrice [2][c] == "x":
                    print("x a gagné")  
                    return
                if matrice[c] == ['x','x','x'] :
                    print("x a gagné")
                    return
                if matrice[0][c] == matrice[1][c] == matrice [2][c] == "o":
                    print("o a gagné")
                    return
                if matrice[c] == ["o","o","o"] :
                    print("O a gagné")
                    return
                c +=1
            if matrice [0][0] == matrice [1][1] == matrice [2][2] == "x":
                print("Le joueur X a gagné")
                return
            if matrice [0][2] == matrice [1][1] == matrice [2][0] == "x":
                print("Le joueur X a gagné")
                return

            if matrice [0][0] == matrice [1][1] == matrice [2][2] == "o":
                print("Le joueur O a gagné")
                return
            if matrice [0][2] == matrice [1][1] == matrice [2][0] == "o":
                print("Le joueur O a gagné")
                return
            ligne = int(input("quel rang voulez vous jouer ?"))
            col = int(input("dans quelle colonne"))
            mystr = ''.join(matrice[0] + matrice[1] + matrice[2])
            counterx = mystr.count('x')
            countero = mystr.count('o')
            if counterx == countero:
                matrice[ligne][col] = 'x'
            elif counterx > countero:
                matrice[ligne][col] = 'o'
            
            print("_____"*5)
            print("|"+"___"+f"{matrice[0][0]}"+"___"+"|"+"___"+f"{matrice[0][1]}"+"___"+"|"+"___"+f"{matrice[0][2]}"+"___"+"|")
            print("|"+"___"+f"{matrice[1][0]}"+"___"+"|"+"___"+f"{matrice[1][1]}"+"___"+"|"+"___"+f"{matrice[1][2]}"+"___"+"|")
            print("|"+"___"+f"{matrice[2][0]}"+"___"+"|"+"___"+f"{matrice[2][1]}"+"___"+"|"+"___"+f"{matrice[2][2]}"+"___"+"|")
winorlose()
        
