# |---------------------------------IMPORTS---------------------------------|

import sys

# |---------------------------------OPEN---------------------------------|

'''Palindromes are words that are the same forwards as reversed
This program opens a text file, strips whitespace, and splits based on new-line
Then it iterates over a list using a comprehension to check if a word
is the same forward as it is reversed using string slicing'''


def load_file():
    fname = '2of4brif.txt'

    try:
        with open(fname) as file:
            loaded_txt = file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            palindromes =set ([x for x in loaded_txt if x == x[::-1]])
            print(palindromes)
            return loaded_txt, palindromes
    except IOError as e:
        print(f'\nError opening {fname}. Terminating program.')
        sys.exit(1)

# |---------------------------------MAIN---------------------------------|
if __name__ == '__main__':
    load_file()
