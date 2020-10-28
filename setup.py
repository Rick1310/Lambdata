import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

    REQUIRED = ["numpy", "pandas"]

setuptools.setup(
    name="lambdata_rick1310", # Replace with your own username
    version="0.0.1",
    author="Rick1310",
    author_email="author@example.com",
    description="Collection of DS functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rick1310/Lambdata",
    packages=setuptools.find_packages(),
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)