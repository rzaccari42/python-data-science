# ft_package

A small Python package for Exercise 09 of the 42 Python for Data Science Piscine. It provides `count_in_list`, which returns how many times a value appears in a list.

## Usage

```python
from ft_package import count_in_list

items = ["toto", "tata", "toto"]

print(count_in_list(items, "toto"))  # 2
print(count_in_list(items, "tutu"))  # 0
```

## Build and install

With your virtual environment active, run these commands from the directory containing `pyproject.toml`:

```bash
python -m pip install build
python -m build
python -m pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

To install from the source archive instead, run:

```bash
python -m pip install ./dist/ft_package-0.0.1.tar.gz
```

## License

MIT. See [LICENSE](LICENSE).

