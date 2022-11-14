
# Ex 1. C10_EX04 (Tema10 ex1): Generator pentru primele n nr prime
#def prime_gen(n):
#    pass

#for nr in prime_gen(7):
#    print(nr)
# 1
# 2
# 3
# 5
# 7
# 11
# 13

def prime_gen():
    num = 1
    prime = False
    while True:
        for i in range(2, num+1):
            if num % i == 0:
                prime = False
                if i == num:
                    prime = True
                break
        if prime:
            yield num
            num += 1
        else:
            num += 1

prime = prime_gen()
for num in range(7):
    print(next(prime))


# EX 2. C10_EX04 (Tema10 ex2): Scrieti o clasa context manager care sa afiseze timpul de executie al unei functii (de ex: get_n_primes).
# TIP: In  functia __enter__ ar trebui sa salvati timpul initial, iar in __exit__ sa determinat diferenta  dintre
# timpul curent si cel initial


from time import perf_counter

class executiontime:
    def __enter__(self):
        self.time = perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        self.time = perf_counter() - self.time

with executiontime() as t:
    def is_prime(nr):
        for i in range(2, nr // 2 + 1):
            if nr % i == 0:
                return False
        return True

    def get_n_primes(n):
        primes = []
        number = 1
        while len(primes) != n:
            if is_prime(number):
                primes.append(number)
            number += 1
        return primes
print(f'Timpul de executie este de {t.time} secunde')


# Ex 3. C10_EX05 (Tema10 ex3): Fiind date urmatoarele functii, scrieti un decorator tva_decorator pt cele 2 functii care sa returneze pretul produsului cu TVA adaugat (tva = 19%).

#def get_tv_price(price):
#    return price

#def get_laptop_price(price):
#    return price

#Ex: print(get_tv_price(2000)) # => 2380

def get_tv_price(price):
    return price

def get_laptop_price(price):
    return price

def tva_decorator(original_func):
    def wrapper_func(*args):
        initial_price = original_func(*args)
        final_price = 0.19 * initial_price + initial_price
        print(f"Price with VAT is {final_price}")
        return final_price
    return wrapper_func

@tva_decorator
def get_tv_price(price):
    print(f"Price of TV is: {price}")
    return price

@tva_decorator
def get_laptop_price(price):
    print(f"Price of laptop is: {price}")
    return price

print(get_tv_price(4000))
print(get_laptop_price(8000))


# Ex 4. C10_EX06 (Tema10 ex4): Incercati sa mai adaugati un decorator (2 in total; hint: trebuie cautat pe google cum putem adauga 2 decoratori la o singura functie) functiilor get_tv_price si get_laptop_price pentru a oferi un discount
#(discount sa fie optional si sa aiba valoare default 10%)
#Ex: print(get_tv_price(2000, discount=25))   # daca se aplicam discount prima data si apoi tva obtinem 2000 - 500 = 1500 (discount) , 1500 +   285 (tva) =  1785 pretul final :)
#get_tv_price(price)  # discount e considerat 10

def discount_decorator(original_func):
    def wrapper_func(price, discount):
        initial_price = original_func(price, discount)
        final_price = initial_price - discount/100 * initial_price
        print(f"Price with discount applied is {final_price}")
        return final_price
    return wrapper_func


@discount_decorator
@tva_decorator
def get_tv_price(price, discount):
    print(f"Price of TV is: {price}")
    return price


get_tv_price(4000, 25)
