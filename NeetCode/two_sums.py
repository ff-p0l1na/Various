# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.

array_of_integers = [1, 45, 5, 533, 13, 0, 45, 7, 87]
int_target = 14

def makeSum(array, int_target):

# create a dict with the frequency of each integer:
    integer_count = {}
    for i in array:
        if i not in integer_count:
            integer_count[i] = 1
        else:
            integer_count[i] += 1

# create a dict where each key is index of each integer:
    integer_index = {}
    for j in range(len(array)):
        integer_index[j] = array[j]

    for num_1 in integer_count:
        num_2 = int_target - num_1
        if num_2 in integer_count:


            print(f"""The numbers that make {int_target} and their indices are: 
                {num_1} : xx \n
                {num_2} : xx""")
            
            return num_1, num_2
        else:
            continue

makeSum(array_of_integers, int_target)

        
            


