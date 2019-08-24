# -*- coding: utf-8 -*-

import random

randomizerMsg = """
Feeling lucky? Come try these randomly generated answers from the wizard: 

/rollDice - Roll a virtual six-sided dice
/drawCard - Draw a random poker card
/4Dnumber - Get your lucky number!
/YayOrNay - To be or not to be. That is the question.
/luckyColour - Good fortune awaits you with this lucky colour!
/twoSentenceHorrorStory - Time to get spooooooooky
"""

def rollDice():
    return "You rolled a: " + random.randint(1, 6).__str__()

def drawCard():
    rank = ["2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟", "🎃", "👸", "🤴", "🅰️"]
    suit = ["♦️", "♣️", "♥️", "♠️"]
    val = random.randint(1, 53)
    if (val == 33):
        return "🃏"
    else: 
        return "You have drawn: " + rank[random.randint(0, 12)] + suit[random.randint(0, 3)]

def YayOrNay():
    val = random.randint(0,1)
    if (val == 1):
        return "Nay"
    else:
        return "Yay"

def getNumber():
    return "Your lucky number is: " + random.randint(0,9999).__str__().zfill(4)

def luckyColour():
    colours = ["red", "orange", "mauve", "green", "azure", "beryl",
    "jade", "celadon", "black", "white", "celeste", "saffron", "pink", 
    "fuschia", "turquoise", "scarlett", "cyan", "vermillion", "pewter"]
    return "Your lucky colour is: " + colours[random.randint(0, 18)]

def horrorStory():
    stories = ["I woke up to hear knocking on glass. At first, I thought it was the window until i heard it come from the mirror again.",
    "I begin tucking him into bed and he tells me, \"Daddy check for monsters under my bed.\" I look underneath for his amusement and see him, another him, under the bed, staring back at me quivering and whispering, \"Daddy there’s somebody on my bed.\"",
    "They delivered the mannequins in bubble wrap. From the main room I begin to hear popping.",
    "Day 321. Internet still not working.", "The officer finally got back to me. The call was coming from inside the house.",
    "After a hard day's work, I came home to see my wife cradling our child. I didn't know which was more frightening, seeing my dead wife and stillborn child, or knowing that someone broke into my aprartment to place them there.",
    "The upstairs neighbours are awfully noisy. I told my landlord, and was informed that it's been vacant for months.",
    "As I played in the basement, Mother called me upstairs. From behind me, she whispered, 'Don't go up there.'",
    "I arrived at the funeral a few minutes late. Nobody acknowledge me, and I figured out why when I looked into the casket and saw myself.",
    "I wondered why I was casting two shadows. After all there is only a single lightbulb in the room."
    ]    
    return stories[random.randint(0, 9)]