programing_dictionary = { "bug": "an error in program",
                     "function": "a piece of code that can be called over and over",
}
print(programing_dictionary["function"])

#to add something new
# programing_dictionary["loop"] = "the action of doing something over and over"

# emty_dictionary = {}
# wipe an exiting dictionary
# programing_dictionary = {}
# print(programing_dictionary)
# edit an item in dictionary
#programing_dictionary["bug"] = "a moth in your computer"
#print(programing_dictionary)
#loop through a dictionary
for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])