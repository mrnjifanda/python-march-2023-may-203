premier_nombre = float(input("Entrez le  premier nombre: "))
deuxieme_nombre = float(input("Entrez le  deuxième nombre: "))
operation = input("Opérations disponible: +, -, *, /: ")

resultat = None
match operation:
    case "+":
        resultat = premier_nombre + deuxieme_nombre
    case "-":
        resultat = premier_nombre - deuxieme_nombre
    case "*":
        resultat = premier_nombre * deuxieme_nombre
    case "/":
        if deuxieme_nombre != 0:
            resultat = premier_nombre / deuxieme_nombre
        else:
            resultat = "Impossible de diviser par 0"
    case _:
        resultat = "Opération non reconnue."

if resultat is not None:
    print(f"Resultat: {resultat}")