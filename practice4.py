# I have an input nums = [2,7,11,15] and target = 9
# Write a function that will return the indices of the 2 numbers that add up to the target number
# There is only 1 solution for each input
# Output = [0, 1]

nums = [2, 7, 11, 15]
target1 = 9

def finding_indices_of_two_numbers(a_list, target):

    for i in range(0, len(a_list)):

        for j in range(0, len(a_list)):

            if a_list[i] + a_list[j] == target and i != j:

                return [i, j]


            
print(finding_indices_of_two_numbers(nums, target1))