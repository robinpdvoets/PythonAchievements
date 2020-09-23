print ("Hello You!")
import time

time.sleep(1)

print ("Ik ben Robin Voets")
print ("Wie ben jij?")

time.sleep(1)

print ("Typ je naam in: ")

inputnaam = input()

time.sleep(1)

print ("Hallo " + inputnaam) 

time.sleep(1)

print ("Waar woon ik?")

time.sleep(1)
print ("A. Heemstede")
time.sleep(1)
print ("B. Hoofddorp")
time.sleep(1)
print ("C. Haarlem")

antwoord = input("typ A, B of C: ").lower()
 
if antwoord =="a":

    print ("Jouw antwoord was: " + antwoord + ", " + "dit klopt niet!")

elif antwoord =="b":

    print ("Nee dat klopt niet, ik heb hier wel op school gezeten.")

elif antwoord =="c":

    print ("Dit klopt, ik woon hier al heel mijn leven.")

else:

    print ("Je kunt alleen met A, B of C antwoorden.")

print ("Hoe oud ben ik?")
time.sleep(1)
print ("A. 17")
time.sleep(1)
print ("B. 16")
time.sleep(1)
print ("C. 18")

antwoord = input("typ A, B of C: ").lower()
 
if antwoord =="a":

    print ("Jouw antwoord was: " + antwoord + ", " + "dit klopt wel! Ik ben inderdaad 17 :D!")

elif antwoord =="b":

    print ("JAAAAA! Gefeliciteerd je hebt het antwoord fout!.")

elif antwoord =="c":

    print ("Ehh ik ben toch jonger dan 18")

else:

    print ("Je kunt alleen met A, B of C antwoorden.")

print ("Hoe heet mijn oude school?")
time.sleep(1)
print ("A. Haarlemmermeer Lyceum")
time.sleep(1)
print ("B. Kaj Munk")
time.sleep(1)
print ("C. KSH")

antwoord = input("typ A, B of C: ").lower()
 
if antwoord =="a":

    print ("Jouw antwoord was: " + antwoord + ", " + "dit klopt niet!")

elif antwoord =="b":

    print ("Nee zekers niet, wat een rot school")

elif antwoord =="c":

    print ("Dit klopt! Ik heb ook het KSH gezeten voor 5 jaartjes.")

else:

    print ("Je kunt alleen met A, B of C antwoorden.")
 # .lower() maakt alles lowercase waardoor je alleen hoeft te checken voor a/b/c