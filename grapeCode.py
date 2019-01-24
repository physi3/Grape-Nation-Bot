import datetime
import discord
import time
import pickle

class myUser:
    def __init__(self, idGiven):
        self.id = idGiven
        self.grapes = 0
        self.lastDailyTime = datetime.datetime(2018,1,1,1,1,1,1)
        self.collectedDaily = False
    def getDaily(self):
        self.currentTime = datetime.datetime.now()
        if datetime.datetime.now() - self.lastDailyTime >= datetime.timedelta(1,0,0):
            self.grapes += 500
            self.collectedDaily = True
            self.lastDailyTime = self.currentTime
        else:
            self.collectedDaily = False

class myUsers:
    def __init__(self):
        self.myUsersList = []
    def findUser(self,idGiven):        
        for i in range(len(self.myUsersList)):
            if self.myUsersList[i].id == idGiven:
                return i
def updateUsers():
    pickle_out = open("dict.pickle","wb")
    pickle.dump(myUsers.myUsersList, pickle_out)
    pickle_out.close()

myUsers = myUsers()
pickle_in = open("dict.pickle","rb")
#myUsers.myUsersList = pickle.load(pickle_in)
myUsers.myUsersList = []
pickle_in.close()

TOKEN = 'NTM0NzgzOTYxNTkxOTcxODQw.DyE0Mw.eLFuXO6LRDdWCc0XtxzeueoWRIM'

client = discord.Client()

@client.event
async def on_message(message):
    exists = False
    for i in range(len(myUsers.myUsersList)):
        if myUsers.myUsersList[i].id == message.author.mention:
            exists = True
    if exists == False:
        myUsers.myUsersList.append(myUser(message.author.mention))
    updateUsers()
    splitContent = message.content.split(" ")
    for i in range(len(splitContent)):
        splitContent[i] = splitContent[i].lower()
    if message.author == client.user:
        return
    if splitContent[0] == "gn!":
        if splitContent[1] == "hello":
            msg = 'Hello {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)
            poll(message,1,1)
        if splitContent[1:6] == ["what","do","they","say","about"]:
            if message.mentions[0].mention == "<@!388774545328177153>":
                msg = 'You know what they say. {0.mentions[0].mention} has a peen the length of 2 coke cans stacked on top of each other.'.format(message)
            elif message.mentions[0].mention =='<@!425783117165363200>':
                msg = "You know what they say. {0.mentions[0].mention} has the smallest peen of them all. Plus he's ginger. And bad.".format(message)
            else:
                msg = 'You know what they say. {0.mentions[0].mention} has a small peen.'.format(message)
            await client.send_message(message.channel, msg)
            print(msg)
        if splitContent[1:5] == ["how","laggy","am","i"]:
            msg = "{0.author.mention} is almost as laggy as a 1920's PC in eastern Mongolia".format(message)
            await client.send_message(message.channel, msg)
        if splitContent[1:4] == ["how","laggy","is"]:
            msg = "{0.mentions[0].mention} is almost as laggy as a 1920's PC in eastern Mongolia".format(message)
            await client.send_message(message.channel, msg)
        if splitContent[1] == 	"daily":
            userToUse = myUsers.myUsersList[myUsers.findUser(message.author.mention)]
            userToUse.getDaily()
            if userToUse.collectedDaily:
                msg = "Okay, {0.author.mention} You now have "+str(userToUse.grapes)+" grapes"
            else:
                msg = "Sorry, {0.author.mention} you've got to wait another "+(str(datetime.timedelta(1,0,0) - (datetime.datetime.now() - userToUse.lastDailyTime))).split(".")[0].split(":")[0]+" hours and "+(str(datetime.timedelta(1,0,0) - (datetime.datetime.now() - userToUse.lastDailyTime))).split(".")[0].split(":")[1]+" minutes. You have "+str(userToUse.grapes)+" grapes."
            msg = msg.format(message)
            await client.send_message(message.channel, msg)
            updateUsers()
        if splitContent[1] == 	"balance":
            userToUse = myUsers.myUsersList[myUsers.findUser(message.author.mention)]
            msg = "Okay, {0.author.mention} You have "+str(userToUse.grapes)+" grapes."
            msg = msg.format(message)
            await client.send_message(message.channel, msg)
        if splitContent[1:5] == ["when","did","i","join"]:
            date = str(message.author.joined_at).split(" ")[0].split("-")+str(message.author.joined_at).split(" ")[1].split(":")[:-1]
            msg = "Okay, {0.author.mention} you joined "+date[1]+" "+date[2]+" "+date[0]+" at "+date[3]+":"+date[4]
            msg = msg.format(message)
            await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
