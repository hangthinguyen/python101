# def test():
#     print("Hello")

# test()

def capitalize_the_vowels(word):

    capitalized_word = ""

    for i in range(0, len(word)):
        print(word[i] == "a" or "e" or "i" or "o" or "u")

        if word[i] in ("a", "e", "i", "o", "u"):

           capitalized_word += word[i].upper()

        else:

            capitalized_word += word[i]

    return capitalized_word

word = capitalize_the_vowels("my baby la con heo")

print(word)
