from setuptools import setup
# NOTE: necessary to import __version__
# exec(open("apple_heartrate_pandas/_version.py").read())

from os import path
with open(path.join(path.abspath(path.dirname(__file__)), "README.md")) as f:
    readme = f.read()

setup(
    name='apple_heartrate_pandas',
    version="0.1.6",
    license='MIT',
    url='https://github.com/LeonardoAlchieri/apple-heartrate-pandas',
    author='Leonardo Alchieri',
    author_email='leonardo@alchieri.eu',
    description='A Python package to convert Apple Health Heartrate in Pandas',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords=['apple', 'health', 'heartrate', 'pandas'],
    packages=['apple_heartrate_pandas'],
    # py_modules=['apple_heartrate_pandas'],
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