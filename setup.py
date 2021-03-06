from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    required = f.read().splitlines()

setup(
    name="simple-einet",
    version="0.0.1",
    author="Steven Lang",
    packages=find_packages(include=['simple_einet', 'simple_einet.*']),
    install_requires=required,
    long_description=long_description,
)
