from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

groupNames = {}
groupLink = {} #Link participants to their group

def get_grp_step(cid): # Gives the step in which the group is in now
    if cid in groupNames:
        return groupNames[cid]["Step"]
    else:
        return 0

def voteJoin():
    joinKeyboard = InlineKeyboardMarkup()
    joinKeyboard.row_width = 1
    joinKeyboard.add(InlineKeyboardButton("Join Best Fit Game", callback_data="bestFitGame"))
    return joinKeyboard

def genderKeyboard():
    genderKeyboard = InlineKeyboardMarkup()
    genderKeyboard.row_width = 2
    genderKeyboard.add(InlineKeyboardButton("Male", callback_data="Male"))
    genderKeyboard.add(InlineKeyboardButton("Female", callback_data="Female"))
    return genderKeyboard

def constrainsKeyboard():
    constrainsKeyboard = InlineKeyboardMarkup()
    constrainsKeyboard.row_width = 2
    constrainsKeyboard.add(InlineKeyboardButton("No Restrictions", callback_data="No Restrictions"))
    constrainsKeyboard.add(InlineKeyboardButton("Opposite Gender", callback_data="Opposite Gender"))
    constrainsKeyboard.add(InlineKeyboardButton("Males Only", callback_data="Males Only"))
    constrainsKeyboard.add(InlineKeyboardButton("Females Only", callback_data="Females Only"))
    return constrainsKeyboard


def bestFitMsg(cid):
    groupNames[cid] = {} # Each group ID will have differnt details
    groupNames[cid]["Step"] = 1 # To show that the game has started
    groupNames[cid]["Names"] = {}
    groupNames[cid]["Male"] = {}
    groupNames[cid]["Female"] = {}
    groupNames[cid]["NumParticipants"] = 0 # Counter for how many people playing
    return """Welcome to the Best Fit Game. Please press the button to join the game. 
Then prompt /startBestFitGame once everyone has joined and ready to start the game."""

def startMessages(cid, join, save):
    groupNames[cid]["BestJoin"] = join # Join inline message
    groupNames[cid]["Participants"] = save # Participant list message

def trackNumPlayers(cid):
    result = "Current number of players: " + str(groupNames[cid]["NumParticipants"]) + "\n"
    for name in groupNames[cid]["Male"]:
        result += name + "\n"
    for name in groupNames[cid]["Female"]:
        result += name + "\n"
    return result

def qualityCheck(uid, cid): # To check whether participant press Join again
    if uid in groupLink:
        return False
    else:
        groupLink[uid] = cid
        return True

def genderQuestion(cid, uid):
    groupLink[uid] = cid
    return "This is a warm up question. Choose the gender that best fits you."

def setMaleParticipant(uid, ufn):
    gid = groupLink[uid]
    groupNames[gid]["NumParticipants"] += 1
    groupNames[gid]["Male"][ufn] = {}
    groupNames[gid]["Names"][ufn] = {}
    groupNames[gid]["Names"][ufn]["userID"] = uid
    groupNames[gid]["Names"][ufn]["votes"] = []
    groupNames[gid]["Male"][ufn]["userID"] = uid

def setFemaleParticipant(uid, ufn):
    gid = groupLink[uid]
    groupNames[gid]["NumParticipants"] += 1
    groupNames[gid]["Female"][ufn] = {}
    groupNames[gid]["Names"][ufn] = {}
    groupNames[gid]["Names"][ufn]["userID"] = uid
    groupNames[gid]["Names"][ufn]["votes"] = []
    groupNames[gid]["Female"][ufn]["userID"] = uid

def startPrompt(cid):
    groupNames[cid]["Step"] = 1.1
    return "For the person asking the question, use /questionBestFit to set the settings for the question."

def storePromptID(cid, mid):
    groupNames[cid]["promptID"] = mid

def constrainQuestion(cid, uid):
    groupLink[uid] = cid
    groupNames[cid]["Step"] = 1.2
    return "Please select the restriction for your question."

# Need to create a different keyboard for the different restriction
def createKeyboard(gid, restriction):
    pollKeyboard = InlineKeyboardMarkup()
    pollKeyboard.row_width = 2
    if restriction == "No Restrictions":
        for users in groupNames[gid]["Names"]:
            pollKeyboard.add(InlineKeyboardButton(users, callback_data=users)) 
    elif restriction == "Opposite Gender":
        pollKeyboard1 = InlineKeyboardMarkup()
        pollKeyboard1.row_width = 2
        for users in groupNames[gid]["Male"]:
            pollKeyboard.add(InlineKeyboardButton(users, callback_data=users))
        for users in groupNames[gid]["Female"]:
            pollKeyboard1.add(InlineKeyboardButton(users,callback_data=users))
        groupNames[gid]["Keyboard1"] = pollKeyboard1
    elif restriction == "Males Only":
        for users in groupNames[gid]["Male"]:
            pollKeyboard.add(InlineKeyboardButton(users, callback_data=users))
    else:
        for users in groupNames[gid]["Female"]:
            pollKeyboard.add(InlineKeyboardButton(users, callback_data=users))
    groupNames[gid]["Keyboard"] = pollKeyboard

def trackVotes(gid):
    groupNames[gid]["Voted"] = [] #Keep track of who has voted already
    return "The voting has started! Number of people who voted: 0"

def trackMsgId(gid, msgID):
    groupNames[gid]["trackMsg"] = msgID

def votingMessage():
    return "Please vote for the person that best fit the question asked:"

def collateResult(uid, ufn, gid, vote):
    groupNames[gid]["Voted"].append(ufn)
    groupNames[gid]["Names"][vote]["votes"].append(ufn)
    result = "Current number of voters: " + str(len(groupNames[gid]["Voted"])) + "\n"
    for names in groupNames[gid]["Voted"]:
        result += names + "\n"
    return result

def showResult(gid):
    result = "Everyone has voted. Here are the results: \n"
    for names in groupNames[gid]["Names"]:
        result += names + " (" + str(len(groupNames[gid]["Names"][names]["votes"])) + " vote(s)): \n"
        for votes in groupNames[gid]["Names"][names]["votes"]:
            result += votes + "\n"
        result += "\n"
        groupNames[gid]["Names"][names]["votes"] = []
    return result