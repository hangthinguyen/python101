
# input = nums = [1,2,3,1], output = True
# Write a function that will return true 
# if any value appears at least twice in the array, and return false if every element is distinct.

numbers1 = [1,2,3,1]
numbers2 = [1,2,3,4]
numbers3 = [1,1,1,3,3,4,3,2,4,2]

def appear_twice(nums):
    
    for i in range(0, len(nums)):

        for j in range(0, len(nums)):

            if i != j and nums[i] == nums[j]:
                return True
    
    return False
                     

print(appear_twice(numbers1))

print(appear_twice(numbers2))

print(appear_twice(numbers3))
