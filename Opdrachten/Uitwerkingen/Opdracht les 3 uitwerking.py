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
    exit()

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
adult_or_child = input('Is the patient an adult or a child? [Adult/Child] ')

if adult_or_child in ["Adult", "ADULT", "adult"]:
    common_tb_symptoms = input('Has common TB symptoms? [Yes/No]')

    if common_tb_symptoms in ["YES", "yes", "Yes"]:
        print("Treat as likely TB patient and perform full TB exam.")

    elif common_tb_symptoms in ["NO", "No", "no"]:
        print("Have patient report back if unwell, return in 1 month for checkup.")

    else:
        print("Abort, unknown input.")
        exit()

elif adult_or_child in ["Child" , "CHILD" , "child"]:
    tb_test_given = input("Can TB test be given? [Yes/No]")

    if tb_test_given in ["YES" , "yes" , "Yes"]:
        print("Administer TB test.")
        print("Assess TB test results and child's condition.")

    elif tb_test_given in ["NO" , "No" , "no"]:
        child_health = input("Is the child feeling well? [Yes/No]")


        if child_health in ["Yes" , "YES" , "yes"]:
            print("6 months preventive isoniazide.")
            print("Have parent bring in if child shows any symptoms.")

        elif child_health in ["No" , "NO" , "no"]:
            print("Take full history Examine for TB.")
            print("If TB likely diagnosis, treat for TB.")
            print("If other diagnosis more likely, treat as needed and watch for TB symptoms.")

        else:
            print("Abort, unknown input.")
            exit()
    else:
        print("Abort, unknown input.")
        exit()
else:
    print("Abort, unknown input.")
    exit()

# Flowchart
# Maak een Python programma die onderstaande flowchart implementeert. Van alle elipsen/ronde/rechthoek/rechthoekgolf symbolen print je de tekst van de flowchart. De diamanten zijn je if statements, waar je aan de gebruiker een input vraagt. Bijvoorbeeld: yes of no antwoord.

print("Shopping Cart")
payment_method = input("Payment Method? Online/Offline ")

if payment_method.upper() == "ONLINE":
    print("Online, Place Purchase Order")
    admin_user = input("Admin User? ")
    if admin_user.upper() == "YES":
        print("Enter payment details")
        print("Place Order")

    elif admin_user.upper() == "NO":
        approval_rules = input("Approval Rules")
        if approval_rules.upper() == "APPROVED":
            print("Enter payment details.")
            print("Place Order.")
        elif approval_rules.upper() == "REJECTED":
            print("Purchase Order Rejected")

        else:
            print("Abort, Unknown input.")
            exit()

    else:
        print("Abort, Unknown input.")
        exit()

elif payment_method.upper() == "OFFLINE":
    print("Place Purchase Order")
    admin_user = input("Admin User? ")
    if admin_user.upper() == "YES":
        print("Order Created Automatically")
    elif admin_user.upper() == "NO":
        approval_rules = input("Approval Rules")
        if approval_rules.upper() == "APPROVED":
            print("Order Created Automatically")
        elif approval_rules.upper() == "REJECTED":
            print("Purchase Order Rejected")

else:
    print("Abort, Unknown input.")
    exit()
