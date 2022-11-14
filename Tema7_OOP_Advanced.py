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

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    # pi = 3.14
    def __init__(self):
        self.pi = 3.14

    @abstractmethod
    def arie(self):
        pass


    def descriere(self):
        print('Cel mai probabil am colturi')



class Patrat(FormaGeometrica):
    def __init__(self,latura):
        super().__init__()
        self.__latura = latura
        print(f'In initul clasei patrat, pi= {self.pi}')

    def arie(self):
        return self.__latura**2

    @property
    def latura(self):
        return self.__latura


    # @latura.setter
    def set_latura(self, new_latura):
        self.__latura = new_latura

    @latura.getter
    def get_latura(self):
        return self.__latura

    @latura.deleter
    def del_latura(self):
        self.__latura = None
        print('Am sters latura')



class Cerc(FormaGeometrica):
    def __init__(self, raza):
        super().__init__()
        self.__raza = raza
    def arie(self):
        return self.pi*(self.__raza**2)

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def set_raza(self, new_raza):
        self.__raza = new_raza

    @raza.getter
    def get_raza(self):
        return self.__raza

    @raza.deleter
    def del_raza(self):
        self.__raza = None
        print('Am sters raza')

    def descriere(self):
        print('Eu nu am colturi')

def descriere_interfata(obj):
    obj.descriere()

p1 = Patrat(4)
p1.descriere()
descriere_interfata(p1)

print(f'Latura este {p1.latura}')
print(f'Aria este {p1.arie()}')
p1.set_latura(6)
print(f'Noua latura este {p1.get_latura}')
del p1.del_latura

c = Cerc(9)
c.descriere()
descriere_interfata(c)
print(f'Raza este {c.raza}')
print(f'Aria este {c.arie()}')
c.set_latura=6
print(f'Noua raza este {c.get_raza}')
del c.del_raza

# Ex 2. Creati o clasa Student cu 2 atribute:
# - name: str, numele studentului
# - grade: int, nota acestuia
# Nota nu trebuie sa fie primita neaparat la initializare si trebuie sa nu poata fi accesata din afara clasei.
# a) Scrieti 2 functii pentru nota: get_grade care sa returneze nota studentului si set_grade care sa ii modifice nota. Asigurati`va ca nota e corecta, in caz contrar aruncati o exceptie custom (clasa) cu un mesaj relevant  - probabil va trebui sa Google-uiti putin pt exceptie :)
# b) Scrieti o functie care sa descrie studentul: "The student`s name is .... and has the grade ..." si permiteti afisarea  descrierii prin intermediul functiei print de ex:
# s = Student(...)
# print(s)
# c) Testati cele 3 functii creandu-va un student caruia sa ii dati nota 7, sa ii afisati detaliile, dupa care sa ii modificati nota in 10 si sa o afisati, iar ulterior sa o modificati in 12 pt a testa exceptia.

class WrongGradeException(Exception):
    pass


class Student:
    def __init__(self, name, grade=None):
        self.name = name
        self.set_grade(grade)

    def set_grade(self, new_grade):
        if new_grade is not None:
            try:
                new_grade = int(round(new_grade))
            except TypeError:
                raise TypeError(f"The given grade ({new_grade}) is not a number!")
            else:
                if new_grade not in range(1, 11):
                    raise WrongGradeException(f"The given grade ({new_grade}) is not valid!")
                else:
                    self.__grade = new_grade
        else:
            self.__grade = None

    def get_grade(self):
        return self.__grade

    def __str__(self):
        return f"The student`s name is {self.name} and has the grade {self.get_grade()}"

    def is_passing_grade(self):
        return self.get_grade() >= 5


my_student = Student("Christine Williams", 7)
print(my_student)
my_student.set_grade(10)
print(my_student.get_grade())
my_student.set_grade(11)


