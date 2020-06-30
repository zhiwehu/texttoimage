import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="texttoimage", # Replace with your own username
    version="0.0.1",
    author="Jeffrey Hu",
    author_email="zhiwehu@gmail.com",
    description="A package which can convert text to image.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhiwehu/texttoimage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['Pillow'],
    python_requires='>=3.6',
)