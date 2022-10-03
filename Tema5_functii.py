# Ex 1. Functie care sa calculeze si sa returneze suma a 2 numere

def sum(a,b):
    return a+b

suma = sum(8,9)
print(suma)

suma = sum(2,3)
print(suma)

# Sau
def sum(numere):
    total = 0
    for i in numere:
        total += i
    return total
print(sum((8,9)))
print(sum((2,3)))


# Ex 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
def par_imp(n):
    if(n % 2 == 0):
        return True
    else:
        return False
numar = par_imp(3)
print(numar)

numar = par_imp(4)
print(numar)

# Ex 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)
def caractere(nume):
  return len(nume) - nume.count(' ')
nume_dat = caractere('Anghelet Cristina Filofteia')
print(nume_dat)

nume_dat = caractere('Anghelet Cristina')
print(nume_dat)

# Ex 4. Functie care returneaza aria dreptunghiului

def aria_dreptunghi(lungime,latime):
    return lungime*latime
ar_dreptunghi = aria_dreptunghi(8,9)
print(ar_dreptunghi)

ar_dreptunghi = aria_dreptunghi(10,20)
print(ar_dreptunghi)

# Ex 5. Functie care returneaza aria cercului

import math
def arie_cerc(raza_cerc):
    return (raza_cerc ** 2) * math.pi
aria = arie_cerc(8)
print (aria)

aria = arie_cerc(9)
print(aria)

# Ex 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu

def string_dat(string):
    if ('l' in string):
        return True
    else:
        return False
string_introdus = string_dat('Anabel')
print(string_introdus)

string_introdus = string_dat('Andra')
print(string_introdus)

# Ex 7. Functie fara return, primeste un string si printeaza pe ecran:
#  Nr de caractere lower case este x
# Nr de caractere upper case exte y

def string_introdus(string):
    upper = 0
    lower = 0
    for i in string:
        if i.isupper():
           upper +=1
        elif i.islower():
           lower +=1
    print (f'String original: {string}')
    print (f'Numarul caracterelor lower case este: {lower}')
    print (f'Numarul caracterelor upper case este: {upper}')

string_introdus('Cristina')
string_introdus('AmALIA')

# Ex 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive

def nr_pozitive(numere):
    pozitive = []
    for numar in numere:
        if numar >=0:
            pozitive.append(numar)
    return pozitive
numere = [1,2,3,4,5,6,7,-1,-2]
print(nr_pozitive(numere))

numere = [1,-2,-3,-4,-5,-6,7,8,9]
print(nr_pozitive(numere))


# Ex 9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.

def max_numere(x, y):
    if x > y:
        print (f'Primul numar {x} este mai mare decat {y}')
    if y > x:
        print (f'Al doilea numar {y} este mai mare decat {x}')
    if x == y:
        print ('Numerele sunt egale')

max_numere(2,3)
max_numere(10,9)

# Ex 10. Functie care primeste un numar si un set de numere.
#  Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

def numere(num, set):
    if num  in set:
        print('Nu am adaugat numarul in set. Acesta exista deja')
        return False
    else:
        set.add(num)
        print('Am adaugat numarul in set')
        return True
print(numere(8, {1, 6, 7, 5}))

# EX 11. Functie care primeste o luna din an si returneaza cate zile are acea luna

from calendar import monthrange
def numar_zile(an=2022, luna=9):
    return monthrange(an, luna)[1]
print(numar_zile(2022, 9))
print(numar_zile(2022,8))

# Ex 12. Functie calculator care sa returneze 4 valori
# Suma, diferenta, inmultirea, impartirea a 2 numere

# In final vei putea face:
# a, b, c, d = calculator(10,2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

def calculator(x, y):
    return x+y, x-y, x*y, x/y

a, b, c, d = calculator(8, 6)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

