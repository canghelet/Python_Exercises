# EX 1. Clasa Cerc
#  Atribute: raza, culoare
#  Constructor pt ambele atribute
#
#  Metode:
#  descrie_cerc() - va PRINTA culoarea si raza
#  aria() - va RETURNA aria
#  diametru()
#  circumferinta()

import math

class Cerc:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare
    def descrierea_cercului(self):
        print(f'Raza: {self.raza}')
        print(f'Culoare: {self.culoare}')
    def aria_cerc(self):
        return math.pi*(self.raza**2)
    def diametru_cerc(self):
        return 2*self.raza
    def circumferinta_cerc(self):
        return 2*math.pi*self.raza

Cerc1 = Cerc(9,'rosu')
Cerc2 = Cerc (10, 'albastru')
Cerc1.descrierea_cercului()
print(Cerc1.aria_cerc())
print(Cerc1.diametru_cerc())
print(Cerc1.circumferinta_cerc())
Cerc2.descrierea_cercului()
print(Cerc2.aria_cerc())
print(Cerc2.diametru_cerc())
print(Cerc2.circumferinta_cerc())


# Ex 2. Clasa Dreptunghi
#  Atribute: lungime, latime, culoare
#  Constructor pt toate atributele
#
#  Metode:
#  descrie()
#  aria()
#  perimetrul()
#  schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie at

class Dreptunghi:
    lungime = None
    latime = None
    culoare = None
    culoare_noua = None

    def __init__(self, lungime, latime, culoare, culoare2):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare
        self.culoare_noua = culoare2

    def descriere_dreptunghi(self):
        print(f'Lungime: {self.lungime}')
        print(f'Latime: {self.latime}')
        print(f'Dreptunghiul este {self.culoare}')
    def aria_dreptunghi(self):
        return self.lungime*self.latime
    def perimetru_dreptunghi(self):
        return (self.lungime+ self.latime)*2
    def schimbare_culoare(self):
        print(f'Culoarea noua este {self.culoare_noua}')

Drept1 = Dreptunghi(10,20,'rosu', 'albastru')
Drept2 = Dreptunghi(10,30, 'alb', 'galben')
Drept1.descriere_dreptunghi()
print(Drept1.aria_dreptunghi())
print(Drept1.perimetru_dreptunghi())
Drept1.schimbare_culoare()
Drept2.descriere_dreptunghi()
print(Drept2.aria_dreptunghi())
print(Drept2.perimetru_dreptunghi())
Drept2.schimbare_culoare()

# Ex 3.  Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
#
#  Metode:
#  descrie()
#  nume_complet()
#  salariu_lunar()
#  salariu_anual()
#  marire_salariu(procent)

class Angajat:
    nume = None
    prenume = None
    salariu = None
    marire_salariu = None

    def __init__(self,nume, prenume, salariu, marire ):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
        self.marire_salariu = marire

    def descriere(self):
        print(f'Nume: {self.nume}')
        print(f'Prenume: {self.prenume}')
        print(f'Salariu: {self.salariu}')

    def nume_complet(self):
        return 'Numele complet:' +self.nume+ ' ' +self.prenume
    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu*12

    def marire_angajat(self):
        return str((self.marire_salariu)/(self.salariu)*100) + '%'

Angajat1 = Angajat('Williams', 'Andrew', 2000, 75)
Angajat1.descriere()
print(Angajat1.nume_complet())
print(Angajat1.salariu_lunar())
print(Angajat1.salariu_anual())
print(Angajat1.marire_angajat())
Angajat2 = Angajat('Brown', 'Amy', 3000, 100)
Angajat2.descriere()
print(Angajat2.nume_complet())
print(Angajat2.salariu_lunar())
print(Angajat2.salariu_anual())
print(Angajat2.marire_angajat())

# Ex 4. Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate
#
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
#  creditare_cont(suma)

class Cont:
    iban = None
    titular_cont = None
    sold = None
    debitare_cont = None
    creditare_cont = None

    def __init__(self, iban, titular,sold, debitare, creditare):
        self.iban = iban
        self.titular_cont = titular
        self.sold = sold
        self.debitare_cont = debitare
        self.creditare_cont = creditare

    def descrie(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold}')

    def suma_dupa_debitare(self):
         return self.sold - self.debitare_cont

    def suma_dupa_creditare(self):
        return self.sold + self.creditare_cont

Cont1 = Cont('RO77INGB1234000023455553', 'John Brown', 10000, 4000, 3000)
Cont2 = Cont('RO77INGB2345678910007848', 'Mary Smith', 8000, 3000, 2000)
Cont1.descrie()
print(Cont1.suma_dupa_debitare())
print(Cont1.suma_dupa_creditare())
Cont2.descrie()
print(Cont2.suma_dupa_debitare())
print(Cont2.suma_dupa_creditare())

# EX 8. C06_EX01 (Homework ex8): Creati un fisier rectangle.py in care sa va definiti o clasa Rectangle, care are 2 atribute width si length,
# instantiate in cadrul constructorului cu 2 valori integer.
# # a) Pentru clasa respectiva creati o functie get_area care returneaza aria dreptunghiului.
#  b) Creati si o functie display care afiseaza dreptunghiul folosind un parametru optional pentru a desena; in cazul in care
#  parametrul nu este dat, se foloseste ca default caracterul *.
# c) Creati un fisier nou test_rectangle.py unde sa va importati clasa Rectangle (din rectangle.py) si testati codul.
# Exemplu de rulare:
# new_rectangle = Rectange(2, 4)
# print(new_rectangle.get_area()) => 8
# new_rectangle.display() => ****     sau: new_rectangle.display('#') => ####
#                            ****                                        ####
# Fisier rectangle.py

class Rectangle:
    width = None
    length = None

    def __init__(self, width, length=2):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

    def display(self,character = '*'):
        for i in range(self.length):
            for j in range(self.width):
                if(i == 0 or i == self.length - 1 or j == 0 or j == self.width - 1):
                    print(character, end = '  ')
                else:
                    print(' ', end = '  ')
            print()

# Fisier test_rectangle.py
# Importam clasa rectangle din fisierul rectangle.py in fisierul test_rectangle.py

from rectangle import Rectangle
new_rectangle = Rectangle(4)
new_rectangle1 = Rectangle(4,3)
print(new_rectangle.get_area())
new_rectangle.display()
print(new_rectangle1.get_area())
new_rectangle1.display()