# I want to initalize a function that take a list as an input
# I want to assign the result to an empty list because the output has data structure of a list
# I want to iterate through each index of the list. For each indeex, I want to add the name at that index to the new list, plus an underscore, followed by square of 1 to 6 in order of the indices
# I want to return the result list

people = ["Hang", "Vinh", "Rumble", "Hoa", "Lan", "Chinh"]

def name_squares(names):

    names_with_squares = []

    for i in range(0, len(names)):

        names_with_squares.append(names[i] + "-" + str((i+1)**2))

    return names_with_squares

print(name_squares(people))