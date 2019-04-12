from random import choice

def initialisation():
    grille = []
    for index in range(81):
        grille.append(0)
    return grille

def affiche(grille):

    for i in range(9):
        L=[]
        for j in range(9):
            L.append(grille[9*i+j])
        print(L)

def interdit_rangees(index, grille):
    interdit_ligne = {grille[index2] for index2 in range(81) if (index2 // 9) == (index // 9)}
    interdit_colon = {grille[index2] for index2 in range(81) if (index2 % 9) == (index %9)}
    interdit = interdit_ligne.union(interdit_colon)
    return interdit

def interdit_carre(index, grille):
    ligne = index // 9
    colon = index % 9
    ligne_carre = ligne // 3
    colon_carre = colon // 3
    interdit =[]
    for index2 in range(81):
        ligne2 = index2 // 9
        colon2 = index2 % 9
        ligne_carre2 = ligne2 // 3
        colon_carre2 = colon2 // 3
        if (ligne_carre2 == ligne_carre) and (colon_carre2 == colon_carre):
            interdit.append(grille[index2])
    return interdit

def conflits(grille, index):
    conflit = interdit_rangees(index, grille).union(interdit_carre(index, grille))
    return conflit

def add_element(grille, untrieds, index, candidats):
    grille[index] = choice(list(candidats))
    untrieds[index] -= {grille[index]}

def solve1(grille):
    cases_vides = [index for index in range(81) if grille[index] == 0]
    nombre_de_cases = len(cases_vides)
    print("Cases vides : ", nombre_de_cases)
    if nombre_de_cases == 0: return True
    index = cases_vides[0]
    candidats ={1,2,3,4,5,6,7,8,9}-conflits(grille, index)
    if candidats == set():
        return False
    else:
        grille[index] = choice(list(candidats))
    return True

def resolve(grille, forbiden = [0,0]):
    case_interdite = forbiden[0]
    print("Case interdite :", case_interdite)
    valeur_interdite = forbiden[1]
    print("Valeur interdite :", valeur_interdite)
    cases_vides = [index for index in range(81) if grille[index] == 0]
    untrieds = []
    nombre_de_cases = len(cases_vides)
    print("Cases vides : ", nombre_de_cases )
    for index in range(81):
        untrieds.append({1,2,3,4,5,6,7,8,9})
    index = 0
    while index < nombre_de_cases:
        index_case = cases_vides[index]
        candidats = untrieds[index_case]-conflits(grille, index_case)
        if index_case == case_interdite:
            candidats -= {valeur_interdite}
        if candidats == set():
            if index == 0:
                return False
            else:
                untrieds[index_case] = {1,2,3,4,5,6,7,8,9}
                grille[index_case] = 0
            index = index-1
            untrieds[index_case] =untrieds[index_case]- {grille[index_case]}
        else:
            add_element(grille, untrieds, index_case, candidats)
            index += 1
    return True

def remove_random_element(grille):
    cases_pleines = fcases_pleines(grille)
    index = choice(cases_pleines)
    print(index)
    valeur = grille[index]
    grille[index] = 0
    return grille, index, valeur

def remove_safe_element(grille):
    grille1 = grille[:]
    grille1, index, valeur = remove_random_element(grille1)
    if resolve(grille1, [index, valeur]):
        print("Impossible d'effacer la case ", index, " (la solution n'est plus unique)")
        return index, False
    else:
        print("Case ", index, "effacée ( valeur : ", valeur ," )")
        return index, True

def remove1(grille):
    not_removed = []
    cases_pleines = fcases_pleines(grille)
    while set(cases_pleines) != set(not_removed):
        index, reussite = remove_safe_element(grille)
        if reussite:
            return index, True
        else:
            not_removed.append(index)
    return index, False

def fcases_pleines(grille):
    cases_pleines = [index for index in range(81) if grille[index] != 0]
    return cases_pleines

def affiche_candidats(grille):
    liste_candidats = []
    for index in range(81):
        liste_candidats.append(len(list({1,2,3,4,5,6,7,8,9}-set(conflits(grille, index)))))
    affiche(liste_candidats)
    print()
