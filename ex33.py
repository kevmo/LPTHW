from sys import argv

goto = int(argv[1])


def func(lim):
    """Look at this func"""
    i = 0
    numbers = []

    while i < lim:
        print "At the top i is %d" % i
        numbers.append(i)
        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

func(goto)