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
# Bestelling bij de FastFood Restaurant
dine_in = False
cancelled = False

SEPARATOR = "/"

def format_valid_options(options):
    # Formatteert de lijst met opties als een string om aan de gebruiker te tonen
    if len(options) > 0:
        options_text = " [" + SEPARATOR.join(options) + "]"
    return options_text


def ask_user(question, options=()):
    # Maakt een lijst met de opties in hoofdletters
    valid_options = [option.upper() for option in options]

    # Stelt de vraag met beschikbare opties
    full_question = question + format_valid_options(options) + ": "

    # Blijf vragen tot een geldig antwoord wordt gegeven
    user_input = ""
    while user_input not in valid_options:
        user_input = input(full_question).upper()

    return user_input


def dine_in_or_takeout():
    # Vraagt of de gebruiker in het restaurant wil eten of afhalen
    dining_choice = ask_user("Eet je hier of neem je mee?", ["Hier", "Mee"])
    if dining_choice == "HIER":
        print("Eten in het restaurant")
        return True
    else:
        print("Afhalen")
        return False


def choose_burger():
    # Laat de gebruiker een burger kiezen
    burger_choice = ask_user(
        "Welke burger wil je?", ["Hamburger", "Cheeseburger", "Big Mac", "Quarter Pounder"]
    )
    print(f"Je hebt gekozen voor een {burger_choice}")


def choose_hot_drink():
    # Laat de gebruiker een warme drank kiezen
    hot_drink_choice = ask_user("Welke warme drank wil je?", ["Koffie", "Cappuccino", "Chocolademelk"])
    print(f"Je hebt gekozen voor een {hot_drink_choice}")


def choose_cold_drink():
    # Laat de gebruiker een koude drank kiezen
    cold_drink_choice = ask_user(
        "Welke koude drank wil je?", ["Coca Cola", "Cola Zero", "7-Up", "Fanta", "Fristi"]
    )
    print(f"Je hebt gekozen voor een {cold_drink_choice}")


def place_order():
    # Vraag of de gebruiker eten of drinken wil
    order_type = ask_user("Wil je burgers of drankjes?", ["Burgers", "Drankjes"])
    if order_type == "BURGERS":
        choose_burger()
    else:
        # Vraag of de gebruiker warme of koude drank wil
        drink_type = ask_user("Wil je warme of koude drank?", ["Warme", "Koude"])
        if drink_type == "WARME":
            choose_hot_drink()
        else:
            choose_cold_drink()


# Hoofdprogramma
def main():
    print("Welkom bij MacDonald's")
    dine_in = dine_in_or_takeout()

    place_order()

    if dine_in:
        print("Bedankt voor je bestelling en geniet van je maaltijd in het restaurant.")
    else:
        print("Bedankt voor je bestelling, veilige reis en smakelijk eten!")


# Start het programma
if __name__ == "__main__":
    main()

# Mijn uitwerking Opdracht: Studenten rapport
classes = dictionary['SWDVT-2023-1A', ]

# Je kunt optioneel een dataset genereren met de code in generate_fake_students.py. Nadat je succesvol een bestand hebt weggeschreven importeer je het resultaat met het volgende commando boven in je Python bestand:
# from students_classrooms import students_per_classroom

