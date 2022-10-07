# Example Package

This is a simple example package based on [this tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

```
python build
```

```
twine upload --repository testpypi dist/*
```

After installing the package using pip
e.g.

```
pip install dist/example_package_szabgab-0.0.1-py3-none-any.whl
```

I can

```
from example_package_szabgab.example import add_one
add_one(1)
```


* [hatchling](https://hatch.pypa.io/latest/)

pip install hatch

```
hatch build
```
