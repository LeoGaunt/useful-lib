import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='usefullibrary',
    version='0.1.2',
    scripts=['usefullibrary'] ,
    author="Leo Gaunt",
    author_email="leogaunt05@outlook.com",
    description="A package containing scripts to help boost your python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LeoGaunt/usefullibrary",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)