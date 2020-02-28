import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iot-processor",
    version="0.0.1",
    author="Mark Bernardinis",
    author_email="mark@mtnsconsulting.com",
    description="IOT Processor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bernarma/pypi-fitness-broker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)