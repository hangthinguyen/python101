# I have an input and I need to write a function to produce me the output

input = "I speak Goat Latin"
# the result I want: 
output = "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

def goat_latin(sentence):

    output = ""
    words = sentence.split()

    for i in range(0, len(words)):
        first = words[i][0]
        
        if first in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
            output += words[i] + "ma" + (i+1)*"a"

        else:
            output += " " + words[i].strip(words[i][0]) + words[i][0] + "ma" + (i+1)*"a"

    return output

poopoo = goat_latin(input)

print(poopoo == output)


