import os
from PIL import Image

# Load the image
image_path = "piece_4_2.png"  # Replace with your image path
image = Image.open(image_path)

# Create a new directory for the pieces
output_dir = image_path[:9] + "-" + "image_pieces"  # Replace with your desired directory name
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Get image dimensions
img_width, img_height = image.size
print(img_width, img_height)

# Number of vertical and horizontal splits
vertical_splits = 6
horizontal_splits = 5

# Calculate the dimensions of each piece
piece_width = img_width // vertical_splits
piece_height = img_height // horizontal_splits

# Split the image
for i in range(horizontal_splits):
    for j in range(vertical_splits):
        left = j * piece_width
        upper = i * piece_height
        right = (j + 1) * piece_width
        lower = (i + 1) * piece_height

        # Crop the image to create a piece
        piece = image.crop((left, upper, right, lower))

        # Save the piece with a unique name
        piece_path = os.path.join(output_dir, f"piece_{i + 1}_{j + 1}.png")
        # piece_path = f"piece_{i + 1}_{j + 1}.png"
        piece.save(piece_path, format="PNG", quality=100)

        print(f"Saved {piece_path}")
