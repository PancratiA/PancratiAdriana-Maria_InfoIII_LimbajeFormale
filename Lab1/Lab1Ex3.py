from itertools import product

#merge
"""
def palindroame(alfabet, nrlit):
    for lungime in range(1, nrlit + 1):
        for varianta in sorted(product(alfabet, repeat=lungime)):  
            if is_palindrom(''.join(varianta)): 
                print(''.join(varianta))
               
    return 

def is_palindrom(s):
    return s == s[::-1]
"""

def palindroame(alfabet, nrlit):
    for lungime in range(1, nrlit + 1):
        new_lungime = (lungime + 1) // 2 
        for jum in sorted(product(alfabet, repeat=new_lungime)):
          
            if lungime % 2 == 0:
                palindrome =  ''.join(jum) +  ''.join(jum)[::-1]
            else:
                palindrome =  ''.join(jum) +  ''.join(jum)[:-1][::-1] #sterg ultima litera apoi fac inversu
            print(palindrome)


E = {'0', '1', '2'}
palindroame(E, 5)