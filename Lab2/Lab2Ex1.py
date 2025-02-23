
state='q0'
while(state!='q3'):
    print(f"State este {state}.")
    input_curent=int(input("Introduce un input (1/0):"))
    if input_curent not in (0, 1):
            input_curent=int(input("Ai introdus un imput gresit, introduce unul nou :"))
    if(state=='q0'):
          if(input_curent==0):
                state='q1'
          else:
                state='q2' 
    elif(state=='q1'):
          if(input_curent==0):
                state='q3'
          else:
                state='q0' 
    elif(state=='q2'):
          if(input_curent==0):
                state='q1'
          else:
                state='q3' 
print('Felicitari ai ajuns la stop! :)')

   
