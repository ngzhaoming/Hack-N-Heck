notificationMsg = """
You can use Hack 'N' Heck to send push notifications to groups in which he's in.

Telegram indentify each chat through their unique chat ID. Hence, Hack 'N' Heck would need the chat ID before it can send notifications to the group.

Hack 'N' Heck bot is able to identify the chat ID of each group he's in through /chatInformation command.

We are unable to provide users with the chat ID of private chats due to privacy issues.

To start sending notifications to groups please follow this instructions:
1) Get the chat ID of the group by using /chatInformation command in the group
2) Use /sendNotifications command to start up the process
3) Hack 'N' Heck bot will request for the chat ID of the respective groups. Note that multiple IDs can be inputted.
Example: Typing in "111111 12345 10101 99999" will send notifications to these 5 groups
4) After Hack 'N' Heck  bot received the chat IDs, type in the message that you wish to send.
"""

def chatInformation(message):
    if message.chat.type == "private":
        return "Your chat ID with Hack 'N' Heck bot is: " + str(message.chat.id)
    else:
        return  """
        Here are the chat details for {0}:

Group name: {1}
Group type: {2}
Chat  ID: (To be copied to send notifications)
        """.format(message.chat.title, message.chat.title, message.chat.type)

def sendNotification():
    return """
    Please input the group(s) chat ID that you wish to the the push notifications to. You can send the notification to multiple groups at once by adding a space between each chat ID.
    
Example: 11111 12345 10101 99999 will send notifications to these 5 groups
    """

def notificationNextStep():
    return "Chat ID has been registered please type in the message that you wish to send to the group."

def notificationError(a):
    return a + " is not a valid chat ID. Please check that you have typed in a correct chat ID."

def sendComplete():
    return "Message sent! Use /sendNotifications to send another message."