# -*- coding: utf-8 -*-

import random

helpMsg = """
Here are the categories Hack 'N' Heck have:

/start - Allows Hack 'N' Heck to register you
/hello - Obnoxiously greets the user
/currentTime - Gives you the current time
/pushNotifications - Send messages to group(s)
/bestFitGame - To be played only in a group
/quizzes - Test your knowledge with these quizzes
/usefulResources - Everything nice in here 
/others - Miscellaneous features
/aboutMe - Get to know more about Hack 'N' Heck bot and his maker
/leaveFeedback - Send a message to the creator to tell him how you find Hack 'N' Heck bot
"""

aboutMsg = """
First and foremost, thank you for testing out Hack 'N' Heck bot. I really appreciate it! 

Hack 'N' Heck bot is currently deployed and fully functional. I hope to incorporate many different cool features into him so that he can be obnoxiously useful to you in your daily life. 

Do try out the features that he has now and hope you have fun while doing so! 😄
"""

bdayLink = """
Here is your link: https://www.youtube.com/watch?v=RaeLAwacDG4.

Do enjoy your day and have a blast! 😄😄😄
"""

feedbackMsg = """
Thank you for trying out Hack 'N' Heck bot! You can send any message that you want to the creator through this feature.

I will read all your messages and continue to improve Hack 'N' Heck bot!
"""

feedbackPrompt = "Please type your message after this text."

def greet(name):
    adj = ["addled", "cowardly", "inept", "silly", "vapid", 
    "wretched", "ridiculous", "pathetic", "obnoxious", "meddling",
    "egomaniacal", "jabbering", "tilted", "warped", "blithering"]
    noun = ["amateur", "chicken", "egg", "iguna", "moron",
    "oaf", "retchet", "turd", "vermin", "bafoon", "dunce", "goose",
    "noob", "parrot", "snake"]
    return "Hello, " + name + ". Try me, you " + adj[random.randint(0, 14)] + " " + noun[random.randint(0, 14)] + "!" + " 🧙‍♂️"

def feedbackSent():
    return "Thank you, your message has been sent to the developer. Have a nice day!"