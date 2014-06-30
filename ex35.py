from sys import exit

def gold_room():
    print "Welcome to the gold room. How much do you take?"
    amt = raw_input("> ")

    if "0" in amt or "1" in amt:
        how_much = int(amt)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you ain't greedy, you only want %d" % how_much
        print "You win"
        exit(0)
    else:
        dead("Greedy loser")

def bear_room():
    print "Fuck, there is a bear in here!"
    print "It has a bunch of %s" % 'honey'
    print "The fat fucker is front of another door"
    print "How u gon move him? taunt, take, open"
    bear_moved = False

    while True:
        next = raw_input ("> ")

        if next == "take":
            dead ("bear fucks you up")
        elif next == "taunt" and not bear_moved:
            print "the bear moved!"
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("Bear chews your leg off")
        elif next == "open" and bear_moved:
            gold_room()
        else:
            print "Dunno what you want"

def cthulhu_room():
    print "The great evil Cthulhu is here.  flee or feast?"

    next = raw_input("> ")

    if flee in next:
        start()
    elif "feast":
        dead ("Tasty, goodbye")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You in a dark room"
    print "Doors to your right and left"
    print "Which do you take? R or L"

    door = raw_input("> ")

    if door == "L":
        bear_room()
    elif door == "R":
        cthulhu_room()
    else:
        dead("You stumble into a hole and die")

start()