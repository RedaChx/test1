"""
A = input("saisir un caractere :")
print("Le caractere saisie est", A)
B = input("saisir une chaine de caracteres:")
print("La chaine de caracteres saisie est", B)
C = int(input("saisir un nombre entier:"))
print("Le nombre entier saisie est", C)
D = float(input("saisir un nombre reel:"))
print("Le nombre reel saisie est", D)

A = int(input("Saisir un nombre entier"))
B = int(input("Saisir un nombre entier"))
print("la somme de", A, "et", B, "est", A + B)
print("la difference de", A, "et", B, "est", A - B)
print("la divison de", A, "et", B, "est", A / B)
print("la divison entiere de", A, "et", B, "est", A // B)
print("le produit de", A, "et", B, "est", A * B)

A = int(input("saisir un nombre entier"))
print("le carre de", A , "est", A**2)

A = int(input("saisir une valeur A"))
B = int(input("saisir une valeur B"))
C = int(input("saisir une valeur C"))
D = int(input("saisir une valeur D"))

A = B
B = C
C = D
D = A
print("la valeur de A est", A)
print("la valeur de B est", B)
print("la valeur de C est", C)
print("la valeur de D est", D)

r = float(input("Saisir la valeur du rayon"))
Pi = 3.14
A = 2*Pi*r
B = Pi*(r**2)
print("la surface du cercle est", A)
print("la circonference du cercle est", B)

"""

A = int(input("saisir une valeur A"))
B = int(input("saisir une valeur B"))
C = int(input("saisir une valeur C"))

A, B, C = B, C, A

print("la valeur de A est", A)
print("la valeur de B est", B)
print("la valeur de C est", C)
