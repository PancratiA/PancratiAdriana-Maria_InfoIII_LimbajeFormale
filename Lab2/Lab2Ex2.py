

state='q0'
end_state='q3'
text='salut ca tac tca ca t caat caaatt cat'
tranzitii={
   'q0':{'c':'q1'},
   'q1':{'a':'q2','c':'q1'},
   'q2':{'t':'q3','c':'q1'},
   'q3':{}

}

for char in text:
    if char in tranzitii[state]: ##statet=====ranzitii[state][char] == q's  , tr[state]=:{'c':'q1'}, deci aci verifica  daca in {'c':'q1'exista caracteru
        state=tranzitii[state][char]
    else:
        state='q0'
    if state==end_state:
        print('a aparut cat!')
        




