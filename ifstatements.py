varA = 55
varB = 1

if (1 + 1 == 3):
    print("Hallo")

if (varB > varA):
    print("varB is inderdaad groter dan varA")
elif (varA > 50):
    print("Doe dan dit")
else:
    print("Nee, varB is niet groter dan varA")


if (varA == 51):
    pass
else:
    print("Leuk man, geweldig van je. Lul die je bent")
    if (varA == 55):
        print("EXACT 55")

varX = True
varY = 13

if ( varX == True and varY > 2 ):
    print("Cool")
if ( varX == False or (varY > 0 and varY < 10) ):
    print("Ja hoor")


W = False
X = True
Y = True
Z = True

if ( W and (X or Y) and Z):
    print("Geweldig!")
