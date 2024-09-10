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
            print(input1, "-", input2, "=", substract(input1, input2))
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

# Functies met standaard waarden
# Je kunt een functie argument een standaard waarde geven. Als je de functie aanroept zonder dat argument, dan wordt de standaard waarde gebruikt. Bijvoorbeeld:
def print_hello(name='John'):
    print(f'Hello {name}')
print_hello()  # drukt "Hello John" af
print_hello('Jane')  # drukt "Hello Jane" af

# Opdracht: Rekenmachine met extra output
# Pas de functies van de rekenmachine aan om een derde waarde te accepteren, "debug", met een standaard waarde van False. Als de waarde True is, druk dan naast het antwoord de hele som af én een waarschuwing als één van de getallen een 0 is. Bijvoorbeeld:
add(1, 2, True) # drukt "Debug: 1 + 2" en daarna "3" af
add(1, 2) # drukt "3" af
# Voeg een vraag toe voor de gebruiker om te vragen of hij debug informatie wil zien.

# Mijn uitwerking Opdracht: Rekenmachine met extra output
def add(x,y, debug=False):
    if debug:
        print(f"Debug: {x} + {y}")
        if x == 0 or y == 0:
            print("Waarschuwing: één van de getallen is 0!")
    return x + y

def substract(x,y, debug=False):
    if debug:
        print(f"Debug: {x} - {y}")
        if x == 0 or y == 0:
            print('Waarschuwing: één van de getallen is 0!')
    return x - y

def multiply(x,y, debug=False):
    if debug:
        print(f"Debug: {x} * {y}")
        if x == 0 or y == 0:
            print('Waarschuwing: één van de getallen is 0%')
    return x * y

def divide(x, y, debug=False):
    if debug:
        print(f"Debug: {x} / {y}")
        if x == 0 or y == 0:
            print('Waarschuwing: één van de getallen is 0%')
    return x / y

