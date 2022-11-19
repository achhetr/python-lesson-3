# The sum of the squares of the first ten natural numbers is,

# The square of the sum of the first ten natural numbers is,

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# solution for first 10 -> 2640
# 25164150

# TDD
answer_1 = 2640
answer_2 = 25164150
answer_3 = 250166416500

def sum_of_squares(number):
    sum = 0
    for i in range(number + 1):
        sum += i ** 2

    return sum


def sum_sq_difference(number):
    return ((sum(range(number + 1)) ** 2) - sum_of_squares(number))


# tests I am writing for my program
result_1 = sum_sq_difference(10)
result_2 = sum_sq_difference(100)
result_3 = sum_sq_difference(1000)

# my tests
print(f'My program with 10 natural numbers gives {result_1} is: {answer_1 == result_1}')
print(f'My program with 100 natural numbers gives {result_2} is: {answer_2 == result_2}')
print(f'My program with 1000 natural numbers gives {result_3} is: {answer_3 == result_3}')
