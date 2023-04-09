import random

print("Bot: Hey, what do you want me to call you?")
user_name = input()

name = "Botty"
weather = "windy"
mood = "happy!"

bot_template = name + " : {0}"
user_template = user_name + " : {0}"

responses = { 
            "what's your name?": [ 
            "They call me {0}".format(name), 
            "I usually go by {0}".format(name), 
            "My name is the {0}".format(name) ],
            
            "what's today's weather?": [ 
            "The weather is {0}".format(weather), 
            "It's {0} today".format(weather), 
            "Let me check, it looks {0} today".format(weather) ],
            "Are you a robot?": [ 
            
            "What do you think?", 
            "Maybe yes, maybe no!", 
            "Yes, I am a robot with human feelings.", ],
            
            "how are you?": [ 
            "I am feeling {0}".format(mood), 
            "{0}! How about you?".format(mood), 
            "I am {0}! How about yourself?".format(mood), ],
            
            "": [ 
            "Hey! Are you there?", 
            "What do you mean by saying nothing?", 
            "Sometimes saying nothing tells a lot :)", ],
            
            "fine":[
            "It's great",
            "I happy of you."],
            
            "default": [
            "ha - ha - ha, it's default"]
            }

def respond(messege):
    if messege in responses:
        bot_messege = random.choice(responses[messege])
    
    else:
        bot_messege = random.choice(responses[messege]) 
    
    return bot_messege     

def related(x_text):
    
    if "name" in x_text:
        y_text =  "what's your name?"
    elif "waether" in x_text:
        y_text = "what's today's weather?"
    elif "robot" in x_text:
        y_text = "are you a robot?"
    elif "how are" in x_text:
        y_text = "how are you?"
    elif "fine" in x_text:
        y_text = "fine"    
    else:
        y_text = ""
    
    return y_text                

def send_messege(messege):
    print(user_template.format(messege))
    response = respond(messege)
    print(bot_template.format(response)) 

while True:
     
    my_input = input() 
    my_input = my_input.lower() 
    related_text = related(my_input) 
    send_messege(related_text)
    if my_input == "exit" or my_input == "stop" or my_input == "q": 
            break
                     