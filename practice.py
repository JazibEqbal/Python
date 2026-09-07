def palindrome_string(s):
    s1 = s[::-1]
    # for i in range(len(s)-1, -1, -1):
    #     s1 += s[i]

    if s.casefold() == s1.casefold():
        print(f'{s} is palindrome')
    else:
        print(f'{s} is not palindrome')

palindrome_string('Madam')


def sum_of_all_digits_of_a_number(num):
    sum = 0
    while num > 0:
        last_digit = num % 10
        num = num // 10
        sum += last_digit

    print(sum)

sum_of_all_digits_of_a_number(108)


def reverse_a_number(num):
    rev = 0
    while num > 0:
        last_digit = num % 10
        num = num // 10
        rev = rev * 10 + last_digit

    print(rev)

reverse_a_number(1008)


def count_digits(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1

    print(count)

count_digits(10880)


def check_a_number_is_palindrome(num):
    original_num = num
    rev = 0
    while num > 0:
        last_digit = num % 10
        num = num // 10
        rev = rev * 10 + last_digit

    if original_num == rev:
        print(original_num, "is a palindrome")
    else:
        print(original_num, "is not a palindrome")

check_a_number_is_palindrome(1221)


def sum_of_natural_numbers(num):
    sum = 0
    # for i in range(1, num + 1):
    #     sum += i
    i = 0
    while i < num:
        i += 1
        sum += i

    print(sum)

sum_of_natural_numbers(7)

def print_all_numbers_till_upto_given_number_which_is_divisible_by_3(num):
    i = 1
    while i <= num:
        if i % 3 == 0:
            print(i)
        i += 1

print_all_numbers_till_upto_given_number_which_is_divisible_by_3(10)


def factorial_of_a_number(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(factorial)

factorial_of_a_number(5)

def fibonacci_of_a_number(num):
    a, b = 0, 1
    for i in range(1, num):
        # c = a + b
        a, b = b, a + b
        # b = c

    print(a)

fibonacci_of_a_number(5)
# 0 1 1 2 3 5 8

def factors_of_a_number(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

factors_of_a_number(6)

def check_if_given_number_is_prime(num):
    c = 0
    for i in range(1, num + 1):
        if num % i == 0:
            c += 1

    if c == 2:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

check_if_given_number_is_prime(17)
