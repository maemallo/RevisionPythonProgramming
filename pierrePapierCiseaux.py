import random

myList = [ "pierre","papier", "ciseaux"]
counterUser = 0
counterSystem = 0

def systemChoice():
    progChoice = random.choice(myList)
    return progChoice


def userChoice():
    choice = input("Veuillez preciser votre choix (pierre,papier,ciseaux): ")
    while choice not in myList:
        choice=input("Vous devez choisir entre les objets suivants:pierre/papier/ciseaux: ")
    return(choice)


def winner(user,system):
    if ((user=="pierre" and system=="ciseaux") or (user=="papier" and system=="pierre") or (user=="ciseaux" and system=="papier")) : 
        etat= True
    else:
        etat=False 
    return (etat)

def counterScore(count):
    count = count+1
    return count



#programme principale

while True:
    choixClient = userChoice()
    choixSysteme = systemChoice()
    while choixClient ==  choixSysteme:
        print("Vous avez un choix identique au challeger,merci de rejouer")
        choixClient = userChoice()
        choixSysteme = systemChoice()
        
    gagnant = winner(choixClient,choixSysteme)
    if gagnant==True:
        oldcounteruser=counterUser
        counterUser = counterScore(counterUser)
        print(f"Vous avez choisi {choixClient} et le systeme {choixSysteme} ")
        print(f"Felictation!vous remportez 01 points et votre score passe de {oldcounteruser} à {counterUser}")
    else:
        oldcounterSystem=counterSystem
        counterSystem=counterScore(counterSystem)
        print(f"Désolé!Le point reviens à votre challenger et son score passe de {oldcounterSystem} à {counterSystem}")
    Choix=input("Souhaitez vous quitter le programme (Q)")
    if Choix.upper()=="Q":
        break

print("user = {} point  system = {} point ".format(counterUser,counterSystem))
