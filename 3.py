import numpy as np

# Function to check if a matrix is invertible
def is_invertible(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        return False  # Only square matrices can be invertible
    return np.linalg.det(matrix) != 0  # A matrix is invertible if its determinant is non-zero

# Function to find the inverse of a matrix
def find_inverse(matrix):
    if not is_invertible(matrix):
        return None  # Matrix is not invertible
    
    return np.linalg.inv(matrix)

# Function to display a matrix
def display_matrix(matrix):
    for row in matrix:
        print(row)

# Example matrices
matrix_A = np.array([[1, 2], [3, 4]])
matrix_B = np.array([[5, 6], [7, 8]])

# 1. Matrix Addition, Subtraction, Multiplication
addition_result = matrix_A + matrix_B
subtraction_result = matrix_A - matrix_B
multiplication_result = np.dot(matrix_A, matrix_B)

print("1. Matrix Addition:")
display_matrix(addition_result)
print("\n1. Matrix Subtraction:")
display_matrix(subtraction_result)
print("\n1. Matrix Multiplication:")
display_matrix(multiplication_result)

# 2. Check if matrices are invertible
print("\n2. Check if matrices are invertible:")
print(f"Matrix A is invertible: {is_invertible(matrix_A)}")
print(f"Matrix B is invertible: {is_invertible(matrix_B)}")

# 3. Find the inverses of matrices if they are invertible
print("\n3. Find Inverse:")
inverse_A = find_inverse(matrix_A)
inverse_B = find_inverse(matrix_B)

if inverse_A is not None:
    print("Inverse of Matrix A:")
    display_matrix(inverse_A)
else:
    print("Matrix A is not invertible.")

if inverse_B is not None:
    print("\nInverse of Matrix B:")
    display_matrix(inverse_B)
else:
    print("Matrix B is not invertible.")
