import sympy as sp

# Define the 2x2 matrix as a list of lists
matrix = [
    [1, 2],
    [3, 4]
]

# Create a SymPy Matrix object from the list
mat = sp.Matrix(matrix)

# Find the row echelon form of the matrix
rref_mat, pivot_columns = mat.rref()

# Find the rank of the matrix
rank = rref_mat.rank()

# Print the row echelon form and rank
print("Row Echelon Form:")
print(rref_mat)
print("Rank of the Matrix:", rank)
