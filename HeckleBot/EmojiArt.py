# -*- coding: utf-8 -*-

import random

gif  =  {
        "superSaiyan": "CgADBQADgwADlex4VXshgUo0iyicAg",
        "happyBirthday": "CgADBQADZQADqyp4VV2G9CWEuVr7Ag",
        "chineseNewYear": "BQADBQADuQADrz8oVZGmQsNp60BDFgQ",
}

EmojiArtDesc = '''
Most of these features does not work as intended on the phone. Do ensure that you are using Telegram web / app to view these:

/emojiArt - Abracadabra I create a masterpiece for you
/copyPasta - Custom made copy pasta for you
/superSaiyan - Cute super saiyan transformation
/happyBirthday - Kawaii way to wish a friend!
/chineseNewYear - 新年快乐, 恭喜发财! 🍊🍊
'''

chineseNewYearMsg = """
Instructions to view the Chinese New Year Emoji message:
1) If you are a Computer Scientist you should know how to compile Java files already (Go to step 8 instead)!
2) Go to an online Java compiler: https://www.jdoodle.com/online-java-compiler/
3) Open up the Java file using textEdit
4) Copy the whole message by using crtl + a and then crtl + c to copy the message
5) Remove the default code that is given in the Online Java Compiler IDE
6) Paste the code into the compiler by using crtl + v
7) Execute the code by pressing on the blue execute button
8) Once the code is compiled and executed, the Chinese New Year emoji message will be shown! 新年快乐, 恭喜发财! 🍊🍊
"""

copyPasta = '''
I am a dynamic figure, often seen scaling walls and crushing ice. I have been known to remodel train stations on my lunch breaks, making them more efficient in the area of heat retention. I translate ethnic slurs for Cuban refugees, I write award-winning operas, I manage time efficiently. Occasionally, I tread water for three days in a row.

I woo women with my sensuous and godlike trombone playing, I can pilot bicycles up severe inclines with unflagging speed, and I cook Thirty-Minute Brownies in twenty minutes. I am an expert in stucco, a veteran in love, and an outlaw in Peru.

Using only a hoe and a large glass of water, I once single-handedly defended a small village in the Amazon Basin from a horde of ferocious army ants. I play bluegrass cello, I was scouted by the Mets, I am the subject of numerous documentaries. When I’m bored, I build large suspension bridges in my yard. I enjoy urban hang gliding. On Wednesdays, after school, I repair electrical appliances free of charge.

I am an abstract artist, a concrete analyst, and a ruthless bookie. Critics worldwide swoon over my original line of corduroy evening wear. I don’t perspire. I am a private citizen, yet I receive fan mail. I have been caller number nine and have won the weekend passes. Last summer I toured New Jersey with a traveling centrifugal-force demonstration. I bat 400. My deft floral arrangements have earned me fame in international botany circles. Children trust me.

I can hurl tennis rackets at small moving objects with deadly accuracy. I once read Paradise Lost, Moby Dick, and David Copperfield in one day and still had time to refurbish an entire dining room that evening. I know the exact location of every food item in the supermarket. I have performed several covert operations for the CIA. I sleep once a week; when I do sleep, I sleep in a chair. While on vacation in Canada, I successfully negotiated with a group of terrorists who had seized a small bakery. The laws of physics do not apply to me.

I balance, I weave, I dodge, I frolic, and my bills are all paid. On weekends, to let off steam, I participate in full-contact origami. Years ago I discovered the meaning of life but forgot to write it down. I have made extraordinary four course meals using only a mouli and a toaster oven. I breed prizewinning clams. I have won bullfights in San Juan, cliff-diving competitions in Sri Lanka, and spelling bees at the Kremlin. I have played Hamlet, I have performed open-heart surgery, and I have spoken with Elvis.
'''

