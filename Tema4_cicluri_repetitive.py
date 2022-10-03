# Ex 1. Avand lista
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# A. Folositi un for ca sa iterati prin toata lista cu ajutorul indexilor si sa afisati
# ‘Masina mea preferata este x’
# B. Faceti acelasi lucru cu un for each
# C. Faceti acelasi lucru cu un while
# folosind for
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for marca in masini:
    print(f"Masina mea preferata este {marca}")

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in range(0, len(masini)):
    print(f'Masina mea preferata este {masini[i]}')

# folosing while
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
i =0
while (i<len(masini)):
    print(f'Masina mea preferata este {masini[i]}')
    i+=1

# Ex 2.  Aceeasi lista. Folositi un for in for.
# Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul (v1 - caracter, v2 - element)
# Printati varianta finala a listei.
# Incercati sa rezolvati atat v1 => output: ['aUDi', 'vOLVo', 'bMw', 'mERCEDEs', 'aSTON MARTIn', 'lASTUn', 'fIAt', 'tRABANt', 'oPEl']
# Cat si v2 => output: ['audi', 'VOLVO', 'BMW', 'MERCEDES', 'ASTON MARTIN', 'LASTUN', 'FIAT', 'TRABANT', 'opel']
# v1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in range(0, len(masini)):
    masini[i] = (masini[i][0].lower()+masini[i][1:-1].upper()+masini[i][-1].lower())
print(masini)

# v2
for i in range(len(masini)):
    if i == 0 or i == len(masini)-1:
        masini[i] = masini[i].lower()
    else:
        masini[i] = masini[i].upper()
print(masini)

# Ex 3. Aceeasi lista,
# Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea cu for
# Daca masina e mercedes (if)
# Printam ‘am gasit masina dorita de dvs’
# Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel:
# Printam Am gasit masina X. Mai cautam

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for marca in masini:
    if marca =='Mercedes':
        print('Am gasit masina  dorita de dvs')
        break
    else:
        print(f'Am gasit masina {marca}. Mai cautam')

# Ex 4. Aceasi lista.
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
# Folositi un cuvant cheie care sa dea skip la ce urmeaza
# Printati S-ar putea sa va placa masina x
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for marca in masini:
    if marca =='Trabant' or marca == 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {marca}')

# Ex 5. Modernizati parcul de masini. Creati o lista goala, masini_vechi. Iterati prin masini.
# Cand gasiti Lastun sau Trabant:
# Salvati aceste masini in masini_vechi
# Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for i in range(len(masini)):
    if masini[i] in ('Trabant', 'Lastun'):
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
print(f"Modele vechi: {masini_vechi}")
print(f"Modele noi: {masini}")

# Ex 6. Avand dict:
# pret_masini = {
# 'Dacia': 6800,
# 'Lastun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina x
# Iterati prin lista

pret_masini = {'Dacia': 6800,'Lastun': 500,'Opel': 1100,'Audi': 19000,'BMW': 23000}
for marca, pret in pret_masini.items():
    if pret <= 15000:
        print(f'Pentru un buget de sub 15000 puteti alege masina {marca}')

# Ex 7. Avand lista
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

counter_3 = 0
for n in numere:
    if n == 3:
        counter_3 += 1
print(f"Nr 3 apare de {counter_3} ori")


# Ex 8. Aceeasi lista. Iterati prin ea.
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
total =0
ele = 0
while(ele < len(numere)):
    total = total + numere[ele]
    ele += 1
print(total)

# Sau
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
total = 0
for ele in range(0, len(numere)):
    total = total + numere[ele]
print(total)

# Ex 9. Aceeasi lista. Iterati prin ea.
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numar_mare = numere[0]
for numar in numere:
    if numar > numar_mare:
        numar_mare = numar
print(numar_mare)

# Sau

numere=[5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
length = len(numere)-1
for i in range(length):
    if numere[i] > numere[i + 1]:
        numere[i], numere[i + 1] = numere[i + 1], numere[i]
print(numere[-1])

# Ex 10. Aceeasi lista. Iterati prin ea.
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(0, len(numere)):
    if (i>=0):
        numere[i] = (-abs(numere[i]))
print(numere)

# Ex 11. alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterati prin lista alte_numere
# Populati corect celelalte liste
# Afisati cele 4 liste la final

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for i in alte_numere:
    if (i>0):
        numere_pozitive.append(i)
    else:
        numere_negative.append(i)
    if (i%2 ==0):
        numere_pare.append(i)
    else:
        numere_impare.append(i)
print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)

# Ex 12. ceeasi lista. Ordonati crescator lista fara sa folositi sort
# Va puteti inspira vizual de aici
# https://www.youtube.com/watch?v=lyZQPjUT5B4
# Folosind bubble sort
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for j in range(len(alte_numere)):
    swapped = False
    i = 0
    while i<len(alte_numere)-1:
        if alte_numere[i]>alte_numere[i+1]:
            alte_numere[i],alte_numere[i+1] = alte_numere[i+1],alte_numere[i]
            swapped = True
        i = i+1
    if swapped == False:
        break
print (alte_numere)

# Ex 13. Ghicitoare de numar.
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
# User alege un numar
# Programul ii spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitari! Ai ghicit!

import random

numar_secret = random.randint(1,30)
numar_ghicit = None
while numar_ghicit != numar_secret:
    numar_ghicit = int(input('Ghiceste un numar intre 1 si 30\n'))
    if numar_secret > numar_ghicit:
        print(f'Nr secret e mai mare')
    elif numar_secret < numar_ghicit:
        print(f'Nr secret e mai mic')
    else:
        print(f'Felicitari! Ai ghicit')

# Ex 14. Alegeti un numar de la tastatura
# Scrieti un program care sa genereze in consola urmatoarea piramida

linii = int(input('Introdu numar: '))
for i in range(linii+1):
    for j in range(i):
        print(i, end=" ")
    print(" ")

# EX 15. tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
#]
# Iterati prin lista 2d
# Printati ‘Cifra curenta este x’
# (hint: nested for - adica for in for)

tastatura_telefon = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[0]]
for rand in tastatura_telefon:
    for tasta in rand:
        print(f'Cifra curenta este {tasta}')