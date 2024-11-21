'''
In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. Your task will be to return the sum of the numbers that occur only once.

For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. Every other number occurs twice.
'''
def sum_arrays(arr):

    sum_result = 0
    for current_position in range(len(arr)):
        if arr.count(arr[current_position]) > 1:
            continue
        else:
            sum_result += arr[current_position]

    return sum_result