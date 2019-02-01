import pickle
import glob

class Grape:
    def __init__(self, nameGiven, imageGiven, idGiven):
        self.id = idGiven
        self.name = nameGiven
        self.image = imageGiven

grapesRaw = glob.glob("Grapes\*.png")

grapes = []

x = 0
for i in grapesRaw:
     grapes.append(Grape(i.split("\\")[1].split(".")[0],i,x))
     x += 1

for i in grapes:
    print(i.name,i.image,i.id)
