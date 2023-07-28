class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        # Evaluate the polynomial at the given point x
        result = 0
        power = 1
        for coefficient in self.coefficients:
            result += coefficient * power
            power *= x
        return result

    def __add__(self, other):
        # Find the maximum degree of the two polynomials
        max_degree = max(len(self.coefficients), len(other.coefficients))

        # Pad the coefficients with zeros to make both polynomials of the same degree
        self_coeffs_padded = self.coefficients + [0] * (max_degree - len(self.coefficients))
        other_coeffs_padded = other.coefficients + [0] * (max_degree - len(other.coefficients))

        # Perform the addition of the coefficients element-wise
        new_coefficients = [a + b for a, b in zip(self_coeffs_padded, other_coeffs_padded)]

        return Polynomial(new_coefficients)

# Example 1
poly = Polynomial([10, -1])
print(poly(0))  # Output: 10
print(poly(1))  # Output: 9
print(poly(2))  # Output: 8

print()

# Example 2
poly1 = Polynomial([0, 1])  # x
poly2 = Polynomial([10])    # 10
poly3 = poly1 + poly2       # x + 10
poly4 = poly2 + poly1       # x + 10

# Evaluate poly3 and poly4 at various points
print(poly3(-2), poly4(-2))  # Output: 8 8
print(poly3(-1), poly4(-1))  # Output: 9 9
print(poly3(0), poly4(0))    # Output: 10 10
print(poly3(1), poly4(1))    # Output: 11 11
print(poly3(2), poly4(2))    # Output: 12 12
