from itertools import product
import random
import re
state='q0'
alfabet='abd'
#alfabet='abcd'
tranzitii={
    'q0': {'a': 'q1', 'b': 'q0', 'c': 'q0', 'd': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2', 'c': 'q1', 'd': 'q1'},
    'q2': {'a': 'q2', 'b': 'q2', 'c': 'q2', 'd': 'q3'},
    'q3': {'a': 'q3', 'b': 'q3', 'c': 'q3', 'd': 'q3'}
}
def star(alfabet, nrlit):
    rezultat = []
    for lungime in range(1, nrlit + 1):  
        for varianta in sorted(product(alfabet, repeat=lungime)): 
            word=''.join(varianta)
            if len(word) == 6:
                counts = [word.count(char) for char in set(word)]
                if counts.count(2) == 3:
                    rezultat.append(word)



    return rezultat
 
word=""
L=star(alfabet,6)
def verifica(cuvant, tranzitii,state):
    for char in cuvant:
        if char in tranzitii[state]: 
            state=tranzitii[state][char]
        else:
           # print('not')
            return False
    return state=='q3'
"""
s1=random.choice(L)
s2=random.choice(L)
s3=random.choice(L)
print(f"s1= {s1} apare in L ? {verifica(s1,tranzitii,'q0')}")

print(f"s2= {s2} apare in L ? {verifica(s2,tranzitii,'q0')}")
print(f"s3= {s3} apare in L ? {verifica(s3,tranzitii,'q0')}")
"""

for cuv in L:
    print(f"s= {cuv} apare in L ? {verifica(cuv,tranzitii,'q0')}")


