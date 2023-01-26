################################################################################
# ~ Auteur: Gabriel DELAGE                                                     #
# ~ Mail: delage.gabriel83@gmail.com                                           #
# ~ Version: 1.1.0.0                                                           #
# ~ Date de création: lundi 23 janvier 2023                                    #
################################################################################
from random import *
from math import *

################################################################################
# <summary>Méthode qui permet d'arrondir à 0 ou 5 le dernier chiffre           #
# d'un nombre</summary>                                                        #
# <param>nnombre(int) le nombre à arrondir</param>                             #
################################################################################
def set_nombre(nombre):
    # Conversion du nombre entré en string
    nombre_str = str(nombre)
    # Chaîne de caractère qui accueillera le nouveau nombre
    nouveau_nombre = ""

    for i in range(len(nombre_str)):
        # Si i est égal à l'index 0, on conserve le chiffre
        if i == 0:
            nouveau_nombre += str(nombre_str[i])
        # Sinon:
        else:
            # Si i+1 est égal à la longueur de notre nombre sous forme de chaîne
            # de caractère
            if i+1 == len(nombre_str):
                # Si le chiffre dont l'index est égal à i est entre 0 ET 4
                if int(nombre_str[i]) >= 0 and int(nombre_str[i]) <= 4:
                    # Alors le dernier chiffre sera 0
                    nouveau_nombre += "0"
                # Sinon si le chiffre dont l'index est égal à i est entre 5 et 9
                elif int(nombre_str[i]) >= 5 and int(nombre_str[i]) <= 9:
                    # Alors le dernier chiffre sera 5
                    nouveau_nombre += "5"
            # Sinon
            else:
                # On ajoute le chiffre au nouveau nombre dont l'index est à égal
                # à i
                nouveau_nombre += str(nombre_str[i])
    return int(nouveau_nombre)

################################################################################
# <summary>Méthode Calcul_Exp qui permet de calculer l'expérience              #
# que donne une créature</summary>                                             #
# <param>niveau(int) niveau de la créature </param>                            #
# <param>nature(string) nature de la créature (s'il est humain, démon, ...)    #
# </param>                                                                     #
# <param>indiceMenace(int) l'indice de menace de la créature, calculée dans un #
# excel </param>                                                               #
################################################################################
def get_experience_ennemi(niveau, nature, indice_menace):
    try:
        # switch : changement du modificateur en fonction
        # de la nature de la créature
        match nature:
            case "Humanoïde":
                modificateur = 0.7
            case "Bête":
                modificateur = 0.5
            case "Démon":
                modificateur = 0.5
            case "Inorganique":
                modificateur = 0.5
            case "Insectoïde":
                modificateur = 0.5
            case "Volatiles":
                modificateur = 0.5
            case "Aquatique":
                modificateur = 0.5
            case "Revenants":
                modificateur = 0.4
            case "Fée":
                modificateur = 0.4
            case "Dragon":
                modificateur = 0.4
            case "Inconnu":
                modificateur = 0.3
            case "Titan":
                modificateur = 0.1
            case "Déité":
                modificateur = 0.05
        # switch : changement du multiplicateur en fonction
        # du niveau de la créature
        match niveau:
            case 1:
                base = randint(0,11)
                multiplicateur = 11
            case 2:
                base = randint(10,21)
                multiplicateur = 12
            case 3:
                base = randint(20,31)
                multiplicateur = 13
            case 4:
                base = randint(30,41)
                multiplicateur = 14
            case 5:
                base = randint(40,51)
                multiplicateur = 15
            case 6:
                base = randint(50,61)
                multiplicateur = 16
            case 7:
                base = randint(60,71)
                multiplicateur = 17
            case 8:
                base = randint(70,81)
                multiplicateur = 18
            case 9:
                base = randint(80,91)
                multiplicateur = 19
            case 10:
                base = randint(90,101)
                multiplicateur = 20
            case 11:
                base = randint(100,111)
                multiplicateur = 21
            case 12:
                base = randint(110,121)
                multiplicateur = 22
            case 13:
                base = randint(120,131)
                multiplicateur = 23
            case 14:
                base = randint(130,141)
                multiplicateur = 24
            case 15:
                base = randint(140,151)
                multiplicateur = 25
            case 16:
                base = randint(150,161)
                multiplicateur = 26
            case 17:
                base = randint(160,171)
                multiplicateur = 27
            case 18:
                base = randint(170,181)
                multiplicateur = 28
            case 19:
                base = randint(180,191)
                multiplicateur = 29
            case 20:
                base = randint(190,201)
                multiplicateur = 30
        return set_nombre(round(((base + (niveau * indice_menace) / modificateur) *
        multiplicateur) / 4))
    except:
        return "Une ou plusieurs information rentrées ne sont pas valides"

