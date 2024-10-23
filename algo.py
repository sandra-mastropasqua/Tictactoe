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
                    print("x a gagn")  
                if matrice[c] == ['x','x','x']:
                    print("x a gagné")
                if matrice[0][c] == matrice[1][c] == matrice [2][c] == "o":
                    print("o a gagné")
                if matrice[c] == ["o","o","o"] :
                    print("O a gagné")
                
                    return
                c +=1

            ligne = int(input("quel rang voulez vous jouer ?"))
            col = int(input("dans quelle colonne"))

            matrice[ligne][col] = 'x'
            print("_____"*5)
            print("|"+"___"+f"{matrice[0][0]}"+"___"+"|"+"___"+f"{matrice[0][1]}"+"___"+"|"+"___"+f"{matrice[0][2]}"+"___"+"|")
            print("|"+"___"+f"{matrice[1][0]}"+"___"+"|"+"___"+f"{matrice[1][1]}"+"___"+"|"+"___"+f"{matrice[1][2]}"+"___"+"|")
            print("|"+"___"+f"{matrice[2][0]}"+"___"+"|"+"___"+f"{matrice[2][1]}"+"___"+"|"+"___"+f"{matrice[2][2]}"+"___"+"|")

        if matrice [0][0] == matrice [1][1] == matrice [2][2] 
        == "x":
            print("Le joueur X a gagné")
        if matrice [0][2] == matrice [1][1] == matrice [2][0] == "x":
            print("Le joueur X a gagné")

        if matrice [0][0] == matrice [1][1] == matrice [2][2] == "o":
            print("Le joueur O a gagné")
        if matrice [0][0] == matrice [1][1] == matrice [2][2] == "o":
            print("Le joueur O a gagné")
