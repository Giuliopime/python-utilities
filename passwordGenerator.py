import string
import random
import itertools


def password_generator():
    """
        Creates a list with all the characters of the string we pass to the list() method
        I passed a string which contains:
        - ascii letters
        - digits
        - punctuation but only those who are common in most keyboard layouts (seen that I often switch keyboard layout)

        Then the list gets shuffled to randomize it
    """
    charList = list(f'{string.ascii_letters}{string.digits}{string.punctuation[0:25]}')
    random.shuffle(charList)

    # Chooses random characters from the list created before, and we join the obtained list with empty strings
    psw = random.choices(charList, k=random.randint(9, 13))
    return ''.join(psw)


for _ in itertools.repeat(None, 20):
    print(password_generator())
