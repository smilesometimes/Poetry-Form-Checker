import unittest
from poetry_functions import check_syllables

#Define the global variable
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


class Test_check_syables(unittest.TestCase):
    """
     
    Precondition: len(poem_lines) == len(pattern[0])

    """    

    def test_poem_of_one_line(self):
        """

        Poem_lines consist of one line is being tested.
        
        """
        
        poem_lines = ['The first line leads off,']
        pattern = ([5], ['*'])
        self.assertEqual(check_syllables(poem_lines,pattern,word_to_phonemes),
                         [], 'Poem_lines consists of one line')
        
    def test_poem_of_mutiple_lines(self):
        """

        Poem_lines consist of mutiple lines and the order of returned lines is
        beng tested
       
        """
        poem_lines = ['The first line leads off,',
                      'With a gap before the next.',
                      'Then the poem ends.']
        pattern = ([5, 5, 4], ['*','*','*'])
        expected_list = ['With a gap before the next.', 'Then the poem ends.']
        
        self.assertEqual(check_syllables(poem_lines,pattern,word_to_phonemes),
                          expected_list, 'Poem_lines consists of mutiple lines')
        
        self.assertFalse(check_syllables(poem_lines,pattern,word_to_phonemes) \
                         == expected_list[::-1],'Order of returned lines')

    def test_no_syllabic_requirements(self):
        """

        Test the pattern has no syllabic requirements ,all pattern[0] being zeros,
        the returned lines should be empty list.
        
        """
        poem_lines = ['The first line leads off,',
                      'With a gap before the next.']
        pattern = ([0, 0], ['*', '*'])
        expected_list = []
        self.assertEqual(check_syllables(poem_lines,pattern,word_to_phonemes),
                          expected_list, 'No syllabic requirements')        

        
unittest.main(exit=False)
