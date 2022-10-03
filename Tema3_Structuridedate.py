# Ex 1. 1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
#  a) Afiseaz-o
#  b) Inverseaza ordinea folosind slicing si suprascrie aceasta lista
#  c) Printeaza varianta actuala (inversata)
#  d) Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii
#  inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta
#  automat)
#  e) Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
#  Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista
#  sau sa o salvezi intr-o lista noua. Metoda gasita de tine, face suprascrierea automat si
#  permanentizeaza aceste modificari. Ambele variante isi gasesc utilitatea in functie de ce ne
#  dorim in acel moment.
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)

# Ex2. 2. Utilizand aceeasi lista, de cate ori apare 'do'?

print(note_muzicale.count('do'))

# Ex 3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# Gasiti 2 variante sa le uniti intr-o singura lista.

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista3 = lista1 + lista2
print(lista3)

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
print([*lista1, * lista2])

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista1.extend(lista2)
print(lista1)

# Ex 4. Sortati si afisati lista generata la ex anterior. Stergeti numarul 0 folosind o functie. Afisati iar lista

lista = [3, 1, 0, 2, 6, 5, 4]
lista.sort()
print(lista)
lista.remove(0)
print(lista)

# Ex 5. Folosind un if verificati lista generata la ex3 si afisati:

# Afiseaza lista este goala
lista1 = [3, 1, 0, 2, 6, 5, 4]
lista2 = []
if len(lista2)==0:
    print('Lista este goala')
else:
    print('Lista nu este goala')

# Afiseaza lista nu este goala
lista1 = [3, 1, 0, 2, 6, 5, 4]
lista2 = []
if len(lista1)>0:
    print('Lista nu este goala')
else:
    print('Lista ste goala')

# Ex 6. Folositi o functie care sa goleasca lista de la ex3

lista1 = [3, 1, 0, 2, 6, 5, 4]
del lista1[:]
print(lista1)

# Ex 7. Copy paste la ex 5. Verificati inca o data. Acum ar trebui sa se afiseze ca lista e goala.

lista1 = [3, 1, 0, 2, 6, 5, 4]
del lista1[:]
if len(lista1)==0:
    print('Lista este goala')
else:
    print('Lista nu este goala')

# Ex 8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}. Folositi o functie ca sa afisati Elevii (cheile)
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

# Ex 9. rintati cei 3 elevi si notele lor.
#  Ex: ‘Ana a luat nota {x}’
# Doar nota o veti lua folosindu-va de cheie.

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
for elev, nota in dict1.items():
    print(f'\n{elev} a luat nota {nota}')

# Ex 10. Dorel a facut contestatie si a primit 6. Modificati nota lui Dorel in 6. Printati nota dupa modificare.
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict1['Dorel'] = 6
print(dict1)

# Ex 11. Dorel a facut contestatie si a primit 6. Modificati nota lui Dorel in 6. Printati nota dupa modificare.

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
del dict1['Gigel']
dict1['Ionica'] = 9
print(dict1)

# Ex 12. Set zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}, weekend = {'sambata', 'duminica'}.
# Adaugati in zilele_sapt ‘luni’. Afisati zile_sapt

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)

# Ex 13. Folositi un if si verificati daca:
# Weekend este un subset al zilelor din sapt
# Weekend nu este un subset al zilelor din sapt
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
if weekend.issubset(zile_sapt):
    print('weekend este subset al zilelor saptamanii')
else:
    print('weekend nu este subset al zilelor saptamanii')

# Ex 14. Afisati diferentele dintre aceste 2 seturi

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
print(zile_sapt.difference(weekend))

# Ex 15. Afisati intersectia elementelor din aceste 2 seturi

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
print(zile_sapt.intersection(weekend))


# Ex 16. Ne imaginam o echipa de fotbal pt teren sintetic. 3 Schimbari maxime admise.
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
# Schimbari_max = 3
#
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# Efectuam schimbarea
# Stergem jucatorul scos din lista
# Adaugam jucatorul intrat
# Afisam a intra x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Afisati ‘mai aveti z schimbari’
# Testati codul cu diferite valori
# Google search hint
# “how to check if item is in list python”
# Jucatorul este in teren
# Intra jucator6, iese jucator1, mai am 3 schimbari
echipa = ['jucator1', 'jucator2', 'jucator3', 'jucator4', 'jucator5', 'jucator6', 'jucator7', 'jucator8', 'jucator9']
teren = ['jucator1', 'jucator2', 'jucator3', 'jucator4', 'jucator5' ]
schimbari = [1, 2, 3]
if 'jucator1' in teren and len(schimbari)>0:
     teren.remove('jucator1')
     teren.append('jucator6')
     print(f'A intrat {echipa[5]}, a iesit {echipa[0]}, mai ai {schimbari[2]} schimbari')


# Sau
echipa = ['jucator1', 'jucator2', 'jucator3', 'jucator4', 'jucator5', 'jucator6', 'jucator7', 'jucator8', 'jucator9']
teren = ['jucator1', 'jucator2', 'jucator3', 'jucator4', 'jucator5' ]
schimbari = [1, 2, 3]
while len(schimbari)>0:
 if 'jucator1' in teren:
     teren.remove('jucator1')
     teren.append('jucator6')
     print(f'A intrat {echipa[5]}, a iesit {echipa[0]}, mai ai {schimbari[2]} schimbari')

# Intra jucator 7, iese jucator2, mai am 2 schimbari
echipa = ['jucator1', 'jucator2', 'jucator3', 'jucator4', 'jucator5', 'jucator6', 'jucator7', 'jucator8', 'jucator9']
teren = ['jucator1', 'jucator2', 'jucator3', 'jucator4', 'jucator5' ]
schimbari = [1, 2, 3]
if 'jucator2' in teren and len(schimbari)>0:
     teren.remove('jucator2')
     teren.append('jucator7')
     print(f'A intrat {echipa[6]}, a iesit {echipa[1]}, mai ai {schimbari[1]} schimbari')

# Jucatorul nu este in teren
# Jucatorul 6 nu este in teren

echipa = ['jucator1', 'jucator2', 'jucator3', 'jucator4', 'jucator5', 'jucator6', 'jucator7', 'jucator8', 'jucator9']
teren = ['jucator1', 'jucator2', 'jucator3', 'jucator4', 'jucator5' ]
schimbari = [1,2,3]
if 'jucator6' not in teren and len(schimbari)>0:
     print(f'Nu se poate efectua schimbarea deoarece {echipa[5]} nu e in teren')
     print(f'Mai ai {schimbari[2]} schimbari')

# Jucatorul 9 nu este in teren

echipa = ['jucator1', 'jucator2', 'jucator3', 'jucator4', 'jucator5', 'jucator6', 'jucator7', 'jucator8', 'jucator9']
teren = ['jucator1', 'jucator2', 'jucator3', 'jucator4', 'jucator5' ]
schimbari = [1,2,3]
if 'jucator9' not in teren and len(schimbari)>0:
     print(f'Nu se poate efectua schimbarea deoarece {echipa[8]} nu e in teren')
     print(f'Mai ai {schimbari[2]} schimbari')

