import numpy as np
def matrix_rank(matrix):
    # Use numpy's linear algebra function to calculate the rank
    return np.linalg.matrix_rank(matrix)
def row_echelon_form(matrix):
    # Ensure the matrix has 2 rows and 2 columns
    if matrix.shape != (2, 2):
        raise ValueError("Matrix must be of order 2x2")

    # Convert the matrix to float64 data type
    matrix = matrix.astype('float64')

    # Perform row operations to convert to row echelon form
    if matrix[0, 0] == 0:
        matrix[[0, 1]] = matrix[[1, 0]]  # Swap rows if the first element is zero

    factor = matrix[1, 0] / matrix[0, 0]
    matrix[1] -= factor * matrix[0]

    return matrix

# Example matrix (replace with your own)
matrix = np.array([[2, 4], [1, 3]])

# Convert to row echelon form
result_matrix = row_echelon_form(matrix)
print("Row Echelon Form:")
print(result_matrix)
rank = matrix_rank(matrix)
print("Rank of the Matrix:", rank)
