import random
import copy

#Je donne 1000 points
point = 300 

#Je genere un prix entier aleatoire.
prix=random.randint(0, 10000)
print(prix)
isIputTrue = False
historiqueTentative=[]
customerStatus={
    "Juste Prix":0,
    "Prix Saisie":[],
    "Point Restant":[]
}
while (isIputTrue == False) and point > 0:

#Je demande a l'utilisateur de me donner le prix
    while True:
        try :
            prixRecu = int(input("veuillez me communiquer le juste prix: "))
        except:
            print("veuillez me communiquer le juste prix: ")
        else:
            break


    #condition de traitement
    if prixRecu < prix:
        print("Votre prix est inferieur au juste prix ")
        point = point - 100
        print(f"il vous reste {point}")
    elif prixRecu > prix:
        print("votre prix est superieur au juste prix")
        point = point - 100
        print(f"il vous reste {point}")
    elif prixRecu == prix:
        print("c'est le juste prix,vous avez gagné!")
        isIputTrue = True
    #historiqueTentative.append(prixRecu)
    #historiqueTentative.append(point)
    #print(historiqueTentative)
    newStatus=copy.deepcopy(customerStatus)

    newStatus["Juste Prix"] = prix 
    newStatus["Prix Saisie"].append(prixRecu)
    newStatus["Point Restant"].append(point)
    historiqueTentative.append(newStatus)
print(historiqueTentative)

     
    


