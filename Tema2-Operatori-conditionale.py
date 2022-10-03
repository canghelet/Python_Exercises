
# Ex 1

# "if else" evalueaza daca o conditie este adevarata sau falsa. Daca conditia "if" este adevarata, se executa codul.
# In caz contrar, se executa "else" statement.

# Ex 2. Verificati si afisati daca x este numar natural sau nu

x = int(input('Introdu numar: '))
if x >= 0 and isinstance(x, int):
    print(f'Numarul {x} este natural')
else:
    print(f'Numarul {x} nu este natural')

# Ex 3. Verificati si afisati daca x este numar pozitiv, negativ sau neutru

x = int(input('Introdu numar: '))
if (x) > 0:
  print('Pozitiv')
elif (x) < 0:
    print('Negativ')
else:
    print('Neutru')

# Ex 4. Verificati si afisati daca x este intre -2 si 13

x = int(input("Introduceti un numar: "))
if x in range(-2, 13):
    print(True)
else:
    print(False)

# Ex 5. Verificati si afisati daca dif dintre x si y e mai mica decat 5

x = int(input('introduceti un numar '))
y = int (input('introduceti un alt  numar '))
if (x-y)<5:
    print('Diferenta dintre cele doua numere este mai mica decat 5')
elif (x-y)>5:
    print('Diferenta dintre cele doua numere este mai mare decat 5')
else:
    print ('Diferenta dintre cele 2 numere este egala cu 5')

# Ex 6. Verificati daca x NU este intre 5 si 27. (a se folosi ‘not’)

x = int(input('Introduceti un numar '))
if not(x>5 and x<27):
    print ('Numarul nu este intre 5 si 27')
elif x>5 and x<27:
    print('Numarul este intre 5 si 27')

# Ex 7. x si y (int). Verificati si afisati daca sunt egale, daca nu afisati care din ele este mai mare

x = int(input('Introduceti o valoare '))
y = int(input('Mai introduceti o valoare '))
if x > y:
    print( x, "e mai mare decat", y)
elif x < y:
    print (y, "e mai mare decat", x)
else:
    print (x, "si", y, "sunt egale")


# Ex 8. x, y, z - laturile unui triunghi. Afisati daca triunghiul este isoscel, echilateral sau oarecare.
# x = int(input("x = "))

X = int(input('Introduceti valoare latura A '))
y = int(input('Introduceti valoarea laturei B '))
z = int(input('Introduceti valoarea laturei C '))
if X==y and y==z:
    print('triunghiul este echilateral')
elif X==y or y==z or y==z:
    print('triunghiul este isoscel')
else:
    print ('triunghiul este oarecare')


# Ex 9. Cititi o litera de la tastatura. Verificati si afisati daca e vocala sau nu.

litera = input('Introdu o litera: ')
vocale = ('a', 'e', 'i', 'o', 'u')
if litera.lower() in vocale:
    print('Litera e vocala')
else:
    print('Litera nu e vocala')

# Ex 10. Transformati si printati notele din sistem romanesc in  >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
nota = input("Introduceti nota: ")
if nota.replace('-', '', 1).replace('.', '', 1).isnumeric():
    nota = round(float(nota))
    if nota > 10 or nota < 1:
        print("Introduceti o valoare intre 1 si 10 ")
    elif nota > 9:
        print("A")
    elif nota > 8:
        print("B")
    elif nota > 7:
        print("C")
    elif nota > 6:
        print("D")
    elif nota > 4:
        print("E")
    else:
        print("F")
else:
    print("Nu ati introdus un numar ")


# Ex 11. Verificati daca x are minim 4 cifre (x e int) (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

x = input('x = ')
x = str(x)

if x[0] == '-':
    x = x[1:]
if x[0] == '0':
    x = x[1:]

if x.isnumeric():
    if len(x) < 4:
        print("Numarul nu are minim 4 cifre!")
    else:
        print("Numarul are minim 4 cifre!")
else:
    print("Nu ati introdus un numar valid!")

# Ex 12.Verificati daca x are exact 6 cifre.

x = input('x = ')
x = str(x)
if x.replace('-', '', 1).replace('.', '', 1).isnumeric():
    if x[0] == '0':
        x = x[1:]
    if (len(x) == 6 and '.' not in x) or (len(x) == 7 and ('.' in x or '-' in x)) or (len(x) == 8 and '.' in x and '-' in x):
        print('Numarul are exact 6 cifre!')
    else:
        print('Numarul nu are exact 6 cifre!')
