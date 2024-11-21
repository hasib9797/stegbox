from setuptools import setup

setup(
    name="stegbox",
    version="1.0",
    py_modules=['stegbox'],
    install_requires=[
        "Pillow",
        "bitarray",
    ],
    entry_points={
        'console_scripts': [
            'stegbox=stegbox:main',
        ],
    },
    author="Hasib",
    author_email="hasib69780@gmail.com",
    description="A CLI tool for embedding and extracting files in images using steganography",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/hasib9797/stegbox",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
