"""
Raindrops Exercise

Convert a number to its corresponding raindrop sounds based on divisibility rules.
If divisible by 3, 5, or 7, append the corresponding sound.
If not divisible by any, return the number as a string.
"""


def convert(number):
    results = ""
    if number % 3 == 0 :
        results += "Pling"
    if number % 5 ==0:
        results += "Plang"
    if number %7 ==0 :
        results += "Plong"

    if not results:
        return str(number)
    return results

# Example usage

if __name__ =="__main__":
    test_cases = [28, 30, 34]
    for  test in test_cases:
        print(f"for this number:{test}, the output is {convert(test)}")
