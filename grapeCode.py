import datetime
import discord
import time
import pickle
import random

rules = [['scissors', 'cuts', 'paper'], ['paper', 'covers', 'rock'], ['rock', 'crushes', 'lizard'], ['lizard', 'poisons', 'spock'], ['spock', 'smashes', 'scissors'], ['scissors', 'decapitates', 'lizard'], ['lizard', 'eats', 'paper'], ['paper', 'disproves', 'spock'], ['spock', 'vaporizes', 'rock'], ['rock', 'crushes', 'scissors']]
choices = ["scissors","paper","rock","spock","lizard"]
outcomes = ["Oh, sorry {0.author.mention}, you lost, because they chose: ","Great {0.author.mention}, you won, because they chose: "]

def rpslsContest(playerInput,computerInput):
    won = False
    for i in range(len(rules)):
        if rules[i][0] == playerInput:
            if rules[i][2] == computerInput:
                won = True
                statement = i
                return [won,rules[statement]]
                break
    if won != True:
        for j in range(len(rules)):
            if rules[j][0] == computerInput:
                if rules[j][2] == playerInput:
                    won = False
                    statement = j
                    return [won,rules[statement]]
                    break

#    playRpls = True
#    computerInput = random.choice(choices)
#    outcome = contest(input(">>> ").lower(),computerInput)
#    print(outcomes[outcome[0]]+computerInput+", remember, "+outcome[1][0],outcome[1][1],outcome[1][2]+".\n")

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
myUsers.myUsersList = pickle.load(pickle_in)
pickle_in.close()


r = open("Token.env","r")
TOKEN = r.read()
r.close()

r = open("Help Menu.txt","r")
helpMenu = r.read()
r.close()

r = open("BMovieScript.txt","r")
BMovieScript = r.read()
r.close()

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
        elif splitContent[1:6] == ["what","do","they","say","about"]:
            if message.mentions[0].mention == "<@!388774545328177153>":
                msg = 'You know what they say. {0.mentions[0].mention} has a peen the length of 2 coke cans stacked on top of each other.'.format(message)
            elif message.mentions[0].mention =='<@!425783117165363200>':
                msg = "You know what they say. {0.mentions[0].mention} has the smallest peen of them all. Plus he's ginger. And bad.".format(message)
            else:
                msg = 'You know what they say. {0.mentions[0].mention} has a small peen.'.format(message)
            await client.send_message(message.channel, msg)
            print(msg)
        elif splitContent[1:5] == ["how","laggy","am","i"]:
            msg = "{0.author.mention} is almost as laggy as a 1920's PC in eastern Mongolia".format(message)
            await client.send_message(message.channel, msg)
        elif splitContent[1:4] == ["how","laggy","is"]:
            msg = "{0.mentions[0].mention} is almost as laggy as a 1920's PC in eastern Mongolia".format(message)
            await client.send_message(message.channel, msg)
        elif splitContent[1:6] == ["read","out","the","best","movie"]:
            msg = ("Okay, {0.author.mention} here's a taster:\n"+BMovieScript+"\n\nIf you want more go to: http://www.script-o-rama.com/movie_scripts/a1/bee-movie-script-transcript-seinfeld.html").format(message)
            await client.send_message(message.channel, msg)
        elif splitContent[1] == "daily":
            userToUse = myUsers.myUsersList[myUsers.findUser(message.author.mention)]
            userToUse.getDaily()
            if userToUse.collectedDaily:
                msg = "Okay, {0.author.mention} You now have "+str(userToUse.grapes)+" grapes"
            else:
                msg = "Sorry, {0.author.mention} you've got to wait another "+(str(datetime.timedelta(1,0,0) - (datetime.datetime.now() - userToUse.lastDailyTime))).split(".")[0].split(":")[0]+" hours and "+(str(datetime.timedelta(1,0,0) - (datetime.datetime.now() - userToUse.lastDailyTime))).split(".")[0].split(":")[1]+" minutes. You have "+str(userToUse.grapes)+" grapes."
            msg = msg.format(message)
            await client.send_message(message.channel, msg)
            updateUsers()
        elif splitContent[1] == "balance":
            userToUse = myUsers.myUsersList[myUsers.findUser(message.author.mention)]
            msg = "Okay, {0.author.mention} You have "+str(userToUse.grapes)+" grapes."
            msg = msg.format(message)
            await client.send_message(message.channel, msg)
        elif splitContent[1:5] == ["when","did","i","join"]:
            date = str(message.author.joined_at).split(" ")[0].split("-")+str(message.author.joined_at).split(" ")[1].split(":")[:-1]
            msg = "Okay, {0.author.mention} you joined "+date[1]+" "+date[2]+" "+date[0]+" at "+date[3]+":"+date[4]
            msg = msg.format(message)
            await client.send_message(message.channel, msg)
        elif splitContent[1] == "help":
            await client.send_message(message.author, helpMenu)
            msg = "Okay, {0.author.mention} I dm'd you the help menu. (Be Warned: It's pretty long).".format(message)
            await client.send_message(message.channel, msg)
                    
        elif splitContent[1:6] == ["rock","paper","scissors","lizard","spock"] or splitContent[1] == "rpsls" :
            msg = "Okay, {0.author.mention} let's play.\nWhat do you pick:"
            msg = msg.format(message)
            await client.send_message(message.channel, msg)
            reply = await client.wait_for_message(author = message.author)
            computerInput = random.choice(choices)
            try:
                outcome = rpslsContest(reply.content.lower(),computerInput)
                msg = outcomes[outcome[0]].format(message)+computerInput.capitalize()+".\nRemember, "+outcome[1][0].capitalize()+" "+outcome[1][1]+" "+outcome[1][2].capitalize()+"."
            except:
                if reply.content.lower() in choices:
                    msg = "Woah {0.author.mention}, looks like you drew, you both picked"+reply.content.lower().capitalize()+".\nYou must now input the cammand again if you want to replay."
                    msg = msg.format(message)                    
                else:
                    msg = "Sorry {0.author.mention}, thats not a valid input.\n*If you dont know the rules, do `gn! help`*\nYou must now input the cammand again if you want to replay."
                    msg = msg.format(message)
            await client.send_message(message.channel, msg)
            
        elif splitContent[1] == "dm":		
            if message.mention_everyone:
                for i in message.server.members:
                    try:
                        msg2Dm = message.content.split("(")[1].split(")")[0]
                        await client.send_message(i, message.author.mention+" sent:")
                        await client.send_message(i, msg2Dm)
                        msg = "Okay, {0.author.mention} I dm'd {0}.".format(i)
                        await client.send_message(message.channel, msg)
                    except:
                        print(i)
            else:
                msg2Dm = message.content.split("(")[1].split(")")[0]
                await client.send_message(message.mentions[0], message.author.mention+" sent:")
                await client.send_message(message.mentions[0], msg2Dm)
                msg = "Okay, {0.author.mention} I dm'd {0.mentions[0].mention}.".format(message)
                await client.send_message(message.channel, msg)
        else:
            msg = "Sorry, {0.author.mention} I don't understand. Do `gn! help` for all comands.".format(message)
            await client.send_message(message.channel, msg)
            

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

