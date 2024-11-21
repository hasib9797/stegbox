import os
import argparse
from PIL import Image
from bitarray import bitarray
import hashlib
import getpass

def embed_file_into_image(image_path, file_path, password):
    output_dir = "stegbox_output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_path = os.path.join(output_dir, os.path.basename(image_path))
    
    image = Image.open(image_path)
    image = image.copy()
    pixels = image.load()

    with open(file_path, 'rb') as file:
        file_data = file.read()
    file_name = os.path.basename(file_path).encode()

    password_hash = hashlib.sha256(password.encode()).digest()
    password_bits = bitarray()
    password_bits.frombytes(password_hash)

    file_bits = bitarray()
    file_bits.frombytes(file_data)
    name_bits = bitarray()
    name_bits.frombytes(file_name)

    bits = password_bits + name_bits + bitarray('00000000') + file_bits

    width, height = image.size
    data_index = 0
    for y in range(height):
        for x in range(width):
            if data_index < len(bits):
                r, g, b = pixels[x, y]
                r = (r & 0xFE) | bits[data_index]
                data_index += 1
                if data_index < len(bits):
                    g = (g & 0xFE) | bits[data_index]
                    data_index += 1
                if data_index < len(bits):
                    b = (b & 0xFE) | bits[data_index]
                    data_index += 1
                pixels[x, y] = (r, g, b)

    image.save(output_path)
    print(f"File embedded into image {output_path}")

def extract_file_from_image(image_path, password):
    image = Image.open(image_path)
    pixels = image.load()

    password_hash = hashlib.sha256(password.encode()).digest()
    password_bits = bitarray()
    password_bits.frombytes(password_hash)

    bits = bitarray()
    width, height = image.size
    data_index = 0
    for y in range(height):
        for x in range(width):
            if data_index < width * height * 3:
                r, g, b = pixels[x, y]
                bits.append(r & 0x01)
                data_index += 1
                if data_index < width * height * 3:
                    bits.append(g & 0x01)
                    data_index += 1
                if data_index < width * height * 3:
                    bits.append(b & 0x01)
                    data_index += 1

    extracted_password_bits = bits[:256]
    if extracted_password_bits != password_bits:
        raise ValueError("Incorrect password")

    name_bits = bits[256:]
    null_byte_index = name_bits.index(bitarray('00000000'))
    file_name = name_bits[:null_byte_index].tobytes().decode()
    file_data_bits = name_bits[null_byte_index + 8:]

    file_data = file_data_bits.tobytes()

    with open(file_name, 'wb') as file:
        file.write(file_data)
    print(f"File extracted to {file_name}")

def main():
    parser = argparse.ArgumentParser(description="Embed and extract files in images using steganography.")
    subparsers = parser.add_subparsers(dest='command', required=True)

    embed_parser = subparsers.add_parser('embed', help='Embed a file into an image.')
    embed_parser.add_argument('-i', '--image', required=True, help='Path to the input image.')
    embed_parser.add_argument('-f', '--file', required=True, help='Path to the file to be embedded.')
    embed_parser.add_argument('-p', '--password', help='Password for embedding the file.')

    extract_parser = subparsers.add_parser('extract', help='Extract a file from an image.')
    extract_parser.add_argument('-i', '--image', required=True, help='Path to the image containing the embedded file.')
    extract_parser.add_argument('-p', '--password', help='Password for extracting the file.')

    args = parser.parse_args()

    if args.command == 'embed':
        password = args.password if args.password else getpass.getpass("Enter password: ")
        embed_file_into_image(args.image, args.file, password)
    elif args.command == 'extract':
        password = args.password if args.password else getpass.getpass("Enter password: ")
        extract_file_from_image(args.image, password)

if __name__ == "__main__":
    main()
