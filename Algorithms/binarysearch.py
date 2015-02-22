"""
Binary Search is used to find a value in a sorted sequence by reducing the 
number of items to check by half with each iteration, until the value is 
found.
"""

#define our seach function which takes an array (list) and the target 
#to find
def binary(numlist, target):
    #keep track of where we are at in the list
    low = 0 
    high = len(numlist) - 1

    while low <= high:
        #set the middle and out attempt to find the target
        mid = (low + high) // 2
        attempt = numlist[mid]

        # if our attempt is the target return it
        if attempt == target:
            return mid
        # if our attempt is too high chop off the top half 
        if attempt > target:
            high = mid - 1
        # otherwise our attempt must be too low, so chop off the bottom
        # half 
        else:
            low = mid + 1
    return None
         
list_a = [2, 5, 6, 8, 10, 15, 17, 20, 22, 30, 31]

# some tests
print binary(list_a, 22)
print binary(list_a, 6)
print binary(list_a, 55)
   
