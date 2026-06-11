# SampleRepo
### Boston University #### author craman
This repository contains a few basic Python and R scripts, plus unit tests.

## Scripts

The scripts live in `./scripts`:

- `add_numbers.R`: adds two numbers
- `string_reverse.R`: reverses text
- `is_even.R`: checks if an integer is even
- `add_numbers.py`: adds two numbers
- `string_reverse.py`: reverses a string
- `is_even.py`: checks if an integer is even
- Adding an extra line


## How to run the scripts

From the repository root, execute:

```bash
python scripts/add_numbers.py 8 9
python scripts/string_reverse.py hello
python scripts/is_even.py 8
```

To run the R versions:

```bash
Rscript scripts/add_numbers.R 20 21
Rscript scripts/string_reverse.R hello
Rscript scripts/is_even.R 8
```

## Run unit tests

```bash
python -m unittest discover -s tests -q
```
