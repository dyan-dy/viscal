from setuptools import setup, find_packages

setup(
    name="viscal",
    version="0.1.0",
    description="Scaling law visualization for model/data/compute",
    author="Dongyu",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "torch",
        "ptflops"
    ],
    python_requires=">=3.8",
)