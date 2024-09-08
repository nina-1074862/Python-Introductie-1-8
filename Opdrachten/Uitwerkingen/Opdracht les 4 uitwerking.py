# Opdracht les 4 uitwerking

# List

# Een lijst is een verzameling van elementen. Deze elementen kunnen van elk data type zijn. Een lijst wordt gedefinieerd door vierkante haken [] te gebruiken. De elementen in de lijst worden gescheiden door een komma ,.

# Create a list
my_list = [1, 2, 3, 4, 5]
print(my_list)
# Elementen mogen van elk data type zijn
my_list = [1, 2, 3, "four", 5]
print(my_list)
# Elementen hebben een "index" nummer om hun locatie in de lijst aan te geven. Die index begint bij 0.
print(my_list[0])
# Elementen toevoegen achteraan een lijst
my_list.append(6)
# ..of op een specifieke locatie
my_list.insert(3, "three")

# List of games

# Gegeven een lijst met 10 populaire games in 2021.
    # Player’s Unknown Battle Ground (PUBG) 50 Million 2018
    # Fortnite Battle Royale 39 Million 2017
    # Apex Legends 50 Million (1 Month) 2019
    # League of Legends (LOL) 27 Million 2009
    # Counter Strike; Global Offensive 32 Million 2014
    # Heartstone 29 Million 20120
    # Minecraft 91 Million 2011
    # DOTA 2 5 million 2015
    # The Division 2 N/A 2019
    # The Splatoon 2

# Opdrachten
# Maak een Python programma waarin de games in een lijst worden opgeslagen. Daarna gaan we operaties loslaten op die lijst. Na elke opdracht geef je de lijst op het scherm weer.

# [a] Geef de 5de game (Counter Strike) uit de lijst op het scherm weer met 5] ervoor.
popular_games_2021 = ("", "Player’s Unknown Battle Ground (PUBG) 50 Million 2018", "Snake" , "Fortnite Battle Royale 39 Million 2017", "Apex Legends (1 Month) 2019", "League of Legends (LOL) 27 Million 2009", "Counter Strike; Global Offensive 32 Million 2014", "Heartstone 29 Million 20120", "Minecraft 91 Million 2011", "DOTA 2 5 million 2015", "The Division 2 N/A 2019", "The Splatoon 2" )
print(f"[5] {popular_games_2021[5]}")
aantal_games = len(popular_games_2021)

# [b] Geef de lengte van de tekst van de 8ste game (DOTA) uit de lijst weer.
print(len(popular_games_2021[8]))

# [c] Geef op het scherm weer met een volzin: "Er zitten [aantal games] games in de lijst." Vervang daarbij [aantal games] door het aantal elementen in de lijst. Vraag het aantal elementen op uit de lijst.
# -1 for Empty Index
print(f"Er zitten {aantal_games -1} games in de lijst")

# [d] De ranking moet worden aangepast want de game Snake blijkt een instant hit en komt binnen op de 2de plaats. Voeg de game Snake toe aan de lijst op de tweede plaats.
print(f"[2] {popular_games_2021[2]}")

# [e] Verwijder de game "The Splatoon" uit de lijst en geef de naam op het scherm weer zoals deze uit de lijst is gekomen in een volzin: "Helaas heeft de game [naam van de game] het niet gered om in de top 10 te blijven. We nemen waardig afscheid van [naam van de game]."
print(f"Helaas heeft de game {popular_games_2021[11]} het niet gered om in de top 10 te blijven. We nemen waardig afscheid van {popular_games_2021[11]}.")

# [f] Nadat de redactie de lijst had gezien, hebben ze de opmerking geplaatst dat er een fout zit in de tekst van de game "Heartstone". Het jaartal moet 2012 zin. Pas de tekst in de lijst aan met Python code.
print({popular_games_2021[7]})
# Replacing "Heartstone 29 Million 20120" with "Heartstone 29 Million 2012"
popular_games_list = list(popular_games_2021)
popular_games_list[7] = "Heartstone 29 Million 2012"
popular_games_2021 = tuple(popular_games_list)

print({popular_games_2021[7]})

# Tuple
# Tuples zijn vergelijkbaar met lists. Ze zijn echter niet meer wijzigbaar nadat ze zijn aangemaakt. Om een tuple te maken gebruik je ronde haakjes in plaats van vierkante haakjes.

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# Tuples zijn niet wijzigbaar
my_tuple[0] = 6 # Geeft een error

