import os
import argparse
from PIL import Image
from pillow_heif import register_heif_opener

def convert_heic_to_jpg(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    file_list = os.listdir(input_dir)

    for file_name in file_list:
        if file_name.lower().endswith('.heic'):
            heic_file = os.path.join(input_dir, file_name)
            with open(heic_file, 'rb') as f:
                register_heif_opener()
                image = Image.open(f)
                jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
                jpg_file_path = os.path.join(output_dir, jpg_file_name)
                image.save(jpg_file_path, 'JPEG')

                print(f"Converted {file_name} to {jpg_file_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert HEIC files to JPEG.")
    parser.add_argument("input_directory", help="Input directory containing HEIC files")
    parser.add_argument("output_directory", help="Output directory to save converted JPEG files")
    args = parser.parse_args()

    convert_heic_to_jpg(args.input_directory, args.output_directory)
