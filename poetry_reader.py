"""
A pronunciation dictionary: dict of {str: list of str}
  - each key is a word (a str)
  - each value is a list of phonemes for that word (a list of str)
"""


def read_pronunciation(pronunciation_file):
    """ (file open for reading) -> pronunciation dictionary

    Read pronunciation_file, which is in the format of the CMU Pronouncing
    Dictionary, and return the pronunciation dictionary.
    """
    pronunciation_dict = dict()

    for line in pronunciation_file:
        # Skip over the comments beginning with ;;;  
        if line[0:3] != ";;;":
            temp = line.split()
            word = temp[0]
            pronunciation_dict[word] = temp[1:]
            
    #Close the pronunciation_file
    pronunciation_file.close()        
    return pronunciation_dict     

def read_poetry_form_description(poetry_forms_file):
    """ (file open for reading) -> poetry pattern

    Precondition: we have just read a poetry form name from poetry_forms_file.

    Return the next poetry pattern from poetry_forms_file.
    """
    # Initialize two lists
    syllables_number_list = []
    rhyme_list = []
    flag = True
    
    while (flag):
        # The character of new line '\n' should be  removed. 
        line = poetry_forms_file.readline().rstrip('\n')
##        print(line,type(line))
        # If a blank line is read,change the flag to break the while loop
        if len(line) == 0:
            flag = False
        else:     
            temp = line.split()
            syllables_number_list.append(int(temp[0]))
            rhyme_list.append(temp[1])
            
    return (syllables_number_list,rhyme_list)

def read_poetry_form_descriptions(poetry_forms_file):
    """ (file open for reading) -> dict of {str: poetry pattern}

    Return a dictionary of poetry form name to poetry pattern for the
    poetry forms in poetry_forms_file.
    """
    # Initialize
    pattern_name = []
    poetry_pattern = []
    
    for line in poetry_forms_file:
        # The character of new line '\n' should be  removed.
        pattern_name.append(line.rstrip('\n'))
##        print(pattern_name,type(pattern_name))        
        poetry_pattern.append(read_poetry_form_description(poetry_forms_file))
##        print(poetry_pattern,type(poetry_pattern))
        
    # Create the dictionary
    pattern_dict = dict(zip(pattern_name,poetry_pattern))    
    return pattern_dict
