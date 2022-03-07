#########################################
# groupe MI 1
# Pierre RATCLIFFE
# Yassine BAGHDAD-BEY
# Sephora TAHA
# Nique PRYSCIA
# https://github.com/uvsq22008849/projet_tas_de_sable.git
#########################################


##################### Import des modules ##########################

import tkinter as tk
import random

##################### variables globales ##########################
racine = tk.Tk()

HEIGHT = 500
WIDTH = 500
#nombre_sable_cellule = random.randint(0,9)
rows, cols = (5, 5)
liste_cellule = [[random.randint(0,5) for i in range(cols)] for j in range(rows)]
liste_rectangle = [[0 for i in range(cols)] for j in range(rows)]
generer = False

####################### Import module #############################



######################### Fonctions ###############################

def configuration_initiale():
    nombre_sable_cellule = random.randint(0,5)


def configuration_courante():
    #coordonnées_x = event.x
    #coordonnées_y = event.y
    global generer
    for i in range(0, 5):
        for j in range(0, 5):
            if liste_cellule[i][j] == 0:
                rectangle = canvas.create_rectangle((j * 100, i * 100), (j * 100 + 100, i * 100 + 100), fill = "white")
                liste_rectangle[i][j] = rectangle
                #print(rectangle)
            elif liste_cellule[i][j] == 1:
                rectangle = canvas.create_rectangle((j * 100, i * 100), (j * 100 + 100, i * 100 + 100), fill = "#caddee")
                liste_rectangle[i][j] = rectangle
            elif liste_cellule[i][j] == 2:
                rectangle = canvas.create_rectangle((j * 100, i * 100), (j * 100 + 100, i * 100 + 100), fill = "#7aabd4")
                liste_rectangle[i][j] = rectangle
            elif liste_cellule[i][j] == 3:
                rectangle = canvas.create_rectangle((j * 100, i * 100), (j * 100 + 100, i * 100 + 100), fill = "#397bb3")
                liste_rectangle[i][j] = rectangle
            elif liste_cellule[i][j] == 4:
                rectangle = canvas.create_rectangle((j * 100, i * 100), (j * 100 + 100, i * 100 + 100), fill = "#255075")
                liste_rectangle[i][j] = rectangle
            elif liste_cellule[i][j] == 5:
                rectangle = canvas.create_rectangle((j * 100, i * 100), (j * 100 + 100, i * 100 + 100), fill = "#112637")
                liste_rectangle[i][j] = rectangle
    generer = True
    #print(liste_rectangle)


def modif_configuration_courante():
    for i in range(0, 5):
        for j in range(0, 5):
            if liste_cellule[i][j] == 0:
                canvas.itemconfigure(liste_rectangle[i][j], fill = "white")
                #print(rectangle)
            elif liste_cellule[i][j] == 1:
                canvas.itemconfigure(liste_rectangle[i][j], fill = "#caddee")
            elif liste_cellule[i][j] == 2:
                canvas.itemconfigure(liste_rectangle[i][j], fill = "#7aabd4")
            elif liste_cellule[i][j] == 3:
                canvas.itemconfigure(liste_rectangle[i][j], fill = "#397bb3")
            elif liste_cellule[i][j] == 4:
                canvas.itemconfigure(liste_rectangle[i][j], fill = "#255075")
            elif liste_cellule[i][j] == 5:
                canvas.itemconfigure(liste_rectangle[i][j], fill = "#112637")


def iteration():
    if generer:
        for i in range(0, 5):
            for j in range(0, 5):
                if liste_cellule[i][j] >= 4:
                    liste_cellule[i][j] -= 4
                    if i > 0 and i < 4:
                        liste_cellule[i-1][j] += 1
                        liste_cellule[i+1][j] += 1
                    if j > 0 and j < 4:
                        liste_cellule[i][j-1] += 1
                        liste_cellule[i][j+1] += 1
        modif_configuration_courante()
    #configuration_courante()
                

######################### Pogramme ################################

canvas = tk.Canvas(racine, bg = "white", height=HEIGHT, width=WIDTH)
bouton_aleatoire = tk.Button(racine, text = "Générer configuration aléatoire",command = configuration_courante, padx = 20, pady = 20, font =("Helvetica", "20"))
bouton_iteration = tk.Button(racine, text = "Effectuer une iteration",command = iteration, padx = 20, pady = 20, font =("Helvetica", "20"))

canvas.grid(row = 0, column = 0)
bouton_aleatoire.grid(row = 1, column = 0)
bouton_iteration.grid(row = 0, column = 1)
for i in range(5):
    canvas.create_line((i * 100, 0), (i * 100, 500), fill="blue", width=5)
    canvas.create_line((0, i * 100), (500, i * 100), fill="blue", width=5)

#print(liste_cellule)


racine.mainloop()
#sephora test#