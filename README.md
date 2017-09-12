# Memunit

[![Build Status](https://travis-ci.org/mschwager/memunit.svg?branch=master)](https://travis-ci.org/mschwager/memunit)
[![Coverage Status](https://coveralls.io/repos/github/mschwager/memunit/badge.svg?branch=master)](https://coveralls.io/github/mschwager/memunit?branch=master)
[![Python Versions](https://img.shields.io/pypi/pyversions/memunit.svg)](https://img.shields.io/pypi/pyversions/memunit.svg)
[![PyPI Version](https://img.shields.io/pypi/v/memunit.svg)](https://img.shields.io/pypi/v/memunit.svg)

`Memunit` is a testing library for ensuring memory usage levels in Python.

# Installing

```
$ pip install memunit
```

# Using

`Memunit` can easily be added to existing tests via a decorator:

```python
#!/usr/bin/env python

import unittest

import memunit


class TestMemunit(unittest.TestCase):

    @memunit.assert_lt_mb(35)
    def test_low_memory_usage(self):
        data = [str(i) for i in range(10)]

        self.assertTrue(data)

    @memunit.assert_lt_mb(35)
    def test_high_memory_usage(self):
        data = [str(i) for i in range(100000)]

        self.assertTrue(data)


if __name__ == "__main__":
    unittest.main()
```

Code with poor memory performance can be protected against:

```
$ python profile.py
E.
======================================================================
ERROR: test_high_memory_usage (__main__.TestMemunit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/matt/documents/memunit/lib/memunit.py", line 27, in wrapper
    raise MemoryUsageException(failure_message.format(max_usage))
MemoryUsageException: Max usage 39.88Mb >= 35Mb

----------------------------------------------------------------------
Ran 2 tests in 0.108s

FAILED (errors=1)
```

`memunit.assert_mb` can be used to determine a memory usage baseline:

```
======================================================================
ERROR: test_memory_usage (__main__.TestMemunit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/matt/documents/memunit/lib/memunit.py", line 27, in wrapper
    raise MemoryUsageException(failure_message.format(max_usage))
MemoryUsageException: Max usage 40.14

----------------------------------------------------------------------
Ran 1 test in 0.072s

FAILED (errors=1)
```

# Developing

First, clone the repository and install the required packages:

```
$ git clone https://github.com/mschwager/memunit.git
$ cd memunit
$ pip install -r requirements.txt
$ pip install -r requirements-dev.txt
```

## Testing

```
$ nose2 --with-coverage
```

## Linting

```
$ flake8
```
