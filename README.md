# FinTxtClient

[![Project Status: Inactive – The project has reached a stable, usable state but is no longer being actively developed; support/maintenance will be provided as time allows.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active) [![lifecycle](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://www.tidyverse.org/lifecycle/#experimental)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)

Python client to work with the FinTxt news intensities API.

## Installing

You can install the package by executing:

```python
pip install git+https://github.com/FinTxt/FinTxtClient-Py.git --user
```

## Basics

Import the package using

```python
from FinTxtClient import FinTxtClient
```

Initiate the client by executing

```python
client = FinTxtClient()
```

If you have a key, make sure to add it to the client:

```python
client = FinTxtClient(key='<yourkey>')
```

See the [documentation](https://fintxt.github.io/documentation/theapi.html) for more information.

// TODO: add travis

// TODO: add codecov

// TODO: add unit tests
