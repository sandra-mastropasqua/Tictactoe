def winorlose():
    empty = ' '
    matrice = [
        [empty for i in range(3)],
        [empty for i in range(3)],
        [empty for i in range(3)]
    ]
    counter = 0
    
    player = input('quel signe voulez vous jouer en premier')
    for row in matrice:
        for case in row:
            c = 0
            while c < 3:
                if matrice[0][c] == matrice[1][c] == matrice [2][c] == "X":
                    print("X a gagn")
                    return
                if matrice[c] == ['X','X','X']:
                    print("X a gagné")
                    return
                if matrice[0][c] == matrice[1][c] == matrice [2][c] == "O":
                    print("0 a gagné")
                    return
                if matrice[c] == ["O","O","O"] :
                    print("O a gagné")
                    return
                c +=1
            ligne = int(input("quel rang voulez vous jouer ?"))
            col = int(input("dans quelle colonne"))

            mystr = ''.join(matrice[0] + matrice[1] + matrice[2])
            counterx = mystr.count('X')
            countero = mystr.count('O')
            if matrice[ligne][col] != empty:
                print('case déjà utilisée')
                continue
            def playerx():
                if counterx == countero:
                    matrice[ligne][col] = 'X'
                elif counterx > countero:
                    matrice[ligne][col] = 'O'
            def playero():
                if countero == counterx:
                    matrice[ligne][col] = 'O'
                elif counterx < countero:
                    matrice[ligne][col] = 'X'
            if player == 'x':
                playerx()
            elif player == 'o':
                playero()
            else : return
            
        
            print("_____"*5)
            print("|"+"   "+f"{matrice[0][0]}"+"   "+"|"+"   "+f"{matrice[0][1]}"+"   "+"|"+"   "+f"{matrice[0][2]}"+"   "+"|")
            print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
            print("|"+"   "+f"{matrice[1][0]}"+"   "+"|"+"   "+f"{matrice[1][1]}"+"   "+"|"+"   "+f"{matrice[1][2]}"+"   "+"|")
            print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
            print("|"+"   "+f"{matrice[2][0]}"+"   "+"|"+"   "+f"{matrice[2][1]}"+"   "+"|"+"   "+f"{matrice[2][2]}"+"   "+"|")
            print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")