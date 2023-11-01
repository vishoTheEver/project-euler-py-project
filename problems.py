import math


# Problem 1: Multiples of 3 or 5
def multiplesOf3or5(n):
    sum = 0
    for num in range(n):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum

# Problem 2: Even Fibonacci Numbers
def evenFibonacciNumbers(n):
    t1, t2 = 1, 2
    sum = 0
    while (t2 <= n):
        if (t2 % 2 == 0):
            sum += t2
        ## t1 --> t2 and t2 --> t1 + t2
        t1, t2 = t2, t1 + t2
    return sum

# Problem 3: Largest Prime Factor
def largestPrimeFactor(n):
    factors = []
    for num in range(2, int(math.sqrt(n))):
        if n % num == 0:
            factors.append(num)
    # prime factors
    prime_factors = []
    is_prime = True # check
    for divisors in factors:
        for i in range(2, divisors):
            if divisors % i == 0:
                is_prime = False # condition dissatisfied
                break # prevents further loops
        if(is_prime):
            prime_factors.append(divisors)

    # largest prime factor
    lpf = prime_factors[-1] # largest pf at the end.
    return lpf

# Problem 4: Largest Palindrome Product
def largestPalindromeProduct(n):
    # finding all palindromes between 10^(n-1) and 10^n-1
    min_num = 10**(n-1)
    max_num = 10**n - 1
    palindromes = []
    for num1 in range(min_num, max_num+1):
        for num2 in range(min_num, max_num+1):
            product_str = str(num1 * num2)
            product_str_reversed = product_str[::-1]
            if(product_str == product_str_reversed):
                palindromes.append(int(product_str))
    # finding the max palindrome
    palindromes.sort()
    max_palindrome = palindromes[-1]
    return max_palindrome

# Problem 5: Smallest Multiple
def smallestMultiple(a, b):
    count = (b-1)+1
    found_smallest_multiple = False
    while not found_smallest_multiple:
        count +=1
        cases_passed = 0
        for cases in range(a,b+1):
            if(count % cases == 0):
                cases_passed += 1
        if cases_passed == b-a+1:
            found_smallest_multiple = True
    return count;

# Problem 6: Sum Square Difference
def sumSquareDifference(a,b):
    sum_of_squares = 0
    sum = 0
    for num in range(a,b+1):
        sum_of_squares += num**2
        sum += num
    squares_of_sum = sum**2

    return squares_of_sum-sum_of_squares

# Problem 7: 10001st Prime
def prime10001st(n):
    primes = []
    primes.append(2)
    current_number = 3
    while(len(primes) < n):
        is_prime = True;
        for prime in primes:
            if(prime * prime > current_number):
                break;
            if current_number % prime == 0:
                is_prime = False;
                break;
        if(is_prime):
            primes.append(current_number);
        current_number += 1
    return primes[-1]