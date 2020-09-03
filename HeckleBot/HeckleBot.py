# -*- coding: utf-8 -*-

#This will be the main python file to be run
import os
import telebot

#Importing self-made python files
import Greetings
import Notifications
import Quiz
import Vote
import Resources
import Capture
import Others

from datetime import datetime, timedelta
from telebot import types
from flask import Flask, request

knownUsers = []  # todo: save these in a file
userStep = {} # Current command: 7
notificationID = {}

fizzSelect = types.ReplyKeyboardMarkup()
fizzSelect.add("Increase", "Fizz", "Buzz", "Fizzbuzz")
hideBoard = types.ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard

TOKEN = '789464724:AAEmGvrkh4CobozZ0VUaCzAFGgYYp1Cj3Ho'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

#=========================================================================================================

#Register user into bot data base

def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("New user detected, who hasn't used \"/start\" yet")
        return 0

@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    cfn = m.chat.first_name
    cln = m.chat.last_name
    cun = m.chat.username
    if cid not in knownUsers:  # if user hasn't used the "/start" command yet:
        knownUsers.append(cid)  # save user id, allow brodcast of messages to all users later
        userStep[cid] = 0  # save user id and his current "command level"
        bot.send_message(cid, "Hello, stranger, let me scan you...")
        bot.send_message(cid, "Scanning complete, I know you now. 🎉🎉🎉")
        bot.send_message("394614415", str(cfn) + " " + str(cln) + 
        " has just used the bot. With username: " + str(cun) + ", and chat_id: " + str(cid))
        greet(m)
    else:
        bot.send_message(cid, "I already know you mortal! Now try me! 🤙")
        help(m)

#=========================================================================================================

#About the bot and author section
@bot.message_handler(commands=['greet', 'hello'])
def greet(message):
    bot.send_message(message.chat.id, Greetings.greet(message.from_user.first_name))
    help(message)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, Greetings.helpMsg)

@bot.message_handler(commands=['aboutMe'])
def aboutMe(message):
    bot.send_message(message.chat.id, Greetings.aboutMsg)

@bot.message_handler(commands=['bdayLink'])
def aboutMe(message):
    cid = message.chat.id
    cfn = message.chat.first_name
    cln = message.chat.last_name
    bot.send_message("394614415", str(cfn) + " " + str(cln) + 
        " has successfully completed the challenge. Chat id is: " + str(cid))
    bot.send_message(message.chat.id, Greetings.bdayLink)

@bot.message_handler(commands=['leaveFeedback'])
def leaveFeedback(message):
    bot.send_message(message.chat.id, Greetings.feedbackMsg)
    bot.send_message(message.chat.id, Greetings.feedbackPrompt)
    userStep[message.chat.id] = 5

@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 5,
content_types=['text'])
def creatorMessage(message):
    bot.send_message("394614415", message.text)
    bot.send_message(message.chat.id, Greetings.feedbackSent())
    userStep[message.chat.id] = 0

#=========================================================================================================

#Time / Dynamic features
@bot.message_handler(commands=['currentTime'])
def giveTime(message):
    currTime = datetime.now() + timedelta(hours=8)
    current_time = '{:%H:%M:%S}'.format(currTime)
    bot.send_message(message.chat.id, 'Current Time: ' + current_time)

#=========================================================================================================
    
#Notification features

@bot.message_handler(commands=['chatInformation'])
def chatInformation(message):
    cid = message.chat.id
    bot.send_message(cid, Notifications.chatInformation(message))
    if message.chat.type != "private":
        bot.send_message(cid, message.chat.id)

@bot.message_handler(commands=['pushNotifications'])
def sendNotifications(message):
    bot.send_message(message.chat.id, Notifications.notificationMsg)

@bot.message_handler(commands=['sendNotifications'])
def sendNotifications(message):
    cid = message.chat.id
    bot.send_message(cid, Notifications.sendNotification())
    userStep[cid] = 4

