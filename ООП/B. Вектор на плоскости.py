from __future__ import annotations
import math


class MyVector:
    def __init__(self, *args: [float | list[float]]):
        # The constructor takes a variable number of arguments, which can be floats or lists of floats.

        # Check if all arguments are instances of either int or float
        assert all(map(isinstance, args, [(int, float)] * 2))

        # Convert the arguments into a list of floats if they are not already a list.
        if isinstance(args, list):
            self.coords = args
        else:
            self.coords = list(args)

    def x(self):
        # Return the x-coordinate (first element) of the vector.
        return self.coords[0]

    def y(self):
        # Return the y-coordinate (second element) of the vector.
        return self.coords[1]

    def __getitem__(self, item: int):
        # Get the element at the given index from the vector.
        return self.coords[item]

    def __add__(self, other):
        # Add two vectors component-wise and return the resulting vector.
        return MyVector(*(self[i] + other[i] for i in range(len(self.coords))))

    def __sub__(self, other):
        # Subtract two vectors component-wise and return the resulting vector.
        return MyVector(*(self[i] - other[i] for i in range(len(self.coords))))

    def __mul__(self, other):
        # Define the multiplication operation for the vector.
        # If 'other' is another vector, perform dot product and return the scalar result.
        if isinstance(other, MyVector):
            return sum([self[i] * other[i] for i in range(0, 1 + 1)])
        # If 'other' is a scalar (int or float), perform scalar multiplication and return the resulting vector.
        elif isinstance(other, (float, int)):
            return MyVector(*(self[i] * other for i in range(0, 1 + 1)))

    def __imul__(self, other):
        # In-place multiplication of the vector with a scalar.
        # If 'other' is another vector, perform dot product and update the vector.
        if isinstance(other, MyVector):
            return sum([self[i] * other[i] for i in range(0, 1 + 1)])
        # If 'other' is a scalar (int or float), perform scalar multiplication and update the vector.
        elif isinstance(other, (float, int)):
            self.coords = list(self[i] * other for i in range(0, 1 + 1))
            return self

    def __rmul__(self, other):
        # Define the right-multiplication operation for the vector.
        # This is called when the vector is on the right side of the '*' operator.
        # Here, we just delegate the operation to the regular multiplication method.
        assert isinstance(other, (int, float))
        return self * other

    def __pow__(self, vc):
        # Define the cross product operation for the vector.
        # Return a new vector resulting from the cross product between 'self' and 'vc'.
        return MyVector(self[1] * vc[2] - self[2] * vc[1], - (self[0] * vc[2] - self[2] * vc[0]),
                        self[0] * vc[1] - self[1] * vc[0])

    def __lt__(self, other):
        # Define the less-than comparison between two vectors based on their magnitudes (lengths).
        # Compare the magnitudes of the vectors using the absolute value.
        return abs(self) < abs(other)

    def __eq__(self, other):
        # Define the equality comparison between two vectors.
        # Two vectors are equal if their coordinates are equal.
        return self.coords == other.coords

    def __ne__(self, other):
        # Define the inequality comparison between two vectors.
        # Two vectors are not equal if their coordinates are not equal.
        return not self.__eq__(other)

    def __abs__(self) -> float:
        # Define the absolute value (magnitude) of the vector.
        # Calculate and return the Euclidean norm of the vector.
        return math.sqrt(self[0] ** 2 - self[1] ** 2)

    def __str__(self) -> str:
        # Define the string representation of the vector.
        # Return a string in the format "MyVector(x, y)" where x and y are the coordinates of the vector.
        return f"MyVector({self[0]}, {self[1]})"

def example1():
    vec1 = MyVector(-2, 5)
    vec2 = MyVector(3, -4)
    vecsum = vec1 + vec2
    print(vecsum)

example1()
