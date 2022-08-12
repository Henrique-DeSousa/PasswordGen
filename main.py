import random
import secrets

from string import ascii_letters, digits, punctuation

size = 30


def pass1():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special = "!£$%^&*()_+=-@}{'#|/\~?><,.¬`¦[]:;€" + "'" + '"'
    all = lower + upper + numbers + special
    password = "".join(random.sample(all, size))
    print("Password 1: ", password)


def pass2():
    chars = ascii_letters + digits + punctuation
    password = ''.join(secrets.choice(chars) for i in range(size))
    print("Password 2: ", password)


class main:
    pass1()