# Gegeven een lijst met computer leveranciers
    # Apple
    # Asus
    # Dell
    # Lenovo
    # Acer
    # Samsung
    # MSI
    # Hewlett - Packard(HP)
    # Toshiba
    # Microsoft
    # Chuwi
    # Sony

# Opdracht
# Maak een Python programma waarin de computer leveranciers in een tuple worden opgeslagen. Na elke opdracht geef je de tuple op het scherm weer.
aantal_comp_leveranciers = ('Apple', 'Asus', 'Dell', 'Lenovo', 'Acer', 'Samsung', 'MSI', 'Hewlett-Packard (HP)', 'Toshiba', 'Microsoft', 'Chuwi', 'Sony')
print(aantal_comp_leveranciers)

# [a] Geef in een volzin het aantal computer leveranciers in de tuple. "De tuple bevat [aantal computer leveranciers] computer leveranciers."
print(f"De tuple bevat {len(aantal_comp_leveranciers)} computer leveranciers")
print(aantal_comp_leveranciers)

# [b] Geef in een volzin het aantal karakters van computer leverancier nummer 8; "De naam van [Naam computer leverancier] bestaat uit [aantal karakters] karakters."
print(f"De naam van {aantal_comp_leveranciers[7]} bestaat uit {len(aantal_comp_leveranciers[7])} karakters.")

# [c] Geef de naam van de computer leverancier op de 10de plaats
index = aantal_comp_leveranciers.index('Samsung')
print(f"De index van computer leverancier {aantal_comp_leveranciers[5]} is {index}")

# Dictionary
# Een heel belangrijk datatype is de "dictionary", in andere talen ook wel een "map" of "object" genoemd. Hierin kun je key/value pairs opslaan. Een key is een unieke waarde die je gebruikt om een value op te halen. Een value is een waarde die je opslaat in de dictionary. Een dictionary maak je met behulp van accolades.
dictionary = {"key": "value"}
print(dictionary)
print(dictionary["key"])
dictionary["key"] = ("new value")
print(dictionary["key"])
dictionary["new key"] = "new value"
print(dictionary)

# Dictionaries hebben heel veel operaties en zul je veel gebruiken in alle talen.
# Gegeven een dictionary met telefoonnummers uit films (naam van de film is de key, het nummer de value):
    # The Simpsons, 636-555-3226
    # Vegas Vacation, 555-0100
    # Ghostbusters, 555-23678
    # Billy Madison, 555-0840
    # Swingers, 213-555-4679
    # Bruce Almighty, 555-0123
    # Seinfeld, 555-FILK
    # Arrested Development, 555-0113
    # Die Hard With a Vengeance, 555-0001
    # The A-Team, 555-6162

# Opdrachten
# Zet bovenstaande lijst in een python dictionary. Handel daarna de volgende acties af in je code:
dictionary = {'The Simpsons': '636-555-3226', 'Vegas Vacation': '555-0100', 'Ghostbusters': '555-23678', 'Billy Madison': '555-0840', 'Swingers': '213-555-4679', 'Bruce Almighty': '555-0123', 'Seinfeld': '555-FILK', 'Arrested Development': '555-0113', 'Die Hard With a Vengeance': '555-0001', 'The A-Team': '555-6162'}
print(dictionary)

# [a] Geef het telefoonnummer van Bruce Almighty in de volzin: "Het telefoonnummer van Bruce Almighty is [telefoonnummer]."
dictionary = {"film": "phone-number"}
print(dictionary)
dictionary["film"] = "Bruce Almighty"
dictionary["phone-number"] = "555-0123"

print(f"Het telefoonnummer van {dictionary['film']} is {dictionary['phone-number']}")

# [b] Voeg het telefoonnummer van de Harry Potter toe, nummer: 605-475-6961 aan de dictionary.

# [c] Pas het telefoonnummer van de Ghostbusters aan. Dit moet zijn 555-2368. Geef in een volzin weer. "Het telefoonnummer [telefoonnummer] van de Ghostbusters is gewijzigd naar [nieuwe nummer]."

# [d] Verwijder het telefoonnummer van Seinfeld. Gebruik de volzin: "Telefoonnummer [telefoonnummer] van Seinfeld is verwijderd."

# [e] Geef aan hoeveel telefoonnummers er nu in dictionary zitten. Gebruik de volzin: "In de dictionary zitten [aantal telefoonnummers] telefoonnummers."
