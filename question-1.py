# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# track sum of the variable
# pass a list of numbers and you make sure that you give sum of multiples

def number_divided_by(number, multiples):
    for num in multiples: # [3, 5] => 9
        if (number % num == 0):
            return True

    return False

# for works for range and list

def sum_of_multiples(range_of_number, multiples):
    sum = 0

    # iterate from 1 to 999
    for i in range_of_number:
        # find multiples of 3, 5, 6, 9, 10, 12, 15
        if number_divided_by(i, multiples): # (i % first_multiple == 0) or (i % second_multiple == 0):
            sum += i

        # if (i % 5 == 0):
        #     sum += i 

        # remove multiples of 15
        # if (i % 15 == 0):
        #     sum -= i
    
    return sum


# print
print(sum_of_multiples(range_of_number = range(1, 1000), multiples = [3,5]))
# 233168

