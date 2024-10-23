
from truc2 import *

def winorlose():
    empty = '_'
    symbx = 'x' #input de user
    symbo= 'o'
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
                if matrice[0][c] == matrice[1][c] == matrice [2][c] == symbx:
                    print("x a gagn")
                    return
                if matrice[0][c] == matrice[1][c] == matrice [2][c] == symbo:
                    print("o a gagné")
                if matrice[c] == []:
                    print("x a gagné")
                    return
                c +=1

            ligne = int(input("quel rang voulez vous jouer ?"))
            col = int(input("dans quelle colonne"))

            matrice[ligne][col] = 'x'
            print("_____"*5)
            print("|"+"___"+f"{matrice[0][0]}"+"___"+"|"+"___"+f"{matrice[0][1]}"+"___"+"|"+"___"+f"{matrice[0][2]}"+"___"+"|")
            print("|"+"___"+f"{matrice[1][0]}"+"___"+"|"+"___"+f"{matrice[1][1]}"+"___"+"|"+"___"+f"{matrice[1][2]}"+"___"+"|")
            print("|"+"___"+f"{matrice[2][0]}"+"___"+"|"+"___"+f"{matrice[2][1]}"+"___"+"|"+"___"+f"{matrice[2][2]}"+"___"+"|")

