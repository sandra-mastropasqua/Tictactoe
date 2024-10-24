def grilledejeu():
    empty = " "
    matrice = [empty for i in range(10)]

    print("_____"*5)
    print("|"+"   "+f"{matrice[1]}"+"   "+"|"+"   "+f"{matrice[2]}"+"   "+"|"+"   "+f"{matrice[3]}"+"   "+"|")
    print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
    print("|"+"   "+f"{matrice[4]}"+"   "+"|"+"   "+f"{matrice[5]}"+"   "+"|"+"   "+f"{matrice[6]}"+"   "+"|")
    print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
    print("|"+"   "+f"{matrice[7]}"+"   "+"|"+"   "+f"{matrice[8]}"+"   "+"|"+"   "+f"{matrice[9]}"+"   "+"|")
    print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")

    print("Bienvenue dans le tictactoe de Muriel, Sandra et Emmanuelle :)")
    print("La grille de jeu est agencée avec 9 cases. Voici les numéros de chaque case :")
    print("____"*4+"___")
    print("|"+"  "+"1"+"  "+"|"+"  "+"2"+"  "+"|"+"  "+"3"+"  "+"|")
    print("|"+"_____"+"|"+"_____"+"|"+"_____"+"|")
    print("|"+"  "+"4"+"  "+"|"+"  "+"5"+"  "+"|"+"  "+"6"+"  "+"|")
    print("|"+"_____"+"|"+"_____"+"|"+"_____"+"|")
    print("|"+"  "+"7"+"  "+"|"+"  "+"8"+"  "+"|"+"  "+"9"+"  "+"|")
    print("|"+"_____"+"|"+"_____"+"|"+"_____"+"|")

    def conditiongagnante():
        player = input("Entrez le signe du joueur 1 (X ou O): ")
        case = int(input("Choisir case"))
        for num in matrice : 
            matrice[case] = "X"
            if player == "X":
                print("Joueur 1 a gagné")
            else : 
                print("Joueur 2 a gagné")
        print("_____"*5)
        print("|"+"   "+f"{matrice[1]}"+"   "+"|"+"   "+f"{matrice[2]}"+"   "+"|"+"   "+f"{matrice[3]}"+"   "+"|")
        print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
        print("|"+"   "+f"{matrice[4]}"+"   "+"|"+"   "+f"{matrice[5]}"+"   "+"|"+"   "+f"{matrice[6]}"+"   "+"|")
        print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
        print("|"+"   "+f"{matrice[7]}"+"   "+"|"+"   "+f"{matrice[8]}"+"   "+"|"+"   "+f"{matrice[9]}"+"   "+"|")
        print("|"+"_______"+"|"+"_______"+"|"+"_______"+"|")
    conditiongagnante()
grilledejeu()

    





        








