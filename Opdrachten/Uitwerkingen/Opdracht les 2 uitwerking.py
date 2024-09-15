# Opdracht Les 2 Uitwerking

# # Mijn uitwerking: Opdracht 1 (Integers)
people = 7861304740
print(people)
# Ik maak nu gebruik van underscores om de getallen leesbaar te maken
people = 7_861_304_740
print(people)

# Mijn uitwerking: Opdracht 2 (Integers)
people = 7_861_304_740
# Calculation with big numbers
meals = 3
people_eat = people * meals
print(people_eat)

days = 365
meals_per_year = people_eat * days
print(meals_per_year)

# What is the data type?
print (type(meals_per_year))

# Mijn uitwerking: Opdracht 1 (Float)
ethernet_speed_mbps = 1000
efficiency = 0.7
maximum_capacity = ethernet_speed_mbps * efficiency
print(maximum_capacity)

# Mijn uitwerking: Opdracht 2 (Float)
ethernet_speed_mbps = 1000
download_speed_average = 96.25
usage = ethernet_speed_mbps / download_speed_average
print(usage)

# Mijn uitwerking: Opdracht 3 (Float)
speed_of_light = 299_792_458

# Distance between Rotterdam and New York in km
distance_Rotterdam_NewYork = 5_862.03

# Distance between Rotterdam to new York in meters divided by the speed of light
time_to_reach_NYC = (distance_Rotterdam_NewYork * 1000) / speed_of_light
print(f'Time to reach New York is: {time_to_reach_NYC * 1000} milliseconds.')

# What is the data type?
print (type(time_to_reach_NYC))

# Mijn uitwerking: Opdracht 1 (String)
ship = 'Titanic'
print(ship)
ship = "Titanic"
print(ship)
ship = """Titanic"""
print(ship)

# Mijn uitwerking: Opdracht 2 (String)
zonder_escape = 'This is a "good" plan'
print(zonder_escape)
met_escape = "This is a \"good\" plan"
print(met_escape)

paragraph = """Computer Technology means all designs, drawings, procedures (including design, manufacturing, test and maintenance procedures), specifications, software (other than as described within the meaning of the term "Software" defined elsewhere herein), printed circuit board art work, integrated circuit masks, test equipment, tools, fixtures, documentation, training materials, and information, in whatever form, related to, useful, utilizable or necessary in the design, manufacture, test and/or maintenance of the computer system, or relate to any Technology Licenses."""
print(paragraph)
characters_in_paragraph = len(paragraph)
print(f"{paragraph}\n\nThe paragraph has {characters_in_paragraph} characters.")

# Mijn uitwerking: Opdracht 3 (String)
year = 1936
inventor = "Alan Turing"
name_of_machine = "automatic machine"
# Note: Within the text double quotes are used. We need to use single quotes to embrace the string
invention = f'The Turing machine was invented in {year} by {inventor}, who called it an "a-machine" ({name_of_machine}).'
print(invention)

# What is the data type?
print(type(invention))


# Mijn uitwerking: Opdracht 1 (Boolean)
logged_in = False
print(logged_in)

netwerk_activity = True
print(netwerk_activity)

# Mijn uitwerking: Opdracht 1 (Logische operatoren)
user_name = 'John Doe'
entered_name = input("User name, please: ")
size_user_name = len(user_name)
size_entered_name = len(entered_name)
user_name_is_bigger = size_user_name > size_entered_name
entered_name_is_bigger = size_entered_name > size_user_name
print(f"The user name {user_name} has more characters then the entered name {entered_name} is: {user_name_is_bigger}")
print(f"The entered name {entered_name} has more characters then the user name {user_name} is: {entered_name_is_bigger}")

lights_on = False
lock_closed = True
# Not keert de waarde van de boolean om, not True is hetzelfde als False
# Andersom is not False dus True
alarm_activated = not lights_on and lock_closed
print(f"The alarm is activated, is: {alarm_activated}")

# Mijn uitwerking: Opdracht 1 (Containers)
containers_lossen = 331
containers_los_tijd = 441
containers_geladen = 287
containers_laadtijd = 295

lostijd_per_container = containers_los_tijd / containers_lossen
laadtijd_per_container = containers_laadtijd / containers_geladen

print(f"De gemiddelde lostijd bedraagt: {lostijd_per_container} minuten per container")
print(f"De gemiddelde laadtijd bedraagt: {laadtijd_per_container} minuten per container")

# Mijn uitwerking: Formule 1 (Berekening)
import math
x = 9.1
term1 = (3 * x) -1
term2 = 1 + x
term3 = term2**2
y = math.sqrt(term1) + term3
print(f"De waarde van y = {y} als x = {x}")

# Mijn uitwerking: Formule 2 (Berekening)
a = 0.87
b = 22.7
c =  5.03
term1 =  b**2
term2 = 4 * a * c
term3 = term1 - term2
term4 = math.sqrt(term3)
term5 = -b + term4
term6 = 2 * a
y = term5 / term6

print(f"De waarde van y = {y} als a = {a}, b = {b} en c = {c}")

# Mijn uitwerking: Formule 3 (Berekening)
t = 4
v = 179875474.8
c = 299_792_458

term1 = v**2
term2 = c**2
term3 = term1 / term2
term4 = 1 - term3
term5 = v * term4
term6 = 1 / term5
delta = t * term6

print(f"Vanaf een komeet gezien zit u {delta} uur op de tuinstoel.")
print(f"Vanaf een komeet gezien zit u {delta * 60.0} minuten op de tuinstoel.")
print(f"Vanaf een komeet gezien zit u {delta * 60.0 * 60.0} seconden op de tuinstoel.")