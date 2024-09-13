# Opdracht Les 7 Uitwerking (nina-1074862)

# Mijn uitwerking Opdracht: Rekenmachine
def add(x,y):
    return x + y

def subtract(x,y):
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

# Mijn uitwerking Opdracht: Rekenmachine met extra output

def add(x,y, debug=False):
    if debug:
        print(f"Debug: {x} + {y}")
        if x == 0 or y == 0:
            print("Waarschuwing: één van de getallen is 0!")
    return x + y

def subtract(x,y, debug=False):
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
            print(input1, "-", input2, "=", subtract(input1, input2, debug))
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

# Mijn uitwerking Opdracht: Refactoring
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
date_of_rapport = "02-09-2023"

students_per_classroom = {
    "SWDVT-2023-1A": [
        {
            "naam": "Celina van den Boom",
            "resultaten": {
                "WP1": "uitstekend",
                "WP2": "voldoende",
                "WP3": "uitstekend",
                "WP4": "voldoende",
            },
        },
        {
            "naam": "Kees van der Spek",
            "resultaten": {
                "WP1": "goed",
                "WP2": "goed",
                "WP3": "goed",
                "WP4": "goed",
            },
        },
    ],
    "SWDVT-2023-1B": [
        {
            "naam": "Peter de Vries",
            "resultaten": {
                "WP1": "onvoldoende",
                "WP2": "voldoende",
                "WP3": "voldoende",
                "WP4": "onvoldoende",
            },
        },
        {
            "naam": "Cindy Visser",
            "resultaten": {
                "WP1": "voldoende",
                "WP2": "uitstekend",
                "WP3": "goed",
                "WP4": "voldoende",
            },
        },
    ],
}

def get_excellent_students(list_of_students):
    excellent = False
    excellent_count = 0
    no_low_grade = True

    for result in student["resultaten"]:
        if student["resultaten"][result] == "uitstekend":
            excellent_count += 1
        if (
                student["resultaten"][result] == "onvoldoende"
                or student["resultaten"][result] == "voldoende"
        ):
            no_low_grades = False

    if no_low_grades or excellent_count > 1:
        excellent = True

    return excellent


def get_excellent_students(students):
    excellent_students = []
    for student in students:
        if get_is_student_excellent(student):
            excellent_students.append(student)
    return excellent_students


def get_most_excellent_classroom(students_per_classroom):
    best_classroom = None
    best_classroom_count = -1
    for classroom in students_per_classroom:
        excellent_students = get_excellent_students(students_per_classroom[classroom])
        if len(excellent_students) > best_classroom_count:
            best_classroom = classroom
            best_classroom_count = len(excellent_students)
        elif len(excellent_students) == best_classroom_count:
            best_classroom = f"{best_classroom}, {classroom}"
    return best_classroom


def calculate_score_per_student(student):
    score = 0
    for result in student["resultaten"]:
        if student["resultaten"][result] == "uitstekend":
            score += 3
        if student["resultaten"][result] == "goed":
            score += 2
        if student["resultaten"][result] == "voldoende":
            score += 1
    return score


def get_best_scoring_classroom(students_per_classroom):
    best_classroom = ""
    best_classroom_score = 0
    for classroom in students_per_classroom:
        classroom_score = 0
        for student in students_per_classroom[classroom]:
            classroom_score += calculate_score_per_student(student)
        if classroom_score > best_classroom_score:
            best_classroom = classroom
            best_classroom_score = classroom_score
        elif classroom_score == best_classroom_score:
            best_classroom = f"{best_classroom}, {classroom}"
    return best_classroom


def get_failed_students(students, min_score=3):
    failed_students = []
    for student in students:
        score = calculate_score_per_student(student)
        if score < min_score:
            student["score"] = score
            failed_students.append(student)
    return failed_students

def full_rapport(list_of_students):
    all_students = []
    for classroom in list_of_students:
        for student in list_of_students[classroom]:
            all_students.append(student)

    print(f"------ Rapport {date_of_rapport} ------")
    print("Excellente studenten:")
    excellent_students = get_excellent_students(all_students)
    for student in excellent_students:
        print(f'\t{student["naam"]}')

    print("Klas met de meest excellente studenten:")
    best_classroom = get_most_excellent_classroom(students_per_classroom)
    print(f"\t{best_classroom}")

    print("Klas met de hoogste scores gemiddeld:")
    best_classroom = get_best_scoring_classroom(students_per_classroom)
    print(f"\t{best_classroom}")

    print("Studenten met inhaalopdracht:")
    failed_students = get_failed_students(all_students)
    for student in failed_students:
        print(f'\t{student["naam"]}')
    for subject, result in student["resultaten"].items():
        print(f"\t\t{subject}: {result}")

full_rapport(students_per_classroom)