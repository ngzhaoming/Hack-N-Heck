import Randomizer
import EmojiArt

doc = {
    "chineseNewYearVideo": "BAADBQADuwADBzJhVPEfnltTrx4UFgQ",
}

chineseNewYearVideoMsg = """
    新年快乐, 恭喜发财! 🍊🍊 Here is a well-known Chinese New Year song, 贺新年 sang by the one and only rubber chicken! 🐔Enjoy!
"""

othersMsg = """
Miscellaneous features that Hack 'N' Heck bot can do for your entertainment:

/randomizer - Try out all things random
/emojiLibrary - Beautiful wall of text
/chineseNewYearVideo - 贺新年 sang by the one and only rubber chicken! 🐔
/captureTheFlag - You require my assistant? 🧙
/chatInformation - Get details on the current chat
"""

#=========================================================================================================

#Randomizer library

def randomizerDesc():
    return Randomizer.randomizerMsg

def rollDice():
    return Randomizer.rollDice()

def drawCard():
    return Randomizer.drawCard()

def YayOrNay():
    return Randomizer.YayOrNay()

def getNumber():
    return Randomizer.getNumber()

def luckyColour():
    return Randomizer.luckyColour()

def stories():
    return Randomizer.horrorStory()

#=========================================================================================================

#Emoji library

def emojiDesc():
    return EmojiArt.EmojiArtDesc

def giveArt():
    return EmojiArt.giveArt()

def copyPasta():
    return EmojiArt.copyPasta    