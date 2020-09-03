# -*- coding: utf-8 -*-

import random

quizMsg = """
Let Hack 'N' Heck bot test your knowledge through these quizzes:

/fizzbuzzChallenge - Test your 3 and 5 multiplication skills!
/binaryTest - There are 10 kinds of people in this world. Those who knows binary and those who don't
/areaTest - Find the area of a selected shape
"""

fizzBuzzMsg = """
Welcome to the FizzBuzz challenge. The rules of this game is simple:
1) Each user starts with their own individual counter which starts from 0.
2) The goal is the increase the counter as high as possible using the command "Increase".
3) If the next counter number is divisible by 15, call "Fizzbuzz" instead
4) Else if the counter number is divisible by 3, call "Fizz" instead
5) Else if the counter number is divisible by 5, call "Buzz" instead
6) Please be patient while playing the game. Wait till Hack 'N' Heck bot reply to your command before selecing the next one to prevent any bugs.
7) Do note that stopping the game at Fizz / Buzz / Fizzbuzz will resume with this shown as the counter

Here are the commands to take note of when playing the game:

Increase - To increase your counter if it's not divisible by 3, 5, 15
Fizz - When the next number of your counter is divisible by 3
Buzz - When the next number of your counter is divisible by 5
Fizzbuzz - When the next number of your counter is divisible by 15

/startFizzBuzz - Setup / resume your counter to react to your commands
/stopFizzBuzz - Tired and need a break? Use this command to stop your counter and resume later
/fizzbuzzHighscore - See who has the highest counter score!
"""

binaryTestList = {} # Hashtable for binary quiz
fizzBuzzList = {} # Hashtable for fizzbuzz challenge
fizzDetails = {
    "fizzBuzzHighest": 0,
    "fizzBuzzName": "NIL"
}
areaTestList = {} # Hashtable for area quiz

def binaryTest(chat_id):
    val = random.randint(1, 100)
    binaryTestList[chat_id] = val
    return "What is the binary of " + str(val) + "?"

def binaryCheckAns(chat_id, guess):
    ans = "{0:b}".format(binaryTestList[chat_id])
    if ans == guess:
        del binaryTestList[chat_id]
        return True
    else:
        return False

def fizzBuzzStartChallenge(chat_id, name):
    if chat_id in fizzBuzzList:
        val = int(fizzBuzzList[chat_id])
        typed = ""
        if val % 15 == 0:
            typed = "Fizzbuzz"
        elif val % 3 == 0:
            typed = "Fizz"
        elif val % 5 == 0:
            typed = "Buzz"
        else:
            typed = fizzBuzzList[chat_id]
        return "Welcome back, " + name + ". Your current counter is at: " + typed
    else: 
        fizzBuzzList[chat_id] = "0"
        return "Welcome, " + name + " to the Fizzbuzz challenge. Your current counter is at: 0"


def fizzBuzzAction(chat_id, name, action):
    val = int(fizzBuzzList[chat_id]) + 1
    expected = ""
    if val % 15 == 0:
        expected = "Fizzbuzz"
    elif val % 3 == 0:
        expected = "Fizz"
    elif val % 5 == 0:
        expected = "Buzz"
    else: 
        expected = "Increase"

    if expected == action:
        fizzBuzzList[chat_id] = str(val)
        if expected == "Increase":
            return "Awesome! Your counter is now at: " + str(val)
        else: 
            return "Awesome! Your counter is now at: " + expected
    else:
        if (val - 1 > fizzDetails["fizzBuzzHighest"]):
            fizzDetails["fizzBuzzHighest"] = (val - 1)
            fizzDetails["fizzBuzzName"] = name
        del fizzBuzzList[chat_id]
        if (val == 200):
            return "Game Over. Password: g@nd@1F_<3_200"
        return "Game Over"

def fizzBuzzStop():
    return "Game paused. To resume playing, please enter the command /startFizzBuzz"

def fizzbuzzHighscore():
    return "Current champion is: " + fizzDetails["fizzBuzzName"] + ". With a counter score of: " + str(fizzDetails["fizzBuzzHighest"])

def areaTest(chat_id):
    return "What is the area of a point?"