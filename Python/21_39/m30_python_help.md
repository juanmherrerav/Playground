# Como usar la ayuda de Python

1. invocar python

```bash
python
```

1.1. invocar ayuda de comando print

```python
help(print)
```

1.2. invocar ayuda de comando, por ejemplo "open"

```python
help(open)
```

1.3 Generar ayuda con el DocString

```python
def my_function(input:str)-> int:
    """[summary]

    Args:
        input (str): [description]

    Returns:
        int: [description]
    """
    try:
        return int(input)
    except ValueError as e:
        print(f"The input '{input}' is not a number, the error is '{e}'")
    finally:
        print("Finally")
```
