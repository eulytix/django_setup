from setuptools import setup, find_packages

setup(
    name='setup',
    version='0.1.0',
    packages=find_packages(),  # Automatically find and include packages
    install_requires=["os", "sys"],  # List your dependencies here
    python_requires='>=3.9',  # Specify your supported Python versions
)