################################################################################
# <summary>Méthode qui renvoie la courbe d'expérience                          #
# de la créature</summary>                                                     #
# <param>progression(string) "rapide, moyenne, lente</param>                   #
# <param>base_expérience(int) le montant FINAL requis pour atteindre le niveau #
# 20</param>                                                                   #
# <param>creature(string) si c'est un personnage ou un familier                #
# 20</param>                                                                   #
################################################################################
def get_courbe_experience(progression, base_experience, creature):
    try:
        # switch : change le modificateur en fonction de la progression entrée
        # par l'utilisateur
        match progression:
            case "Rapide":
                print(base_experience)
                experience_totale = base_experience
                modificateur = 2500
            case "Moyenne":
                print(base_experience)
                experience_totale = base_experience
                modificateur = 5000
            case "Lente":
                print(base_experience)
                experience_totale = base_experience
                modificateur = 7500
        # switch : si c'est un personnage, le nombre de niveau est de 20, si
        # c'est un familier, le nombre de niveau est de 10
        match creature:
            case "Personnage":
                for i in range(1,19):
                    modificateur *= 1.33
                    experience_totale += modificateur
                    print(set_nombre(round(experience_totale)), "—", i+1)
            case "Familier":
                for i in range(1,9):
                    modificateur *= 1.33
                    experience_totale += modificateur
                    print(set_nombre(round(experience_totale)), "—", i+1)
        return "Calcul terminé !"
    except:
        print("Une erreur a été rencontrée.")

################################################################################
# <summary>Méthode qui permet d'obtenir le grade que les joueurs gagnent       #
# à la fin d'un combat </summary>                                              #
# <param>tour(int) nombre de tour pour finir le combat</param>                 #
# <param>nombre_combo(int) nombre de combo que les joueurs ont pu placer       #
# </param>                                                                     #
# <param>coups_recus(int) le nombre total de coups pris par les joueurs</param>#
# <param>coup_grace(bool) True s'il y a eu un coup de grâce</param>            #
# <param>contre_attaque_reussie(bool) True s'il y a eu une contre attaque      #
# réussie </param>                                                             #
################################################################################
def get_grade_combat(tour, nombre_combo, coups_recus, coup_grace,
            contre_attaque_reussie):

    points_totaux = 10

    try:
        # Vérifie le nombre de tour qu'il y a eu pour terminer le combat
        if tour == 1:
            points_totaux = points_totaux + 750
        elif tour >= 2 and tour <= 5:
            points_totaux = points_totaux + 500
        elif tour >= 6 and tour <= 10:
            points_totaux = points_totaux + 250
        elif tour > 10:
            points_totaux = points_totaux + 100

        # On multiplie la points_totaux par le nombre de combo
        points_totaux *= nombre_combo

        # Vérifie le nombre de coups total sur les joueurs qu'il y a eu durant
        # le combat
        if coups_recus == 0:
            points_totaux = points_totaux + 1000
        elif coups_recus >= 1 and coups_recus <= 3:
            points_totaux = points_totaux + 250
        elif coups_recus >= 4 and coups_recus <= 6:
            points_totaux = points_totaux + 125
        elif coups_recus >= 7 and coups_recus <= 10:
            points_totaux = points_totaux + 50
        elif coups_recus > 10:
            points_totaux = points_totaux + 10

        # S'il y a eu un coup de grâce, on multiplie par 2
        if coup_grace == True:
            points_totaux *= 2
        # Si au moins UNE contre-attaque a été réussie, on multiplie par 2
        if contre_attaque_reussie == True:
            points_totaux *= 2

        # On vérifie le nombre de points total et on attribue le grade
        if points_totaux >= 20000:
            return "Grade S"
        elif points_totaux <= 19999 and points_totaux >= 15000:
            return "Grade A"
        elif points_totaux <= 14999 and points_totaux >= 10000:
            return "Grade B"
        elif points_totaux <= 9999 and points_totaux >= 5000:
            return "Grade C"
        elif points_totaux <= 4999 and points_totaux >= 1000:
            return "Grade D"
        elif points_totaux <= 999 and points_totaux > 0:
            return "Grade E"
    except:
        print("Une erreur a été rencontrée.")

################################################################################
# ~ Dernière modification : 26/01/23                                           #
################################################################################