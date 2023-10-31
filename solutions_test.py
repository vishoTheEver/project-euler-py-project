import problems

def test_multiples_of3or5():
    assert problems.multiplesOf3or5(10) == 23
    assert problems.multiplesOf3or5(1000) == 233168 # find

def test_evenFibonacciNumbers():
    assert problems.evenFibonacciNumbers(10) == 10
    assert problems.evenFibonacciNumbers(4000000) == 4613732 # find

def test_largestPrimeFactor():
    assert problems.largestPrimeFactor(13195) == 29
    assert problems.largestPrimeFactor(600851475143) == 6857 # find

def test_largestPalindromeProduct():
    assert problems.largestPalindromeProduct(2) == 9009
    assert problems.largestPalindromeProduct(3) == 906609 # find

def test_smallestMultiple():
    assert problems.smallestMultiple(1,10) == 2520
    assert problems.smallestMultiple(1,20) == 232792560