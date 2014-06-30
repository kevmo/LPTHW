def cheese_and_crackerss(cheese_count, boxes):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes
    print "Man, that's enough for a party"
    print "Get a blanket \n"

print "We can just give the function numbers directly:"
cheese_and_crackerss(20, 30)

print "OR we can use var from script"

cheese = 10
crackers = 50

cheese_and_crackerss(cheese, crackers)

print "We can even do math inside too:"
cheese_and_crackerss(10+30, 100+2000)