# Ex 13. Functie care primeste o lista de cifre (adica doar 0-9)
#  Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un DICT care ne spune de cate ori apare fiecare cifra
#  => dict {
#  0: 0
#  1 :2
#  2: 0
#  3: 1
#  4: 0
#  5: 3
#  6: 0
#  7: 2
#  8: 0
#  9: 1
#  }

def num_ocurenta(lst):
   count = {}
   for i in lst:
    count[i] = count.get(i, 0) + 1
   return count
if __name__ == "__main__":
    lst =[1, 3, 1, 5, 9, 7, 7, 5, 5]
    print(num_ocurenta(lst))
    lst = [1, 2, 1, 2, 1, 3, 4, 5, 6]
    print(num_ocurenta(lst))

# Ex 14. Functie care primeste 3 numere
# Returneaza valoarea maxima dintre ele

def max_num(x, y, z):
    if (x >= y) and (x >= z):
        numar_mare = x
    elif (y >= x) and (y >= z):
        numar_mare = y
    else:
        numar_mare = z
    return numar_mare
print(max_num(2, 5, 10))
print(max_num(5, 9, 7))

# Ex 15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3
# Suma va fi 6 (0+1+2+3)

def sum1_n(n):
    return sum(range(n+1))
num = sum1_n(4)
print(num)

num =sum1_n(3)
print(num)

# Ex 16. Functie care nu primeste argumente, dar cere un input de la tastatura si va printa
# “Numarul ales este pozitiv” sau “Numarul ales este negativ” sau “Numarul ales este 0”, dupa caz, iar daca nu introducem un numar, sa se afiseze “Nu ati ales un numar valid”; la final sa se afiseze “Sfarsitul functiei” indiferent de caz.

def numar():
    nr = input("Introdu numar: ")
    try:
        nr = float(nr)
    except ValueError:
        print("Nu ati ales un numar valid")
    else:
        if nr > 0:
            print("Numarul ales este pozitiv")
        elif nr < 0:
            print("Numarul ales este negativ")
        else:
            print("Numarul ales este 0")
    finally:
        print("Sfarsitul functiei")

numar()

# Ex 17. Functie care primesete 2 liste de numere (numerele pot fi dublate)
# Returnati numerele comune

def num_comune(a, b):
    set1 = set(a)
    set2 = set(b)
    if len(set1.intersection(set2)) > 0:
        return(set1.intersection(set2))
    else:
        return('Nu sunt elemente comune')

a = [1, 1, 2, 3]
b = [2, 2, 3, 4]
print(num_comune(a, b))

a =[2, 6, 7, 0]
b =[1, 3, 5, 8]
print(num_comune(a, b))


# Ex 18. Functie care sa aplice o reducere de pret. Daca apelul functiei nu primeste valoarea reducerii, sa ia valoarea default 10%.
# Daca produsul costa 100 lei si aplicam reducere de 10%
# Pretul va fi 90
# Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida

def discount(pret, reducere=10):
    if reducere in range(0, 100):
        return pret - pret * reducere / 100
    else:
        print("Reducerea aplicata nu este valida")


print(discount(100, 30))
print(discount(80))

# Ex 19. Functie care sa afiseze data si ora curenta din ro
# (bonus: afisati si data si ora curenta din China)

from datetime import datetime, timedelta, timezone

def display_date_time():
    now = datetime.now()
    print(f"Date and time Romania: {now}")
    print(f"Date and time China: {now + timedelta(hours=5)}")

display_date_time()

# EX 20. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)
# from datetime import datetime

from datetime import date
def num_zile(data1, data2):
    return (data2-data1).days
data1 = date(2022, 9, 17)
data2 = date(2022, 12, 7)
print(num_zile(data1, data2), 'zile')

# Ex 21. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
# ‘Numele este de baiat’ sau ‘Numele este de fata’

def name_type(name):
    if name[-1] == 'a' or name in ('Cristina',):
        print('Numele este de fata')
    else:
        print('Numele este de baiat')

name_type('Cristina')
name_type('Bogdan')