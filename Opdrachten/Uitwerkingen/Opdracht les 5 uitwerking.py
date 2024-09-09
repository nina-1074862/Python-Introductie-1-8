# Opdracht Les 5 Uitwerking (nina-1074862)

# Modulo
# We gebruiken in deze oefeningen een aantal keren de kreet "is deelbaar". Een snelle manier om te zien of een getal netjes deelbaar is is door de restwaarde van een deling op te zoeken en als die 0 is noemen we dat "is deelbaar door".

# Programmeertalen gebruiken daarvoor de "modulo" operator, het "%" teken. 4 % 3 is 1 bijvoorbeeld. Plat gezegd past 3 past één keer in 4 en er blijft dan 1 over.

# Nog wat voorbeelden:
    # 4 % 2 is 0, want 2 past twee keer in 4 en er blijft dan 0 over.
    # 4 % 4 is 0, want 4 past één keer in 4 en er blijft dan 0 over.
    # 4 % 5 is 4, want 5 past niet in 4 en er blijft dan 4 over.

# Itereren over een lijst

# Een techniek die je heel veel zult gebruiken is het doorlopen van een lijst en het uitvoeren van een actie op elk element uit deze lijst.
# Een hele bekende opdracht om te oefenen met programmeren is "Fizz Buzz".
# De regels zijn heel simpel:
    # Loop door alle getallen van 1 tot 30
    # Als het getal deelbaar is door 3 (bijvoorbeeld 3, 6 en 9) print "Fizz"
    # Als het getal deelbaar is door 5 (dus 5, 10, 15) print "Buzz"
    # Als het getal deelbaar is door 3 en 5 (dus 15, 30) print "FizzBuzz"
    # In alle andere gevallen, print het getal zelf

# Stel dat je door de getallen 1 tot 10 zou lopen zou dit bijvoorbeeld de uitkomst zijn:
# Expected output: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz

# Opdracht
# Schrijf een programma dat de Fizz Buzz opdracht uitvoert door met module te controleren of de getallen deelbaar zijn. We helpen je wat op weg door alvast een lijst met getallen te maken. Gebruik een "for ... in" loop om door de lijst te lopen.
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

# Als je het jezelf moeilijker wilt maken kun je proberen ditzelfde programma op te lossen niet met een "for .. in" maar met een "while" loop en één van de vele functies die je kunt aanroepen op een lijst object. Je zou hier ook de "walrus" operator kunnen toepassen, een recente toevoeging aan Python.
# Breaks 