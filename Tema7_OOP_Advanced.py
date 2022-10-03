# Ex 1.
# ABSTRACTION
# Clasa abstracta FormaGeometrica
# Contine un field PI=3.14
# Contine o metoda abstracta aria (optional)
# Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’

# INHERITANCE
# Clasa Patrat - mosteneste FormaGeometrica
# constructor pt latura

# ENCAPSULATION
# latura este proprietate privata
# Implementati getter, setter, deleter pt latura
# Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)
# Clasa Cerc - mosteneste FormaGeometrica
# constructor pt raza
# raza este proprietate privata
# Implementati getter, setter, deleter pt raza
# Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte (optional, doar daca ati ales sa implementati metoda abstracta aria)

# POLYMORPHISM
# Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
# Creati un obiect de tip Patrat si jucati-va cu metodele lui
# Creati un obiect de tip Cerc si jucati-va cu metodele lui

class FormaGeometrica():
    def __init__(self):
        self.pi = 3.14
    def descrie(self):
        print('Cel mai probabil am colturi')

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        super().__init__()
        self.__latura = latura
    def get_latura(self):
        print(self.__latura)
    def set_latura(self,a):
        self.__latura = a
        print(self.__latura)
    def del_latura(self):
        del self.__latura
        print('Am sters latura')

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        super().__init__()
        FormaGeometrica.__init__(self)
        self.__raza = raza
    def get_raza(self):
        print(self.__raza)
    def set_raza(self,b):
        self.__raza = b
        print(self.__raza)
    def del_raza(self):
        del self.__raza
        print('Am sters raza')
    def descrie(self):
        print('Eu nu am colturi')

Patrat1 = Patrat(3000)
Patrat1.get_latura()
Patrat1.set_latura(2000)
Patrat1.del_latura()
Patrat1.descrie()
Cerc1 = Cerc(20)
Cerc1.get_raza()
Cerc1.set_raza(30)
Cerc1.del_raza()
Cerc1.descrie()

# Ex 2. Creati o clasa Student cu 2 atribute:
# - name: str, numele studentului
# - grade: int, nota acestuia
# Nota nu trebuie sa fie primita neaparat la initializare si trebuie sa nu poata fi accesata din afara clasei.
# a) Scrieti 2 functii pentru nota: get_grade care sa returneze nota studentului si set_grade care sa ii modifice nota. Asigurati`va ca nota e corecta, in caz contrar aruncati o exceptie custom (clasa) cu un mesaj relevant  - probabil va trebui sa Google-uiti putin pt exceptie :)
# b) Scrieti o functie care sa descrie studentul: "The student`s name is .... and has the grade ..." si permiteti afisarea  descrierii prin intermediul functiei print de ex:
# s = Student(...)
# print(s)
# c) Testati cele 3 functii creandu-va un student caruia sa ii dati nota 7, sa ii afisati detaliile, dupa care sa ii modificati nota in 10 si sa o afisati, iar ulterior sa o modificati in 12 pt a testa exceptia.

class Student():
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade
    def get_grade(self):
        print(self.__grade)

    def set_grade(self,a):
        self.__grade = a
        print(self.__grade)
    def describe(self):
        print(f"The student's name is {self.name} and has the grade {self.__grade}")

    def __str__(self):
        return f'The student\'s name  is {self.name} and has the grade {self.__grade}'


class InvalidGradeError(Exception):
    def __init__(self,name, grade):
        super().__init__(name, grade)
        self.__grade = grade
try:
    grade = int(input('Enter your grade '))
    if grade <1 or grade >10:
        raise InvalidGradeError('Sorry, the grade does not exist! ')
    print(f'Student has the grade {grade} ')
except ValueError:
    print('Invalid input')

except InvalidGradeError as ige:
    print(ige)

s = Student('Corina', 9)
s.get_grade()
s.set_grade(10)
s.describe()
print(s)