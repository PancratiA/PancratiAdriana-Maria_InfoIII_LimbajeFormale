import random
from itertools import product

def star(alfabet, nrlit):
    rezultat = []
    for lungime in range(1, nrlit + 1):  
        for varianta in sorted(product(alfabet, repeat=lungime)):
            rezultat.append(''.join(varianta))
    return rezultat



def concat(s1, s2):
    return s1 + s2

def repetare(s, n):
    return s * n


def reverse(s):
    return s[::-1]

def extract(s,i,j):
    return s[i:j+1] #pt ca cere 1-2-3 far 4 altfel


def replace(s,sub, new_sub):
    return s.replace(sub,new_sub,1) #1 pt 'prima' 


simboluri={'A','B','C'}
sigma1 = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
sigma2 = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'}
sigma3 = {'x1', 'x2', 'x3', 'x4', 'x5', 'y1', 'y2', 'y3', 'y4', 'y5'}

sigma = sigma1.union(sigma2).union(sigma3).union(simboluri) #ceapa -> fara repetitii
L = star(sigma,random.randint(2,5))
s = random.choice(L)


#print(f"Limbaj L= {L}") #wee lag
print(f"s= {s}")
print(f"s concat cu string '<333' ={concat(s,'<333')}")
print(f"Repetare a lui s de 5ori ={repetare(s,5)}")
print(f"invers s={reverse(s)}")
random1=random.randint(0,len(s)-1)
random2=random.randint(0,len(s)-1)
substring=extract(s,min(random1,random2), max(random1,random2))
print(f"Extragere din s a unui substring random= {substring}")
print(f"Replace la {substring}  cu '<333' in s={replace(s,substring,'<333')}")



