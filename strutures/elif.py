user_class = "CM2"

# Struture if
if user_class == "CM2":
    print("Il compose le CEP")
    
if user_class == "3eme":
    print("Il compose le BEPC")

if user_class == "Pr":
    print("Il compose le Probatoire")
    
if user_class == "Tle":
    print("Il compose le BAC")

# Struture if - elif - else   
if user_class == "CM2":
    print("Il compose le CEP")
elif user_class == "3eme":
    print("Il compose le BEPC")
elif user_class == "Pr":
    print("Il compose le Probatoire")
elif user_class == "Tle":
    print("Il compose le BAC")
else:
    print("Il ne compose pas d'examen")
    
    
# Struture Switch case
match user_class:
    case "CM2":
        print("Il compose le CEP")
    case "3eme":
        print("Il compose le BEPC")
    case "Pr":
        print("Il compose le Probatoire")
    case "Tle":
        print("Il compose le BAC")
    case _:
        print("Il ne compose pas d'examen")
