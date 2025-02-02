"""
The course material includes two different ways to implement the function count_even:
# implementation 1
def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result# implementation 2
def count_even(numbers):
    return sum(x % 2 == 0 for x in numbers)
Compare the efficiencies of the two implementations using a list that contains 10^7 randomly chosen numbers.
In this exercise, you get a point automatically when you submit the test results and the code that you used.
Implementation 1 run time: _____ s
Implementation 2 run time: _____ s
"""
