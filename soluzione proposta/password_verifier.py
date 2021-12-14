import re

while True:
    password = input("Scrivi qui la password da verificare: ")

    valid = True

    # La password deve essere lunga almeno 8 caratteri
    if len(password) < 8:
        print("La password deve essere lunga almeno 8 caratteri!")
        valid = False

    # La password deve contenere almeno un carattere maiuscolo
    if re.search("[A-Z]+", password) == None:
        print("La password deve contenere almeno un carattere maiuscolo!")
        valid = False

    # La password deve contenere almeno un carattere minuscolo
    if re.search("[a-z]+", password) == None:
        print("La password deve contenere almeno un carattere minuscolo!")
        valid = False

    # La password deve contenere almeno un numero
    if re.search("[0-9]+", password) == None:
        print("La password deve contenere almeno un numero!")
        valid = False

    # La password deve contenere almeno un carattere speciale: .,_-
    if re.search("[\.,_\-]+", password) == None:
        print("La password deve contenere almeno un carattere speciale: .,_-!")
        valid = False


    if valid:
        print("La tua password è perfettamente valida!")
        break
    else:
        print("\n\n")
        continue


print("Chiudo il programma.")