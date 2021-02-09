import pathlib

import setuptools

ROOT = pathlib.Path(__file__).parent

setuptools.setup(
    name="bottom",
    version="0.0.1",
    description="Pure python implementation of https://github.com/bottom-software-foundation/bottom-rs",
    url="https://github.com/bottom-software-foundation/bottom-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires=">=3.0",
)
