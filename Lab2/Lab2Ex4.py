import re

def validate_factura(factura_text):
    client_re = r"^client:\s+([A-Za-z ]+)$"
    zi_re = r"^zi nastere:\s+(\d{2}/\d{2}/\d{4})$"
    companie_re = r"^companie:\s*([A-Za-z0-9 .]+)$" #s* ->  pt ca poate sa fie gol
    email_re = r"^email:\s+([a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$"
    produs_re = r"^produs:\s+([A-Za-z ]+)$"  
    pret_re = r"^pret:\s+(\d+(\.\d{1,2})?)$"  # ? ->  - ,, - 
    cod_re = r"^cod:\s+(\d{5})$" 
    
    errors = []
   
    client_matches = re.findall(client_re, factura_text, re.MULTILINE)
    if len(client_matches) > 1:
        errors.append("Error: 'client' apare de mai multe ori" if len(client_matches) > 1 else "Error: 'client' lipseste")
    else:
        client_match = client_matches[0]
        if not re.match(client_re, f"client: {client_match}"):
            errors.append("Error: 'client' format aiurea. Format: client: Nume (doar litere si spatii)")

    zi_matches = re.findall(zi_re, factura_text, re.MULTILINE)
    if len(zi_matches) != 1:
        errors.append("Error: 'zi nastere' apare de mai multe ori" if len(zi_matches) > 1 else "Error: 'zi nastere' lipseste")
    else:
        zi_match = zi_matches[0]
        if not re.match(zi_re, f"zi nastere: {zi_match}"):
            errors.append("Error: 'zi nastere' L  format . Format: zi nastere: dd/mm/yyyy.")

    companie_matches = re.findall(companie_re, factura_text, re.MULTILINE)
    if len(companie_matches) != 1:
        errors.append("Error: 'companie' apare de mai multe ori" if len(companie_matches) > 1 else "Error: 'companie' lipseste")
    else:
        companie_match = companie_matches[0]
        if not re.match(companie_re, f"companie: {companie_match}"):
            errors.append("Error: 'companie' format incorect. Format: companie: (doar litere si numere).")
    
    email_matches = re.findall(email_re, factura_text, re.MULTILINE)
    if len(email_matches) != 1:
        errors.append("Error: 'email' apare de mai multe ori" if len(email_matches) > 1 else "Error: 'email' lipseste")
    else:
        email_match = email_matches[0]
        if not re.match(email_re, f"email: {email_match}"):
            errors.append("Error: 'email' format incorect. Format: email: xxxxx@xxxx.xxx ")

    
    lines = factura_text.splitlines()
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("produs:"):
            produs_match = re.match(produs_re, line)
            if not produs_match:
                errors.append(f"Error: Produs {i + 1} invalid. Format: produs: Nume (doar litere si spatii)")
            
            if i + 1 < len(lines) and lines[i + 1].strip().startswith("pret:"):
                pret_line = lines[i + 1].strip()
                pret_match = re.match(pret_re, pret_line)
                if not pret_match:
                    errors.append(f"Error: Pret  {i + 2} invalid . Format: pret: Numar (maxim 2 zecimale)")
            else:
                errors.append(f"Error: Lipseste 'pret' pe linia {i + 1}.")
            
            if i + 2 < len(lines) and lines[i + 2].strip().startswith("cod:"):
                cod_line = lines[i + 2].strip()
                cod_match = re.match(cod_re, cod_line)
                if not cod_match:
                    errors.append(f"Error:  cod produs  {i + 3} invalid . Format: cod: xxxxx (5 cifre)")
            else:
                errors.append(f"Error: lipseste 'cod' pe linia {i + 1}.")
            
            i += 3
        elif line.startswith("pret:") or line.startswith("cod:"):
            errors.append(f"Error: Apare in plus '{line.split(':')[0]}' la linia {i + 1}. Lipseste 'produs:'.")
            i += 1
        else:
            i += 1
    
    if errors:
        for error in errors:
            print(error)
    else:
        print("Factura Este Corecta !!!!")

file_path = r"C:\Users\Acasa\Desktop\Uni\LimbajeFormale\Lab2\text.txt"
file = open(file_path, 'r', encoding='utf-8') 
factura_text = file.read()
validate_factura(factura_text)