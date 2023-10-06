import numpy as np

# Define the 2x2 matrix
matrix_2x2 = np.array([[4, 3],
                       [2, 1]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix_2x2)

# Display eigenvalues and eigenvectors
print("Eigenvalues of the 2x2 matrix:")
print(eigenvalues)
print("\nEigenvectors of the 2x2 matrix:")
print(eigenvectors)
matrix_3x3 = np.array([[4, 2, 1],
                       [3, 5, 2],
                       [1, 2, 3]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix_3x3)

# Display eigenvalues and eigenvectors
print("Eigenvalues of the 3x3 matrix:")
print(eigenvalues)
print("\nEigenvectors of the 3x3 matrix:")
print(eigenvectors)
