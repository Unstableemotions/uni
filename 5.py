import cv2
import numpy as np

# Load two images
image1 = cv2.imread('image.jpg')  # Replace 'image1.jpg' with your first image file
image2 = cv2.imread('image.jpg')  # Replace 'image2.jpg' with your second image file

# Check if the images were loaded successfully
if image1 is None or image2 is None:
    print("Error: Could not load one or both of the images.")
else:
    # Ensure both images have the same dimensions (resize if needed)
    if image1.shape != image2.shape:
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))  # Resize to match dimensions

    # Perform image operations
    # Addition (you can use cv2.add() or simply the + operator)
    addition_result = cv2.add(image1, image2)
    cv2.imshow('Image Addition', addition_result)

    # Subtraction (you can use cv2.subtract() or simply the - operator)
    subtraction_result = cv2.subtract(image1, image2)
    cv2.imshow('Image Subtraction', subtraction_result)

    # Multiplication (you can use cv2.multiply() or simply the * operator)
    multiplication_result = cv2.multiply(image1, image2)
    cv2.imshow('Image Multiplication', multiplication_result)

    # Save the resulting images (optional)
    cv2.imwrite('addition_result.jpg', addition_result)
    cv2.imwrite('subtraction_result.jpg', subtraction_result)
    cv2.imwrite('multiplication_result.jpg', multiplication_result)

    # Wait for a key press and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
