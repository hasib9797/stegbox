# StegBox

**StegBox** is a versatile and robust CLI tool designed for embedding and extracting files in images using steganography. With StegBox, you can securely hide any type of file within an image, ensuring that your sensitive information remains concealed until needed.

## Features

- **Embed Files:** Effortlessly hide various file types within an image.
- **Password Protection:** Secure your embedded files with a strong password.
- **File Extraction:** Retrieve and extract hidden files using the correct password.
- **Cross-Platform:** Works seamlessly on various operating systems, including Ubuntu.

## Installation

To install StegBox, use the following command:

```sh
pip install stegbox
```

## Usage

### Embedding a File

To embed a file into an image:

```sh
stegbox embed -i input_image.png -f file_to_embed.txt -p your_password
```

If you don't provide a password in the command, you will be prompted to enter it:

```sh
stegbox embed -i input_image.png -f file_to_embed.txt
```

### Extracting a File

To extract a file from an image:

```sh
stegbox extract -i output_image.png -p your_password
```

If you don't provide a password in the command, you will be prompted to enter it:

```sh
stegbox extract -i output_image.png
```

## How It Works

StegBox uses steganography to hide files within the least significant bits of an image's pixels. The process involves the following steps:

1. **Read the Image:** Load the image into memory.
2. **Read the File:** Load the file to be embedded.
3. **Password Hashing:** Hash the password using SHA-256 for security.
4. **Combine Data:** Combine the hashed password, file name, and file data into a single bit array.
5. **Embed Data:** Embed the bit array into the image's pixel data.
6. **Save Image:** Save the modified image with the embedded file.
7. **Extract Data:** Extract the embedded file using the correct password.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to reach out:

**Author:** Hasib  
**Email:** [hasib69780@gmail.com](mailto:hasib69780@gmail.com)  
**GitHub:** [hasib9797](https://github.com/hasib9797/stegbox)