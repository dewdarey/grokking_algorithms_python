from random import randint

# Selection sort
# Find Smaller
def findSmaller(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):  # Fix: Use range to get indices
        if arr[i] <= smallest:
            smallest = arr[i]
            smallest_index = i  # Fix: Update with the index
    return smallest_index


# Selection Sort
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmaller(arr)
        newArr.append(arr.pop(smallest))
    return newArr

# Binary search
def binarySearch(arr, toFind):
    low = 0  # Fix: Use index 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]  # Fix: Use arr instead of list
        if guess == toFind:
            return mid
        if guess > toFind:
            high = mid - 1
        else:
            low = mid + 1
    return None

# To execute
arrLen = int(input("Enter array length: "))
arr = [randint(0, 10) for i in range(arrLen)]
toFind = int(input("Enter the number to search it in array: "))
newArr = selectionSort(arr)

# Prints
print(newArr)
print(binarySearch(newArr, toFind))
