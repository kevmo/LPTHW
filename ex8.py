formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ('uno', 2, 'tres', 4)
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("I had this thing",
"where",
"fuck",
"is up"
)