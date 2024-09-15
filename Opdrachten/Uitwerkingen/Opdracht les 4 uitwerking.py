# Opdracht Les 4 Uitwerking (nina-1074862)

# Mijn uitwerking: Opdracht 1 (List)
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

# Mijn uitwerking: Opdracht 1 (Tuple)
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

# Mijn uitwerking: Opdracht 1 (Dictionary)
dictionary = {'The Simpsons': '636-555-3226', 'Vegas Vacation': '555-0100', 'Ghostbusters': '555-23678', 'Billy Madison': '555-0840', 'Swingers': '213-555-4679', 'Bruce Almighty': '555-0123', 'Seinfeld': '555-FILK', 'Arrested Development': '555-0113', 'Die Hard With a Vengeance': '555-0001', 'The A-Team': '555-6162'}
print("\n",dictionary)

# [a] Geef het telefoonnummer van Bruce Almighty in de volzin: "Het telefoonnummer van Bruce Almighty is [telefoonnummer]."
print("\n",f"Het telefoonnummer van Bruce Almighty is {dictionary['Bruce Almighty']}.")
print(dictionary)

# [b] Voeg het telefoonnummer van de Harry Potter toe, nummer: 605-475-6961 aan de dictionary.
# Adding Harry Potter to the dictionary
dictionary['Harry Potter'] = '605-475-6961'
print("\n",dictionary)

# [c] Pas het telefoonnummer van de Ghostbusters aan. Dit moet zijn 555-2368. Geef in een volzin weer. "Het telefoonnummer [telefoonnummer] van de Ghostbusters is gewijzigd naar [nieuwe nummer]."
old_number_ghostbusters = dictionary['Ghostbusters']

# Changing the phone number of Ghostbusters
dictionary['Ghostbusters'] = '555-2368'

# Saving the new number
new_number_ghostbusters = dictionary['Ghostbusters']

print("\n",f"Het telefoonnummer {old_number_ghostbusters} van de Ghostbusters is gewijzigd naar {new_number_ghostbusters}.")
print(dictionary)

# [d] Verwijder het telefoonnummer van Seinfeld. Gebruik de volzin: "Telefoonnummer [telefoonnummer] van Seinfeld is verwijderd."
old_number_seinfeld = dictionary['Seinfeld']

# Verwijder Seinfeld
del dictionary['Seinfeld']

print("\n",f"Telefoonnummer {old_number_seinfeld} van Seinfeld is verwijderd. ")
print(dictionary)

# [e] Geef aan hoeveel telefoonnummers er nu in dictionary zitten. Gebruik de volzin: "In de dictionary zitten [aantal telefoonnummers] telefoonnummers."
print("\n",f"In de dictionary zitten {len(dictionary)} telefoonnummers.")
print(dictionary)