# Opdracht Les 3 Uitwerking (nina-1074862)

# Mijn uitwerking: Opdracht 1 (Input vragen)
age_str = input('What is your age? ')
print(f'Your age is {age_str}')

# Mijn uitwerking: Opdracht 1 (Internet verbinding selectie)
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

# Mijn uitwerking: Opdracht 1 (Vergelijken met een sub-string)
print("Is Hello with a capital 'H' within the string 'Hello, everyone!'")
if "Hello" in "Hello, everyone!":
    print('Yes, Hello is within the Hello, everyone! string')

print("Is Hello with a lower case 'h' within the string 'Hello, everyone!'")
if "hello" in "Hello, everyone!":
    print('Yes, hello is within the Hello, everyone! string')
else:
    print('No, hello with small letters is not within the string')

# Mijn uitwerking: Opdracht 1 (Flowchart)
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

# Mijn uitwerking: Opdracht 2 (Flowchart)
print("Shopping Cart")
payment_method = input("Payment Method? Online/Offline ")

if payment_method.upper() == "ONLINE":
    print("Online, Place Purchase Order")
    admin_user = input("Admin User? [Yes/No] ")
    if admin_user.upper() == "YES":
        print("Enter payment details")
        print("Place Order")

    elif admin_user.upper() == "NO":
        approval_rules = input("Approval Rules? [Approved/Rejected]")
        if approval_rules.upper() == "APPROVED":
            print("Enter payment details.")
            print("Place Order.")
        elif approval_rules.upper() == "REJECTED":
            print("Purchase Order rejected.")
        else:
            print("Abort, Unknown input.")
            exit()
    else:
        print("Abort, Unknown input.")
        exit()

elif payment_method.upper() == "OFFLINE":
    print("Offline, Place Purchase Order")

    admin_user = input("Admin User? [Yes/No]  ")
    if admin_user.upper() == "YES":
        print("Order Created Automatically")
    elif admin_user.upper() == "NO":
        approval_rules = input("Approval Rules? [Approved/Rejected]")
        if approval_rules.upper() == "APPROVED":
            print("Order Created automatically.")
            exit()
        elif approval_rules.upper() == "REJECTED":
            print("Purchase Order Rejected")
            exit()
        else:
            print("Abort, Unknown input.")
            exit()
else:
    print("Abort, Unknown input.")
    exit()

# Mijn uitwerking: Opdracht 1 (Bestellen)
print("Welkom bij de Mac Donald's ")
takeaway_or_restaurant = input("Hier opeten of meenemen? [Opeten/Meenemen]: ")

# FOR EATING AT THE RESTAURANT
if takeaway_or_restaurant.upper() == "OPETEN":
    print("Hier opeten")
    burgers_drankjes = input("Burgers of drankjes? [Burgers/Drankjes]: ")
    # FOR BURGERS AT THE RESTAURANT
    if burgers_drankjes.upper() == "BURGERS":
        burger_menu = input("Burgers [Hamburger, Cheeseburger, Big Mac, Quarter Pounder]: ")
        burger_menu_choice = ["HAMBURGER", "CHEESEBURGER", "BIG MAC", "QUARTER POUNDER"]

        if burger_menu.upper() in burger_menu_choice:
            print(burger_menu.title())
            print("Bedankt voor uw bestelling en eet smakelijk in ons restaurant.")
            exit()

    # FOR DRINKS AT THE RESTAURANT
    elif burgers_drankjes.upper() == "DRANKJES":
        koud_of_warm = input("Drankjes [Warme/Koude]: ")

        if koud_of_warm.upper() == "WARME":
            drinks_menu_warm = input("Warme Drankjes [Koffie, Cappuccino, Chocolademelk]: ")
            drinks_menu_warm_choice = ["KOFFIE", "CAPPUCCINO", "CHOCOLADEMELK"]

            if drinks_menu_warm.upper() in drinks_menu_warm_choice:
                print(drinks_menu_warm.title())
                print("Bedankt voor uw bestelling en eet smakelijk in ons restaurant.")
                exit()
    else:
        print("Abort, Unknown input.")
        exit()

# FOR TAKEAWAY AT MCDONALD'S
elif takeaway_or_restaurant.upper() == "MEENEMEN":
    print("Meenemen")
    burgers_drankjes = input("Burgers of drankjes? [Burgers/Drankjes]: ")
    # FOR BURGERS
    if burgers_drankjes.upper() == "BURGERS":
        burger_menu = input("Burgers [Hamburger, Cheeseburger, Big Mac, Quarter Pounder]: ")
        burger_menu_choice = ["HAMBURGER", "CHEESEBURGER", "BIG MAC", "QUARTER POUNDER"]

        if burger_menu.upper() in burger_menu_choice:
            print(burger_menu.title())
            print("Bedankt voor uw bestelling, goede reis en eet smakelijk.")
            exit()

        else:
            print("Abort, Unknown input.")
            exit()

    # FOR DRINKS
    elif burgers_drankjes.upper() == "DRANKJES":
        koud_of_warm = input("Drankjes [Warme/Koude]: ")

        if koud_of_warm.upper() == "WARME":
            drinks_menu_warm = input("Warme Drankjes [Koffie, Cappuccino, Chocolademelk]: ")
            drinks_menu_warm_choice = ["KOFFIE", "CAPPUCCINO", "CHOCOLADEMELK"]

            if drinks_menu_warm.upper() in drinks_menu_warm_choice:
                print(drinks_menu_warm.title())
                print("Bedankt voor uw bestelling, goede reis en eet smakelijk.")
                exit()

            else:
                print("Abort, Unknown input.")
                exit()

        elif koud_of_warm.upper() == "KOUDE":
            drinks_menu_cold = input("Koude Drankjes [Coca Cola, Cola Zero, 7-Up, Fanta, Fristi]: ")
            drinks_menu_cold_choice = ["COCA COLA", "COLA ZERO", "7-UP", "FANTA", "FRISTI"]

            if drinks_menu_cold.upper() in drinks_menu_cold_choice:
                print(drinks_menu_cold.title())
                print("Bedankt voor uw bestelling, goede reis en eet smakelijk.")
                exit()
            else:
                print("Abort, Unknown input.")
                exit()
        else:
            print("Abort, Unknown input.")
            exit()
    else:
        print("Abort, Unknown input.")
        exit()
else:
    print("Abort, Unknown input.")
    exit()
