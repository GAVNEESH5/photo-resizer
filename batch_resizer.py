from PIL import Image
import os

def resize_all_images(folder, width, height):
    """Resize all images in a folder"""
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            input_path = os.path.join(folder, filename)
            name, ext = os.path.splitext(filename)
            output_path = os.path.join(folder, f"{name}_resized{ext}")
            
            with Image.open(input_path) as img:
                resized = img.resize((width, height), Image.Resampling.LANCZOS)
                resized.save(output_path)
                print(f"Resized: {filename}")

# Usage
if __name__ == "__main__":
    folder = input("Enter folder path: ")
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    
    resize_all_images(folder, width, height)
    print("All images resized!")
