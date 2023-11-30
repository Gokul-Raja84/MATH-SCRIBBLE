import cv2
import numpy as np

def load_and_preprocess_image(image_path, target_size=(224, 224)):
    # Load image using OpenCV
    image = cv2.imread(image_path)
    
    # Resize image
    image = cv2.resize(image, target_size)
    
    # Convert BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Normalize pixel values to be between 0 and 1
    image = image / 255.0
    
    return image

def augment_image(image):
    # Example of image augmentation using OpenCV
    # You can customize this based on your requirements
    
    # Randomly apply horizontal flip
    if np.random.rand() < 0.5:
        image = cv2.flip(image, 1)
    
    # Randomly adjust brightness and contrast
    alpha = 1.0 + np.random.uniform(-0.2, 0.2)
    beta = np.random.uniform(-0.2, 0.2)
    image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    
    return image

def main():
    # Example usage
    image_path = 'path/to/your/image.jpg'
    target_size = (224, 224)
    
    # Load and preprocess a single image
    processed_image = load_and_preprocess_image(image_path, target_size)
    
    # Display the original and processed images
    cv2.imshow('Original Image', cv2.imread(image_path))
    cv2.imshow('Processed Image', cv2.cvtColor((processed_image * 255).astype(np.uint8), cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
