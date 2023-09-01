import random as r
print(" __  __   __  ___")
print("|   |__| |   |___")
print("|__ |  \ |__  ___| Robotics Team")
print("___________________________________________________")
print("\nRobot Autonomous Task Data Converter")
print("\n\nWhat this does:")
print("This program converts the raw output from")
print("the RobotC Debug Stream into RobotC code")
print("that is used for the autonomous task.")
print("\n\nHow to use:")
print("Run main.c in RobotC while connected to")
print("the robot. Make sure the debug stream is")
print("opened and clear. Hit the autonomous task")
print("record button. Record the autonomous task")
print("and do NOT hit the record button again.")
print("Stop the robot code but do NOT close out")
print("of the debug dialog. Use CTRL+A to")
print("highlight all of the output and")
print("CTRL+C to copy the data. Paste")
print("the info where it says \"Input recording string: \"")
print("below. The program will then output the code")
print("to output.txt if successful. Paste this code")
print("between the autonomous task code comments at")
print("the beginning of main.c, and download the update")
print("to the robot. (This may require direct USB connection")
print("to the computer if the update continuously fails.\n")
print("___________________________________________________\n\n")

rawData = input("Input recording string: ")
try:
    #Split string into lsit
    dataList = rawData.split(", ")
    del dataList[0]
    events = []
    timing = []
    status = []
    cycle = 0
    # Cycles through list in sets of three
    # 1st goes to event
    # 2nd goes to timing
    # 3rd goes to status
    # Go back to 1
    for i in dataList:
        if cycle == 3:
            cycle = 0
        if cycle == 0:
            events.append(i)
        if cycle == 1:
            timing.append(int(i))
        if cycle == 2:
            if i == "true":
                i = 1
            elif i == "false":
                i = 0
            status.append(int(i))
        cycle += 1
except Exception as i:
    print("Something went wrong...")
    print("An exception occured while splitting the code. (Tell Atticus error A-" + str(r.randint(100000,999999)) + ")\n")
    print("Error details:")
    print(i)
    print(i.args)
    print("\n")
    input("Press ENTER to close")
    quit()
if len(events) == 0:
    print("Something went wrong...")
    print("The code output has a length of 0. (Tell Atticus error B-" + str(r.randint(100000,999999)) + ")\n")
    print("Error details:")
    print("len(events) == 0")
    print("\n")
    input("Press ENTER to close")
    quit()
if not len(events) == len(timing):
    print("Something went wrong...")
    print("The event timing length does not match the event length. (Tell Atticus error C-" + str(r.randint(100000,999999)) + ")\n")
    print("Error details:")
    print("Timing", len(timing), "Events", len(events))
    print("\n")
    input("Press ENTER to close")
    quit()
if not len(events) == len(status):
    print("Something went wrong...")
    print("The event status length does not match the event length. (Tell Atticus error D-" + str(r.randint(100000,999999)) + ")\n")
    print("Error details:")
    print("Status", len(status), "Events", len(events))
    print("\n")
    input("Press ENTER to close")
    quit()
# Code Generation
theCode = "int autoTaskLength = " + str(len(events)) + ";\n"
theCode += "string eventsList[" + str(len(events))
theCode = "// Automatically Generated Autonomous Task Code\n" + theCode
theCode += "] = "
events = str(events)
events = events.replace("[", "{")
events = events.replace("]", "}")
events = events.replace("'", '')
theCode += events + ";\n"
theCode += "int timingList[" + str(len(timing)) + "] = "
timing = str(timing)
timing = timing.replace("[", "{")
timing = timing.replace("]", "}")
theCode += timing + ";\n"
theCode += "int statusList[" + str(len(status)) + "] = "
status = str(status)
status = status.replace("[", "{")
status = status.replace("]", "}")
theCode += status + ";\n"
theCode += "// End Automatic Code"
print("\n\nThe following code will be inserted\n\n")
print(theCode)
a = open("output.txt", "w")
a.write(theCode)
a.close()
print("\n\n")
input("Success! The code has been output to output.txt.")

# Old Code
"""file = open("main backup.c", "r")
fileList = file.read().split("\n")
placeHere = False
started = False
newList = fileList
a = 0
for i in fileList:
    if i == "// Automatically Generated Autonomous Task Code":
        print("Found header.")
        started = True
        placeHere = True
    if placeHere:
        del newList[a]
    if "// End Automatic Code" in i:
        newList.insert(a, theCode)
        print("Found footer.")
        placeHere = False
    
        
    a+= 1
    pass
file.close()
print(newList)
if started == False:
    input("Could not find automatic code header comment!")
elif placeHere:
    input("Could not find automatic code footer comment!")
else:
    longString = ""
    for i in newList:
        longString += i + "\n"
    print(longString)
    a = open("main backup.c", "w")
    a.write(longString)
    a.close()
    input("Pass")"""
