

# Problem 1: Multiples of 3 or 5
def multiplesOf3or5(n):
    sum = 0
    for num in range(n):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum