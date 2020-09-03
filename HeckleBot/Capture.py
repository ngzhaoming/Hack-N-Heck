doc = {
    "sideQuest" : "BQACAgUAAxkBAAIUc15t-8qC7hc0e6_oMLVfbHISS3UBAALnAAMkHXFXli2_QSwX68UYBA",
}

captureMsg = """
Capture the flag game from Github: https://github.com/ngzhaoming/Capture-the-Flag-Wargame

/ctfSideQuest - Congratualations on finding me now here are the clues to my house lock
"""

def sideQuestDetails():
    return "Here is the txt file containing the clue to my house lock!"

def answerKey(chat_id):
    return "Greetings traveller, so what is the password to my house lock?"

def checkFactorial(cid, message):
    if message == "7853981633974483082":
        return True
    else:
        return False
