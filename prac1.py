print("Stop! Who would cross the Bridge of Death\nMust answer me these questions three, 'ere the other side he see.\t")
name = input("What is your name ?")
if name.lower()!="arthur":
    seek = input("What do you seek ?")
    
    if "grail" in seek.lower():
        color = input("What is your favourite colour ?")
        
        if color.lower()[0]==name.lower()[0]:
            print("You may enter.")
            
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")
            
    else:
        print("Only those who seek the Grail may pass.")
        
else:
    print("My liege! You may pass!")
    