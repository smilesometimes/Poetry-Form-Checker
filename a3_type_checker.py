import builtins

# Check for use of functions print and input.

our_print = print

def disable_print(*args):
    raise Exception("You must not call built-in function print!")

def disable_input(*args):
    raise Exception("You must not call built-in function input!")

builtins.print = disable_print
builtins.input = disable_input


import poetry_functions

# Type check poetry_functions.count_lines
result = poetry_functions.count_lines(['First line;\n', '\n', 'last line\n'])
assert isinstance(result, int), \
       '''poetry_functions.count_lines should return an int, but returned {0}
       .'''.format(type(result))

# Type check poetry_functions.get_poem_lines
result = poetry_functions.get_poem_lines('One,\ntwo,\nthree.\n')
assert isinstance(result, list), \
       '''poetry_functions.get_poem_lines should return a list, but returned {0}.''' \
       .format(type(result))
for item in result:
    assert isinstance(item, str), \
       '''poetry_functions.get_poem_lines should return a list of str,
        but returned a list of {0}.''' \
       .format(type(item))

# Set-up for the next two type checks.
poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
pattern = ([5, 7, 5], ['A', 'B', 'A'])
word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
                    'GAP': ['G', 'AE1', 'P'],
                    'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
                    'LEADS': ['L', 'IY1', 'D', 'Z'],
                    'WITH': ['W', 'IH1', 'DH'],
                    'LINE': ['L', 'AY1', 'N'],
                    'THEN': ['DH', 'EH1', 'N'],
                    'THE': ['DH', 'AH0'], 
                    'A': ['AH0'],
                    'FIRST': ['F', 'ER1', 'S', 'T'],
                    'ENDS': ['EH1', 'N', 'D', 'Z'],
                    'POEM': ['P', 'OW1', 'AH0', 'M'],
                    'OFF': ['AO1', 'F']}

# Type check poetry_functions.check_rhyme_scheme
result = poetry_functions.check_rhyme_scheme(poem_lines, pattern, word_to_phonemes)
assert isinstance(result, list), \
       '''poetry_functions.check_rhyme_scheme should return a list of list of str, but returned {0}.''' \
       .format(type(result))
for item in result:
    assert isinstance(item, list), \
       '''poetry_functions.check_rhyme_scheme should return a list of list of str,
        but returned a list of {0}.''' \
       .format(type(item))

# Type check poetry_functions.check_syllables
result = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
assert isinstance(result, list), \
       '''poetry_functions.check_syllables should return a list, but returned {0}.''' \
       .format(type(result))
for item in result:
    assert isinstance(item, str), \
       '''poetry_functions.check_syllables should return a list of str,
        but returned a list of {0}.''' \
       .format(type(item))


our_print("""

The type checker passed.

This means that the functions in poetry_functions.py:
- are named correctly,
- take the correct number of arguments, and
- return the correct types.  

This does NOT mean that the functions are correct!

Run the doctests to execute one test case per required poetry_functions.py function.

Be sure to thoroughly test your functions yourself before submitting.
""")


