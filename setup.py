from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='georeference-image-library',
    version='0.0.1',
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/lazyspot/georeference-image-library',
    license='',
    author='LazySpot',
    author_email='',
    description='',
)