def giveArt():
    art = [
        """
        .
__________🎈_____^v^________________⋰☀⋰
☁️_________🎈________^v^
__________🎈________☁️☁️☁️____☁️☁️
________🎈______☁️☁️_______☁️
_______🎈________☁️________☁️☁️
________🎈____^v^____^v^
__________🎈________^v^__________^v^
_________💓💓
_________💓💓
___💗💗💗💗💗💗💗💗💗💗💗💗
__💗💗💗💗💗💗💗💗💗💗💗💗💗
_💗💗💗💗💗💗💗💗💗💗💗💗💗💗
💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗
.___💗_______________________________💗
.___💗__💗💗💗__💢💢__💢💢____💗
.___💗__💗💗💗__💢💢__💢💢____💗
.___💗__💗💗💗__💢💢__💢💢____💗
.___💗__💗💗💗____________________💗...🌹.🌹
.___💗__💗💗💗____________________💗_🌾_🌾
._🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹
._🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾
        """,
        """
.
📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱
📱📱📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱📱📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜📱📱📱📱⬜⬜⬜⬜⬜⬜⬜📱📱📱📱⬜⬜⬜📱
📱⬜⬜📱⬜⬜⬜📱📱⬜⬜⬜⬜⬜📱📱⬜⬜⬜📱⬜⬜📱
📱⬜📱⬜⬜⬜⬜⬜⬜📱⬜⬜⬜📱⬜⬜⬜⬜⬜⬜📱⬜📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜📱📱📱📱⬜⬜⬜⬜⬜⬜⬜📱📱📱📱⬜⬜⬜📱
📱⬜⬜📱📱📱📱📱📱📱⬜⬜⬜⬜📱📱📱📱📱📱📱⬜📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜⬜⬜⬜📱⬜⬜⬜📱⬜⬜📱⬜⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜⬜⬜⬜📱📱⬜⬜📱⬜⬜📱📱⬜⬜⬜⬜⬜⬜📱
📱⬜⬜⬜⬜⬜📱📱⬜⬜⬜📱⬜⬜⬜📱📱⬜⬜⬜⬜⬜📱
📱⬜⬜📱📱📱📱⬜⬜⬜📱📱📱⬜⬜⬜📱📱📱📱⬜⬜📱
📱⬜⬜⬜⬜⬜⬜⬜⬜⬜📱📱📱⬜⬜⬜⬜⬜⬜⬜⬜⬜📱
📱📱⬜📱⬜⬜⬜⬜⬜📱📱📱📱📱⬜⬜⬜⬜⬜📱⬜📱📱
📱📱⬜⬜📱📱⬜⬜📱📱📱📱📱📱📱⬜⬜📱📱⬜⬜📱📱
📱📱⬜⬜📱📱⬜⬜📱📱📱⬜📱📱📱⬜⬜📱📱⬜⬜📱📱
📱📱📱⬜⬜📱📱📱📱📱⬜⬜📱📱📱📱📱📱⬜⬜📱📱📱
📱📱⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜📱📱
📱📱📱⬜⬜⬜⬜⬜⬜⬜📱📱⬜⬜⬜⬜⬜⬜⬜⬜📱📱📱
📱📱📱📱⬜⬜⬜⬜⬜⬜⬜📱⬜⬜⬜⬜⬜⬜⬜📱📱📱📱
📱📱📱📱📱⬜⬜⬜⬜⬜📱📱📱⬜⬜⬜⬜⬜📱📱📱📱📱
📱📱📱📱📱⬜⬜⬜⬜⬜📱📱📱⬜⬜⬜⬜⬜📱📱📱📱📱
📱📱📱📱📱📱⬜⬜⬜⬜📱📱📱⬜⬜⬜⬜📱📱📱📱📱📱
📱📱📱📱📱📱📱⬜⬜⬜📱📱📱⬜⬜⬜📱📱📱📱📱📱📱
📱📱📱📱📱📱📱📱⬜⬜⬜📱⬜⬜⬜📱📱📱📱📱📱📱📱
📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱📱
        """,
        """
.
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜🐰🐰🐰🐰🐰⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜🐰🐰🐰🐰🐰⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜🐰🐰🐰🐰🐰⬜⬜⬜🐰🐰🐰🐰🐰⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜🐰🐰🐰🐰🐰⬜⬜🐰🐰🐰🐰🐰🐰🐰🐰⬜⬜⬜⬜
⬜⬜⬜⬜🐰🐰🐰🐰🐰⬜🐰🐰🐰🐰🐰🐰🐰🐰🐰⬜⬜⬜⬜
⬜⬜⬜⬜🐰🐰🐰🐰🐰⬜🐰🐰🐰🐰🐰🐰🐰🐰🐰⬜⬜⬜⬜
⬜⬜⬜⬜⬜🐰🐰🐰⬜⬜🐰🐰🐰🐰⬜⬜🐰🐰🐰⬜⬜⬜⬜
⬜⬜⬜⬜⬜🐰🐰🐰🐰🐰🐰🐰🐰🐰⬜⬜🐰🐰🐰⬜⬜⬜⬜
⬜⬜⬜⬜🐰🐰🐰🐰🐰🐰🐰🐰🐰⬜⬜⬜⬜🐰🐰⬜⬜⬜⬜
⬜⬜⬜🐰🐰🐰🐰🐰🐰🐰🐰🐰⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜🐰🐰🐰🐰🐰🐰🐰🐰🐰⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜🐰🐰🐰🐰🐰🐰🐰🐰🐰⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜🐰📺🐰🐰🐰📺🐰🐰🐰🐰⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜🐰🐰🐰🐰🐰🐰🐰🐰🐰🐰🐰🐰⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜🐰🐰🐰🐰🐰🐰🐰🐰🐰🐰🐰🐰⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜🐰🐰🐰🐰📺🐰🐰🐰🐰🐰🐰🐰⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜🐰🐰🐰📺🐰🐰🐰🐰🐰🐰⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜🐰🐰🐰🐰🐰🐰🐰🐰⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜🐰🐰🐰🐰🐰🏩🌃🏩🏩⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜🏩🌃🏩🏩🏩🏩🏩🌃🏩🏩🏩🏩⬜⬜⬜⬜⬜⬜⬜
⬜⬜🏩🏩🏩🌃🏩🏩🏩🏩🌃🌃🏩🏩🏩🏩🏩⬜⬜⬜⬜⬜⬜
⬜⬜🏩🏩🌃🌃🏩🏩🏩🌃🌃🌃🏩🏩🏩🏩🐰🐰⬜⬜⬜⬜⬜
⬜⬜🐰🏩🌃🌃🌃🌃🌃🌃🌃🌃🌃🏩🏩🐰🐰🐰🐰⬜⬜⬜⬜
⬜🐰🐰🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🐰🐰🐰🐰🐰⬜⬜⬜⬜
⬜🐰🐰🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃⬜🐰🐰🐰🐰⬜⬜⬜
⬜🐰🐰🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃⬜⬜🐰🐰🐰⬜⬜⬜
🐰🐰🐰🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃⬜⬜🐰🐰🐰⬜⬜⬜
🐰🐰🐰🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🎦🎦🐰🐰🐰🎦🎦🎦
🐰🐰🐰🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🎦🍓🐰🐰🐰🍎🍊🎦
🐰🐰🐰🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🎦🍊🍓🍊🍎🍊🍓🎦
⬜🐰🐰🐰🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🎦🍎🍊🍎🍓🍓🍊🎦
⬜⬜⬜🏨🏨🌃🌃🌃🌃🌃🌃🌃🏨🏨⬜🎦🎦🎦🎦🎦🎦🎦🎦
⬜⬜⬜⬜🏨🏨🏨🏨⬜🏨🏨🏨🏨⬜⬜🎦🎦🎦🎦🎦🎦🎦🎦
⬜🐰🐰🐰🐰🏨🏨🏨⬜🏨🏨🏨🐰🐰🐰🎦🎦🎦🎦🎦🎦🎦🎦
🐰🐰🐰🐰🐰🐰🐰🏨⬜🏨🐰🐰🐰🐰🐰🐰🎦🎦🎦🎦🎦🎦🎦
🐰🐰🐰🐰🐰🐰🐰🐰⬜🐰🐰🐰🐰🐰🐰🐰🐰🎦🎦🎦🎦🎦⬜
🐰🐰🐰🐰🐰🐰🐰🐰⬜🐰🐰🐰🐰🐰🐰🐰🐰🐰⬜⬜⬜⬜⬜
🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
        """,
        """
        .
___________________🌸🌸🌸🌸🌸🌸____🌸🌸🌸🌸
_________________🌸🌸§§§1111§🌸🌸§§§§§§🌸🌸
_________🌸🌸🌸🌸🌸🌸§§§11§§§§§§§§§§§§§§§🌸🌸
_______🌸🌸§§§§§§§§§111§§§🌸🌸🌸🌸§§§111§§§🌸🌸
_______🌸🌸§§§1🌸🌸§§11§🌸🌸§§§§🌸🌸§§§§§11§§🌸🌸
_______🌸🌸§§§§🌸🌸111🌸§§§11111🌸🌸§§1111§🌸🌸
_______🌸🌸§§§11§🌸🌸§§1🌸🌸§§§§§§11🌸🌸11111§🌸🌸
_________🌸🌸§111§§🌸🌸§§11🌸🌸§§§§§§🌸🌸1111 🌸🌸
___________🌸🌸1§§§🌸🌸§§11§§11🌸🌸🌸🌸111111🌸🌸
___________🌸🌸1§§§§1🌸🌸§§11111111111111§🌸🌸
___________🌸🌸§1111111🌸🌸§§§§§§§§§11🌸🌸§§11§🌸🌸
___________🌸🌸§§§§§§§11🌸🌸§§§§§§§🌸🌸§§§§111§§§🌸🌸
_____________🌸🌸§§§§§11🌸🌸§§§§🌸🌸§§1111§§§§§§§🌸🌸
_____________🌸🌸§§§§§§§🌱1🌸🌸1§§11§§§§§§§§§§§🌸🌸
_🍃___________🌸🌸🌸🌸__🌱§§§§11§§§§§§§§§§🌸🌸
__🍃🍃🍃____________🌱🌸🌸11§§§§§§§§§§§🌸🌸
__🍃 🍃 🍃 🍃________🌱__🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸
__🍃 🍃 🍃 🍃_______🌱
____🍃 🍃 🍃 🍃____🌱
______🍃🍃🍃 ___🌱_
________________🌱 _____🌱
________________🌱___🌱__________🍃
________________🌱_🌱______🍃🍃🍃
_________________🌱_🌱__🍃🍃🍃🍃
__________________🌱___🍃🍃🍃🍃🍃
___________________🌱_🍃🍃🍃🍃🍃
____________________🌱
_____________________🌱
__________🍃🍃🍃 ___🌱
________🍃 🍃 🍃 🍃___🌱
_____🍃 🍃 🍃 🍃_______🌱
___🍃 🍃 🍃 🍃_________🌱
_________________________🌱
__________________________🌱
__________________________🌱
        """,
        """
.
☁️☁️☁️☁️☁️☁️⚡☁️☁️💦☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️⚡☁️☁️☁️
📺📺📺📺📺📺📺📺📺📺📺📺📺📺📺📺📺📺☁️💦☁️☁️☁️☁️
💦☁️☁️☁️☁️☁️☁️☁️📺📺☁️☁️💦☁️☁️💦☁️💦☁️☁️💦☁️📺📺
☁️💦⚡☁️💦📺📺📺📺📺📺📺☁️☁️☁️☁️⚡☁️☁️💦☁️📺🌀📺
☁️☁️☁️📺📺📺💻💻💻📺📺💻📺☁️☁️💦☁️☁️💦☁️📺📺📺☁️
☁️☁️📺📺💻💻💻💻💻📺💻💻📺📺☁️☁️💦☁️☁️📺📺☁️💦☁️
☁️📺📺💻💻💻💻💻💻📺💻💻📺📺📺📺📺📺📺📺📺📺☁️☁️
☁️📺📺📺📺📺📺📺📺📺📺📺📺📺📺📺📺📺📺📺📺☁️☁️⚡
☁️📺📺📺📺📺📺📺📺📺📺📺📺📺📺📺☁️💦☁️☁️💦☁️☁️☁️
☁️☁️📺📺📺📺📺📺📺📺📺📺📺📺📺☁️💦☁️☁️☁️⚡☁️☁️☁️
☁️💦⚡☁️📺📺☁️💦☁️☁️📺📺💦☁️💦☁️☁️💦☁️💦☁️☁️💦☁️
☁️📺📺📺📺📺📺📺📺📺📺📺📺📺📺☁️☁️☁️☁️☁️💦☁️☁️☁️
☁️💦⚡☁️☁️☁️☁️💦☁️☁️☁️☁️☁️⚡☁️☁️💦☁️☁️💦☁️☁️☁️☁️
☁️☁️☁️☁️☁️☁️☁️💦☁️☁️💦☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️⚡☁️
        """
    ]
    return art[random.randint(0, 4)] 

def saiyanCaption():
        return "This is my final form!"
