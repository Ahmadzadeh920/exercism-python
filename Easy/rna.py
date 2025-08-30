def to_rna(dna:str) -> str:
    """
    Convert a DNA sequence into its RNA complement.
    
    Parameters:
    dna (str): A string representing the DNA sequence (only A, C, G, T).
    
    Returns:
    str: The RNA complement string.

    The task is to transcribe DNA into RNA by replacing each DNA nucleotide with its RNA complement:
        G → C
        C → G
        T → A
        A → U
    """
    rna_complement = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    
    rna = ""
    for nucleotide in dna:
        rna += rna_complement[nucleotide]
       
    return rna
        
#Example usage
if __name__ == "__main__":
    test_cases = [
        "ACGTGGTCTTAA",
        "CCGTA",
        "TTTT",
        "AGCT"
    ]
    
    for dna in test_cases:
        rna = to_rna(dna)
        print(f"DNA: {dna} -> RNA: {rna}")  

