# pywc
Custom implementation for the Unix `wc` (word count) utility, written in Python.

**Project**
- **Description**: Custom Python reimplementation of the `wc` utility. Counts lines, words, bytes and multibyte characters from files or standard input.
- **Author**: Alexandru Prodan

**Features**
- **Lines**: `-l` — count newline characters.
- **Words**: `-w` — count words (split by whitespace after decoding).
- **Bytes**: `-c` — count raw bytes.
- **Characters**: `-m` — count characters after decoding according to locale.
- **Default behavior**: when no flags are provided the program prints lines, words and bytes (in that order).

**Requirements**
- **Python**: `^3.10` (see `pyproject.toml`).

**Installation**
- Using Poetry:

	`poetry install`

- Or with pip (editable install for development):

	`pip install -e .`

**Usage**
- Run against a file:

	`python pywc/main.py [options] [path]`

- Read from standard input (no path):

	`cat data/test.txt | python pywc/main.py -w`

- Options:
	- **`-l`**: number of lines
	- **`-w`**: number of words
	- **`-c`**: number of bytes
	- **`-m`**: number of characters (multibyte-aware, uses locale decoding)

- Output format:
	- When a file `path` is provided the program prints counts separated by tabs and appends the file path as the last column.
	- When reading from `stdin` (no `path`) the path column is omitted.

	Example (default behavior, no flags):

	`python pywc/main.py data/test.txt`

	Output format: `LINES\tWORDS\tBYTES\t/path/to/data/test.txt`

	Example (specific flags):

	`python pywc/main.py -l -w data/test.txt`

	Output format: `LINES\tWORDS\t/path/to/data/test.txt`

**Running Tests**
- Run the test suite with `pytest`:

	`pytest -q`

**Repository layout**
- `pywc/` : package source (main implementation is `pywc/main.py`).
- `tests/` : unit tests (uses `pytest`).
- `data/` : example/test data files.

**Contributing**
- Contributions are welcome. Please open issues or pull requests. Follow standard GitHub workflow and keep changes focused and small.

**License**
- See the `LICENSE` file in the repository root.
