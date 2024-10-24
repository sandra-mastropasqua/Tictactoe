empty = ' '
matrice = [
    [empty for i in range(3)],
    [empty for i in range(3)],
    [empty for i in range(3)]
]
print("Bienvenue dans le tictactoe de Muriel, Sandra et Emmanuelle :)")
player  = input('Entrez le signe du joueur 1 (x ou o) : ')
if player not in ['x', 'o']:
    print('erreur')
    exit()

def winorlose():
    counter = 0
    print("La grille de jeu est agencée en 9 cases. Voici les numéros de chaque case :")
    print("_____"*5)
    print("|"+"   "+"1"+"   "+"|"+"   "+"2"+"   "+"|"+"   "+"3"+"   "+"|")
    print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
    print("|"+"   "+"4"+"   "+"|"+"   "+"5"+"   "+"|"+"   "+"6"+"   "+"|")
    print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
    print("|"+"   "+"7"+"   "+"|"+"   "+"8"+"   "+"|"+"   "+"9"+"   "+"|")
    print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")

    for row in matrice:
        for case in row:
            c = 0
            while c < 3:
                x_wins(c)
                o_wins(c)
                c +=1
            case = int(input("entre le num de la case "))
            i = 0
            counter = 1
            while i <= 2:
                j = 0
                while j <= 2:
                    if case == counter:
                        ligne = i
                        col = j
                    counter+=1
                    j +=1
                i +=1
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
            print("_____"*5)
            print("|"+"   "+f"{matrice[0][0]}"+"   "+"|"+"   "+f"{matrice[0][1]}"+"   "+"|"+"   "+f"{matrice[0][2]}"+"   "+"|")
            print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
            print("|"+"   "+f"{matrice[1][0]}"+"   "+"|"+"   "+f"{matrice[1][1]}"+"   "+"|"+"   "+f"{matrice[1][2]}"+"   "+"|")
            print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
            print("|"+"   "+f"{matrice[2][0]}"+"   "+"|"+"   "+f"{matrice[2][1]}"+"   "+"|"+"   "+f"{matrice[2][2]}"+"   "+"|")
            print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")

def x_is_player1():
    if player == 'x':
        print("Joueur 1 a gagné")
    else : print("Joueur 2 a gagné")

def o_is_player1():
    if player == 'o':
        print("Joueur 1 a gagné")
    else : print("Joueur 2 a gagné")

def x_wins(c):
    # condition colonne    
    if matrice[0][c] == matrice[1][c] == matrice [2][c] == "X":
        x_is_player1()
        exit()
    # condition ligne
    if matrice[c] == ['X', 'X', 'X']:
        x_is_player1()
        exit()
    # diagonales
    if matrice [0][0] == matrice [1][1] == matrice [2][2] == "X":
        x_is_player1()
        exit()
    if matrice [0][2] == matrice [1][1] == matrice [2][0] == "X":
        x_is_player1()
        exit()

def o_wins(c):
    #colonne
    if matrice[0][c] == matrice[1][c] == matrice [2][c] == "O":
        o_is_player1()
        exit()
    #ligne
    if matrice[c] == ["O","O","O"] :
        o_is_player1()
        exit()
    #diagonales
    if matrice [0][0] == matrice [1][1] == matrice [2][2] == "O":
        o_is_player1()
        exit()
    if matrice [0][2] == matrice [1][1] == matrice [2][0] == "O":
        o_is_player1()
        exit()

winorlose()