# Ex 1.
# O variabila este un nume dat unei zone din memoria calculatorului, in care se stocheaza valori

# Ex 2. Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
# string, int, float, bool
#  Valorile le alegeti voi dupa preferinte

# string
oras = 'Bucuresti'
# integer
an_achizitie = 2022
# float
consum = 3.4
# boolean
absolvent_facultate = True

# Ex 3. Utilizati functia type pentru a verifica daca au tipul de date asteptat
print(type(oras))
print(type(an_achizitie))
print(type(consum))
print(type(absolvent_facultate))

<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>

# Ex 4. Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
# Verificati tipul acesteia

consum = round(3.4)
print(type(consum))
<class 'int'>

# Ex 5. folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
# (rezolvati nepotrivirile de tip prin ce modalitate doriti)

print(f'Locuiesc in {oras}')
print(f'Am cumparat un robot de bucatarie in {an_achizitie}')
print(f'Luna aceasta, am inregistrat un consum de energie electrica de {consum}')
print(f'Daca este absolvent facultate, afiseaza {absolvent_facultate}')

# Ex 6. citeste de la tastatura numele
# citeste de la tastatura prenumele
# afiseaza 'Numele complet are x caractere'

nume = input('Introdu nume ')
prenume = input('Introdu prenume ')
print(f'Numele complet are {len(nume + prenume)} caractere')

# Ex 7. citeste de la tastatura lungimea
# citeste de la tastatura latimea
# afiseaza 'Aria dreptunghiului este x'

lungime = int(input('Introdu lungime '))
latime = int(input('Introdu latimea '))
aria = lungime * latime
print(f'Aria dreptunghiului este {aria}')

# Ex 8. Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
# afisati de cate ori apare cuvantul 'the'

my_string = 'Coral is either the stupidest animal or the smartest rock'
my_string.count('the')
print(my_string.count('the'))

# EX 9. acelasi string
# inlocuieste the cu THE peste tot
# printeaza rezultatul

my_string = 'Coral is either the stupidest animal or the smartest rock'
my_string = my_string.replace('the', "THE")
print(my_string)


# Ex 10. citeste de la tastatura un string de dimensiune impara
# afiseaza caracterul din mijloc

str = input('Introdu nume: ')
x = len(str)
y = x//2
print('Caracterul din mijloc este ',  str[y])

# sau
str = input('Introdu nume: ')
x = len(str)
y = x//2
print(f'Caracterul din mijloc este {str[y]}')

# Ex 11. folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
# si salveaza fiecare cuvant intr-o variabila
# acum printeaza ambele variabile pentru verificare
# Citim de la tastatura un string oarecare

str = input('Introdu string : ').split()
x,y = str
print(x,y)

#sau
x,y = input('Introdu string : ').split()
print(x,y)

# Ex 12.  citeste un string de la tastatura (eg: alabala portocala)
# salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite)
# capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
# => alAbAlA portocAla

my_string = input('Introdu string: ')
primul_caracter = my_string[0]
my_string = my_string[0] + my_string[1:-1].replace(primul_caracter, primul_caracter.upper()) + my_string[-1]
print(my_string)

# Ex 13. citeste un user de la tastatura
# citeste o parola
# afiseaza: 'Parola pt user x este ***** si are x caractere'
# ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
# eg: parola abc => ***
# parola abcd => ****

user = input('Introdu user ')
parola = input('Introdu parola ')
parola = '*' * len(parola)
x = len(parola)
print(f'Parola pentru {user} este {parola} si are {x} caractere')
