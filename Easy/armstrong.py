'''An Armstrong number (also called a narcissistic number) is a number that equals the sum of its digits raised to the power of the number of digits.

Examples:

9 → 9^1 = 9 ✅

153 → 1^3 + 5^3 + 3^3 = 153 ✅

10 → 1^2 + 0^2 = 1 ❌'''

def check_armstrong(digit):
    str_digits= str(digit)
    length = len(str_digits)

    if (sum(int(i)**length for i in str_digits) == digit):
        return True
    else:
        return False

# Example usage:
if __name__ == "__main__":
    numbers = [9, 10, 153, 154, 370, 371, 9474, 9475]

    for number in numbers:
        if check_armstrong(number):
            print(f"{number} is an Armstrong number.")
        else:
            print(f"{number} is not an Armstrong number.")