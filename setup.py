import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='useful-lib',
     version='0.1',
     scripts=['useful-lib'] ,
     author="Leo Gaunt",
     author_email="leogaunt05@outlook.com",
     description="A package containing scripts to help boost your python",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/LeoGaunt/useful-lib",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )