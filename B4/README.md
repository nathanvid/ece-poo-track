# B4 - Inheritance, encapsulation, packages

## Steps

| Step                                 | Notions                                                                      |
| ------------------------------------ | ---------------------------------------------------------------------------- |
| [09 Three kinds](E09_three_kinds.md) | inheritance, `super()`, polymorphism, abstract classes                       |
| [10 The admin](E10_admin.md)         | encapsulation, your own exceptions, `POST` `PUT` `DELETE`, bodies, a handler |
| [11 A real package](E11_package.md)  | `src/` layout, `pyproject.toml`, commands, a storage interface               |

Step 10 done before B5: the admin works. Step 11 can finish in B5.

## Side examples

Run them from the track folder, e.g.

```bash
uv run python B4/side/e09_messages.py
```

| File                                    | Shows                                                     |
| --------------------------------------- | --------------------------------------------------------- |
| [e09_messages.py](side/e09_messages.py) | emails, SMS, letters: an abstract cost, a factory by kind |
| [e10_bank.py](side/e10_bank.py)         | an account nobody can cheat, a family of errors           |
| [e10_bank_api.py](side/e10_bank_api.py) | write routes, bodies, errors turned into statuses         |
| [e11_storage.py](side/e11_storage.py)   | one interface, a JSON storage and a memory storage        |

## Practice repository

Optional, for more practice: `B4/examples`, `B4/packaging.md`, `B5/examples/03_bodies_errors.ipynb`, exercises `B4/exercises/01` to `04`, `B5/exercises/02_bodies_errors`.
