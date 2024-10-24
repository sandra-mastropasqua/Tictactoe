
empty = ' '
matrice = [
    [empty for i in range(3)],
    [empty for i in range(3)],
    [empty for i in range(3)]
]

player  = input('Entrez le signe du joueur 1 (x ou o) : ')
if player not in ['x', 'o']:
    print('erreur')
    exit()
    
def winorlose():
    counter = 0
    print("Bienvenue dans le tictactoe de Muriel, Sandra et Emmanuelle :)")
    print("La grille de jeu est agencée avec 9 cases. Voici les numéros de chaque case :")
    print("____"*4+"___")
    print("|"+"  "+"1"+"  "+"|"+"  "+"2"+"  "+"|"+"  "+"3"+"  "+"|")
    print("|"+"_____"+"|"+"_____"+"|"+"_____"+"|")
    print("|"+"  "+"4"+"  "+"|"+"  "+"5"+"  "+"|"+"  "+"6"+"  "+"|")
    print("|"+"_____"+"|"+"_____"+"|"+"_____"+"|")
    print("|"+"  "+"7"+"  "+"|"+"  "+"8"+"  "+"|"+"  "+"9"+"  "+"|")
    print("|"+"_____"+"|"+"_____"+"|"+"_____"+"|")
    
    player = input('Entrez le signe du joueur 1 (x ou o) : ')
    for num in matrice:
        if matrice[1] == matrice[2] == matrice [3] == "X":
            if player == 'x':
                print("Joueur 1 a gagné")
            else : print("Joueur 2 a gagné")
            return
        if matrice in range[0,3] == ['X','X','X']:
            if player == 'x':
                print("Joueur 1 a gagné")
            else : print("Joueur 2 a gagné")
            return
        if matrice[4] == matrice[5] == matrice [6] == "O":
            if player == 'o':
                print("Joueur 1 a gagné")
            else : print("Joueur 2 a gagné")
            return
        if matrice in range [0,3] == ["O","O","O"] :
            if player == 'o':
                print("Joueur 1 a gagné")
            else : print("Joueur 2 a gagné")
            return
        if matrice [7] == matrice [8] == matrice [9] == "X":
            if player == 'x':
                print("Joueur 1 a gagné")
            else : print("Joueur 2 a gagné")
            return
        if matrice [1] == matrice [5] == matrice [9] == "X":
            if player == 'x':
                print("Joueur 1 a gagné")
            else : print("Joueur 2 a gagné")
            return

        if matrice [1] == matrice [2] == matrice [3] == "O":
                if player == 'o':
                    print("Joueur 1 a gagné")
                else : print("Joueur 2 a gagné")
                return
        if matrice [4] == matrice [5] == matrice [6] == "O":
                if player == 'o':
                    print("Joueur 1 a gagné")
                else : print("Joueur 2 a gagné")
                return
            
        case = int(input("Dans quel case souhaitez-vous jouer ?"))

        mystr = ''.join(matrice in range[0,9])
        counter_x = mystr.count('X')
        counter_o = mystr.count('O')
        if matrice in range[0,9] != empty:                                    
            print('Case déjà utilisée. Veuillez entrer une case vide')
            continue
            def playerx():
                if counter_x == counter_o:
                    matrice in range[0,9] = 'X'
                elif counter_x > counter_o:
                    matrice in range[0,9] = 'O'
            def playero():
                if counter_o == counter_x:
                    matrice in range[0,9] = 'O'
                elif counter_x < counter_o:
                    matrice in range [0.9] = 'X'
            if player == 'x':
                playerx()
            elif player == 'o':
                playero()
            else : return
           
            print("_____"*5)
            print("|"+"   "+f"{matrice[1]}"+"   "+"|"+"   "+f"{matrice[2]}"+"   "+"|"+"   "+f"{matrice[3]}"+"   "+"|")
            print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
            print("|"+"   "+f"{matrice[4]}"+"   "+"|"+"   "+f"{matrice[5]}"+"   "+"|"+"   "+f"{matrice[6]}"+"   "+"|")
            print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
            print("|"+"   "+f"{matrice[7]}"+"   "+"|"+"   "+f"{matrice[8]}"+"   "+"|"+"   "+f"{matrice[9]}"+"   "+"|")
            print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
winorlose()