@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 4,
regexp="([-]?[0-9]+[ ]?)+")
def chatIDNotification(message):
    cid = message.chat.id
    notificationID[cid] = message.text.split(" ")
    bot.send_message(cid, Notifications.notificationNextStep())
    userStep[cid] = 4.5
    
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 4.5,
content_types=['text'])
def massSending(message):
    cid = message.chat.id
    array = notificationID.get(cid)
    for a in array:
        try:
            bot.send_message(a, message.text)
        except:
            bot.send_message(cid, Notifications.notificationError(a))
    bot.send_message(cid, Notifications.sendComplete())
    del notificationID[cid]
    userStep[cid] = 0

#=========================================================================================================

#Capture the flag features

@bot.message_handler(commands=['captureTheFlag'])
def captureDesc(message):
    bot.send_message(message.chat.id, Capture.captureMsg)

@bot.message_handler(commands=['ctfSideQuest'])
def sideQuest(message):
    bot.send_document(message.chat.id, Capture.doc["sideQuest"],
    caption=Capture.sideQuestDetails())

@bot.message_handler(commands=['sideQuestKey'])
def captureDesc(message):
    bot.reply_to(message, Capture.answerKey(message.chat.id))
    userStep[message.chat.id] = 7

@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 7)
def checkFactorial(message):
    cid = message.chat.id
    bot.send_chat_action(cid, 'typing')
    verdict = Capture.checkFactorial(cid, message.text)
    if verdict:
        bot.reply_to(message, "Your answer is correct. Awesome Possum! ⭐️ Here's a tip to you, put this to good use r _ i _ _")
        userStep[message.chat.id] = 0
    else:
        bot.reply_to(message, "Incorrect answer. Please try again!")

#=========================================================================================================

#Quiz features
@bot.message_handler(commands=['quizzes'])
def quizDesc(message):
    bot.send_message(message.chat.id, Quiz.quizMsg)

#Binary Quiz Feature
@bot.message_handler(commands=['binaryTest'])
def binaryTest(message):
    bot.reply_to(message, Quiz.binaryTest(message.chat.id))
    userStep[message.chat.id] = 1

@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1, regexp="[0-1]+")
def checkBinaryAnswer(message):
    cid = message.chat.id
    bot.send_chat_action(cid, 'typing')
    verdict = Quiz.binaryCheckAns(cid, message.text)
    if verdict:
        bot.reply_to(message, "Your answer is correct. Awesome Possum! ⭐️")
        userStep[message.chat.id] = 0
    else:
        bot.reply_to(message, "Incorrect answer. Please try again!")

#FizzBuzz Challenge Feature
@bot.message_handler(commands=['fizzbuzzChallenge'])
def fizzbuzzDesc(message):
        bot.send_message(message.chat.id, Quiz.fizzBuzzMsg)

@bot.message_handler(commands=['startFizzBuzz'])
def fizzBuzzStart(message):
    if message.chat.type != "private":
        bot.send_message(message.chat.id, "This feature is only available in private chat.")
    else:
        cid = message.chat.id
        bot.send_message(cid, 
        Quiz.fizzBuzzStartChallenge(cid, message.chat.first_name), reply_markup=fizzSelect)
        userStep[cid] = 2

@bot.message_handler(commands=['fizzbuzzHighscore'])
def fizzbuzzHighscore(message):
    bot.send_message(message.chat.id, Quiz.fizzbuzzHighscore())

@bot.message_handler(commands=['stopFizzBuzz'])
def fizzBuzzStop(message):
    cid = message.chat.id
    if message.chat.type != "private":
        bot.send_message(message.chat.id, "This feature is only available in private chat.")
    else:
        if userStep[cid] != 2:
            bot.send_message(cid, "You have yet to start the game yet... 👾")
        else:
            bot.send_message(cid, Quiz.fizzBuzzStop(), reply_markup=hideBoard)
            userStep[cid] = 0

