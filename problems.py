

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