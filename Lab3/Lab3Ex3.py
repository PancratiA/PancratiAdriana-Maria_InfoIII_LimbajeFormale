
state = 'q0'

tranzitii = {
    'q0': {0: {'q0', 'q1', 'q2'}, 1: {'q1', 'q2'}, 2: {'q2'}},
    'q1': {1: {'q1', 'q2'}, 2: {'q2'}},
    'q2': {2: {'q2'}}
}
def all_tranzitii(state, input, tranzitii, path=None):
    if path is None:
        path = [state]
    
    if not input:
        print(" - ".join(path), path[-1] == 'q2')
        return

    simbol = int(input[0])
    
    if simbol in tranzitii[state]:
        for urmat in tranzitii[state][simbol]:
            all_tranzitii(urmat, input[1:], tranzitii, path + [urmat])  #input devine input fara primu caracter
    else:
        all_tranzitii(state, input[1:], tranzitii, path + [state]) #pastreaza state curent in caz ca nu are une mere

input = "000011"


all_tranzitii(state, input, tranzitii)
