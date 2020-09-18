# Hoger / Lager spelletje maken.
# Nieuwe stof is gebruik van Random getallen maken.

# Doel:
# Speler krijgt een getal van 1 t/m 10
# Speler moet aangeven of het volgende getal hoger of lager wordt
# Je wint of verliest (of gelijkspel)

import random

willekeur = random.randrange(1, 11)
print("Het getal is ", willekeur)
print("Wordt het volgende getal hoger (H) of lager (L)?")

antwoord = input()




# 1. Er wordt een willekeurig getal gemaakt en in een variabele opgeslagen
# 2. Het getal wordt getoond
# 3. Er wordt de speler gevraagd om input voor hoger of lager, en dit antwoord slaan we op in een variabele.
# 4. Gebruik antwoord om een voorwaarde te definieren
# 5. Als het antwoord "H" is (als antwoord gelijk staat aan "H"), dan...

if( antwoord == "H" ):
    print("Je hebt hoger aangegeven")




