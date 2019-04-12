from sudoku_fonctions import initialisation, remove1, fcases_pleines, affiche, affiche_candidats, resolve

grille = initialisation()
if resolve(grille):
    affiche(grille)
    fichier = open("grille.txt", "w+")
    for valeur in grille:
        fichier.write("%s\n" %valeur)

