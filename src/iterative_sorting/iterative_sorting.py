# TO-DO: Complete the selection_sort() function below
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7] # create new arrray, length of 10
"""
Notes:
1. INdex = 0 starting point
2. For loop all indices 'except' the last index
    a. Loop through values on right-hand-side of current index and find the smallest value
    b. Swap the values at current index with the smallest values found in above loop
Selection sort segments the list into two parts, 1)the left most is sorted 2)the right is unsorted
1. Search through list for smallest element
2. Once found, swap it with the first value, now sorted
3. Find smallest value of remainig items, swap with second value
i = # of values sorted, as i increases we check less items so j decreases
j = iterate over unsorted items, which are
i 0, check j 1-9 items
i 1, check j 2-9 items
"""
'''
Selection Sort:
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.
In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is
picked and moved to the sorted subarray.
'''
def selection_sort(arr): # function for selection_sort operation
    for i in range(0, len(arr)-1): # for loop through n-1 elements
        smallest_index = i # temp variable to store position of min value, assumes 1st value to be min of unsorted array
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            print(f'i: {i}, j:{j}')
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i] # swap
        print("""---
PASS COMPLETE
---""")
    return arr

print(selection_sort(arr1)) # print the function, use on the arr1 array
'''
# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    index_length =  range(0, len(arr) - 1)

    # loop through n-1 elements
    for i in index_length:
        cur_index = i

        for j in range( i + 1 , len(arr)):
            if arr[j] < arr[cur_index]:
                cur_index = j

        if cur_index != i:
            arr[cur_index], arr[i] = arr[i], arr[cur_index]

    return arr

print(selection_sort(arr1)) # print the function, use on the arr1 array
'''
# TO-DO:  implement the Bubble Sort function below
"""
Notes:
1. Loop through the array
    a. Compare each value to its neighbor
    b. If values in wrong position (relative to each other, swap them)
2. If no swaps performed, stop. Else, go back to the value at index 0 and repeat step 1.
"""
'''
Bubble Sort:
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements
if they are in wrong order.
'''
def bubble_sort(arr): # function for bubble_sort operation
    for i in range(0, len(arr)): # for loop over ever item in the array
        for j in range(0, len(arr) - 1): # for every item in array, compare it to it's neighbhor
            print(arr, arr[j], arr[j+1])
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j+1] = temp # swap
        print("""---
PASS COMPLETE
---""")
    return arr

print(bubble_sort(arr1)) # print the function, use on the arr1 array
'''
# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    index_length = len(arr) -1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, index_length):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

print(bubble_sort(arr1)) # print the function, use on the arr1 array
'''

# STRETCH: implement the Count Sort function below
'''
Counting sort is a sorting technique based on keys between a specific range. It works by counting the
number of objects having distinct key values (kind of hashing). Then doing some arithmetic to calculate
the position of each object in the output sequence.
'''
def count_sort(arr, maximum=-1):

    return arr
