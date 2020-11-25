# In this Kata, you will be given an array of numbers in which two numbers occur once and
# the rest occur only twice.
# Your task will be to return the sum of the numbers that occur only once.
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once,
# and their sum is 15.
# More examples in the test cases below.

# Good luck!

# arr = [4, 5, 7, 5, 4, 8] # result 15
# arr = [9, 10, 19, 13, 19, 13] # result 19
# arr = [16, 0, 11, 4, 8, 16, 0, 11] # result 12
# arr = [5, 17, 18, 11, 13, 18, 11, 13] # result 22
arr = [5, 10, 19, 13, 10, 13] # result 24

def repeats(arr):
    total = 0

    for num in arr:
        if arr.count(num) == 1:
            total += num

    return total

print(repeats(arr))
