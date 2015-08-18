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

# ===================== Helper Functions =====================

def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to uppercase and punctuation characters have been stripped
    from both ends. Inner punctuation is left untouched.

    >>> clean_up('Birthday!!!')
    'BIRTHDAY'
    >>> clean_up('"Quoted?"')
    'QUOTED'
    """

    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r"""
    result = s.upper().strip(punctuation)
    return result


# Add your helper functions here.
def strip_str_list(lst):
    r""" (list of str) -> list of str

    Precondition: each str in lst ends in \n or has inleading and trailing
    whitespace.

    Return the list consists of non-blank, non-empty strings.

    >>> strip_str_list([' The first line leads off,\n', '\n', '  \n  ',' daf\n'])
    ['The first line leads off,', 'daf']
    """
    
    # Make a copy of lst.
    my_list = lst[:]
    
    # Remove the '\n' and srip the inleading and trailing whitespace.
    for i in range(len(my_list)):
        my_list[i] = my_list[i].replace('\n','')
        my_list[i] = my_list[i].strip()
        
    # Get the list consists of non-blank, non-empty strings
    stripped_lst = list(filter(None,my_list))
    return stripped_lst

def get_pronounciation_per_line(text,word_to_phonemes):
    """(str,dict of {str: list of str}) -> list of (list of str)
	
    Precondition: text is non-empty. Text contains at least one word.
	
    Return the  list of words' pronounciation ,denoting the pronounciation of one line.
	
    >>> text = 'The first'
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> get_pronounciation_per_line(text,word_to_phonemes)
    [['DH', 'AH0'], ['F', 'ER1', 'S', 'T']]
    
    """
    
    pronounciation_lst = []
    token_lst = text.split()
    
    for element in token_lst:
        word = clean_up(element)
        # The word can't be empty   
        if word:          
            pronounciation_lst.append(word_to_phonemes[word])
            
    return pronounciation_lst

def is_syllable(phoneme):
    """(str) -> bool

    A syllable is a phoneme whose last character is 0, 1, or 2.
    
    Return True if a phoneme is a syllable.

    >>> is_syllable('EH1')
    True
    """
    
    last_character = '012'
    result = False
    
    # If the last character is 0, 1, or 2, return True.
    if phoneme[-1] in last_character:
        result = True
        
    return result  

def count_syllables_per_word(word_phoneme):
    """(list of str) -> int

    The word_phoneme denotes the pronounciation for a word.

    Return the number of syllables of a word_phoneme.

    >>> count_syllables_per_word(['DH', 'AH0'])
    1
    """
    
    number = 0
    
    for each in word_phoneme:
        if is_syllable(each):
            number +=1
            
    return number 

def count_syllables_per_line(pronounciation_per_line):
    """(list of (list of str )) -> int

    The pronounciation_per_line denoes the pronounciation for a line.

    Return the number of syllables of a pronounciation_per_line.
    
    >>> pronounc = [['DH', 'AH0'], ['F', 'ER1', 'S', 'T']]
    >>> count_syllables_per_line(pronounc)
    2
    """
    
    number = 0
    
    for i in range(len(pronounciation_per_line)):
        number += count_syllables_per_word(pronounciation_per_line[i])
        
    return number

def get_rhyme_scheme_info(rhyme_scheme):
    """(list of str ) -> tuple of (list of str, dict of {str :list of int})

    Rhyme_scheme is a list of letter that indicates the rhyme scheme. Return
    a two-item tuple. The list of str denotes appearance order of characters 
    and the dict record the character's index.
    
    >>> get_rhyme_scheme_info(['A', 'B', 'A'])
    (['A', 'B'], {'A': [0, 2], 'B': [1]})
    """
    
    histogram = dict()
    ordered_rhyme = []

    # The appearance order of characters is recorded in ordered_rhyme.
    for i in range(len(rhyme_scheme)):
        if rhyme_scheme[i] not in histogram:
            histogram[rhyme_scheme[i]] = [i]
            ordered_rhyme.append(rhyme_scheme[i])
        else:
            histogram[rhyme_scheme[i]] .append(i)

    return ordered_rhyme,histogram

def get_rhyme_phonemes_str(pronounciation_per_line):
    """(list of list of str) -> str

    Retuen final syllables and all phonemes after those final syllables in
    pronounciation_per_line.

    >>> get_rhyme_phonemes_str([['DH', 'AH0'], ['F', 'ER1', 'S', 'T']])
    'ER1ST'
    """
    
    phonemes_str = ''
    rhyme_phonemes_str = ''
    flag = False

    # Traverse the nested list in reverse order, if flag is True we have got
    #  the result. 
	
    for each in pronounciation_per_line[::-1]:
        for phoneme in each[::-1]:
            phonemes_str = phoneme + phonemes_str
            if is_syllable(phoneme) and (not flag):    
                rhyme_phonemes_str = phonemes_str
                flag = True
    return rhyme_phonemes_str

