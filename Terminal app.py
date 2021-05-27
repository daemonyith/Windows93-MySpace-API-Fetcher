import requests
import json


# List and dictionary used for storing All users and User info
outputunamelist = []
userinfolist = {}


# Pulls Json from MySpace API
def all_fwiends():
    fwiends = requests.get("https://myspace.windows93.net/api.php?")
    return json.loads(fwiends.content)


# Puts all usernames in a list
def allusernames():
    usernamelist = []
    fwiends = all_fwiends()['fwiends']
    for k, v in fwiends.items():
        if "name" in v:
            usernamelist.append(v['name'])
            outputunamelist.append(v['name'])
    return usernamelist


# prints all usernames to text file
def unametext():
    allusernames()
    with open("Usernames.txt", "w") as output:
        for item in outputunamelist:
            output.write(str(item) + "\n")


# Looks up and loads info from inputted userID
def getfwiendinfo(userid):
    f = requests.get("https://myspace.windows93.net/api.php?id=" + userid)
    fl = json.loads(f.content)
    for i, x in fl.items():
        userinfolist[i] = x


# Prints info of requested Fwiend
def printfwiendinfo(userid):
    f = requests.get("https://myspace.windows93.net/api.php?id=" + userid)
    fl = json.loads(f.content)
    for i, x in fl.items():
        userinfolist[i] = x
    for i, x in fl.items():
        print(i, ":", x)


# Saves Fwiend info into a text file and names it the userid
def savefwiendinfo(sfi):
    with open("%d.txt" % int(sfi), "w") as output:
        for k in userinfolist:
            output.write(str(k) + " : " + str(userinfolist[k]) + "\n")


# Command line menu
def mainmenu():
    print("MySpace API Wrapper")
    print("------Please select an option------")
    print("1. Print all Myspace Usernames" + "\n" +
          "2. Save all Myspace Usernames" + "\n" +
          "3. Print UserID info" + "\n" +
          "4. Save UserID info" + "\n" +
          "5. Exit" + "\n")
    menuselect()


# Menu selection code block
def menuselect():
    selectedinput = input("Please select: ")
    try:
        menuchoice = int(selectedinput)
    except ValueError:
        print("\n" + "Only numbers please" + "\n")
        mainmenu()
    if menuchoice == int(1):
        print("List of Usernames", "\n", *allusernames(), sep="\n")
        print("\n")
        mainmenu()
    elif menuchoice == int(2):
        unametext()
        print("Done" + "\n")
        mainmenu()
    elif menuchoice == int(3):
        inputid = input("ID of user: ")
        printfwiendinfo(inputid)
        print("\n")
        mainmenu()
    elif menuchoice == int(4):
        inputid = input("ID of user: ")
        getfwiendinfo(inputid)
        savefwiendinfo(inputid)
        print("Done" + "\n")
        mainmenu()
    elif menuchoice == int(5):
        quit()
    elif menuchoice > int(5):
        print("\n" + "Only 1 through 5" + "\n")
        mainmenu()
    elif menuchoice < int(0):
        print("\n" + "No negatives" + "\n")
        mainmenu()


mainmenu()
