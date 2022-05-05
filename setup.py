from setuptools import setup

from apple_heartrate_pandas import __version__

setup(
    name='apple-heartrate-pandas',
    version=__version__,

    url='https://github.com/LeonardoAlchieri/apple-heartrate-pandas',
    author='Leonardo Alchieri',
    author_email='leonardo@alchieri.eu',

    py_modules=['apple_heartrate_pandas'],
    install_requires=[
    'pandas; python_version>="3.7"',
]
)