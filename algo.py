def winorlose():
    empty = ' '
    matrice = [
        [empty for i in range(3)],
        [empty for i in range(3)],
        [empty for i in range(3)]
    ]
    counter = 0
    print("Bienvenue dans le tictactoe de Muriel, Sandra et Emmanuelle :)")
    print("La grille de jeu est agencée avec 3 lignes et 3 colonnes. Voici les index de chaque case :")
    print("_____"*5)
    print("|"+"  "+"0,0"+"  "+"|"+"  "+"0,1"+"  "+"|"+"  "+"0,2"+"  "+"|")
    print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
    print("|"+"  "+"1,0"+"  "+"|"+"  "+"1,1"+"  "+"|"+"  "+"1,2"+"  "+"|")
    print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
    print("|"+"  "+"2,0"+"  "+"|"+"  "+"2,1"+"  "+"|"+"  "+"2,2"+"  "+"|")
    print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
    
    player = input('Entrez le signe du joueur 1 (x ou o) : ')
    for row in matrice:
        for case in row:
            c = 0
            while c < 3:
                if matrice[0][c] == matrice[1][c] == matrice [2][c] == "X":
                    if player == 'x':
                        print("Joueur 1 a gagné")
                    else : print("Joueur 2 a gagné")
                    return
                if matrice[c] == ['X','X','X']:
                    if player == 'x':
                        print("Joueur 1 a gagné")
                    else : print("Joueur 2 a gagné")
                    return
                if matrice[0][c] == matrice[1][c] == matrice [2][c] == "O":
                    if player == 'o':
                        print("Joueur 1 a gagné")
                    else : print("Joueur 2 a gagné")
                    return
                if matrice[c] == ["O","O","O"] :
                    if player == 'o':
                        print("Joueur 1 a gagné")
                    else : print("Joueur 2 a gagné")
                    return
                if matrice [0][0] == matrice [1][1] == matrice [2][2] == "X":
                    if player == 'x':
                        print("Joueur 1 a gagné")
                    else : print("Joueur 2 a gagné")
                    return
                if matrice [0][2] == matrice [1][1] == matrice [2][0] == "X":
                    if player == 'x':
                        print("Joueur 1 a gagné")
                    else : print("Joueur 2 a gagné")
                    return

                if matrice [0][0] == matrice [1][1] == matrice [2][2] == "O":
                    if player == 'o':
                        print("Joueur 1 a gagné")
                    else : print("Joueur 2 a gagné")
                    return
                if matrice [0][2] == matrice [1][1] == matrice [2][0] == "O":
                    if player == 'o':
                        print("Joueur 1 a gagné")
                    else : print("Joueur 2 a gagné")
                    return
                c +=1
            ligne = int(input("Dans quel rang voulez vous jouer (0, 1 ou 2)?"))
            col = int(input(f"Vous jouez dans le rang {ligne}, quelle case voulez vous jouer (0, 1 ou 2)?"))

            mystr = ''.join(matrice[0] + matrice[1] + matrice[2])
            counter_x = mystr.count('X')
            counter_o = mystr.count('O')
            if matrice[ligne][col] != empty:
                print('Case déjà utilisée. Veuillez entrer une case vide')
                continue
            def playerx():
                if counter_x == counter_o:
                    matrice[ligne][col] = 'X'
                elif counter_x > counter_o:
                    matrice[ligne][col] = 'O'
            def playero():
                if counter_o == counter_x:
                    matrice[ligne][col] = 'O'
                elif counter_x < counter_o:
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