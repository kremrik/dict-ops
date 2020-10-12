# map-ops
![Python package](https://github.com/kremrik/map-ops/workflows/Python%20package/badge.svg)
![coverage](images/coverage.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A simple, but high-powered, module for operating on dictionaries

### Installation
Currently either installable from source, or by pip installing from github:
```
python -m pip install git+https://github.com/kremrik/map-ops.git
```

### Examples
For comprehensive examples, please read the [docs](https://kremrik.github.io/map-ops/)

```python
from map_ops.operations import cut, diff, put

d1 = {"foo": 1, "bar": 1}
d2 = {"foo": 2, "baz": 2}

diff(d1, d2)
{"bar": 1}

put(d1, d2)
{"foo": 2, "baz": 2, "bar": 1}

cut(d1, d2)
{"baz": 2}
```