while True:
    # take input from the user
    operator = input('Geef de operator (+, -, * of /): ')
    debug_ask = input("Do you want to see the debug information? [Yes/No] ")
    debug = False
    if debug_ask.lower() == 'YES':
        debug = True

    # check if choice is one of the four options
    if operator in ('+', '-', '*', '/'):
        try:
            input1 = float(input("Geef het eerste getal: "))
            input2 = float(input("Geef het tweede getal: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if operator == '+':
            print(input1, "+", input2, "=", add(input1, input2, debug))
            break

        elif operator == '-':
            print(input1, "-", input2, "=", substract(input1, input2, debug))
            break

        elif operator == '*':
            print(input1, "*", input2, "=", multiply(input1, input2, debug))
            break

        elif operator == '/':
            print(input1, "/", input2, "=", divide(input1, input2, debug))
            break
    else:
        print("Invalid Input")
        exit()

# Functie met return waarde
# Een functie kan een waarde teruggeven. Dit doe je met het return statement. Bijvoorbeeld:
def add(a, b):
    return a + b

result = add(1, 2)
print(result)

# Functie argumenten op naam
# Wat in praktijk veel zal gebeuren is dat je een functie aanroept met een heleboel argumenten. Bijvoorbeeld:
def print_person(name, age, city, country):
    print(f'{name} is {age} jaar oud en woont in {city}, {country}')

print_person('John', 42, 'Rotterdam', 'Nederland')

# Lastig is dat als je nu in jouw functie een extra argument toevoegt, "achternaam" bijvoorbeeld, dat je al je functie aanroepen moet aanpassen. Dat is niet handig. En dat niet alleen, op een gegeven moment weet je niet meer welke volgorde de argumenten hebben. Dat is niet handig.

# Je kunt argumenten ook op naam meegeven. Bijvoorbeeld:
def print_person(name, age, city, country):
    print(f'{name} is {age} jaar oud en woont in {city}, {country}')

print_person(name='John', age=42, city='Rotterdam', country='Nederland')

# ..als we nu een extra argument toevoegen, dan hoeven we de aanroep niet aan te passen.

# Opdracht: Refactoring
# "Refactoring" is een kreet die je nog veel zult tegenkomen. Refactoring slaat op het herschrijven van code, zonder dat de input of output verandert. Dat doe je vaak omdat je de code beter leesbaar wilt maken, of omdat je de code wilt hergebruiken.

# We gaan de code van een vorige opdracht refactoren. Als je onze uitwerking bekijkt van Les3_Source5.py zijn daar een paar zaken niet heel netjes:

# We vragen gebruikers steeds te kiezen uit een aantal zaken ("KOUD of WARM"), maar die keuze dwingen we niet af. Je kunt nog steeds "LAUW" invoeren waar "KOUD" of "WARM" verwacht wordt. We willen die keuze afdwingen, dat kan bijvoorbeeld met een while loop:
answer = ""
while answer != "KOUD" and answer != "WARM":
    answer = input("Wil je warme of koude drank? (KOUD/WARM) ")
# Je ziet een aantal regels code rondom vragen steeds terugkomen. Maak een aparte functie die vragen kan stellen en het antwoord terug geeft als return, met controle op de antwoorden zoals hierboven beschreven. Bijvoorbeeld:
def ask_question(question, valid_answers):
    ...
    return answer
# We hebben keuzes die leiden tot andere keuzes, waardoor we een hele lange lap code krijgen. We willen overzicht krijgen door de code op te splitsen in functies voor in het restaurant eten / meenemen, voor de burgers keuze, voor warme drankjes en een functie voor koude drankjes. De uiteindelijke code zou er dan ongeveer zo uit kunnen zien:
    food_answer = ask_question("Burgers of drankjes?", ["Burgers", "Drankjes"])
    if food_answer == "BURGERS":
        get_burger_choice()
    elif food_answer == "DRANKJES":
        drink_choice = ask_question("Drankjes", ["Warme", "Koude"])
# Neem de oude code en refactor deze, waarbij je bovenstaande drie verbeteringen doorvoert.

# Opdracht: Studenten rapport
# In deze opdracht gaan we lijsten, dictionaries en functies combineren. We gaan een programma maken dat een rapport afdrukt van een aantal studenten. Van een student heb je de volgende informatie:

# Iedere student zit in één klas, bijvoorbeeld "SWDVT-2023-1A". Niet alle klassen zijn even groot.
# Iedere student heeft 4 werkplaats vakken (WP1, WP2, WP3 en WP4)
# Voor ieder vak is het resultaat bekend. De student heeft een "onvoldoende", een "voldoende", een "goed" of een "uitstekend" gescored.
# We noemen een student "excellent" als hij meer dan één uitstekend heeft of als alle resultaten beter dan "voldoende" zijn.
# We gaan een rapport maken om aan het einde van het jaar aan de onderwijscoordinator te sturen, met de volgende informatie:

# We noemen een student "excellent" als hij meer dan één uitstekend heeft of als alle resultaten beter dan "voldoende" zijn. Welke studenten zijn excellent?
# Welke klas(sen) hebben het hoogste percentage "excellent" studenten?
# Welke klas heeft gemiddeld genomen over alle vakken de hoogste scores? Dit is een lastige. Stel voor het gemak dat een onvoldoende = 0 punten, voldoende 2 punten, goed 3 punten en uitstekend 4 punten.
# Gegeven diezelfde manier van scoren: studenten met een score van 3 of minder punten moeten een inhaal opdracht doen. Welke studenten zijn dat en wat zijn hun resultaten?
# Maak gebruik van de volgende functies voor de vier onderzoeksvragen en bedenk dat je jouw dataset waarschijnlijk eerst in verschillende varianten zult moeten omzetten. Bedenk ook dat als je code aan het herhalen bent, dat je dan waarschijnlijk een functie kunt maken.
def get_excellent_students(list_of_students):
    ...

def get_most_excellent_classroom(list_of_classrooms):
    ...

def get_best_scoring_classroom(list_of_classrooms):
    ...

def get_failed_students(list_of_students, minimum_score = 4):
    ...

# Je kunt optioneel een dataset genereren met de code in generate_fake_students.py. Nadat je succesvol een bestand hebt weggeschreven importeer je het resultaat met het volgende commando boven in je Python bestand:
from students_classrooms import students_per_classroom


























