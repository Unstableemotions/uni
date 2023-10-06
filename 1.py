import numpy as np
import matplotlib.pyplot as plt

# Define two complex numbers
z1 = 3 + 2j
z2 = -1 - 4j

# a. Addition of two complex numbers
sum_result = z1 + z2
print(f"a. Addition of {z1} and {z2} = {sum_result}")

# b. Displaying the conjugate of a complex number
conjugate_result = np.conjugate(z1)
print(f"b. Conjugate of {z1} = {conjugate_result}")

# c. Plotting a set of complex numbers
complex_numbers = [2 + 3j, -1 - 2j, 4 - 1j, -2 + 5j]
real_parts = [z.real for z in complex_numbers]
imaginary_parts = [z.imag for z in complex_numbers]

plt.figure(figsize=(8, 6))
plt.scatter(real_parts, imaginary_parts, color='blue', marker='o')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Complex Numbers Plot')
plt.grid(True)
plt.show()

# d. Creating a new plot by rotating and scaling
angles = [90, 180, 270]
scales = [1/2, 1/3, 2]

for angle in angles:
    for scale in scales:
        rotated_scaled = scale * (np.exp(1j * np.radians(angle)) * z1)
        real_part = rotated_scaled.real
        imaginary_part = rotated_scaled.imag
        plt.figure(figsize=(4, 4))
        plt.scatter(real_part, imaginary_part, color='red', marker='o')
        plt.xlim(-5, 5)
        plt.ylim(-5, 5)
        plt.xlabel('Real Part')
        plt.ylabel('Imaginary Part')
        plt.title(f'Rotated and Scaled Complex Number ({angle} degrees, a={scale})')
        plt.grid(True)
        plt.show()
