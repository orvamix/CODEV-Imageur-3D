import csv
import pickle

points_ME={}
points_MR={}
# Ouvrir le fichier csv
with open('csv_emetteur.csv', 'r') as f:
    # Créer un objet csv à partir du fichier
    obj = csv.reader(f,delimiter=';')
    
    i=0
    for ligne in obj:
        thisdict = {"emetteur": list(map(float, ligne))}
        nom="point"+str(i)
        points_ME[nom]=thisdict
        i=i+1
with open('csv_objet_emetteur.csv', 'r') as f:
    # Créer un objet csv à partir du fichier
    obj = csv.reader(f,delimiter=';')
    
    i=0
    for ligne in obj:
        nom="point"+str(i)
        points_ME[nom]["objet_emetteur"]=list(map(float, ligne))
        i=i+1
with open('csv_objet_recepteur.csv', 'r') as f:
    # Créer un objet csv à partir du fichier
    obj = csv.reader(f,delimiter=';')
    
    i=0
    for ligne in obj:
        thisdict = {"objet_recepteur": list(map(float, ligne))}
        nom="point"+str(i)
        points_MR[nom]=thisdict
        i=i+1
with open('csv_recepteur.csv', 'r') as f:
    # Créer un objet csv à partir du fichier
    obj = csv.reader(f,delimiter=';')
    
    i=0
    for ligne in obj: 
        nom="point"+str(i)
        points_MR[nom]["recepteur"]=list(map(float, ligne))
        i=i+1
print(points_ME)
print(points_MR)
with open("points_coord_ME.codev", "wb") as fp:   #Pickling
            pickle.dump(points_ME, fp)  
with open("points_coord_MR.codev", "wb") as fp:   #Pickling
            pickle.dump(points_MR, fp)  
             