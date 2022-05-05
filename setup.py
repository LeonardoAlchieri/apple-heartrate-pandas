from setuptools import setup
# NOTE: necessary to import __version__
from sys import path
from pathlib import Path
path.append(str(Path(__file__).parent))
from apple_heartrate_pandas import __version__

setup(
    name='apple_heartrate_pandas',
    version=__version__,
    license='MIT',
    url='https://github.com/LeonardoAlchieri/apple-heartrate-pandas',
    author='Leonardo Alchieri',
    author_email='leonardo@alchieri.eu',
    description='A Python package to convert Apple Health Heartbate in Pandas',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords=['apple', 'health', 'heartrate', 'pandas'],
    py_modules=['apple_heartrate_pandas'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces"
    ],
    python_requires=">=3.7",
    install_requires=[
    'pandas; python_version>="3.7"',
]
)