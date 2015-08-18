import unittest
from poetry_functions import count_lines

class Test_count_lines(unittest.TestCase):

    def test_empty_list(self):
        """

        Test the empty list.
        
        """
        self.assertEqual(count_lines([]),0,
            'empty list')
        
    def test_list_of_non_empty_non_blank_string(self):
        """

        Test the list of non-blank, non-empty strings.  
            
        """
        self.assertEqual(count_lines(['dada ']), 1,
            'list of one non-blank, non-empty string')

        self.assertEqual(count_lines(['dada ', 'daa']), 2,
            'list of multiple non-blank, non-empty lines')
    
                         
    def test_list_of_blank_string(self):
        """

        Test the list of blank strings. 
        
        """
        self.assertEqual(count_lines(['  ']), 0,
            'only one blank tring')
        
        self.assertEqual(count_lines(['   ', '  ']), 0,
            'multiple_blank strings')
        
    def test_list_of_empty_string(self):
        """

        Test the list of empty strings.
        
        """ 
        self.assertEqual(count_lines(['']), 0,
            'only one empty string')
        
        self.assertEqual(count_lines(['', '']), 0,
             'multiple empty strings')
        
    def test_list_of_mutiple_types_of_lines(self):
        """

        Test the list of strings with empty string,blank string and non-empty,
        non-blank string.
        
        """
        self.assertEqual(count_lines(['', 'dad', '  ', ' dsadf']), 2,
            'list of srings with empty string,blank string and non-empty,' + \
            'non-blank string')
       
        
    def test_list_of_strings_with_character_of_new_line(self):
        """

        Test the list of strings with characters. 
            
        """
        self.assertEqual(count_lines(['faff\n', '\n', '   \n']), 1,
            'list of strings with character of new line in the end')

        self.assertEqual(count_lines(['fa\nf', ' \n ']), 1,
            'list of strings with character of new line in the middle')

        self.assertEqual(count_lines(['da\n\n', '\n \n  ', '\n  \n']), 1,
            'list of strings with characters of new line in the end or in' + \
            'the middle')
        
  
 
unittest.main(exit=False)        
