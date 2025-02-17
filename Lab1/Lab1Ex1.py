import random
from itertools import product


def star(alfabet, nrlit):
    rezultat = []
    for lungime in range(1, nrlit + 1):  
        for varianta in sorted(product(alfabet, repeat=lungime)): #product genereaza combinatii de lungime repeat basically si gen touple
            rezultat.append(''.join(varianta))
    return rezultat
 
#def random_string(alfabet, lungime):
 #   return ''.join(random.choices(list(alfabet), k=lungime)) 
    #''.join pentru ca random.choices returneaza o lista

def concatenare(s1, s2):
    return s1 + s2

def invers(s):
    return s[::-1]

def substitutie(s, a, b):
    return s.replace(a, b)

def lungime(s):
    return len(s)

A = {'a', 'b','c'}
B = {'x', 'y', 'z'}
C = {'1', '2', '3'}


w1=star(A,random.randint(3,10))
w3=star(C,random.randint(3,10))
w2=star(B,random.randint(3,10))
s1 = random.choice(w1)
s2 = random.choice(w2)
s3 = random.choice(w3)


print('Stringurile sunt')
print(f"s1= {s1}")
print(f"s2= {s2}")
print(f"s3= {s3}")
print(f"concaternare s1  si s2 ={concatenare(s1,s2)}")
print(f"invers s3 ={invers(s3)}")
print(f"substitutie a lui  1 cu o in s3 ={substitutie(s3,'1','o')}")
print(f"lungime s2 ={lungime(s2)}")
