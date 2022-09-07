from setuptools import setup

setup(
    name="Stirge",
    version="1.0",
    author="Melano",
    url="https://github.com/1b0325h/Stirge",
    license="MIT",
    py_modules=["stirge"],
    install_requires=[
        "colorama==0.4.3",
        "fire==0.4.0"],
    entry_points={"console_scripts": ["stirge = stirge:main"]})
