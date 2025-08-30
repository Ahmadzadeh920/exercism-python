'''
This is the Square Root Exercise where we calculate the integer square root without using Python’s math library
'''

def integer_sqrt(n):
    """
    Returns the integer square root of n.
    Assumes n is a perfect square (1, 4, 9, 16...).
    Uses binary search for efficiency.
    """

    if n==1:
        return 1
    else:
        low, heigh = 1, n

        while low<heigh:
            mid = (low +heigh)//2
            square = mid * mid
            if n==square:
                return square
            elif square> n:
                mid = mid-1
            else:
                mid +=1

        return None


# Example Usage
if __name__ =="__main__":
    test_cases =[9, 16, 25]
    for test in test_cases:
        print(f"Square root of {test} is {integer_sqrt(test)}")
        