def get_rhyme_pronounciation(poem_lines, word_to_phonemes):
    """(list of str, pronunciation dictionary) -> list of str

    Return all the final syllables and all phonemes after those final syllables in
    pronounciation_per_line in a poem. 

    >>> poem_lines = ['The first line leads off,', 'With a gap before the.'] 
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> get_rhyme_pronounciation(poem_lines,word_to_phonemes)
    ['AO1F', 'AH0']
    """
    
    rhyme_pronounciation_lst = []
    
    for each in poem_lines:   
        pronounciation_per_line = get_pronounciation_per_line(each,
                                      word_to_phonemes)        
        if count_syllables_per_line(pronounciation_per_line) > 0:
            rhyme_pronounciation_lst.append(get_rhyme_phonemes_str(pronounciation_per_line))
    return rhyme_pronounciation_lst

def is_rhyme(rhyme_str,rhyme_lst,rhyme_pronounciation_lst):
    """(str, list of int, list of str) -> True

    If all lines whose index is in rhyme_lst rhyme as they should, return the true.
 
    >>> rhyme_str = 'A'
    >>> rhyme_lst = [0, 2]
    >>> rhyme_pronounciation_lst = ['AO1F', 'AH0', 'EH1NDZ']
    >>> is_rhyme(rhyme_str,rhyme_lst,rhyme_pronounciation_lst)
    False
    """
	
    result = True
    if rhyme_str != '*' and len(rhyme_lst) > 1:
        for i in range(len(rhyme_lst)-1):
            n1 = rhyme_lst[i]
            n2 = rhyme_lst[i+1]
            if rhyme_pronounciation_lst[n1] != rhyme_pronounciation_lst[n2]:
                result = False
    return result



# ===================== Required Functions =====================

def count_lines(lst):
    r""" (list of str) -> int

    Precondition: each str in lst[:-1] ends in \n.

    Return the number of non-blank, non-empty strings in lst.

    >>> count_lines(['The first line leads off,\n', '\n', '  \n  ',
    ... 'With a gap before the next.\n', 'Then the poem ends.\n'])
    3
    """
	
    # Invoke the strip_str_list(). 
    poem_lines = strip_str_list(lst)
    return len(poem_lines)
    
def get_poem_lines(poem):
    r""" (str) -> list of str

    Return the non-blank, non-empty lines of poem, with whitespace removed 
    from the beginning and end of each line.

    >>> get_poem_lines('The first line leads off,\n\n\n'
    ... + 'With a gap before the next.\nThen the poem ends.\n')
    ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    """
	
    # Return a list of the lines in poem, breaking at line boundaries.
    file_str_list = poem.splitlines()
    # Invoke the strip_str_list().
    poem_lines = strip_str_list(file_str_list)
    return poem_lines
    
def check_syllables(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) -> list of str

    Precondition: len(poem_lines) == len(pattern[0])

    Return a list of lines from poem_lines that do not have the right number of
    syllables for the poetry pattern according to the pronunciation dictionary.
    If all lines have the right number of syllables, return the empty list.

    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 5, 4], ['*', '*', '*'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_syllables(poem_lines, pattern, word_to_phonemes)
    ['With a gap before the next.', 'Then the poem ends.']
    >>> poem_lines = ['The first line leads off,']
    >>> check_syllables(poem_lines, ([0], ['*']), word_to_phonemes)
    []
    """
    wrong_lines = []

    for i in range(len(poem_lines)):
       pronounciation_per_line = get_pronounciation_per_line(poem_lines[i],
                                 word_to_phonemes)
       if (pattern[0][i] != 0) and (count_syllables_per_line \
                                    (pronounciation_per_line) != pattern[0][i]):
           
           wrong_lines.append(poem_lines[i])    
    return wrong_lines

    


def check_rhyme_scheme(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) 
                                                        -> list of list of str

    Precondition: len(poem_lines) == len(pattern[1])

    Return a list of lists of lines from poem_lines that should rhyme with 
    each other but don't. If all lines rhyme as they should, return the empty 
    list.

    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 7, 5], ['A', 'B', 'A'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_rhyme_scheme(poem_lines, pattern, word_to_phonemes)
    [['The first line leads off,', 'Then the poem ends.']]
    """
    wrong_lines_group = []
    all_wrong_lines = []
    rhyme_pronounciation_lst = get_rhyme_pronounciation(poem_lines,
                               word_to_phonemes)
    
    rhyme_flag,rhyme_dict = get_rhyme_scheme_info(pattern[1])
    for each in rhyme_flag:
        if not is_rhyme(each,rhyme_dict[each],rhyme_pronounciation_lst):
            for index in rhyme_dict[each]:
                wrong_lines_group.append(poem_lines[index])
        if wrong_lines_group:       
            all_wrong_lines.append(wrong_lines_group)            
            wrong_lines_group = []
    return all_wrong_lines


if __name__ == '__main__':
    import doctest
    doctest.testmod()
