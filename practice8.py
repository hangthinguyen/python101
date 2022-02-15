# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

    # 1. Open brackets must be closed by the same type of brackets.
    # 2. Open brackets must be closed in the correct order.

s = "()"
s1 = "()[]{}"
s2 = "(]"
s3 = "(){]"
s4 = "{}[](){]"
s5 = "([)]"

def brackets(string):
    
    for i in range(0, len(string)):

        if string[i] == "(" and string[i + 1] != ")":
            return False

        elif string[i] == "[" and string[i + 1] != "]":
            print(string[i], string[i + 1])
            return False

        elif string[i] == "{" and string[i + 1] != "}":
            return False
    

    return True


print(brackets(s))
print(brackets(s1))
print(brackets(s2))
print(brackets(s3))
print(brackets(s4))
print(brackets(s5))

