from statistics import mean                     #imported statistic to calculate mean

print("Swallow Speed Analysis: Version 1.0\n")
KPH = []                                        #empty list for appending KPH 
MPH = []                                        #empty list for appending MPH
while True:
    a = input("Enter the next speed:")
    if a=="":                                   #If input is empty loop breaks
        break
    if a[0]=="U" or a[0]=="u":                  #checks the first element of string is "u" or "U"
        miles = float(a[1:])                    #first element is denied when converting into miles
        MPH.append(miles)
        miles *= 1.60934                        #converts given miles into km
        KPH.append(miles)                       #append output in empty KPH list
    elif a[0]=="E" or a[0]=="e":                #checks the first element of string is "e" or "E"
        km = float(a[1:])                       #first element is denied when converting into kilometer
        KPH.append(km)
        km *= 0.621371                          #converts given km into miles
        MPH.append(km)                          #append output in empty MPH list
    else: 
        print("Wrong Input!")
        break

if len(KPH)!=0:
    print("Result Summary\n")
    plural = "s" if len(KPH)>1 else ""                                                          #more than two reading is passed then "reading" changes into "readings"
    print(f"{len(KPH)} Reading{plural} Analysed.\n",)                                           #string formatting is used to plural the "reading"
    print("Max speed : {:.1f} MPH, {:.1f} KPH.".format(max(MPH),max(KPH)))                      #string formatting is used for displaying max speed and after decimal point only 1 number is displayed
    print("Min speed : {:.1f} MPH, {:.1f} KPH.".format(min(MPH),min(KPH)))                      #string formatting is used for displaying min speed and after decimal point only 1 number is displayed
    print("Avg speed : {:.1f} MPH, {:.1f} KPH.".format(mean(MPH),mean(KPH)))                    #string formatting is used for displaying average speed
else:
    print("No reading entered. Nothing to do.")                                                 #output if nothing is passed
    