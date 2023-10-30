import problems

def test_multiples_of3or5():
    assert problems.multiplesOf3or5(10) == 23
    assert problems.multiplesOf3or5(1000) == 233168 # find

def test_evenFibonacciNumbers():
    assert problems.evenFibonacciNumbers(10) == 10
    assert problems.evenFibonacciNumbers(4000000) == 4613732 # find
