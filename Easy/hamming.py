'''Algorithm:

Check if lengths are equal.

Initialize a counter for differences.

Loop through both strands simultaneously, comparing each position.

Increment the counter whenever characters differ.

Return the counter.'''


def hamming_distance(strand1: str, strand2: str) -> int:
    """
    Calculate the Hamming distance between two DNA strands.
    The Hamming distance is the number of differences at corresponding positions.
    """

    if len(strand1) != len(strand2):
        raise ValueError('the length of two strans is not equal')

    else:
        # Initialize a counter for differences
        distance = 0
        # Loop through both strands simultaneously
        for base1, base2 in zip(strand1, strand2):
            if base1 != base2:
                distance +=1
            else:
                continue
    return distance


#Example Usage
if __name__=="__main__":
    strand_a = "GAGCCTACTAACGGGAT"
    strand_b = "CATCGTAATGACGGCCT"
    print(hamming_distance(strand_a, strand_b))

    print(hamming_distance("AAAA", "AAAT"))
    print(hamming_distance("GATTACA", "GACTATA"))


