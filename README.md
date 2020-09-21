# dict-ops
A simple, but high-powered, module for operation on dictionaries

### Examples
`dict-ops` exposes three functions: `diff`, `put`, and `cut`, 
best explained by example:

```python
from dict_ops import diff, put, cut

d1 = {"foo": 1, "bar": 1}
d2 = {"foo": 2, "baz": 2}

diff(d1, d2)
{'bar': 1}

put(d1, d2)
{'foo': 2, 'baz': 2, 'bar': 1}

cut(d1, d2)
{'baz': 2}
```

Those are neat examples, but the functions are arbitrarily
composable, allowing for sophisticated transformations with
very little effort. Let's say we have a stream of records
(dicts) headed our way. We also know we need those records
to have an identical set of keys on the other side of our
pipeline. Here's how we can do that:

```python
from dict_ops import diff, put, cut

template = {
    "foo": 0,
    "bar": "",
    "baz": 0.0
}

record = {
    "foo": 42,
    "bar": "ni",
    "qux": True
}

# which fields need to be removed?
diff(record, template)
{'qux': True}

# which fields do we need to add?
diff(template, record)
{'baz': 0.0}

# fix it with a one-liner!
put(diff(template, record), cut(diff(record, template), record))
{'foo': 42, 'bar': 'ni', 'baz': 0.0}

# we could actually make it shorter by just letting
# `put` skip existing fields in `template`
put(template, cut(diff(record, template), record))
{'foo': 42, 'bar': 'ni', 'baz': 0.0}
```

Let's do something else:

```python
from dict_ops import diff, put, cut

template = {
    "foo": None,
    "bar": None,
    "baz": None
}

messy_array = {
    "foo": [
        {"foo": 1},
        {"bar": 2},
        {"foo": 3, "bar": 3, "qux": 3}
    ]
}

fixer = lambda d1: put(template, cut(diff(d1, template), d1))

messy_array["foo"] = list(map(fixer, messy_array.get("foo")))
messy_array
messy_array = {
    "foo": [
        {'foo': [{'foo': 1, 'bar': None, 'baz': None},
        {'bar': 2, 'foo': None, 'baz': None},
        {'foo': 3, 'bar': 3, 'baz': None}]}
    ]
}
```
