# Implementation of binary search algorithm!

# We will prove that binary search is faster than the naive search!

def naive_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

# binary search uses divide and conquer!
# we will leverage the fact that our list is SORTED


def binary_search(array, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(array)-1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if array[midpoint] == target:
        return midpoint
    elif target < array[midpoint]:
        return binary_search(array, target, low, midpoint-1)
    else:
        # target > array[midpoint]
        return binary_search(array, target, midpoint+1, high)


if __name__ == '__main__':
    array = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(array, target))
    print(binary_search(array, target))
