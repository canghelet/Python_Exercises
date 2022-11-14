# Fisier Functions.py

# Ex1
#Scrieti o functie care primeste un numar natural si returneaza daca e prim sau nu
# e.g.: is_prime(13) => True
# is_prime(24) => False


from math import sqrt
def is_prime(num):
  if num <= 1 or (num % 2 == 0 and num > 2):
    return False
  return all(num % i for i in range(3, int(sqrt(num)) + 1, 2))
print(is_prime(11))
print(is_prime(16))

# Scrieti o functie care are 2 parametrii nr naturale a,b cu a<b. Functia returneaza lista numerelor prime din intervalul [a,b]
# e.g.: list_of_primes_in_interval(3, 31) => [3,5,7,11,13,17,19,23,29,31]

def list_of_primes(a,b):
  my_list = []
  for i in range(a,b + 1):
    flag = True
    for j in range(2,i):
      if i % j == 0:
        flag = False
    if flag == True:
      my_list.append(i)
  return my_list
print(list_of_primes(2,20))


# Fisier Test_Functions.py

import unittest
from Functions import is_prime, list_of_primes

# Scrieti teste unitare pentru functia is_prime
# Scrieti test unitar pentru functia list_of_primes_in_interval

class FunctionsTestCase(unittest.TestCase):
    def test_is_prime_01(self):
        expected_result = True
        actual_result = is_prime(11)
        self.assertIsInstance(actual_result, bool )
        self.assertEqual(expected_result, actual_result)

    def test_is_prime_02(self):
        expected_result = False
        actual_result = is_prime(16)
        self.assertIsInstance(actual_result, bool)
        self.assertEqual(expected_result, actual_result)

    def test_list_of_primes(self):
        expected_result = [2, 3, 5, 7, 11, 13, 17, 19]
        actual_result = list_of_primes(2, 20)
        self.assertIsInstance(actual_result, list )
        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    if __name__ == "__main__":
        unittest.main()


# EX 2. C09_EX04 (Tema ex2): Vrem sa ne cream un fisier csv numit phones in care sa avem cheile 'brand', 'model' si sa introducem lista urmatoare
# list_of_phones = [{'brand': 'Iphone', 'model': '14'}, {'brand': 'Samsung', 'model': 'Galaxy S22'}, {'brand': 'Huawei', 'model': 'P50'}]
#
# Fisierul rezultat ar trebui sa arate asa:
# brand,model
# Iphone,14
# Samsung,Galaxy S22
# Huawei,P50

import csv
list_of_phones = [{'brand': 'Iphone', 'model': '14'},
                  {'brand': 'Samsung', 'model': 'Galaxy S22'},
                  {'brand': 'Huawei', 'model': 'P50'}]

with open("Phones.csv", "w") as outfile:

    writer = csv.writer(outfile)

    writer.writerow(['brand', 'model'])
    for dictionary in list_of_phones:
        writer.writerow(dictionary.values())

# Ex 3 C09_EX04 (Tema ex3):
# 2. Write a function that will print all the details of a person in a readable way (first name, last name, age, sex, partner, children).
# The function will receive the first_name and last_name of the person.
# e.g.: show_details_by_first_and_last_name("Mike", "McMan") => First name: Mike
#                                                               Last name McMan
#                                                               Age: 52
#                                                               Sex: M
#                                                               Partner: Mary McMan
#                                                               Children: ['Anna', 'Adrian', 'Danna']

import json


def show_details_by_first_and_last_name(people_dict, first_name, last_name):
    for person_id, person in people_dict.items():
        if person['last_name'] == last_name and person['first_name'] == first_name:
            partner_first_name = people_dict.get(person.get('partner'), {}).get('first_name', '')
            partner_last_name = people_dict.get(person.get('partner'), {}).get('last_name', '')

            children = []
            for child in person['children']:
                children.append(people_dict[child]['first_name'])
            print(f"""First name: {person['first_name']}\nLast name {person['last_name']}\nAge: {person['age']}"""
                  f"""\nSex: {person['sex']}\nPartner: {partner_first_name} {partner_last_name}\nChildren: {children}""")



with open('people.json') as f:
    people = json.load(f)['people']

show_details_by_first_and_last_name(people, "Mike", "McMan")