'''   =========PARTIE 1==========
personne = {'nom': 'Mélanie', 'age': 25, 'taille': 1.68}

print(personne)

print(personne['nom'])
print(personne['age'])

personne['nom'] = "Claire"
personne['poste'] = 'Développeur'

print(personne)

achat = ("Chocolat", "Beurre", "Fromage")
personne['achats'] = achat

print(personne)

for i in personne:
    print(f"Clef : {i} - Valeur : {personne[i]}")
'''


# =========== PARTIE 2 =========
''' ========== utilisant des listes================
personnes = [
    ("Mélanie", 25, 1.6),
    ("Paul", 29, 1.8),
    ("Jacques", 35, 1.75),
    ("Martin", 16, 1.65)
]


def obtenir_info(nom, liste):
    for i in liste:
        if i[0] == nom:
            return i
    return None


info_jacques = obtenir_info("Jacques", personnes)
print(info_jacques)
'''


personnes_dict = {
    "Mélanie": (25, 1.6),
    "Paul": (29, 1.8),
    "Jacques": (35, 1.75),
    "Martin": (16, 1.65)
}


infos = personnes_dict.get("Jacques")
if not infos:
    print("La clef n'existe pas")
else:
    print(infos)
