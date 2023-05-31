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

# 5.Clasa Factura
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie

# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti

# Factura seria x numar y
# Data: generati automat data de azi
# Produs | cantitate | pret bucata | Total
# Telefon |      7       |       700       | 4900

from datetime import date

class Bill:
    series = "7777.2.555.88.8"

    def __init__(self, numar, produs, cantitate, pret):
        self.numar = numar
        self.produs = produs
        self.cantitate = cantitate
        self.pret = pret

    def schimba_cantitate(self, cantitate_schimbata):
        self.cantitate = cantitate_schimbata

    def schimba_pret(self, pret_nou):
        self.pret = pret_nou

    def schimba_produs(self, nume_nou_produs):
        self.produs = nume_nou_produs

    def genereaza_factura_v1(self):
        print(
            f"Data: {date.today()}\nProdus|Cantitate|Pret pe bucata|Total\n{self.produs}|{self.cantitate}|{self.pret}|{self.cantitate * self.pret}")

    def genereaza_factura_v2(self):
        print(f"Data: {date.today()}\n| Produs | Cantitate| Pret pe bucata | Total |")
        print("-" * 47)
        print(
            f"| {self.produs:^8}|{self.cantitate:^10}|{self.pret:^16}|{self.cantitate * self.pret:^7}|")


b1 = Bill(1001, "Telefon", 7, 700)
b1.genereaza_factura_v1()

print('\nv2:')

b1.genereaza_factura_v2()


# 6. Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate masinile cand ies din fabrica sunt gri
# Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
# Culori disponibile = alegeti voi 5-7 culori
# Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
# Inmatriculata = False

# Constructor: model, viteza_maxima

# Metode:
# descrie() (se vor printa toate atributele, inafara de culori_disponibile)
# inmatriculare() - va schimba atributul inmatriculata in True
# vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
# accelereaza(viteza) - se va accelera la o anumita viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
# franeaza() - masina se va opri si va avea viteza 0


class SpeedError(Exception):
    pass

class Car:
    def __init__(self, model, viteza_maxima):
        self.brand = "Tesla"
        self.model = model
        self.viteza_maxima = viteza_maxima
        self.viteza_actuala = 0
        self.culoare = 'Gri'
        self.culori_disponibile = set(["Gri", "Alb", "Negru", "Rosu", "Albastru", "Verde", "Mov","Portocaliu"])
        # sau {"Grey", "White", "Black", "Red", "Blue", "Green", "Purple"}
        self.inmatriculata = False

    def descriere(self):
        print(
            f"""Felicitari, ai achizitionat o noua masina {self.brand} {self.model}. Atinge viteza maxima de {self.viteza_maxima}km/h. """
            f"""Are culoarea {self.culoare}, insa tine minte ca o poti schimba oricand contra sumei de 99999 RON. """
            f"""In prezent atinge {self.viteza_actuala}km/h. Este inmatriculata? {'Da' if self.inmatriculata else 'Nu'}""")

    def schimbare_culoare(self, culoare_noua):
        if culoare_noua in self.culori_disponibile:
            self.culoare = culoare_noua
            print(f"Am vopsit masina in culoarea {self.culoare}.")
        else:
            print(f"Culoarea pe care o doresti nu este disponibila... Poti alege din culorile disponibile: {self.culori_disponibile}")

    def masina_inmatriculata(self):
        self.inmatriculata= True

    def accelereaza(self, viteza_noua):
        if viteza_noua < 0:
            raise SpeedError(f"!!Speed error!! {viteza_noua} < 0!")
        else:
            if viteza_noua > self.viteza_maxima:
                self.viteza_actuala = self.viteza_maxima
            else:
                self.viteza_actuala = viteza_noua

        print(f"VRRUUUM, ai atins viteza de {self.viteza_actuala}km/h!!!")

    def incetineste(self):
        self.viteza_actuala = 0
        print(f"SCRRRRR, ai incetinit la {self.viteza_actuala}km/h...")


c1 = Car(model="X", viteza_maxima=250)
c1.descriere()
c1.masina_inmatriculata()
print(f"Dar acum: este inmatriculata acum?? {c1.inmatriculata}")
c1.schimbare_culoare("Rosu")
c1.accelereaza(100)
c1.accelereaza(300)
c1.incetineste()
c1.schimbare_culoare("Galben")
c1.accelereaza(-15)


# 7. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

# Metode:
# adauga_task(nume, descriere) - se va adauga in dict
# finalizeaza_task(nume) - se va sterge din dict
# afiseaza_todo_list() - doar cheile
# afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
# daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
# Daca acesta raspunde nu - la revedere
# daca raspunde da - il cerem detalii task si salvam nume+detalii in dict

class TodoList:
    def __init__(self):
        self.todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere

    def finalizeaza_task(self, nume):
        print(f"Task {self.nume}: \u2713. Sterge de pe lista.")
        #         self.todo.pop(name)
        del self.todo[nume]

    def arata_lista(self):
        print(list(self.todo.keys()))

    def arata_detalii_task(self, nume_task):
        if nume_task not in self.todo:
            to_add = input(f"Task-ul {nume_task} nu se afla pe lista. Doresti sa il adaugi? [da/nu]: ")
            if to_add.lower().startswith('da'):
                detalii = input(f"Adauga o descriere pentru task-ul {nume_task}: ")
                self.todo[nume_task] = detalii
            else:
                print("Ok, La revedere!")
        else:
            print(f">Task: {nume_task}\n>Descriere: {self.todo[nume_task]}")


todo_list = TodoList()
todo_list.arata_lista()
todo_list.adauga_task("Paste",
                   "Aceasta este o reteta delicioasa pentru paste:\n\t 1. fierbe niste apa \n\t 2. se ia o mana de paste... \n\t 3. rupe-le in doua... \n\t 4. adauga pastele in apa.")
todo_list.arata_lista()
todo_list.arata_detalii_task("Paste")
todo_list.arata_detalii_task("Exercitiu")
todo_list.arata_detalii_task("Exercitiu")


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