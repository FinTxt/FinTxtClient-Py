# FinTxtClient

[![Project Status: Inactive – The project has reached a stable, usable state but is no longer being actively developed; support/maintenance will be provided as time allows.](http://www.repostatus.org/badges/latest/inactive.svg)](http://www.repostatus.org) [![lifecycle](https://img.shields.io/badge/lifecycle-stable-brightgreen.svg)](https://www.tidyverse.org/lifecycle/#stable)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg) [![Build Status](https://travis-ci.org/FinTxt/FinTxtClient-Py.svg?branch=master)](https://travis-ci.org/FinTxt/FinTxtClient-Py)

Python client to work with the FinTxt news intensities API.

## Installing

You can install the package by executing:

```bash
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
