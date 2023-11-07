"""
A = int(input("Saisir un nombre entier"))
B = int(input("Saisir un nombre entier"))
C = int(input("Saisir un nombre entier"))

if A >= B and A >= C:
    print("le maximum est A")
elif B >= A and B >= C:
    print("le maximum est B")
elif C >= A and C >= B:
    print("le maximum est C")

A = int(input("Saisir un nombre"))
B = int(input("Saisir un nombre"))

if (A > 0 and B > 0) or (A < 0 and B < 0):
    print("le produit de", A,"et", B,"est positf")
elif (A > 0 and B < 0) or (A < 0 and B > 0):
    print("le produit de", A,"et", B,"est negatif")
elif A == 0 and B == 0:
    print("le produit de", A,"et", B,"est nulle")

moyenne = float(input("Entrez la moyenne de l'étudiant : "))

if 16 <= moyenne <= 20:
    print("Très bien")
elif 14 <= moyenne < 16:
    print("Bien")
elif 12 <= moyenne < 14:
    print("Assez bien")
elif 10 <= moyenne < 12:
    print("Passable")
else:
    print("Insuffisant")

note_oral = float(input("Entrez la note d'oral : "))
note_ecrit = float(input("Entrez la note d'écrit : "))

moyenne = (note_oral + 2 * note_ecrit) / 3

if moyenne >= 10:
    print("Module validé.")
else:
    print("Module non validé.")

age = int(input("Entrez l'âge de l'habitant : "))
sexe = input("Entrez le sexe de l'habitant  : ")

if sexe == "M" and age > 20:
    print("L'habitant est imposable.")
elif sexe == "F" and 18 <= age <= 35:
    print("L'habitant est imposable.")
else:
    print("L'habitant n'est pas imposable.")

while True:
    sexe = input("Entrez le sexe (M/F) : ")
    taille = float(input("Entrez la taille (cm) : "))
    poids = float(input("Entrez le poids (kg) : "))

    if sexe == "M":
        PI = (taille - 100) - (taille - 150) / 4
    elif sexe == "F":
        PI = (taille - 100) - (taille - 120) / 4
    else:
        print("Sexe invalide. Veuillez entrer M ou F.")
        continue

    taille_m = taille / 100
    BMI = poids / (taille_m ** 2)

    if BMI <= 27:
        classification = "Normale"
    elif BMI >= 32:
        classification = "Malade"
    else:
        classification = "Obèse"

    print("Poids idéal :", PI)
    print("BMI :", BMI)
    print("Classification :", classification)

    continuer = int(input("Voulez-vous continuer ? (1 pour Oui, 0 pour Non) : "))
    if continuer == 0:
        break

age = int(input("Entrez l'âge du cadre : "))
anciennete = int(input("Entrez l'ancienneté en années : "))
salaire = float(input("Entrez le dernier salaire : "))

indemnite = 0

if 1 <= anciennete <= 10:
    indemnite = (salaire / 2) * anciennete
elif anciennete > 10:
    indemnite = salaire * anciennete

if age > 45:
    if 46 <= age <= 49:
        indemnite += 2 * salaire
    elif age >= 50:
        indemnite += 5 * salaire
print("Indemnité à verser au cadre :", indemnite)

"""
while True:
    sexe = input("Entrez le sexe  : ")
    taille = float(input("Entrez la taille  : "))
    poids = float(input("Entrez le poids  : "))

    if sexe == "M":
        PI = (taille - 100) - (taille - 150) / 4
    elif sexe == "F":
        PI = (taille - 100) - (taille - 120) / 4
    else:
        print("Sexe invalide. Veuillez entrer M ou F.")
        continue

    taille_m = taille / 100
    BMI = poids / (taille_m ** 2)

    if BMI <= 27:
        classification = "Normale"
    elif BMI >= 32:
        classification = "Malade"
    else:
        classification = "Obèse"

    print("Poids idéal :", PI)
    print("BMI :", BMI)
    print("Classification :", classification)

    continuer = int(input("Voulez-vous continuer ? (1 pour Oui, 0 pour Non) : "))
    if continuer == 0:
        break
