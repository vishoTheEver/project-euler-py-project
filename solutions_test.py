import problems


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

def test_sumSquareDifference():
    assert problems.sumSquareDifference(1, 10) == 2640
    assert problems.sumSquareDifference(1, 100) == 25164150

def test_10001stPrime():
    assert problems.prime10001st(6) == 13
    assert problems.prime10001st(10001) == 104743

def test_specialPythagoreanTriplet():
    assert problems.specialPythagorasTriplet() == 31875000

def test_summationOfPrimes():
    assert problems.summationOfPrimes(10) == 17
def test_powerDigitSum():
    assert problems.powerDigitSum(15) == 26
    assert problems.powerDigitSum(1000) == 1366

def test_factorialDigitSum():
    assert problems.factorialDigitSum(10) == 27
    assert problems.factorialDigitSum(100) == 648