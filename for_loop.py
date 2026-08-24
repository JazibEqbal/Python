def even_numbers(num):
    l = []
    for i in range(0, num, 2):
        l.append(i)

    print(l)

even_numbers(10)


def factorial_of_a_number(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i

    print(fact)

factorial_of_a_number(5)


def sum_of_natural_number(num):
    sum = 0

    for i in range(1, num + 1):
        sum += i

    print(f'Sum of all numbers is: {sum}')

sum_of_natural_number(7)


def fibonacci_series(num):
    a, b = 0, 1
    fib = [a, b]

    for i in range(1, num):
        c = a + b
        a = b
        b = c
        fib.append(c)

    print(fib)

fibonacci_series(7)


def factor_of_a_number(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    return factors

print(f'Factor of 12 are: {factor_of_a_number(12)}')


def check_if_a_number_is_prime(num):
    number_of_factors = len(factor_of_a_number(num))

    if number_of_factors == 2:
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')

check_if_a_number_is_prime(12)


def print_all_prime_numbers(num):
    is_prime = []

    def _is_prime(num):
        number_of_factors = len(factor_of_a_number(num))

        if number_of_factors == 2:
            return True
        else:
            return False

    for i in range(1, num + 1):
        if _is_prime(i):
            is_prime.append(i)

    print(is_prime)

print_all_prime_numbers(100)

