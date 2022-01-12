import random                                                                   #imported random for random respnses and name

rep = ["Hmm.", "Oh my.", "I'm listening.", "Go on.", "Okay"]

def chat_system(email):
    '''checks whether passed email is valid or not'''
    if "@" in email:
        s = email.split("@")                                                    #splits the passed email on "@"
        if len(s) >2 or s[-1] != "pop.ac.uk" or len(s[0])<2:                    #checks the entered email address
            return False
        else:
            return True

def responses(replies):
    '''asked question replies are passed from here'''
    replies = replies.lower()                                                   #lowers the passed string
    if "wifi" in replies or "internet" in replies:                              #checks the specific word written
        print("Wifi is excellent across campus.")
    
    elif "coffee" in replies or "food" in replies or "restaurant" in replies:   #checks the specific word written
        print("Teekee is open until 9pm this evening.")
    
    elif "library" in replies or "book" in replies:                             #checks the specific word written
        print("Library is close today.")
        
    elif "class" in replies or "room" in replies:                               #checks the specific word written
        print("Go through college website for allocating classes.")
        
    elif "deadline" in replies:                                                 #checks the specific word written
        print("Your deadline has been extended by two working days.")
        
    elif "goodbye" in replies or "thankyou" in replies or "exit" in replies:    #checks the specific word written
        return 0 
        
    elif "help" in replies or "information" in replies:                         #checks the specific word written
        print("Call 012345 for help.")
        
    else: 
        print(f"{random.choice(rep)}")                                          #random replies for any other words except given above

def convo():
    '''This function calls and run other function'''
    print("Welcome to Pop Chat\nOne of our operators will be pleased to help you today.")
    name = ["Janice", "Diana", "Kristine", "Shasa", "Bella", "Beyonce", "Adele", "Shakira"]
    email = input("\nPlease enter your Poppleton email address: ")
    
    if chat_system(email) == True: 
        s = email[0:-10]                                                                        #gives the name from email
        print(f"\nHello {s.capitalize()}! Thank you, and Welcome to PopChat!")                  #string formatting is used and name of user is capitalized 
        print(f"My name is {random.choice(name)}, and it will be my pleasure to help you.")     #string formatting is used for displaying random names of operator
        while True:
            replies = input("\n---> ")
            if responses(replies) == 0:                                                         #code exits after response return 0
                print(f"\nThanks, {s.capitalize()}, for using PopChat. See you again soon!")
                break
            if random.randint(0,10)>8:                                                          #code randomly stops after 8 responses 
                print(f"\nThanks, {s.capitalize()}, for using PopChat. See you again soon!")
                print("***Network Error***")
                break
                
    else:
        print("Invalid Poppleton email address.")
        
convo()