'''
Iterative:
A program is called recursive when an entity calls itself. A program is call iterative when there is a loop (or repetition).
'''
# Write a linear search approach
'''
Linear Search:
A simple approach is to do linear search, i.e
Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
    1. If x matches with an element, return the index.
    2. If x doesn’t match with any of elements, return -1.
'''
def linear_search(arr, target): # function to implement linear search
    for i in range(len(arr)): # for the i value in the range of the length of the array
        if arr[i] == target: # if the arr index value for i is equal to the target
            return i # return the value
    return -1   # return not found

# Write an iterative implementation of Binary Search
'''
# Binary Search:
This search algorithm takes advantage of a collection of elements that is already sorted by ignoring
half of the elements after just one comparison.
    1. Compare x with the middle element.
    2. If x matches with the middle element, we return the mid index.
    3. Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray
    after the mid element. Then we apply the algorithm again for the right half.
    4. Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for
    the left half.
'''
def binary_search(arr, target): # function to implement binary search
    start = 0 # set the star to 0
    stop = len(arr) - 1 # set the stop to the length of the arr minus 1

    while start <= stop: # while the start value is less than the stop value
        midpoint = start + (stop - start)//2 # set the midpoint to start value and (stop value minus start value) divided by 2
        midpoint_val = arr[midpoint] # set the midpoint to the arr midpoint
        if midpoint_val == target: # if the midpoint_val is equal to the target
            return midpoint # return the midpoint value
        elif target <midpoint_val: # else if the target is less than the midpoint_val
            stop = midpoint - 1 # set stop to the midpoint minus 1
        else: # else
            start = midpoint + 1 # set the start value to the midpoint plus 1

    return -1  # not found
