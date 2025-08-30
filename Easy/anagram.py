'''Goal: Given a target word and a list of candidate words, find all candidates that are anagrams of the target.

Rules for an anagram:

Must use exactly the same letters as the target.

Must not be identical to the target word itself.

Case-insensitive comparison for letters ("PoTS" == "sTOp").

Preserve the original case of candidate words in the output.'''


def find_anagrams(target: str, candidates: list) -> list:
    """
    Find all candidate words that are anagrams of the target word.

    Args:
        target (str): The target word.
        candidates (list): List of candidate words.

    Returns:
        list: List of anagrams from candidates.
    """
    # Normalize the target to lowercase and sort letters


    sorted_target = sorted(target.lower())
    results = []
    for i in range(len(candidates)):
        # Skip identical words
        if candidates[i]==target:
            continue
        else:
            # Normalize candidate to lowercase and sort letters
            sorted_candidate = sorted(candidates[i].lower())
            # Compare sorted letters
            if sorted_candidate == sorted_target:
                results.append(candidates[i])
    return results


# Exapmple Usage
if __name__ == "__main__":
    test_cases = [
        ("listen", ["enlists", "google", "inlets", "banana"]),
        ("master", ["stream", "pigeon", "maters"]),
        ("Orchestra", ["cashregister", "Carthorse", "radishes"]),
        ("go", ["go Go GO"]),
        ("allergy", ["gallery", "ballerina", "regally", "clergy", "largely", "leading"]),
    ]
    for target, candidates in test_cases:
        print(f"Target: {target}, Candidates: {candidates} => Anagrams: {find_anagrams(target, candidates)}")