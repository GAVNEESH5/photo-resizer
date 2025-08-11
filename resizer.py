import os
from PIL import Image

def resize_images(input_folder, output_folder, width, height, keep_aspect=True):
    """Simple function to resize all images in a folder"""
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Supported image extensions
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif')
    
    # Process each image file
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(image_extensions):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"resized_{filename}")
            
            try:
                with Image.open(input_path) as img:
                    if keep_aspect:
                        # Keep aspect ratio
                        img.thumbnail((width, height), Image.Resampling.LANCZOS)
                    else:
                        # Exact dimensions
                        img = img.resize((width, height), Image.Resampling.LANCZOS)
                    
                    img.save(output_path)
                    print(f"Resized: {filename}")
                    
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    # Simple usage
    input_folder = input("Enter input folder path: ")
    output_folder = input("Enter output folder path: ")
    width = int(input("Enter width (e.g., 800): "))
    height = int(input("Enter height (e.g., 600): "))
    keep_aspect = input("Keep aspect ratio? (y/n): ").lower() == 'y'
    
    resize_images(input_folder, output_folder, width, height, keep_aspect)
    print("Done! Check your output folder.")
