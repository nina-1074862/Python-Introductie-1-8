# Opdracht Les 7 Uitwerking (nina-1074862)

# Functies
# Functies zijn een manier om code te groeperen en te hergebruiken. Je kan een functie zien als een klein programmaatje binnen je programma. Je kan een functie aanroepen, waardes mee geven om mee te werken en deze kan dan een waarde teruggeven.

# Code splitsen in functies heeft een heleboel voordelen:

# Je voorkomt dat je code gaat dupliceren. Gedupliceerde code is lastig leesbaar en onderhoudbaar.
# Je kunt code hergebruiken, zowel in hetzelfde programma als in andere programma's.
# Je kunt code makkelijker testen en debuggen.
# Het is makkelijker om samen te werken in code die gesplitst is in functies
# Code die je schrijft moet je zo snel mogelijk in functies zetten. Je zult zien dat je code veel leesbaarder wordt en dat je veel minder fouten maakt.

# Functie aanroepen
# Een functie aanroepen doe je door de naam van de functie te gebruiken met daarachter haakjes. Bijvoorbeeld:

def print_hello():
    print('Hello')
print_hello()

# Functies kun je argumenten meegeven. De variabelen die je mee geeft in de functie aanroep worden op volgorde aangenomen als argumenten in de functies. Deze argumenten kun je gebruiken binnen de functie. Bijvoorbeeld:
def print_hello(name):
    print(f'Hello {name}')

print_hello('John')

# of, een voorbeeld met meerdere argumenten:
def greeter(name, greeting_type):
    if greeting_type == 'formal':
        greeting = 'Hello'
    elif greeting_type == 'informal':
        greeting = 'Hi'
    else:
        greeting = 'Hey'
    print(f'{greeting} {name}')

greeter('John', 'formal')

# Opdracht: Rekenmachine
    # We gaan een simpele rekenmachine maken die de volgende functies heeft:

    # add telt twee getallen bij elkaar op en drukt het resultaat af
    # subtract trekt twee getallen van elkaar af en drukt het resultaat af
    # multiply vermenigvuldigt twee getallen met elkaar en drukt het resultaat af
    # divide deelt twee getallen door elkaar en drukt het resultaat af
    # De functies moeten als volgt werken:

    # add(1, 2) drukt 3 af
    # subtract(1, 2) drukt -1 af
    # multiply(1, 2) drukt 2 af
    # divide(1, 2) drukt 0.5 af
# ..daarnaast moet de rekenmachine ook nog een functie hebben die de gebruiker vraagt om twee getallen en een operator, en vervolgens de juiste functie aanroept. Bijvoorbeeld:

input1 = input('Geef het eerste getal: ')
input2 = input('Geef het tweede getal: ')
operator = input('Geef de operator (+, -, * of /): ')

# Let wel, hier gebeurt nog iets bijzonders. De functie input geeft een string terug en daar kunnen we niet mee rekenen. Voer bijvoorbeeld de volgende code uit:
string1 = "1"
string2 = "2"
print(string1 + string2)  # drukt "12" af
print(string1 - string2)  # geeft een error (strings kun je niet van elkaar aftrekken)

# We moeten dus de string omzetten naar een getal. Dat kan met de functie int of float. Bijvoorbeeld:
input1 = input('Geef het eerste getal: ')
number1 = int(input1)
print(number1 + number1)  # drukt "2" af

# Mijn uitwerking Opdracht: Rekenmachine
def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x, y):
    return x / y

while True:
    # take input from the user
    operator = input('Geef de operator (+, -, * of /): ')

    # check if choice is one of the four options
    if operator in ('+', '-', '*', '/'):
        try:
            input1 = float(input("Geef het eerste getal: "))
            input2 = float(input("Geef het tweede getal: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if operator == '+':
            print(input1, "+", input2, "=", add(input1, input2))
            break

        elif operator == '-':
            print(input1, "-", input2, "=", subtract(input1, input2))
            break

        elif operator == '*':
            print(input1, "*", input2, "=", multiply(input1, input2))
            break

        elif operator == '/':
            print(input1, "/", input2, "=", divide(input1, input2))
            break
    else:
        print("Invalid Input")
        exit()




