@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 2, 
regexp="^(Increase)|(Fizz)|(Buzz)|(Fizzbuzz)$")
def fizzBuzzAction(message):
    cid = message.chat.id
    verdict = Quiz.fizzBuzzAction(cid, message.chat.first_name, message.text)
    if verdict == "Game Over":
        bot.send_message(cid, verdict, reply_markup=hideBoard)
        userStep[cid] = 0
    elif verdict == "Game Over. Password: g@nd@1F_<3_200":
        bot.send_message(cid, verdict, reply_markup=hideBoard)
        userStep[cid] = 0
    else:
        bot.send_message(cid, verdict)

#Area Quiz Feature
@bot.message_handler(commands=['areaTest'])
def areaTest(message):
    bot.reply_to(message, Quiz.areaTest(message.chat.id))
    userStep[message.chat.id] = 3

#=========================================================================================================

#Vote features

@bot.message_handler(commands=['bestFitGame'])
def bestFitGame(m):
    cid = m.chat.id
    if m.chat.type != "private":
        joinMsg = bot.send_message(cid, Vote.bestFitMsg(cid), reply_markup=Vote.voteJoin())
        save = bot.send_message(cid, Vote.trackNumPlayers(cid))
        Vote.startMessages(cid, joinMsg.message_id, save.message_id)

@bot.callback_query_handler(func=lambda call: Vote.get_grp_step(call.message.chat.id) == 1)
def callback_query(call):
    cid = call.message.chat.id
    uid = call.from_user.id
    if get_user_step(uid) == 6.1:
        bot.send_message(uid, "You are already in the game.")
    elif call.data == "bestFitGame":
        userStep[uid] = 6
        bot.send_message(uid, Vote.genderQuestion(cid, uid), reply_markup=Vote.genderKeyboard())

@bot.callback_query_handler(func=lambda call: get_user_step(call.message.chat.id) == 6)
def setGender(call):
    cid = call.from_user.id
    gid = Vote.groupLink[cid]
    if call.data == "Male":
        Vote.setMaleParticipant(cid, call.from_user.first_name)
    elif call.data == "Female":
        Vote.setFemaleParticipant(cid, call.from_user.first_name)
    userStep[cid] = 6.1
    bot.edit_message_text(chat_id=gid, message_id=Vote.groupNames[gid]["Participants"],
        text=Vote.trackNumPlayers(gid))

@bot.message_handler(func=lambda message: Vote.get_grp_step(message.chat.id) == 1, 
commands=['startBestFitGame'])
def startBestFitGame(m):
    cid = m.chat.id
    bot.delete_message(cid, Vote.groupNames[cid]["BestJoin"])
    bot.delete_message(cid, Vote.groupNames[cid]["Participants"])
    promptID = bot.send_message(cid, Vote.startPrompt(cid))
    Vote.storePromptID(cid, promptID.message_id)

@bot.message_handler(func=lambda message: Vote.get_grp_step(message.chat.id) == 1.1, 
commands=['questionBestFit'])
def questionBestFit(m):
    cid = m.chat.id
    uid = m.from_user.id
    userStep[uid] = 6.2
    bot.delete_message(cid, Vote.groupNames[cid]["promptID"])
    bot.send_message(uid, Vote.constrainQuestion(cid, uid), reply_markup=Vote.constrainsKeyboard())

