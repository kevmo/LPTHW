# New stuff:
#  - lists have a pop method.
#       0-indexed at the start.
#       -1-indexed from the end.
#  - strings have a split method
#  - sorted() built-in method

def break_words(stuff):
    """this function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sort the words"""
    return sorted(words)

def print_first_words(words):
    """Prints the first word after
       popping it off"""
    word = words.pop(0)
    print word

def print_last_word(words):
    """prints last word after popping it off"""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence, returns sorted words"""
    return sort_words(break_words(sentence))

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence"""
    broken = break_words(sentence)
    print_first_words(broken)
    print_last_word(broken)

def print_first_and_last_sorted(sentence):
    newp = sort_sentence(sentence)
    print_first_words(newp)
    print_last_word(newp)