# Opdracht Les 5 Uitwerking (nina-1074862)

# Mijn uitwerking: Opdracht 1
numbers = list(range(1, 31))
for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        exit()

# Mijn uitwerking: Opdracht 2
numbers = list(range(1, 100))
for priemgetal in numbers:
    if priemgetal == 1:
        continue
    for deler in range(2, priemgetal):
        if priemgetal % deler == 0:
            break
    else:
        print(priemgetal)

# Mijn uitwerking: BINGO Opdracht 1:
import random
bingo_number_total = 4 ** 2
numbers_all = list(range(1, 100))
random.shuffle(numbers_all)
bingo_numbers = numbers_all[:bingo_number_total]
bingo_numbers_card = [
    bingo_numbers[:4],
    bingo_numbers[4:8],
    bingo_numbers[8:12],
    bingo_numbers[12:]
]
for row in bingo_numbers_card:
    print([', ' .join(map(str, row))])

# Mijn uitwerking: BINGO Opdracht 2:
import random
# Totaal aantal getallen op de kaart zal hoogte x breedte zijn
total_bingo_numbers = 4 ** 2
# Daarna maken we een lijst met 99 getallen waar we uit gaan kiezen
numbers_all = list(range(1, 100))
# We gooien alle ballen door elkaar
random.shuffle(numbers_all)
# en pakken de eerste 16 getallen
bingo_numbers2 = numbers_all[:total_bingo_numbers]
bingo_numbers_card = [
    bingo_numbers2[:4],
    bingo_numbers2[4:8],
    bingo_numbers2[8:12],
    bingo_numbers2[12:]
]
for row in bingo_numbers_card:
    print([', ' .join(map(str, row))])

# Mijn uitwerking: BINGO Opdracht 3:

# Mijn uitwerking: While loops Opdracht 1:
numbers_all = list(range(1, 100))

def priemgetal(number):
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

while True:
    try:
        number_input = int(input("Geef een getal tussen (1-100):"))

        if number_input < 1 or number_input > 100:
            print("Het getal moet tussen 1 en 100 zijn.")
            continue

        if priemgetal(number_input):
            print(f"{number_input} is een priemgetal")
        else:
            print(f"{number_input} is geen priemgetal")
            continue
    except ValueError:
        print("Tot ziens!")
        break