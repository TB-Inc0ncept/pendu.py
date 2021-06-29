nom_fichier=input("Nom du fichier: ")

fichier1=open(nom_fichier,'r')
fichier2=open("data.txt",'w')

fichier2.write("choix=[")

for ligne in fichier1:
  fichier2.write('{!r},'.format(ligne))

fichier2.write("'crocodile']")

fichier1.close()
fichier2.close()