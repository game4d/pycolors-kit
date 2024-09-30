# **pycolors-kit**
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

## Description

Search for color names through HEX, or search for color information through names

## Installation

Install `pycolors-kit` into your python environment, using:

```shell
pip install pycolors-kit
```

After installing, you can use the project as follows:

## Example

```python
from pycolors_kit import ColorEx


def test():
    color = ColorEx()

    print(color.get_name_by_hex('#fe9956'))
    print(color.get_color_by_name('acapulco sun'))


if __name__ == '__main__':
    test()
```

***