def gramatica(lungime,a,b):
    result = ['ε']

    for nrlit in range(1, lungime + 1):
        for i in range(0, nrlit + 1):
            result.append(a * (nrlit - i) + b * i)

    return result



rez = gramatica(4,'a','b')

for s in rez:
    print(s)
