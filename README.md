[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.org/project/YoutubeScraper/)
[![PyPI version fury.io](https://badge.fury.io/py/ansicolortags.svg)](https://pypi.org/project/apple-heartrate-pandas/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pybadges.svg)](https://pypi.org/project/apple-heartrate-pandas/)

# apple-heartrate-pandas
Simple package to read as a pandas dataframe the heartrate from the Apple Watch.

## Requirements
For the moment, only pandas is required. Since in this package I make use of the `attrs` field in pandas, I suggest to install [my fork](https://github.com/LeonardoAlchieri/pandas/tree/attrs_in_parquet_metadata) to have those saved as well using `parquet` file format. However, if no interest in the `attrs`, just go for a standard Pandas installation.

For reference, in the `requirements.txt` file, I have put the installation link to my fork.

## Usage

Just do:
```python
from apple_heartrate_pandas import get_json_heartrate
```
to import the main module required. Once this is done, just feed the method a path to the json file, extracted with the [Auto Export](https://apps.apple.com/us/app/health-auto-export-json-csv/id1115567069) application on iOS, and you are done. 

@2022, Leonardo Alchieri

<sub>People-Centered Computing Lab - Università della Svizzera italiana, Switzerland</sub>
