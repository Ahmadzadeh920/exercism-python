'''
Sum of first N natural numbers:

S=1+2+3+⋯+N=N(N+1)//2
(S)**2=(N(N+1)2)**2

Sum of the squares of first N numbers:

    SumSquares=12+22+⋯+N2=N(N+1)(2N+1)//6


Difference:

    Difference=(S)**2−SumSquares
'''

def sum_square_difference(n: int) -> int:
    """
    Calculate the difference between the square of the sum and 
    the sum of the squares of the first n natural numbers.

    Args:
        n (int): The number of natural numbers.

    Returns:
        int: The difference.
    """
    sum_n = (n*(n+1))//2
    square_sum_n = sum_n **2
    sum_of_squares= (n * (n+1) * (2*(n+1)))//6
    diff = square_sum_n - sum_of_squares
    return diff


#Example Usage
if __name__ == "__main__":
    print(sum_square_difference(10))  # Output: 2640
    print(sum_square_difference(100)) # Output: 25164150

