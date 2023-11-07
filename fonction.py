"""
def somme(n):
    s = 0
    for i in range(1, n+1):
        s = s+i
    return s

X = int(input("Donner une valeur"))
A = somme(X)
print("la somme est", A)
"""
"""
def max(a, b):
    if a > b:
        return a
    else:
        return b

A = int(input("Donnez une valeur pour A : "))
B = int(input("Donnez une valeur pour B : "))
maximum = max(A, B)
print("La valeur la plus grande est", maximum)

def max(a, b):
    if a > b:
        print("le max est", a)
    else:
        print("le max est", b)
A = int(input("Donnez une valeur pour A : "))
B = int(input("Donnez une valeur pour B : "))
max(A, B)
"""
"""
def pgcd(a, b):
    for i in range(1, min(a, b)):
        if a%i == 0 and b%i == 0 :
            d=i
    return d

A = int(input("Enter la valeur A : "))
B = int(input("Enter la valeur B : "))
d = pgcd(A, B)
print("pgcd de ", A, "et ", B, " est ", d)

def pgcd(a, b):
    if b == 0:
        return a
    else:
        return pgcd(b, a % b)

A = int(input("Enter la valeur A :"))
B = int(input("Enter la valeur B :"))
result = pgcd(A, B)
print("pgcd de ", A, "et ", B, " est ", result)
"""
"""
def nombre_de_chiffres(n):
    chiffres = str(n)
    longueur = len(chiffres)
    return longueur

nombre = 12345
resultat = nombre_de_chiffres(nombre)
print("Le nombre de chiffres dans", nombre, "est :", resultat)
"""
"""
def pgcd(a, b):
    for i in range(1, min(a, b)):
        if a%i==0 and b%i==0:
            d=i
    return d

A = int(input("Enter la valeur A : "))
B = int(input("Enter la valeur B : "))
d = pgcd(A, B)
print("pgcd de ", A, "et ", B, " est ", d)
"""
""" 
A = int(input("Donnez une valeur pour A : "))
B = int(input("Donnez une valeur pour B : "))

def max(a, b):
    if a > b:
        return a
    else:
        return b

max = max(A, B)
print("La valeur la plus grande est", max)
"""
"""
def nombre_de_chiffres(n):
    C = 0
    while n > 0:
        C += 1
        n //= 10
    return C

n = int(input("donner une valeur"))
while x != 0:
    resultat = nombre_de_chiffres(n)
    print("Le nombre de chiffres dans", n, "est :", resultat)
    x = int(input("Donner une autre valeur"))
"""
"""
Variable.: n : Entier
    Fonction nombre_de_chiffres(n : entier)
    Variable : n , C: Entier 
    Debut:
    C <- 0
    Tant que (n > 0) :
        C += 1
        n //= 10
    Fin Tant que

    Retourner C
Fin Fonction
Debut:
Lire n
Résultat <- nombre_de_chiffres(n)
Afficher ("Le nombre de chiffres dans", n, "est :", Résultat)

"""
def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n - 1)

def calculer_somme(n):
    if n <= 5 or n % 2 == 0:
        return 0
    else:
        somme = 0
        for i in range(1, n + 1):
            somme += 1 / factoriel(i)
        return somme

n = int(input("Donner un nombre"))
resultat = calculer_somme(n)
print(f"S = {resultat}")

"""
Variable: n : entier
    fonction factoriel (n : entier)
    si n==0 Alors:
        Retourner 1
    sinon 
        Retourner n * factoriel(n - 1)
    Fin si
    Fin fonction
    fonction calculer_somme (n : entier)
    Variable : S : entier
    si (n <= 5 ou n % 2 == 0) 
        Retourner 0
    else
           
"""
"""
Variable : n , p , r: entier
Fonction somme_puissances(n: Entier, p: Entier) : Entier
    variable : s , i : entier
    s <- 0
    Pour i de 1 à n :
        s <- s + i^p
    Fin Pour
    Retourner s
Fin Fonction
Debut:
Ecrire("Donner une valeur")
Lire (n)
Ecrire("Donner une valeur")  
Lire (p)  
r <- somme_puissances(n, p)
Afficher ("La somme des puissances", p, "-ièmes de 1 à", n, "est égale à", r)

"""
"""
def somme_puissances(n, p):
    s = 0
    for i in range(1, n + 1):
        s += i**p
    return s

n = int(input("Donner une valeur n"))
p = int(input("Donner une valeur p"))
resultat = somme_puissances(n, p)
print("La somme des puissances", p, "et", n, "est égale à", resultat)

"""
"""
Variable : n : Entier
Fonction est_cubique( n : entier) : entier
    si 100 <= n <= 999 :
        chiffre1 <- n//100
        chiffre2 <- (n//10)%10
        chiffre3 <- n%10

"""

"""
def est_cubique(n):
    if 100 <= n <= 999:
        a = n % 100
        b = (n // 10) % 10
        c = (n // 10 // 10) % 10
        S = a**3 + b**3 + c**3
        if S == n :
            
    else:
        return False

n = int(input("Donner un nombre n"))
if est_cubique(n):
    print(f"{n} est un nombre cubique.")
else:
    print(f"{n} n'est pas un nombre cubique.")

"""

"""
def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n - 1)

def calculer_somme(n):
    if n <= 5 or n % 2 == 0:
        return 0
    else:
        somme = 0
        for i in range(1, n + 1):
            somme += 1 / factoriel(i)
        return somme

n = int(input("Donner un nombre"))
R = calculer_somme(n)
print("la somme est", R)
"""
def factoriel(n):
    if n == 0:
        return 1
    else:
        R = 1
        for i in range(1, n + 1):
            R *= i
        return R


n = int(input("Un nombre n"))
resultat = factoriel(n)
print("Le factoriel de ",n," est :",resultat)
