from gettext import find

from setuptools import setup, find_packages

setup(
    name="ia32_python",
    version="1.0.1",
    description="x86-64 definitions for Python 2/3",
    author="guye1296",
    packages=find_packages(),
    url="https://github.com/guye1296/ia32-python",
    install_requires=["future"],
)