# This callback chooses the restriction for the current question
@bot.callback_query_handler(func=lambda call: get_user_step(call.message.chat.id) == 6.2)
def setRestriction(call):
    uid = call.from_user.id
    gid = Vote.groupLink[uid]
    Vote.createKeyboard(gid, call.data)
    if call.data == "Opposite Gender":
        for users in Vote.groupNames[gid]["Male"]:
            userid = Vote.groupNames[gid]["Male"][users]["userID"]
            userStep[userid] = 6.3
            Vote.groupLink[uid] = gid
            bot.send_message(userid, Vote.votingMessage(), reply_markup=Vote.groupNames[gid]["Keyboard1"])
        for users in Vote.groupNames[gid]["Female"]:
            userid = Vote.groupNames[gid]["Female"][users]["userID"]
            userStep[userid] = 6.3
            Vote.groupLink[uid] = gid
            bot.send_message(userid, Vote.votingMessage(), reply_markup=Vote.groupNames[gid]["Keyboard"])
    else:
        for users in Vote.groupNames[gid]["Names"]:
            userid = Vote.groupNames[gid]["Names"][users]["userID"]
            userStep[userid] = 6.3
            Vote.groupLink[uid] = gid
            bot.send_message(userid, Vote.votingMessage(), reply_markup=Vote.groupNames[gid]["Keyboard"])

    trackMsg = bot.send_message(gid, Vote.trackVotes(gid))
    Vote.trackMsgId(gid, trackMsg.message_id)

@bot.callback_query_handler(func=lambda call: get_user_step(call.message.chat.id) == 6.3)
def collateResult(call):
    uid = call.from_user.id
    ufn = call.from_user.first_name
    gid = Vote.groupLink[uid]
    userStep[uid] = 6.4
    bot.edit_message_text(chat_id=gid, message_id=Vote.groupNames[gid]["trackMsg"],
        text=Vote.collateResult(uid, ufn, gid, call.data))
    if len(Vote.groupNames[gid]["Voted"]) == Vote.groupNames[gid]["NumParticipants"]:
        bot.delete_message(gid, Vote.groupNames[gid]["trackMsg"])
        bot.send_message(gid, Vote.showResult(gid))
        promptID = bot.send_message(gid, Vote.startPrompt(gid))
        Vote.storePromptID(gid, promptID.message_id)

#=========================================================================================================

# Resources feature

@bot.message_handler(commands=["usefulResources"])
def resourcesMsg(m):
    bot.send_message(m.chat.id, Resources.resourcesMsg)

@bot.message_handler(commands=["niftyStudyTricks"])
def niftyMsg(m):
    bot.send_message(m.chat.id, Resources.niftyMsg)

@bot.message_handler(commands=["miscellaneousResources"])
def miscMsg(m):
    bot.send_message(m.chat.id, Resources.miscMsg)

@bot.message_handler(commands=["timeComplexity"])
def timeComplexity(m):
    bot.send_photo(m.chat.id, Resources.doc["timeComplexity"]
    , caption=Resources.timeComplexity())

@bot.message_handler(commands=["vimHacks"])
def vimHacks(m):
    bot.send_message(m.chat.id, Resources.vimMsg)

@bot.message_handler(commands=["secretToCAP5"])
def secret(m):
    bot.send_document(m.chat.id, Resources.doc["CAP5"])
    bot.send_document(m.chat.id, Resources.doc["snake"])

@bot.message_handler(commands=["internshipApplication"])
def internshipApplication(m):
    bot.send_document(m.chat.id, Resources.doc["internship"],
    caption=Resources.internDetails())

# Miscellaneous section
@bot.message_handler(commands=["nusLinks"])
def nusLinks(m):
    bot.send_message(m.chat.id, Resources.nusLinks(), 
    reply_markup=Resources.linkKeyboard())
    bot.send_sticker(m.chat.id, Resources.doc["stackSticker"])

@bot.message_handler(commands=['moduleRegGuide'])
def moduleRegGuide(m):
    bot.send_photo(m.chat.id, Resources.doc["modTimeflow"],
    caption=Resources.modReg(0))
    bot.send_document(m.chat.id, Resources.doc["modCalendar"],
    caption=Resources.modReg(1))
    bot.send_document(m.chat.id, Resources.doc["modRegGuide"],
    caption=Resources.modReg(2))

