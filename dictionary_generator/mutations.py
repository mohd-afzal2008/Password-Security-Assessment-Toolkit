import itertools


def leetspeak(word):
    table = {
        "a": "4",
        "e": "3",
        "i": "1",
        "o": "0",
        "s": "5",
        "t": "7"
    }

    result = word

    for letter, value in table.items():
        result = result.replace(letter, value)

    return result


def generate_mutations(word):

    passwords = set()

    passwords.add(word.lower())
    passwords.add(word.upper())
    passwords.add(word.capitalize())

    passwords.add(word + "123")
    passwords.add(word + "1234")
    passwords.add(word + "@123")
    passwords.add(word + "786")
    passwords.add(word + "2026")

    passwords.add(leetspeak(word.lower()))

    return sorted(passwords)

