'''We need to classify a triangle based on side lengths a, b, and c:

Equilateral → all sides equal: a == b == c

Isosceles → at least two sides equal: a == b or b == c or a == c

Scalene → all sides different: a != b != c != a

Triangle Validity Check:

All sides must be positive (> 0)

Sum of any two sides ≥ third side:'''

def classify_triangle(a,b,c):
    if a<0 or b<0 or c<0:
        return "Not a triangle"
    if a+b<c or c+a<b or b+c<a:
        return "Not a triangle"
    if a==b and b==c and c==a:
        return "Equilateral"
    elif a==b or b==c or c==a:
        return "Isosceles"
    else:
        return "Scalene"

# Example usage:
if __name__ == "__main__":
    triangles = [(3, 3, 3), (3, 4, 3), (3, 4, 5), (1, 2, 3), (0, 4, 5)]

    for sides in triangles:
        a, b, c = sides
        print(f"Sides: {a}, {b}, {c} => Type: {classify_triangle(a, b, c)}")
