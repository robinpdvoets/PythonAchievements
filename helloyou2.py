hello = "Hello, mijn naam is {owner}. Wat is die van jou?"
print(hello.format(owner = "Robin Voets"))

username = input("Mijn naam is:")
print("Goededag " + username, "Ik zal jou meteen even de datum doorgeven!")

import datetime

x = datetime.datetime.now()

print("Vandaag is het " + x.strftime("%d"), "van " + x.strftime ("%B"), ".")
while True: 
     query = input('Wil je doorgaan honneponnetje? Y/N') 
     Fl = query[0].lower() 
     if query == '' or not Fl in ['y','n']: 
        print('Please answer with yes or no!') 
     else: 
        break 
if Fl == 'y': 
    print("Joeperdepoepjes")
if Fl == 'n': 
    print("Nu mag je opkankeren ook lul")