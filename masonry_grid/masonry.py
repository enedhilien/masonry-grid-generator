import os
from PIL import Image
import argparse

def masonry_layout(images, num_columns):
    columns = [[] for _ in range(num_columns)]  # Create empty columns
    current_heights = [0] * num_columns  # Track column heights

    # Distribute images across columns
    for img in images:
        min_column_index = current_heights.index(min(current_heights))
        columns[min_column_index].append(img)
        current_heights[min_column_index] += img.size[1]

    return columns

def create_masonry_grid(input_dir, output_file, num_columns):
    image_files = sorted([img for img in os.listdir(input_dir) if img.endswith(('.png', '.jpg', '.jpeg'))])
    images = [Image.open(os.path.join(input_dir, img)) for img in image_files]
    
    total_width = max(img.width for img in images)
    column_width = total_width // num_columns

    resized_images = []
    for img in images:
        aspect_ratio = img.width / img.height
        new_width = column_width
        new_height = int(new_width / aspect_ratio)
        resized_images.append(img.resize((new_width, new_height)))

    columns = masonry_layout(resized_images, num_columns)
    total_height = max(sum(img.size[1] for img in column) for column in columns)
    final_img = Image.new('RGB', (total_width, total_height), (255, 255, 255))

    x_offset = 0
    for column in columns:
        y_offset = 0
        for img in column:
            centered_x_offset = x_offset + (column_width - img.size[0]) // 2
            final_img.paste(img, (centered_x_offset, y_offset))
            y_offset += img.size[1]
        x_offset += column_width

    final_img.save(output_file)
    print(f"Masonry grid saved as {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Generate a masonry grid image.")
    parser.add_argument('--input_dir', type=str, help='Directory containing images.')
    parser.add_argument('--output_file', type=str, help='Path to the output image file.')
    parser.add_argument('--num_columns', type=int, help='Number of columns in the grid.')

    args = parser.parse_args()
    create_masonry_grid(args.input_dir, args.output_file, args.num_columns)


if __name__ == "__main__":
    main()
