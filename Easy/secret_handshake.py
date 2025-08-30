'''
Any number between 1 and 31 can be represented in 5 bits of binary (since 2^5 = 32).
Example:

9 → 01001
26 → 11010

Mapping Binary Digits to Actions:
We read the binary digits from right to left:

00001 (1)  → "wink"
00010 (2)  → "double blink"
00100 (4)  → "close your eyes"
01000 (8)  → "jump"
10000 (16) → reverse the order of previous actions

Meaning:
Bit 0 (value 1)  → wink
Bit 1 (value 2)  → double blink
Bit 2 (value 4)  → close your eyes
Bit 3 (value 8)  → jump
Bit 4 (value 16) → reverse
'''

def handshake(n: int) -> list:
    """
    Convert a number (1–31) into a secret handshake sequence.
    """

    # Define actions mapped to each binary bit (except reverse)
    actions = ["wink", "double blink", "close your eyes", "jump"]
    result = []

    # Check bits 0–3
    for i in range(4):
        if n & (1 << i):        # check if the i-th bit is set
            result.append(actions[i])

    # Check bit 4 → reverse
    if n & (1 << 4):
        result.reverse()

    return result


# Example Usage
if __name__ == "__main__":
    test_cases = [9, 12, 26]
    for case in test_cases:
        print(f"For input {case}, the output is {handshake(case)}")
