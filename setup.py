import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='georeference-image-library',
    version='0.0.1',
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/lazyspot/georeference-image-library',
    license='',
    author='LazySpot',
    author_email='marcin@lazyspot.net',
    description='Library for georeference image.',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
	packages=['os'],
)
