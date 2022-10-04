import copy
from random import shuffle

QR = []
def nouvelleQR(questions, choix, rep):
    if (len(choix) != len(rep)):
        raise ValueError("The number of the choices should be the same as the number of the answers.")
    return [questions, choix, rep]

def ajouterQR (qr):
    global QR
    return QR.append(qr)

def orderAleatoire():
    global QR
    n = len(QR)
    order = range(n)
    shuffle(order)
    return order

exec(open("QR.py").read())

answer = "q"
indices = []
while answer == "q":
    # infinite loop
    n = int(input("Nombre de questions: "))
    if n > len((QR)):
        print("Vous avez dépassé le nombre de questions que vous avez répondu !")
        break
    #indices des question
    indices = list(range(len(QR)))
    #mélanger les indices
    shuffle(indices)
    score = 0.0
    #afficher et lire les n premieres questions obtenues après le mélange
    for i in range(n):
        idx = indices[i]
        qcm = QR[idx]
        print("La question :", qcm[0])
        ## si la reponse est incorrect afficher "Incorrect! " et la bonne réponse##
        if qcm[1] != qcm[2]:
            print("Votre réponse à cette question est incorrecte")
        ##si non afficher "Trés bien, continuez (o/n)?"
        else:
            print("Votre réponse à cette question est correcte ! ")
            score = score + 1
    #affichage du score
    print(" votre score = {}".format(score/n))
    answer = input("Voulez-vous continuer ? (o/q)")
    if answer == "q":
        continue
    else:
        break



