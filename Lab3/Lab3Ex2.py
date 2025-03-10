n = 5  
nr = 0 
s = {'q0'}  #set

tranzitii = {
    'q0': {'v': {'q1'},'q':{'q3'}}, #gol
    'q1': {'v': {'q1', 'q2'}, 'p': {'q0', 'q1'},'q':{'q3'}}, #partial
    'q2': {'p': {'q1'},'q':{'q3'}} ,#plin
    'q3':{}
}

def ftranzitii(simbol):
    global s
    new_s = set()
    for state in s:
        if simbol in tranzitii.get(state, {}):
            new_s.update(tranzitii[state][simbol]) 
    if new_s:
        s = new_s
        print(f"tranzitie pana la {s}")
    
    else:
        print("!!!TNf")

while True:
    print("\n\nState:", s)
    print("Nr curent masini:", nr)
    action = input("Vine : 'v' , Pleaca  : 'p', 'q' iesire ").strip().lower()
    print("\n\n\n")

    if action == 'v':
        if nr < n:
            nr += 1
            ftranzitii('v')
            if nr == n:
                s = {'q2'} 
        else:
            print("!!!Parcare Plina")
    elif action == 'p':
        if nr > 0:
            nr -= 1
            ftranzitii('p')  
            if nr == 0:
                s = {'q0'}  
        else:
            print("!!!Parcare goala")
    elif action == 'q':
        ftranzitii('q')
    else:
        print("!!!Input gresit")
    if s=={'q3'}:
        print("Iesireee")
        break
