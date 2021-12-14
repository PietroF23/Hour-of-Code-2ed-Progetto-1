import re

while True:
    password = input("Inserisci la password da testare:")
    valida = True
    # La password deve essere lunga almeno 8 caratteri
    if (len(password) < 8) :
        print("Lunghezza passowrd errata, almeno 8 caratteri!")
        valida = False
    

    # La password deve contenere almeno un carattere maiuscolo
    if not re.search("[A-Z]+", password):
        print("La password deve contenere almeno un carattere maiuscolo!")
        valida = False
    # La password deve contenere almeno un carattere minuscolo
    if not re.search("[a-z]+", password):
        print("La password deve contenere almeno un carattere minuscolo!")
        valida = False
    # La password deve contenere almeno un numero
    if not re.search("[0-9]+", password):
        print("La password deve contenere almeno un numero!")
        valida = False
    # La password deve contenere almeno un carattere speciale: .,_-
    if not re.search("[\.,_-]+", password):
        print("La password deve contenere almeno un carattere speciale!")
        valida = False
        if valida:
            print("La password è valida!")
            break
        else:
            continue        


print("Chiudo il programma.")