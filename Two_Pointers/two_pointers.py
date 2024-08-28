# Given two integer arrays, return a new array sorted in none-decreasing order

# input1 -> 1234, input2-> 3345 , output -> 12333445

# keywords: two int arrays, sorted in, none-decreasing order

# pseudo code

# set an empty array storage the ints
# a loop append min ints into new array
# compare two array's num by same index, append the min one
# if one of the array finished first, break out from the loop, append the rest of the int in the other array


def merge_sorted_arrays(array1, array2):
    i = 0
    j = 0
    new_order_array = []
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            new_order_array += [array1[i]]
            i += 1
        else:
            # array1[i] >= array2[j]
            new_order_array += [array2[j]]
            j += 1
    if i == len(array1):
        new_order_array += array2[j:]
    else:
        new_order_array += array1[i:]

    return new_order_array


array1 = [1, 2, 2]
array2 = [2, 3, 3, 6, 7]
print(merge_sorted_arrays(array1, array2))
