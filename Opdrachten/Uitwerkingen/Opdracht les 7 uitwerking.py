# Opdracht Les 7 Uitwerking (nina-1074862)

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
# daarnaast moet de rekenmachine ook nog een functie hebben die de gebruiker vraagt om twee getallen en een operator, en vervolgens de juiste functie aanroept. Bijvoorbeeld:

# Let wel, hier gebeurt nog iets bijzonders. De functie input geeft een string terug en daar kunnen we niet mee rekenen. Voer bijvoorbeeld de volgende code uit:

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
# Voeg een vraag toe voor de gebruiker om te vragen of hij debug-informatie wil zien.

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
    if debug_ask.lower() == 'yes':
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
# als we nu een extra argument toevoegen, dan hoeven we de aanroep niet aan te passen.

# Opdracht: Refactoring
# "Refactoring" is een kreet die je nog veel zult tegenkomen. Refactoring slaat op het herschrijven van code, zonder dat de input of output verandert. Dat doe je vaak omdat je de code beter leesbaar wilt maken, of omdat je de code wilt hergebruiken.
# We gaan de code van een vorige opdracht refactoren. Als je onze uitwerking bekijkt van Les3_Source5.py zijn daar een paar zaken niet heel netjes:
# We vragen gebruikers steeds te kiezen uit een aantal zaken ("KOUD of WARM"), maar die keuze dwingen we niet af. Je kunt nog steeds "LAUW" invoeren waar "KOUD" of "WARM" verwacht wordt. We willen die keuze afdwingen, dat kan bijvoorbeeld met een while loop:

# Mijn uitwerking Opdracht: Refactoring
# Ordering at Mac Donald's
eat_in = False
aborted = False


SEPERATOR_CHARACTER = "/"
def get_valid_answer_text(valid_answers):
    valid_answers_text = ""
    if len(valid_answers) > 0:
        # Deze regel kan simpeler, maar dit is duidelijker
        # We kiezen er voor om de opties niet meteen in de "question" string mee te geven,
        # maar de lijst met mogelijke antwoorden mee af te drukken als we de vraag stellen
        valid_answers_text = " ["
        for answer in valid_answers:
            valid_answers_text = valid_answers_text + answer + SEPERATOR_CHARACTER
        valid_answers_text = valid_answers_text[:-1]  # Deze regel verwijdert de laatste /
        valid_answers_text = valid_answers_text + "]"
    return valid_answers_text


def ask_question(question, valid_answers=()):
    valid_answers_upper = []
    # Hier maken we alvast een lijst met de geldige antwoorden in hoofdletters
    for answer in valid_answers:
        valid_answers_upper.append(answer.upper())

    # We bouwen de vraag op uit de vraagtekst en de geldige antwoorden (als die er zijn)
    question_string = question
    question_string = question_string + get_valid_answer_text(valid_answers)
    question_string = question_string + ": "

    # We blijven de vraag stellen tot we een geldig antwoord hebben
    answer_str = ""
    while answer_str not in valid_answers_upper:
        answer_str = input(question_string)
        answer_str = answer_str.upper()

    # We geven het antwoord terug in hoofdletters
    return answer_str


def eat_in_choice():
    eat_in = False
    question_1 = ask_question("Hier opeten of meenemen", ["Opeten", "Meenemen"])
    if question_1 == "OPETEN":
        # Eat in part
        print("Hier opeten")
        eat_in = True
    elif question_1 == "MEENEMEN":
        # Take away part
        print("Meenemen")
        eat_in = False
    return eat_in


def get_burger_choice():
    question_3 = ask_question(
        "Burgers", ["Hamburger", "Cheeseburger", "Big Mac", "Quarter Pounder"]
    )
    if question_3 == "HAMBURGER":
        print("Hamburger")
    elif question_3 == "CHEESEBURGER":
        print("Cheeseburger")
    elif question_3 == "Big MAC":
        print("Big Mac")
    elif question_3 == "QUARTER POUNDER":
        print("Quarter Pounder")


def get_warm_drink_choice():
    question_5 = ask_question("Warme drank", ["Koffie", "Cappucino", "Chocolademelk"])
    if question_5 == "KOFFIE":
        print("Koffie")
    elif question_5 == "CAPPUCINO":
        print("Cappucino")
    elif question_5 == "CHOCOLADEMELK":
        print("Chocolademelk")


def get_cold_drink_choice():
    question_6 = ask_question(
        "Koude drank ", ["Coca Cola", "Cola Zero", "7-Up", "Fanta", "Fristi"]
    )
    if question_6 == "COCA COLA":
        print("Coca Cola")
    elif question_6 == "COLA ZERO":
        print("Cola Zero")
    elif question_6 == "7-UP":
        print("7-Up")
    elif question_6 == "FANTA":
        print("Fanta")
    elif question_6 == "FRISTI":
        print("Fristi")


print("Welkom bij de Mac Donald's")
eat_in = eat_in_choice()
if eat_in:
    food_answer = ask_question("Burgers of drankjes", ["Burgers", "Drankjes"])
    if food_answer == "BURGERS":
        get_burger_choice()
    elif food_answer == "DRANKJES":
        drink_choice = ask_question("Drankjes", ["Warme", "Koude"])
        if drink_choice == "WARME":
            get_warm_drink_choice()
        elif drink_choice == "KOUDE":
            get_cold_drink_choice()
if eat_in:
    print("Bedankt voor uw bestelling en eet smakelijk in ons restaurant.")
else:
    print("Bedankt voor uw bestelling, goede reis en eet smakelijk.")