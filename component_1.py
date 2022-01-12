print("Stop! Who would cross the Bridge of Death\nMust answer me these questions three, 'ere the other side he see.\t")
def bridge_keeper():
    '''function to check the answers of bridge passer'''
    name = input("What is your name ?")
    if "arthur" not in name.lower():                #lowers the passed string and checks the name of passer if arthur in name he can pass without any furthur question
        seek = input("What do you seek ?")
        
        if "grail" in seek.lower():                 #lowers the passed string and checks if grail is in the answer or not
            color = input("What is your favourite colour ?")
        
            if color.lower()[0]==name.lower()[0]:   #lowers the passed string and checks first letter of color and name, if same they can pass
                print("You may enter.")
            
            else:
                print("Incorrect! You must now face the Gorge of Eternal Peril.")
            
        else:
            print("Only those who seek the Grail may pass.")
        
    else:
        print("My liege! You may pass!")
    return

bridge_keeper()