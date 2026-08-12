#!/usr/bin/env python3

import hashlib
import argparse
import sys


def amlpwdefs(password: bytes, salt: bytes) -> bytes:
    if not (4 <= len(password) <= 16):
        raise ValueError("password must be 4-16 bytes")

    if len(salt) != 4:
        raise ValueError("salt must be exactly 4 bytes")

    # H0
    h = bytearray(32)
    h[28:32] = salt

    # Constant block portion
    block = bytearray(48)
    block[28:28 + len(password)] = password
    block[28 + len(password):28 + len(password) + 4] = salt

    # 32 SHA-224 iterations
    for _ in range(32):
        block[0:28] = h[0:28]

        d = hashlib.sha224(block).digest()

        h[0:28] = d
        h[28:32] = salt

    return bytes(h)


def main():
    parser = argparse.ArgumentParser(
        description="Amlogic aml_pwdefs password hash generator"
    )

    parser.add_argument(
        "-p", "--password",
        required=True,
        help="Password (4-16 characters)"
    )

    parser.add_argument(
        "-s", "--salt",
        required=True,
        help="Salt (exactly 4 characters)"
    )

    args = parser.parse_args()

    password = args.password.encode("ascii")
    salt = args.salt.encode("ascii")

    try:
        h = amlpwdefs(password, salt)
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)

    print("Password :", args.password)
    print("Salt     :", args.salt)
    print("Hash     :")
    print(" ".join(f"{b:02X}" for b in h))


if __name__ == "__main__":
    main()
