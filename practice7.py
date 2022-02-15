#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
#typically using all the original letters exactly once.
#Input: s = "anagram", t = "nagaram", Output: true
#Input: s = "rat", t = "car", Output: false

s = "anagram"
t = "nagaram"

s1 = "rat"
t1 = "car"

s2 = "thuhang"
t2 = "hathgn"

def anagram(string1, string2):

    len1 = len(string1)
    len2 = len(string2)

    if len1 != len2:
        return False

    sorted1 = sorted(string1)
    sorted2 = sorted(string2)

    for i in range(0, len1):

        if sorted1[i] != sorted2[i]:

            return False         # we want to use difference and return False here so that when the funcion
                                    # encounter the first mismatch pair, it will return False immediately
                                    # if it goes through all letters and doesn't find a mismatch, it will return 
                                    # True at the end

    return True


print(anagram(s, t))
print(anagram(s1, t1))
print(anagram(s2, t2))



    
    




