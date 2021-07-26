import pathlib
from setuptools import setup

HERE: pathlib.Path = pathlib.Path(__file__).parent
README: str = (HERE / "README.md").read_text()

setup(
    name="sublinput",
    version="1.0.0",
    description="An input pygame alternative for sublime text users.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Sigmanificient/pg-sublime-input",
    author="Sigmanificient",
    author_email="Edhyjox@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["sublinput"],
    include_package_data=True,
    install_requires=[]
)
