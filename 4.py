import cv2
import numpy as np

# Load an image
image_path = "image.jpg"  # Replace with the path to your image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Display the original image
    cv2.imshow("Original Image", image)
    
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", grayscale_image)
    
    # Resize the image
    resized_image = cv2.resize(image, (400, 300))  # Adjust the size as needed
    cv2.imshow("Resized Image", resized_image)
    
    # Rotate the image by 90 degrees
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("Rotated Image", rotated_image)
    
    # Flip the image horizontally
    flipped_image = cv2.flip(image, 1)
    cv2.imshow("Flipped Image", flipped_image)
    
    # Save the transformed image
    cv2.imwrite("transformed_image.jpg", flipped_image)
    
    # Wait for a key press and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