@bot.message_handler(commands=['rebokMember'])
def rebokMembership(m):
    bot.send_document(m.chat.id, Resources.doc["rebokGuide"],
    caption=Resources.rebok(0))
    bot.send_document(m.chat.id, Resources.doc["rebokFAQ"],
    caption=Resources.rebok(1))
    bot.send_message(m.chat.id, Resources.rebok(2))

@bot.message_handler(commands=['nusCard'])
def nusCard(m):
    bot.send_message(m.chat.id, Resources.nusCardMsg)

@bot.message_handler(commands=['fowBooklet'])
def fowBooklet(m):
    bot.send_document(m.chat.id, Resources.doc["fowBooklet"])

#=========================================================================================================

#Others library commands

#Randomizer section
@bot.message_handler(commands=['others'])
def othersLib(message):
    bot.send_message(message.chat.id, Others.othersMsg)

@bot.message_handler(commands=['randomizer'])
def randomizerLib(message):
    bot.send_message(message.chat.id, Others.randomizerDesc())

@bot.message_handler(commands=['rollDice'])
def rollDice(message):
    bot.send_message(message.chat.id, Others.rollDice())

@bot.message_handler(commands=['drawCard'])
def drawCard(message):
    bot.send_message(message.chat.id, Others.drawCard())

@bot.message_handler(commands=['YayOrNay'])
def YayOrNay(message):
    bot.send_message(message.chat.id, Others.YayOrNay())

@bot.message_handler(commands=['4Dnumber'])
def getDigits(message):
    bot.send_message(message.chat.id, Others.getNumber())

@bot.message_handler(commands=['luckyColour'])
def getColour(message):
    bot.send_message(message.chat.id, Others.luckyColour())

@bot.message_handler(commands=['twoSentenceHorrorStory'])
def stories(message):
    bot.send_message(message.chat.id, Others.stories())

@bot.message_handler(commands=['chineseNewYearVideo'])
def chineseNewYearVideo(message):
    bot.send_video(message.chat.id, Others.doc["chineseNewYearVideo"],
    caption=Others.chineseNewYearVideoMsg)

#Emoji section (To create an emoji quiz with inline keyboard to decide which topic to choose from)
@bot.message_handler(commands=['emojiLibrary'])
def emojiArt(message):
    bot.send_message(message.chat.id, Others.emojiDesc())

@bot.message_handler(commands=['emojiArt'])
def emojiArt(message):
    bot.send_message(message.chat.id, Others.giveArt())

@bot.message_handler(commands=['copyPasta'])
def copyPasta(message):
    bot.send_message(message.chat.id, Others.copyPasta())

@bot.message_handler(commands=["superSaiyan"])
def superSaiyan(m):
    bot.send_document(m.chat.id, Others.EmojiArt.gif["superSaiyan"],
    caption=Others.EmojiArt.saiyanCaption())

@bot.message_handler(commands=["happyBirthday"])
def happyBirthday(m):
    bot.send_document(m.chat.id, Others.EmojiArt.gif["happyBirthday"])

@bot.message_handler(commands=["chineseNewYear"])
def chineseNewYear(m):
    bot.send_document(m.chat.id, Others.EmojiArt.gif["chineseNewYear"],
    caption=Others.EmojiArt.chineseNewYearMsg)

#=========================================================================================================

#Handling for each content_types

@bot.message_handler(func=lambda message: True, 
content_types=['audio', 'document', 'photo', 'sticker', 
'video', 'video_note', 'voice', 'location', 'contact'])
def command_default(m):
    if m.chat.type == "private":
        bot.send_message(m.chat.id, "Uploaded file is a " + m.content_type)
        bot.send_message(m.chat.id, getattr(m, m.content_type))

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(m):
    if m.chat.type == "private":
        bot.send_message(m.chat.id, 
        "What kind of sorcery is this \"" + m.text + "\" 🤔\nMaybe try the help page at /help")

#=========================================================================================================

#These are the webhook route code (DO NOT TOUCH!)

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://zhaomingbot.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))