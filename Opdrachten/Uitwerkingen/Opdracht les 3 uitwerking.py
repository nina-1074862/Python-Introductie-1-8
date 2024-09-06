# Opdracht Les 3 Uitwerking (nina-1074862)

#Input vragen
# Met de functie input() kan je input van de gebruiker vragen. Dit ziet eruit als:
age_str = input('What is your age? ')
print(f'Your age is {age_str}')

# De input()functie levert altijd een string terug, vandaar dat de variabele _str heeft meegekregen, om dit te benadrukken. Dit is overigens de enige plaats waarop deze toevoeging handig is.

# Internet verbinding selectie
data_users = input('Welke verbinding wilt u gebruiken [4G, 5G, Wifi open]: ')
if data_users == ("Wifi open" or "wifi open" or "WIFI OPEN"):
    print("U heeft voor de Wifi open gekozen, wij wijzen u erop dat de data door de eigenaar van dit netwerk is te lezen.")
    connection_users = input('Wilt u nog steeds een verbinding maken? [ja/nee]: ')
    if connection_users == ("ja" or "JA" or "Ja"):
            print("U bent verbonden via WIFI OPEN!")
    else:
            print("U bent niet verbonden!")

else:
    print("Unknown input, there won't be any connection")
    (exit)

# Vergelijken met een sub-string
# Controleren of een string als een substring in een string zit doe je middels het keyword in. Bijvoorbeeld:
print("Is Hello with a capital 'H' within the string 'Hello, everyone!'")
if "Hello" in "Hello, everyone!":
    print('Yes, Hello is within the Hello, everyone! string')

print("Is Hello with a lower case 'h' within the string 'Hello, everyone!'")
if "hello" in "Hello, everyone!":
    print('Yes, hello is within the Hello, everyone! string')
else:
    print('No, hello with small letters is not within the string')

# Flowchart
# Opdracht: Maak een Python programma die onderstaande flowchart implementeert. Van alle elipsen/ronde/rechthoek symbolen print je de tekst van de flowchart. De diamanten zijn je if statements, waar je aan de gebruiker een input vraagt. Bijvoorbeeld: yes of no antwoord.

print("Patient exposed to TB")
adult_child = input('Is the patient an adult or a child? [Adult/Child]')
