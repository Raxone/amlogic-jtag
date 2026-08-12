# Amlogic aml_pwdefs Hash Generator

Python implementation of the Amlogic `amlpwdefs` password hashing algorithm.

The implementation generates a 32-byte hash from a password and a 4-byte salt using 32 iterations of SHA-224.

## Features

- SHA-224 based hashing
- 32 iterations
- 4-byte salt
- Password length: 4–16 bytes
- 48-byte SHA-224 input block
- 32-byte final result
- Python 3
- No external dependencies

## Requirements

- Python 3.x

The script uses only Python's standard library.

## Usage

```bash
python3 amlpwdefs.py -p PASSWORD -s SALT
