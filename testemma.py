empty = ' '
#création de la grille avec des espaces vides
matrice = [
    [empty for i in range(3)],
    [empty for i in range(3)],
    [empty for i in range(3)]
]
print("Bienvenue dans le tictactoe de Muriel, Sandra et Emmanuelle :)")
name1 = input('Entrez le prénom du joueur 1')
player = input(f' Bonjour {name1}.Entrez votre symbole (x ou o) : ')
name2 = input('Entrez le prénom du joueur 2.')
print(f'bonjour {name2}.')

# si le joueur1 a entré x alors le symbol est initialisé a X 
# a chaque tour de boucle le symbol égal soit a X soit a O 
# verification que l'utilisateur entre bien un x ou un o comme symbole
if player not in ['x', 'o']:
    print('erreur')
    exit()

def winorlose():
    print("La grille de jeu est agencée en 9 cases. Voici les numéros de chaque case :")
    print("_____"*5)
    print("|"+"   "+"1"+"   "+"|"+"   "+"2"+"   "+"|"+"   "+"3"+"   "+"|")
    print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
    print("|"+"   "+"4"+"   "+"|"+"   "+"5"+"   "+"|"+"   "+"6"+"   "+"|")
    print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
    print("|"+"   "+"7"+"   "+"|"+"   "+"8"+"   "+"|"+"   "+"9"+"   "+"|")
    print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
    #iteration sur chaque rang de la grille
    for row in matrice:
        #iteration sur chaque case du rang
        for case in row:
            #boucle pour appeler les fonctions de verification de victoire (boucle 3 pour parcourir toues les possibilités)
            c = 0
            while c < 3:
                x_wins(c)
                o_wins(c)
                c +=1
            case = int(input("entre le num de la case "))
            #boucle pour traduire les num de case en index de rang et index case
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
            # transformation de l'intégralité du contenu de matric en string pour pouvoir compter le nb de x et de o
            mystr = ''.join(matrice[0] + matrice[1] + matrice[2])
            counter_x = mystr.count('X')
            counter_o = mystr.count('O')
            # sécurité pour ne pas pouvoir réécrire sur une case déjà utilisée 
            if matrice[ligne][col] != empty:
                print('Case déjà utilisée. Veuillez entrer une case vide')
                continue
            # fonction pour alterner x et o si le premier coup est un x
            def playerx():
                if counter_x == counter_o:
                    matrice[ligne][col] = 'X'
                elif counter_x > counter_o:
                    matrice[ligne][col] = 'O'
            #fonction pour alterner o et x si le premier coup est un o
            def playero():
                if counter_o == counter_x:
                    matrice[ligne][col] = 'O'
                elif counter_x < counter_o:
                    matrice[ligne][col] = 'X'
            #lance la fonction qui alterne avec un x en premier
            if player == 'x':
                playerx()
            #lance la fonction qui alterne avec un o en premier
            elif player == 'o':
                playero()
            print("_____"*5)
            print("|"+"   "+f"{matrice[0][0]}"+"   "+"|"+"   "+f"{matrice[0][1]}"+"   "+"|"+"   "+f"{matrice[0][2]}"+"   "+"|")
            print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
            print("|"+"   "+f"{matrice[1][0]}"+"   "+"|"+"   "+f"{matrice[1][1]}"+"   "+"|"+"   "+f"{matrice[1][2]}"+"   "+"|")
            print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
            print("|"+"   "+f"{matrice[2][0]}"+"   "+"|"+"   "+f"{matrice[2][1]}"+"   "+"|"+"   "+f"{matrice[2][2]}"+"   "+"|")
            print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
    
    

# fonction pour indiquer si c'est le joueur 1 ou le joueur 2 qui gagne si le joueur 1 est x 
def x_is_player1():
    if player == 'x':
        print(f"{name1} a gagné")
    else : print(f"{name2} a gagné")

# fonction pour indiquer si c'est le joueur 1 ou le joueur 2 qui gange si le joueur est o
def o_is_player1():
    if player == 'o':
        print(f"{name1} a gagné")
    else : print(f"{name2} a gagné")
#fonction qui verifie les victoires de x
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
#fonction qui vérifie les victoires de o
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
def empty_grid():
    matrice[0]= [' ',' ',' ']
    matrice[1]= [' ',' ',' ']
    matrice[2]= [' ',' ',' ']
    return matrice
#lancement du jeu
