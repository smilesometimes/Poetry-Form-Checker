import poetry_functions
import poetry_reader
import os.path

DICTIONARY_FILENAME = 'txt\dictionary.txt'
POETRY_FORMS_FILENAME = 'txt\poetry_forms.txt'

"""
A poetry pattern:  tuple of (list of int, list of str)
  - first item is a list of the number of syllables required in each line
  - second item is a list describing the rhyme scheme rule for each line
"""

"""
A pronunciation dictionary: dict of {str: list of str}
  - each key is a word (a str)
  - each value is a list of phonemes for that word (a list of str)
"""

def get_valid_filename(msg):
    """ (str) -> str

    Prompt the user, using msg, to type the name of a file. This file should 
    exist in the same directory as the starter code. If the file does not
    exist, keep prompting until they give a valid filename.
    Return the name of that file.
    """

    filename = input(msg)
    while not os.path.exists(filename):
        print("That file does not exist.")
        filename = input(msg)
    return filename


def make_menu(poetry_forms):
    r""" (dict of {str: poetry pattern}) -> tuple of (str, dict of {str: str})

    Return a numbered menu of the poetry form names that are keys in
    poetry_forms.

    >>> d = {'Haiku': ([5, 7, 5], ['*', '*', '*']),
    ...         'Unknown': ([1, 2, 3], ['A', 'B', 'C'])}
    >>> menu = make_menu(d)
    >>> menu == ('1: Haiku\n2: Unknown\n', {'1': 'Haiku', '2': 'Unknown'})
    True
    """

    menu = ''
    menu_dict = {}

    # Sort the names so that they appear in alphabetical order in the menu.
    form_names = list(poetry_forms.keys())
    form_names.sort()

    i = 1
    for form_name in form_names:
        menu += '{}: {}\n'.format(i, form_name)
        menu_dict[str(i)] = form_name
        i += 1

    return menu, menu_dict


def check_poem(poem_lines, pattern, word_to_phonemes, form_name):
    """ (list of str, poetry pattern, pronunciation dictionary, str) -> NoneType

    Check whether the poem in poem_lines has the right number of lines to
    match for form given in pattern, and print a message if it doesn't.
    If it does, then check whether the lines in the poem have the right number
    of syllables and report the lines that don't; also check whether the 
    lines of the poem have the correct rhyming scheme and report the lines
    that should rhyme but don't.
    """

    if poetry_functions.count_lines(poem_lines) != len(pattern[0]):
        print("\n== The poem doesn't have the right number of lines. == \n")
    else:
        problem_lines = poetry_functions.check_syllables(
            poem_lines, pattern, word_to_phonemes)

        if len(problem_lines) == 0:
            print('\nThe poem has the right number of syllables on each line.\n')
        else:
            print('\n== The poem is not a {}. These lines don\'t have the '
                  'right number of syllables: == '.format(form_name))
            print('\n'.join(problem_lines) + '\n')

        problem_rhymes = poetry_functions.check_rhyme_scheme(
            poem_lines, pattern, word_to_phonemes)

        if len(problem_rhymes) == 0:
            print('The poem follows the rhyme scheme.\n')
        else:
            print('\n== The poem is not a {}. These lines should rhyme'
                " but don't: ==".format(form_name))
            for lines in problem_rhymes:
                print('\n'.join(lines) + '\n')


def main():
    word_to_phonemes = poetry_reader.read_pronunciation(
        open(DICTIONARY_FILENAME))
    name_to_poetry_pattern = poetry_reader.read_poetry_form_descriptions(
        open(POETRY_FORMS_FILENAME))

    menu, menu_dict = make_menu(name_to_poetry_pattern)
    print('=================================================')
    prompt = \
    'Enter number for poetry form to check (0 to quit):\n{}'.format(menu)
    form_num = input(prompt)

    while form_num != '' and form_num != '0':
        if form_num in menu_dict.keys():
            form_name = menu_dict[form_num]
            poetry_pattern = name_to_poetry_pattern[form_name]

            poem_filename = get_valid_filename("Enter a poem filename: ")
            poem_file = open(poem_filename)
            poem = poem_file.read()
            poem_lines = poetry_functions.get_poem_lines(poem)

            check_poem(poem_lines, poetry_pattern, word_to_phonemes, form_name)

            print('=================================================')
            form_num = input(prompt)
        else:
            form_num = input('Invalid number. ' + prompt)


if __name__ == '__main__':
    main()
