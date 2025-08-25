'''Chessboard: 64 squares

Grains:

Square 1 → 1 grain

Square 2 → 2 grains

Square 3 → 4 grains

Square n → double the previous square → 2n−1 grains'''



def grain_on_square(square):
    if square<1 or square>64:
        raise ValueError("the square must be between 1 and 64")
    else:
        return 2**(square-1)

def total_grains(square):
    total = 0 
    for i in range(1,square+1):
        total += grain_on_square(i)
    return total


# Example usage:
if __name__ == "__main__":
    squares = [1, 2, 3, 4, 16, 32, 64]

    for square in squares:
        print(f"Square {square} has {grain_on_square(square)} grains.")
    
    print(f"Total grains on the chessboard: {total_grains(64)}")
