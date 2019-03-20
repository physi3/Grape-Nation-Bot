import pickle
import glob
import datetime

rarities = ["Common","Uncommon","Rare","Epic","Legendary","Mythic"]

class Grape:
    def __init__(self, nameGiven, imageGiven, descriptionGiven, ratingGiven):
        self.description = descriptionGiven
        self.name = nameGiven
        self.image = imageGiven
        self.rating = ratingGiven
    def addImage(self, imageUrl):
        self.image = imageUrl


grapesRaw = glob.glob("Grapes/*")


grapes = []


pickle_in = open("grapes.pickle","rb")
grapes = pickle.load(pickle_in)
pickle_in.close()

grapeNames=[]

for i in grapes:
    grapeNames.append(i.name)


for i in grapesRaw:
    if (i.split("/")[1].split(".")[0]+" Grape" in grapeNames):
        print(i.split("/")[1].split(".")[0]+" Grape Already Exists")
    else:
        desc = input("Enter Description and Rating For "+i.split("/")[1].split(".")[0]+" Grape"+"\n>>> ")
        rating = int(input(">>> "))
        grapes.append(Grape(i.split("/")[1].split(".")[0]+" Grape",i,desc,rating))


pickle_out = open("grapes.pickle","wb")
pickle.dump(grapes, pickle_out)
pickle_out.close()
