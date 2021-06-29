import random
from data import choix
import os

def clear(): os.system('clear')
solution = random.choice(choix)

tentatives = 7
affichage = ""
lettres_trouvees = ""
mauvaises_lettres = ""

for l in solution:
  affichage = affichage + "_ "

while tentatives > 0:
  clear()
  print("\nMot à deviner : ", affichage)
  print("-> Mauvaises lettres: " + mauvaises_lettres)
  if tentatives > 1:
    print("Vous avez {} tentatives".format(tentatives))
  else:
    print("Vous avez {} tentative".format(tentatives))
  proposition = input("proposez une lettre : ")[0:1].lower()

  if proposition in solution:
    lettres_trouvees = lettres_trouvees + proposition
  elif proposition in mauvaises_lettres:
    tentatives = tentatives
  else:
    tentatives = tentatives - 1
    mauvaises_lettres = mauvaises_lettres + proposition + " / "

  affichage = ""
  for x in solution:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

  if "_" not in affichage:
      print(">>> Gagné! <<<")
      break

print("Le mot était:",solution)     
print("\n    * Fin de la partie *    ")