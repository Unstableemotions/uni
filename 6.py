import numpy as np
import matplotlib.pyplot as plt

# Define the complex number
z = complex(3, 2)  # Replace with your own complex number

# Perform rotations
rotated_90 = z * 1j
rotated_180 = z * (-1)
rotated_270 = z * (-1j)

# Create a plot for each rotation
plt.figure(figsize=(12, 4))

# Original complex number
plt.subplot(131)
plt.plot(z.real, z.imag, 'ro')
plt.title('Original Complex Number')

# Rotated by 90 degrees
plt.subplot(132)
plt.plot(rotated_90.real, rotated_90.imag, 'go')
plt.title('Rotated 90 Degrees')

# Rotated by 180 degrees
plt.subplot(133)
plt.plot(rotated_180.real, rotated_180.imag, 'bo')
plt.title('Rotated 180 Degrees')

# Add spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()
