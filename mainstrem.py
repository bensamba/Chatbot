from customsearching import *
import sqlite3
import re
import random
responses ={
    
    "Hi":["Hey","Hello","Hello, how could i help you"],
    "Hii":["Hey","Hello","Hello, how could i help you"],
    "hi":["Hey","Hello","Hello, how could i help you"],
    "Hello":["Hey","Hello","Hello, how could i help you"],
    "hello":["Hey","Hello","Hello, how could i help you"],
    "Hey":["Hey","Hello","Hello, how could i help you"],
    "hey":["Hey","Hello","Hello, how could i help you"],
    "how are you":["i am fine","i am doing well"],
    "byy":["it was nice talking to you"],
    "admission procedure" :[" First you need to get yourself registered for the online entrance test of GLA University i.e. GLAET. Then you need to appear in the test at the APTECH Attest centers. Verify with the office the availability of the attest center in your city. Alternatively, the exam could be conducted in the office of GLA. You would be given your  result (qualified or not) soon after completing the exam.After qualifying the test one can deposit the fees at GLA University, Mathura or at city office in    form of DD/Cheque/Cash. The Demand draft can be issue from any nationalized bank in the favour of GLA University, Mathura payable at Vrindavan."],
   

    "default": [" try 'admission procedure'",
                "try 'about deepak mangal' ",
                "try 'about Prof. Anand Mohan Agrawal'",
                "try 'about Prof. Anup Kumar Gupta'",
                "try 'who are the developers of this bot'",
                "try 'about charul bhatnagar'",
                "try 'about jalal sir'"],
                
    "dehaii":[ "retry i can't understand ","i am here to solve your problems related to admission procedure ,show you the details of faculty,and basic qweries ",
               "i can tell you about admission procedure","i can tell you about faculties if you ask by their names "]
    }
patt_res={
    "jalal(.*)":["Prof. Anand Singh Jalal \n Professor & Head Institute of Engineering and Technology Department of Computer Engineering & Applications \n Contact Details:\nEmail: asjalal@gla.ac.in\nContact Number: 7351894030"],
    "anant(.*)":["Dr. Anant Ram \nAssociate Professor Institute of Engineering and Technology Department of Computer Engineering & Applications \nContact Details: \nEmail: anant.ram@gla.ac.in \nContact Number: 9456009465"],
    "anoop(.*)":["Prof. Anup Kumar Gupta \nDirector - IAH Institute of Applied Science & Humanities \nContact Details:\nEmail: anoop@gla.ac.in \nContact Number: 05662250900"],
    "pradeep(.*)":["Prof. Pradeep Mishra \nDirector & Professor Institute of Pharmaceutical Research \nContact Details:\nEmail: directoripr@gla.ac.in\nContact Number: 9927064019"],
    "charul(.*)":["Prof. Charul Bhatnagar \nDirector (IQAC) Institute of Engineering and Technology Department of Computer Engineering & Applications \nContact Details:\nEmail: directoriqac@gla.ac.in\nContact Number: 9997077388"],
    "divya(.*)":[" Prof. Divya Saksena \nProfessor Institute of Applied Science & Humanities \nContact Details: \nEmail: divya.saksena@gla.ac.in \nContact Number: 8851040307"],
    "deepak(.*)":["Mr. Deepak Mangal\n Asstt. Professor Institute of Engineering and Technology Department of Computer Engineering & Applications \nContact Details: Email: deepak.mangal@gla.ac.in \nContact Number: 9997549239"],
    "jitesh(.*)":["Mr. Jitesh Kumar Bhatia \nAsstt. Professor Institute of Engineering and Technology Department of Computer Engineering & Applications \nContact Details:Email: jitesh.bhatiya@gla.ac.in\nContact Number: 9997754517"],
    "admission(.*)" :["For taking admission in GLA University 5First you need to get yourself registered for the online entrance test of GLA University i.e. GLAET. Then you need to appear in the test at the APTECH Attest centers. Verify with the office the availability of the attest center in your city. Alternatively, the exam could be conducted in the office of GLA. You would be given your  result (qualified or not) soon after completing the exam.After qualifying the test one can deposit the fees at GLA University, Mathura or at city office in    form of DD/Cheque/Cash. The Demand draft can be issue from any nationalized bank in the favour of GLA University, Mathura payable at Vrindavan."],
    "admission procedure(.*)" :["First you need to get yourself registered for the online entrance test of GLA University i.e. GLAET. Then you need to appear in the test at the APTECH Attest centers. Verify with the office the availability of the attest center in your city. Alternatively, the exam could be conducted in the office of GLA. You would be given your  result (qualified or not) soon after completing the exam.After qualifying the test one can deposit the fees at GLA University, Mathura or at city office in    form of DD/Cheque/Cash. The Demand draft can be issue from any nationalized bank in the favour of GLA University, Mathura payable at Vrindavan."],
    "develop(.*)" :["the developers of this project are:  \nRomit Chand Verma\n Sachin Tandan\n Kshitij Bansal" ],
    "how are you(.*)":["its all good","i am doing well"],
    "hi(.*)":["Hey","Hello","Hello, how could i help you"],
    "hey(.*)":["Hey","Hello","Hello, how could i help you"],
    
    }
bot_template = "BOT : {0}"
user_template = "USER : "#"USER : {0}"
#def sql_responce(fname):
    

    
def match_rule(message):
    response, phrase = None, None
    
    # Iterate over the rules dictionary
    for pattern, responses in patt_res.items():
        # Create a match object
       
        match = re.search(pattern, message)
        if match is not None:
          
            # Choose a random response
            response = random.choice(responses)
            break
        else:
            
            responce = None
    # Return the response and phrase
    return response

f=0
def respond(message):
    # Check if the message is in the responses
    global f
    search = "search"
    resp = match_rule(message)
    r=message.find(search,0,6)
    if r==0:
        str1 = message.replace("search"," ")
        str1 = str1.strip()
        bot_message = glasearch(str1)
    
    #if resp=="121":
     #   bot_message = sql_responce_faculty(message)
    elif resp is not None:
        return resp    
    elif message in responses:
        f=0
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

while message != ("byy"):
    # Print user_template including the user_message
    print(user_template,end="")
    message=input()
    message=message.strip()
    send_message(message)
    
