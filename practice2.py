
def remove_every_other_letter(word):
    # I'd like to initialize a function that remove every other letter of the word

    result_word = ""
    # I create a variable and assign it to an empty string that will contain the result word

    for i in range(0, len(word)):
    # I use the for loop to iterate through each letter of the word, the initial position of the word is at 0, and the last letter is at the length of the word minus 1

        if i % 2 == 0:
            result_word += word[i]
        # to remove every other letter: I only add letters that are at even indices, and not adding letters at odd indices

    return result_word
    # I want to return the result that were added to result_word variable
    
phrase = remove_every_other_letter("Hello, sir")

print(phrase)