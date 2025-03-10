def coffee_machine():
    state = 'q0'
    end_state = 'q4'
    transitions = {
        'q0': {'C': 'q1', 'T': 'q2', 'A': 'q3', 'H': 'q4'},
        'q1': {'OK': 'q4'},
        'q2': {'OK': 'q4'},
        'q3': {'OK': 'q4'},
        'q4': {'OK': 'q0'}
    }

    print("Optiuni: C (Cafea), T (Ceai), A (Cappuccino), H (Ciocolata calda), OK (confirmare) , X (iesire)")
    
    while True:
        button = input("Alege varianta ").strip().upper()
        if button == 'X':
            print("Acu plec")
            break
        
        if button in transitions[state]:
            state = transitions[state][button]
            
            if state == 'q1':
                print("Ai ales Cafea, Apasa OK")
            elif state == 'q2':
                print("ai ales Ceai, Apasa OK")
            elif state == 'q3':
                print("Ai ales Cappuccino, Apasa OK")
            elif state == 'q4':
                if button == 'H':
                    print("Ai ales Ciocolata calda, Apasa OK")
                elif button == 'OK':
                    print("se prepara.,.")
                    print("preparat!")
                    print("selecteaza din nou")
                    state = 'q0'
        
       
        else:
            print("Nu puteti continua cu acest buton.")
            optiuni = list(transitions[state].keys())
            print(f"Optiuni disponibile in starea curenta ({state}): {', '.join(optiuni)} ,X (iesire)")

            


coffee_machine()