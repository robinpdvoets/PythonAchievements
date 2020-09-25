import time

a = True
while a == True:
    hello = "Hello, mijn naam is {owner}. Kan jij mij jou naam vertellen?"
    print(hello.format(owner = "Robin Voets"))

    time.sleep (1)

    username = input("Mijn naam is:")
    print("Goededag " + username, "Ik heb trouwens een paar vragen voor je!")

    time.sleep (1)

    import datetime

    x = datetime.datetime.now()

    print("Vandaag is het " + x.strftime("%d"), " " + x.strftime ("%B"))
    while True: 
             query = input('Wil je doorgaan? Y/N')
             Fl = query[0].lower()
             if query == '' or not Fl in ['y','n']: 
                print('Antwoord even met yes of no!') 
             else: 
                break 
    if Fl == 'y': 
            print("Woohooo nog een keertje dan maar!")
    if Fl == 'n': 
             break 