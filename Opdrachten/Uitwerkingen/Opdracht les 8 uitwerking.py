# Opdracht Les 8 Uitwerking (nina-1074862)

# Mijn uitwerking Opdracht 8: Caching
import time

def zeef_van_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    current_prime = 2
    while current_prime * current_prime <= limit:
        if is_prime[current_prime]:
            for multiple in range(current_prime * current_prime, limit + 1, current_prime):
                is_prime[multiple] = False
        current_prime += 1

    prime_numbers = []
    for number in range(2, limit + 1):
        if is_prime[number]:
            prime_numbers.append(number)

    return prime_numbers


def priemgetal_global(number):
    if number in dictionary:
        print("Nummer gevonden in dictionary")
        return dictionary[number]
    else:
        print("Resultaat niet gevonden in dictionary")
        result = zeef_van_eratosthenes(number)
        dictionary[number] = result
        return result

dictionary = {}

while True:
    priemgetallen_enter = input(
        "Voer een getal om de priemgetallen van te berekenen of type [Enter] om te stoppen: "
    )
    if priemgetallen_enter == "":
        break

    tijd = time.time()
    priemgetallen_results = priemgetal_global(int(priemgetallen_enter))
    tijd_verstreken = time.time() - tijd
    print(f"De gevonden priemgetallen onder de {priemgetallen_enter} zijn:")
    for priemgetal in priemgetallen_results:
        print(priemgetal)
    print(f"Verstreken tijd: {tijd_verstreken:.2f} seconden")

print("Einde programma, Tot Ziens !")