else:
    print("Nu ati introdus un numar valid!")


# ex 13. Verificati daca x este numar par sau impar (x e int)

x = int(input('Introdu numar '))
if (x % 2)==0:
    print('Numarul este par')
else:
    print('Numarul este impar')

# Ex 14. x, y, z (int). Afisati care este cel mai mare dintre ele?

x = int(input('Introdu primul numar: '))
y = int(input('Introdu al doilea numar: '))
z = int(input('Introdu al treilea numar: '))
if (x == y and x > z) or (x == z and x > y) or (y == z and y > x):
    print("Doua numere sunt egale si mai mari decat al 3-lea")
else:
    if x > y and x > z:
        print(f"x={x} e cel mai mare")
    elif y > x and y > z:
        print(f"y={y} e cel mai mare")
    else:
        print(f"z={z} e cel mai mare")

# Ex 15. x, y, z - reprezinta unghiurile unui triunghi. Verificati si afisati daca triunghiul este valid sau nu

X = int(input('Introdu primul unghi: '))
y = int(input('Introdu al doilea unghi: '))
z = int(input('Introdu al treilea unghi: '))


if (X+y+z == 180 and X != 0 and y != 0 and z != 0):
    print("\nEste un triunghi valid")
else:
    print("\nNu este un triunghi valid")

# Ex 16. vand stringul: 'Coral is either the stupidest animal or the smartest rock' cititi de la tastatura un int x.
#  Sa se afiseze stringul fara ultimele x caractere (ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte')
my_string = 'Coral is either the stupidest animal or the smartest rock'
size = len(my_string)
x = int(input('Introdu numar '))
print(my_string[: size -x])

# Ex 17. Acelasi string; declarati un string nou care sa fie format din primele 5 caractere + ultimele 5
my_string = 'Coral is either the stupidest animal or the smartest rock'
y = (my_string[0:5] + my_string[-5:])
print(y)

# sau
my_string = 'Coral is either the stupidest animal or the smartest rock'
count = 0
for i in my_string:
      count = count + 1
new_string = my_string[ 0:5 ] + my_string [count - 5: count ]
print("String nou = "+ new_string)

# Ex 18. Acelasi string.
# Salvati intr-o variabila si afiseaza indexul de start al cuvantului rock.
# (hint: este o functie care va ajuta sa faceti asta).
# Folosind aceasta variabila + slicing, afisati tot stringul pana la acest cuvant
# output: 'Coral is either the stupidest animal or the smartest '
my_string = 'Coral is either the stupidest animal or the smartest rock'
rock_index = my_string.index('rock')
print(f'Indexul de start al cuvantului rock este {rock_index}')
print(my_string[:rock_index])

# Ex 19. Cititi de la tastatura un string. Verificati daca primul si ultimul caracter sunt la fel.
#  Se va folosi un assert. Atentie: se doreste ca programul sa fie case insensitive: 'apA' e acceptat.
my_string = input("Introduceti un string: ")
assert my_string[0].lower() == my_string[-1].lower()

# Ex 20. Avand stringul '0123456789'. Afisati doar numerele pare.
# # Apoi afisati doar numerele impare (hint: folositi slicing, controlati din pas)
my_str = '0123456789'
print(my_str[0:len(my_str):2])
print(my_str[1:len(my_str):2])

# Ex 21. Joc ghicit zarul:
# Cautati pe net si vedeti cum se genereaza un numar random.
# Ne imaginam ca dam cu zarul si salvam acest numar in dice_roll.
# Luati un nr ghicit de la utilizator.
# Verificati si afisati daca utilizatorul a ghicit.
# 3 optiuni:
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# Felicitari! Ai ghicit. Ai ales x si zarul a fost y.

import random

numar_secret = random.randint(0,6)
numar_ghicit = None
while numar_ghicit != numar_secret:
    numar_ghicit = int(input('Ghiceste un numar intre 0 si 6\n'))
    if numar_secret > numar_ghicit:
        print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {numar_ghicit}, dar a fost {numar_secret}')
    elif numar_secret < numar_ghicit:
        print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_ghicit}, dar a fost {numar_secret}')
    else:
        print(f'Ai ghicit. Felicitări! Ai ales {numar_secret} si zarul a fost {numar_secret}')



