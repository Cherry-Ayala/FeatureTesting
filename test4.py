def p(a, b):
    if b == 0:
        print("Error: División por cero")
        return None
    else:
        return a / b
    

def f(n):
    if n < 0:
        print("Error: Número negativo")
        return None
    else:
        r = 1
        for i in range(1, n + 1):
            r *= i
        return r


# Function to find the sum of a number and its factorial, then divide by a given divisor
def sum_of_two_nums(x, y):
    factorial_result = f(x)
    if factorial_result is None:
        print("Error: Unable to compute factorial for input number")
        return None

    sum_result = factorial_result + y
    division_result = p(sum_result, x)  # Dividing the sum by the original number

    return division_result

# Function to multiply a given number by 2
def multiply_by_2(x):
    return x * 2

#write a function that uses quick sort
# Function to sort a list using the quicksort algorithm
def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    pivot = input_list[len(input_list) // 2]
    left = [x for x in input_list if x < pivot]
    middle = [x for x in input_list if x == pivot]
    right = [x for x in input_list if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def usingMergeSort(array):
    # Base case: array of zero or one element is already sorted
    if len(array) <= 1:
        return array

    # Recursive case: divide the array into two halves
    mid = len(array) // 2
    left_half = usingMergeSort(array[:mid])
    right_half = usingMergeSort(array[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    # Merge two sorted arrays into a single sorted array
    result = []
    left_index, right_index = 0, 0

    # Compare elements from left and right arrays and build the result
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left or right array
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result



def QuickSort(list):
    if len(list) <= 1:
        return list
    pivot = list[len(list) // 2]
    left = [x for x in list if x < pivot]
    middle = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]
    return QuickSort(left) + middle + QuickSort(right)

def sum_two_nums(x, y):
    """Function to sum a number and its factorial, then divide by another number."""
    factorial_result = f(x)
    if factorial_result is None:
        print("Error: Unable to compute factorial for input number")
        return None

    sum_result = factorial_result + y
    division_result = p(sum_result, x)  # Dividing the sum by the original number

    return division_result

#make a function that gets a list, and it unsorts it
# Function to "unsort" a sorted list into a random order
import random

def unsort_list(sorted_list):
    shuffled_list = sorted_list[:]
    random.shuffle(shuffled_list)
    return shuffled_list