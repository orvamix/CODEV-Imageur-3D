import csv
import pickle

points={}
# Ouvrir le fichier csv
with open('csv_emetteur.csv', 'r') as f:
    # Créer un objet csv à partir du fichier
    obj = csv.reader(f,delimiter=';')
    
    i=0
    for ligne in obj:
        thisdict = {"emetteur": list(map(float, ligne))}
        nom="point"+str(i)
        points[nom]=thisdict
        i=i+1
with open('csv_objet.csv', 'r') as f:
    # Créer un objet csv à partir du fichier
    obj = csv.reader(f,delimiter=';')
    
    i=0
    for ligne in obj:
        nom="point"+str(i)
        points[nom]["objet"]=list(map(float, ligne))
        i=i+1
with open('csv_recepteur.csv', 'r') as f:
    # Créer un objet csv à partir du fichier
    obj = csv.reader(f,delimiter=';')
    
    i=0
    for ligne in obj: 
        nom="point"+str(i)
        points[nom]["recepteur"]=list(map(float, ligne))
        i=i+1
with open("points_coord.codev", "wb") as fp:   #Pickling
            pickle.dump(points, fp)  