def print_table(n):
    i = 0

    print(f'Table of {n} is:')
    while i < 10:
        i += 1
        print(n, '*', i, '=', n * i)

print_table(7)


def sum_of_all_digits_of_a_number(num):
    sum = 0
    while num > 0:
        sum += num % 10  # get last digit of a number
        num = num // 10  # discard/remove last digit of a number

    print(f'Sum of all digits is: {sum}')

sum_of_all_digits_of_a_number(7654)


def count_digits_of_a_number(num):
    i = 0
    while num > 0:
        i += 1
        num = num // 10

    print(f'Number of digits are: {i}')

count_digits_of_a_number(7654)


def reverse_number(num):
    reversed_num = 0

    while num > 0:
        reminder = num % 10
        num = num // 10
        reversed_num = reversed_num * 10 + reminder

    print(f'Reversed number is: {reversed_num}')

reverse_number(7654)


def check_a_number_is_palindrome(num):
    original_num = num
    reversed_num = 0

    while num > 0:
        reminder = num % 10
        num = num // 10
        reversed_num = reversed_num * 10 + reminder

    if original_num == reversed_num:
        print(f'{original_num} is a palindrome')
    else:
        print(f'{original_num} is not a palindrome')

check_a_number_is_palindrome(1221)


def sum_of_natural_number(num):
    i = sum = 0

    while i < num:
        i += 1
        sum += i

    print(f'Sum of all numbers is: {sum}')

sum_of_natural_number(7)


def finding_maximum_and_minimum(limit):
    maximum = -float('inf')
    minimum = float('inf')
    i = 0
    while i < limit:
        i += 1
        x = int(input(f'Enter {i} number: '))
        if x > maximum:
            maximum = x
        if x < minimum:
            minimum = x

    print(f'Maximum is: {maximum}')
    print(f'Minimum is: {minimum}')

# finding_maximum_and_minimum(3)


def print_all_numbers_till_10_which_is_not_divisible_by_3():
    i = 0
    while i < 10:
        i += 1
        if i % 3 == 0:
            continue
        print(i)

print_all_numbers_till_10_which_is_not_divisible_by_3()


def while_else(n):
    while n > 0:
        if n == 2:
            break
        print(n)
        n -= 1
    else:
        print('else')

    print('out')

while_else(3)
