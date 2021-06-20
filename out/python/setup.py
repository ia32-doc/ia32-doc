from setuptools import setup

setup(
    name="ia32_python",
    version="1.0",
    description="x86-64 definitions for Python 2/3",
    author="guye1296",
    packages=["ia32_python", "ia32_python.intel_manual"],
    install_requires=["future"],
)