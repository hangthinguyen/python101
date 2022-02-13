
people_info = [
    {
        "f_name": "Hang", 
        "l_name": "Nguyen", 
        "age": 30, 
        "gender": "F"
    },
    {
        "f_name": "Vinh", 
        "l_name": "Vu", 
        "age": 29, 
        "gender": "M"
    },
    {
        "f_name": "Rumble", 
        "l_name": "Vu", 
        "age": 49, 
        "gender": "D"
    }
]

def people_introduction(people):

    # I want to look at each person in the list of people

    result = []

    for person in people:

        result.append("Hello, my name is " 
            + person["f_name"] + " " + person["l_name"] 
            + ". I am a " + person["gender"] 
            + ". I am age " + str(person["age"]) + ".")

    return result
    

introduction = people_introduction(people_info)

print(introduction)


            