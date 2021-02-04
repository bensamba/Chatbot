import re
import random
responses ={
    "about (.*)": "121",
    "Hi":["Hey","Hello","Hello, how could i help you"],
    "Hii":["Hey","Hello","Hello, how could i help you"],
    "hi":["Hey","Hello","Hello, how could i help you"],
    "hii":["Hey","Hello","Hello, how could i help you"],
    "Hello":["Hey","Hello","Hello, how could i help you"],
    "hello":["Hey","Hello","Hello, how could i help you"],
    "Hey":["Hey","Hello","Hello, how could i help you"],
    "hey":["Hey","Hello","Hello, how could i help you"],

    "default": [" try 'admission procedure'",
                "try 'about deepak mangal' "],
                
    "dehaii":[ "retry i can't understand ","i am here to solve your problems related to admission procedure ,show you the details of faculty,and basic qweries about placements and other ",
               "i can tell you about admission procedure","i can tell you about faculties if you ask"]
    }
bot_template = "BOT : {0}"
user_template = "USER : "#"USER : {0}"
def sql_responce():
    #responce by kshitij after searching in sql data base
    return "about the faculty"
f=0
def respond(message):
    # Check if the message is in the responses
    global f
    if message in responses:
        f=0
        if responses[message]=="121":
            bot_message = sql_responce(meshisage)
        else:
        # Return the matching message
            bot_message = random.choice(responses[message])
    else:
        # Return the "default" message
        if f<=4:
            bot_message = random.choice(responses["dehaii"])
            f=f+1
        else:
            bot_message = random.choice(responses["default"])
        
    return bot_message

def send_message(message):
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))


message =""

while message != "byy":
    # Print user_template including the user_message
    print(user_template,end="")
    message=input()
    send_message(message)
    
