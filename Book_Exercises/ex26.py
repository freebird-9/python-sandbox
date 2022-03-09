def break_words(stuff):
    print("This function will break up words for us.")
    words = stuff.split()
    return words

def sort_words(words):
    print("Sorts the words.")
    return sorted(words)

def print_first_word(words):
    print("Prints the first word after popping it off.")
    word = words.pop(0)
    return word
    print(word)

# def print_last_word(words):
#     print("Prints the last word after popping it off.")
#     word = words.pop()
#     print(word)

# def sort_sentence(sentence):
#     print("Takes in a full sentence and returns the sorted words.")
#     words = sentence.split()
#     sorted_words= words.sort()
#     return sorted_words
#     print(sorted_words)

# def print_first_and_last(sentence):
#     print("Prints the first and last words of the sentence.")
#     first_word = sentence.split().pop(0)
#     last_word = sentence.split().pop(-1)
#     print("printing_first_word %d" % first_word)
#     print("printing_last_word %d "  % last_word)

# def print_first_and_last_sorted(sentence):
#     print("Sorts the words then prints the first and last one.")
#     words = sentence.sort()
#     first_sorted_word = sentence.split().pop(0)
#     last_sorted_word = sentence.split().pop(-1)
#     print("printing_first_sorted_word %d" % first_sorted_word)
#     print("printing_last_sorted_word %d "  % last_sorted_word)

# print("Let's practice everything.")
# print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

# poem = """
# \tThe lovely world
# with logic so firmly planted
# cannot discern \n the needs of love
# nor comprehend passion from intuition
# and requires an explantion
# \n\t\twhere there is none.
# """


# print("--------------")
# print(poem)
# print("--------------")

# five = 10 - 2 + 3 - 5
# print("This should be five: %s" % five)

# def secret_formula(started):
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars / 100
#     return jelly_beans, jars, crates


# start_point = 10000
# jelly_beans, jars, crates = secret_formula(start_point)

# print("With a starting point of: %d" % start_point)
# print("We'd have %d jelly_beans, %d jars, and %d crates." % (jelly_beans, jars, crates))

# start_point = start_point / 10

# print("We can also do that this way:")
# print("We'd have %d jelly_beans, %d jars, and %d crates." % secret_formula(start_point))


sentence = "All good\tthings come to those who wait."
stuff = "Today beautiful is day a."

# words = ex25.break_words(sentence)
# sorted_words = ex25.sort_words(words)

# print("print_first_word %d" % first_word)
# print_last_word(words)
# .print_first_word(sorted_words)
# print_last_word(sorted_words)
# sorted_words = ex25.sort_sentence(sentence)
# prin sorted_words

# print_irst_and_last(sentence)

#   print_first_a_last_sorted(senence)
