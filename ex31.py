print "Door 1 or door 2?"
door = raw_input("Which door? ")

if door == "1":
    print "Giant bear eating cheesecake."
    print "1 = take the cake"
    print "2 = scream at the bear"

    bear = raw_input("1 or 2?")

    if bear == "1":
        print "The bear eats your face off"
    elif bear == "2":
        print "Bear eats your legs off"
    else:
        print "Well doing %s is probably better" % bear

elif door == "2":
    print "Stare into Chtuhilu's anus"
    print "pick another"
    print "1 = enter"
    print "2 = turn around"
    print "3 = anything else"

    insanity = raw_input("1,2 , or 3? ")

    if insanity == "1" or insanity == "2":
        print "Wtf is wrong with you"
    else:
        print "Good."

else:
    "You fall on a knife and die"