
def winorlose():
    empty = '_'
    matrice = [
        [empty for i in range(3)],
        [empty for i in range(3)],
        [empty for i in range(3)]
    ]
    for row in matrice:
        for case in row:
            c = 0
            while c < 3:
                if matrice[0][c] == matrice[1][c] == matrice [2][c] == 'x':
                    print("x a gagn")
                    return
                
                if matrice[c] == ['x', 'x','x']:
                    print("x a gagné")
                    return
                c +=1
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

        