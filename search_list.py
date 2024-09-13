# RECURSIVE SEARCH ALGORITHM FOR NUMBER IN A list
#
# 1. Create empty list (indices_list) to save indices at which number is
#    present, if found
# 2. Initialize current index, i = 0
# 3. If i < length of list, compare user number with element of list at index i
# 4. If the two numbers are equal in step 3, append index i to indices_list;
#    if they are not equal, do nothing
# 5. While i < length of list, add 1 to i (i + 1) and repeat steps 3 and 4 with
#    new index i
# 6. When i becomes equal to length of list, stop the check
# 7. If the "indices_list" list is empty, the number was not found in the list
# 8. The the "indices_list" list is not empty, the elements present in the list
#    are the indices at which the number was found


test_list = [1, 2, 3, 6, 6, 4, 5, 3, 1, 4, 4, 3, 2, 0, 3]


num_to_find = input("Enter the integer you wish to find: ")

find_index = [i for i, k in enumerate(test_list) if k == int(num_to_find)]

if len(find_index) == 0:
    print("The number was not found in the list")
else:
    print(f"The number was found at indices {find_index} of the list")
