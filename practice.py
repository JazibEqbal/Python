def palindrome_string(s):
    s1 = s[::-1]
    # for i in range(len(s)-1, -1, -1):
    #     s1 += s[i]

    if s.casefold() == s1.casefold():
        print(f'{s} is palindrome')
    else:
        print(f'{s} is not palindrome')

# palindrome_string('Madam')
# palindrome_string('Race car')


def sum_of_all_digits_of_a_number(num):
    sum = 0
    while num > 0:
        last_digit = num % 10
        num = num // 10
        sum += last_digit

    print(sum)

# sum_of_all_digits_of_a_number(108)

def reverse_a_number(num):
    rev = 0
    while num > 0:
        last_digit = num % 10
        num = num // 10
        rev = rev * 10 + last_digit

    print(rev)

# reverse_a_number(1008)


def count_digits(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1

    print(count)

# count_digits(10880)


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

# check_a_number_is_palindrome(1221)


def sum_of_natural_numbers(num):
    sum = 0
    # for i in range(1, num + 1):
    #     sum += i
    i = 0
    while i < num:
        i += 1
        sum += i

    print(sum)

# sum_of_natural_numbers(7)

def print_all_numbers_till_upto_given_number_which_is_divisible_by_3(num):
    i = 1
    while i <= num:
        if i % 3 == 0:
            print(i)
        i += 1

# print_all_numbers_till_upto_given_number_which_is_divisible_by_3(10)


def factorial_of_a_number(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(factorial)

# factorial_of_a_number(5)

def fibonacci_of_a_number(num):
    a, b = 0, 1
    for i in range(1, num):
        # c = a + b
        a, b = b, a + b
        # b = c

    print(a)

# fibonacci_of_a_number(5)
# 0 1 1 2 3 5 8

def factors_of_a_number(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

# factors_of_a_number(6)

def check_if_given_number_is_prime(num):
    c = 0
    for i in range(1, num + 1):
        if num % i == 0:
            c += 1

    if c == 2:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

# check_if_given_number_is_prime(17)


def find_missing_numbers_method_1(l):
    missing_numbers = []
    for i in range(len(l) - 1):
      if l[i] != l[i + 1] + 1:
        for ic in range(l[i] + 1, l[i + 1]):
          missing_numbers.append(ic)

    print(missing_numbers)

# find_missing_numbers_method_1([2, 5, 6, 7, 9, 12])


def find_missing_numbers_method_2(l):
    missing_numbers = []

    for i in range(len(l) - 1):
        if l[i + 1] - l[i] > 1:
            missing_numbers.extend(range(l[i] + 1, l[i + 1]))

    print(missing_numbers)

# find_missing_numbers_method_2([2, 5, 6, 7, 9, 12])

def largest_of_three_numbers(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

# print(largest_of_three_numbers(10, 5, 10))

s = "Python Programming"

def operation_on_string(s):
    number_of_characters = len(s.replace(' ', ''))
    number_of_spaces = len(s) - number_of_characters
    vowels = ['a', 'e', 'i', 'o', 'u']
    number_of_vowels = 0
    number_of_consonants = 0
    for c in s:
        if c.isalpha():
            if c.lower() in vowels:
                number_of_vowels += 1
            else:
                number_of_consonants += 1


    print(number_of_characters, number_of_spaces, number_of_vowels, number_of_consonants)

# operation_on_string(s)


def remove_duplicates(l):
    for idx in range(len(l)):
        for j in range(len(l) -1, idx, -1):
            if l[j] == l[idx]:
                l.pop(j)
    return l

# print(remove_duplicates([2, 5, 2, 7, 5, 9, 7, 10, 10]))


def remove_duplicates_2(l):
    result = []

    for item in l:
        if item not in result:
            result.append(item)

    return result

# print(remove_duplicates_2([2, 5, 2, 7, 5, 9, 7, 10, 10]))


def find_second_largest_distinct(numbers):
    largest = float('-inf')
    second_largest = float('-inf')

    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number

    return second_largest


print(find_second_largest_distinct([10, 5, 20, 8, 20, 15]))


def find_second_largest_unique_occurrence(numbers):
    largest = float('-inf')
    second_largest = float('-inf')

    for i in range(len(numbers)):
        occurrence_count = 0

        for j in range(len(numbers)):
            if numbers[i] == numbers[j]:
                occurrence_count += 1

        if occurrence_count == 1:
            if numbers[i] > largest:
                second_largest = largest
                largest = numbers[i]
            elif numbers[i] > second_largest:
                second_largest = numbers[i]

    return second_largest


print(find_second_largest_unique_occurrence([10, 5, 20, 8, 20, 15]))

"""
Frequency Counter l = [2, 3, 2, 5, 3, 2, 7] Expected: {2: 3, 3: 2, 5: 1, 7: 1} Try using a dictionary.

Word Frequency sentence = "python is easy and python is powerful"

Two Sum :Find the two numbers whose sum equals the target.

Given: l = [2, 7, 11, 15], target = 9

Expected: 2, 7

Then try solving it efficiently using a dictionary.


Move Zeros to the end while maintaining the order of other numbers.

l = [0, 1, 0, 3, 12]

Expected: [1, 3, 12, 0, 0]

Find all duplicate numbers.

l = [1, 3, 4, 2, 3, 5, 1, 6, 4]

Expected: [1, 3, 4]
"""