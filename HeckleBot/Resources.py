from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

doc = {
    "timeComplexity": "AgADBQAD46gxG22BeVUI3ahlqoY2-0l8-TIABPPlTlmEUiGspAcBAAEC",
    "CAP5": "BQADBQADlQADbYF5VU7GLjJbyoXzAg",
    "internship": "BQADBQADiQADlex4VfN4MPFzdocFAg",
    "fowBooklet": "BQADBQADlAADbYF5VZCi8Z5DeAUhAg",
    "modTimeflow": "AgADBQAD56gxG22BeVVGnHKxV7Cwd8m4-TIABBZoDP-qrpt8ZGoAAgI",
    "modCalendar": "BQADBQADiAAD5ed4VS8DskOdgS1VAg",
    "modRegGuide": "BQADBQADmQADbYF5VWnF9rK_La6TAg",
    "snake": "CgADBQADhwAD6Ht4VYlFfLAkGYd4Ag",
    "stackSticker": "CAADAgADGAAD4FP5C0gLHKTxveR4Ag",
    "rebokGuide": "BQADBQADXgADaB3BVeQorS166U3HAg",
    "rebokFAQ": "BQADBQADXwADaB3BVRU_OIg8wMQzAg",
}

resourcesMsg = """
Resources categorized for your every need:
/niftyStudyTricks - Tips and Tricks to help you!
/miscellaneousResources - Other resources that might be useful
"""

niftyMsg = """
Hack 'N' Heck one stop guide to study tips and tricks!
/timeComplexity - Time-complexity for various data structures
/vimHacks - Time to dabble into some Vim Magic
/secretToCAP5 - Never let anyone lay hands on this good stuff
/internshipApplication - Get your application forms to the best organizations
"""

miscMsg = """
Other resources that you might find interesting:
/nusLinks - Links that might come in handy
/moduleRegGuide - Awesome guide for module registration
/rebokMember - Guide to setting up your rebok account
/nusCard - 🚨NEW🚨 Use a virtual card to scan in your gym usage in NUS!
/fowBooklet - Get to know these extraordinary people in Computing!
"""

vimMsg = """
Follow these steps to get your very own VIM hack: 
1) Type in vim ~/.vimrc
2) Add in all these: 
  syntax enable
  set tabstop=4
  set shiftwidth=4
  set softtabstop=4
  set expandtab
  set number
  set autoindent
  set smartindent
  ia sop System.out.println
  ia psvm public static void main (String [] args) {<CR><CR>}<Up>
3) Type :wq
4) EZ CLAP
"""

nusCardMsg = """
Follow these steps to get your very own virtual NUS card:
1) Download the NUS card application
Android: https://play.google.com/store/apps/details?id=sg.edu.nus.nuscard&hl=en_SG
iOS: https://apps.apple.com/sg/app/nus-card/id1464854971
2) Upon your first login, sign up to your NUS account
3) You will be redirected to the homepage where you can generate a QR code for your Matriculation card for scanning
"""


def timeComplexity():
    return "Here are the time-complexity of the common data structure used. EZ CLAP!"


def internDetails():
    return "Apply to this organization today!"


def modReg(n):
    if n == 0:
        return "This is the time-flow of each module registration milestone"
    if n == 1:
        return "This is the calendar which shows all the module registration milestone"
    if n == 2:
        return "Follow this guide if you are unsure of the module registration process"


def linkKeyboard():
    linkKeyboard = InlineKeyboardMarkup()
    linkKeyboard.row_width = 2
    linkKeyboard.add(InlineKeyboardButton(
        "NUSmods", url="https://nusmods.com/timetable/sem-1"))
    linkKeyboard.add(InlineKeyboardButton(
        "EduRec", url="https://myedurec.nus.edu.sg/psp/cs90prd/?cmd=login"))
    linkKeyboard.add(InlineKeyboardButton(
        "LumiNUS", url="https://luminus.nus.edu.sg/?r=%2Fdashboard"))
    linkKeyboard.add(InlineKeyboardButton(
        "Skylab NUS", url="https://nusskylab-dev.comp.nus.edu.sg/"))
    linkKeyboard.add(InlineKeyboardButton(
        "Kattis", url="https://open.kattis.com"))
    linkKeyboard.add(InlineKeyboardButton(
        "Stack Overflow", url="https://stackoverflow.com/"))
    return linkKeyboard


def nusLinks():
    return "Try out these links that might come in useful in the future!"

def rebok(n):
    if n == 0:
        return "Follow this step by step guide to set up your Rebok account!"
    if n == 1:
        return "Got any questions? Try looking at those commonly asked question"
    if n == 2:
        return "🚨NEW🚨 Get your virtual NUS card to register in NUS gym today! Use the command /nusCard for more information"
