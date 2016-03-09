# Poetry Form Checker

标签（空格分隔）： python3

---
[toc]


----------


*这是多伦多大学csc课程的大作业题,完成的是利用cmu发音词典检测英文诗歌的形式是否符合要求，用pyhton3写的.好早之前写的，觉得挺有意思的。毕业找实习无聊的就完善下文档吧。简单用中文介绍以下（翻译的不好）:*


----------


#一 介绍


##CMU发音词典

在卡内基梅隆大学的发音词典中，"Daniel"这个词的输出为 ：D AE1 N Y AH0 L.每个以空格分开的pieces叫做一个音位。一个音位可以表示元音或辅音的发音。每个元音后面都有一个数字来表示重度的程度，数字越大重读的程度越高，在"Daniel"这个音中"AE"这个音的重读程度就比“AH”的重读程度高。重读总是在元音发音上。



##诗歌形式
英文的诗歌如同中国的唐诗一样也遵循一定的模式，比如说行数、每行的音位的数目和韵律等。例如打油诗（Limericks）共有五行，第1、2、5行每行有8个音节相互押韵。第3行和第4行各有5个音节相互押韵。（有附加规则的位置和数量的强调与非重读音节，但暂时先忽视掉这些规则)。

```
一首打油诗（Limericks)例子
============================
 I wish I had thought of a rhyme
 Before I ran all out of time!
 I'll sit here instead,
 A cloud on my head
 That rains 'til I'm covered with slime.

它的诗歌形式描述
--------------------------------------------------
    8 A    // 表明第一行有8个元音的发音，并且第1,2,5行最后一个元音的发音必须一样（押韵）
    8 A
    5 B
    5 B
    8 A
解释： 在每一行，第一条信息是一个表明在这行诗所需的音节数（元音发音的个数）。第二段信息是一个字母，表示韵律。在这里，行1，2，和5必须押韵因为他们都标有相同字母（A），和线3和4必须押韵因为他们都标有相同字母（B）。如果没有音节要求第一段信息会被写为0，如果没有押韵的要求第二段信息将会写为“*”。

```



#二 文件介绍

|文件名|介绍|
|:---|:---:|
|poetry_funtions.py|处理函数     |
|poetry_reader.py|输入函数在此文件中   |
|poetry_program.py|程序主体   |
|a3_type_checker.py | 测试  |
|test_check_syllables.py| 测试   |
|test_count_lines.py  |  测试   |
|txt/dictionary.txt|存的是cmu字典|
|txt/poetry_forms.txt|存的是诗歌格式|
|txt/(haiku1.txt haiku3.txt) |要检测的诗歌|

以下是英文原文

----------

# 1 Poetry Form Checker

Limericks, sonnets, haiku, and other forms of poetry each follow prescribed patterns that give the number of lines, the number of syllables on each line, and a rhyme scheme. For example, limericks are five lines long; the first, second, and fifth lines each have eight syllables and rhyme with each other; and the third and fourth lines each have five syllables and rhyme with each other. (There are additional rules about the location and number of stressed vs. unstressed syllables, but we'll ignore those rules for this assignment.)

Here is a stupendous work of limerick art:

    I wish I had thought of a rhyme
    Before I ran all out of time!
    I'll sit here instead,
    A cloud on my head
    That rains 'til I'm covered with slime.

We're sure that you've all kept yourselves awake wondering if there was a way to have a computer program check whether a poem is a limerick or if it follows some other poetry pattern. Here's your chance to resolve the question!

#2 The CMU Pronouncing Dictionary
 The [Carnegie Mellon University Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) describes how to pronounce words. Head there now and look up a couple of words; try searching for words like "Daniel", "is", and "goofy", and see if you can interpret the results. Do contractions like "I'll" (short for "I will") and "we'll" (short for "we will") work? Try clicking the "Show Lexical Stress" checkbox too, and see how that changes the result.

Here is the output for "Daniel" (with "Show Lexical Stress" turned on): D AE1 N Y AH0 L. Each of the separate pieces describes a sound; these pieces are called phonemes. The phonemes are either vowel sounds or consonant sounds, and they are from a project called [Arpabet](http://en.wikipedia.org/wiki/Arpabet) that was created by the [Advanced Research Projects Agency (ARPA)](http://en.wikipedia.org/wiki/Advanced_Research_Projects_Agency) back in the 1970's. The vowel phonemes all have a number after them; these indicate a level of stress. For example, in "Daniel", the stress falls on the first vowel, AE1, and the second vowel is unstressed, AH0. The higher the level of stress, the larger the number after the vowel phoneme. In the CMU Pronouncing Dictionary, stress is always on a vowel sound.

Your program will read the file dictionary.txt, which is our version of the Pronouncing Dictionary. You must use this file, not any files from the CMU website. Take a look at our dictionary.txt file to see the format; notice that any line beginning with ;;; is a comment and not part of the dictionary.

Notice that the words in dictionary.txt are all uppercase and that they do not contain surrounding punctuation. When your program looks up a word, use the uppercase form, with no leading or trailing punctuation. Function clean_up in the starter code file poetry_functions.py will be be helpful here.


#3 Poetry Form Descriptions


For each type of poetry form (limerick, haiku, etc.), we will write its rules as a poetry form description. For example, at the beginning of this handout, we gave the rules for what it means to be a limerick. Here's our poetry form description for the limerick poetry form:

    8 A
    8 A
    5 B
    5 B
    8 A
On each line, the first piece of information is a number that indicates the number of syllables required on that line of the poem. The second piece of information is a letter that indicates the rhyme scheme. Here, lines 1, 2, and 5 must rhyme with each other because they're all marked with the same letter (A), and lines 3 and 4 must rhyme with each other because they're both marked with the same letter (B).

Some poetry forms don't require lines that rhyme. For example, a haiku has 5 syllables in the first line, 7 in the second line, and 5 in the third line, but there are no rhyme requirements. Here is an example:

    Dan's hands are quiet.
    Soft peace surrounds him gently:
    No thought moves the air.
And another one:

    Jen sits quietly,
    Thinking of assignment three.
    All ideas bad.
We'll indicate the lack of a rhyme requirement by using the symbol *. Here is our poetry form description for the haiku poetry form:

    5 *
    7 *
    5 *
Some poetry forms have rhyme requirements but don't have a specified number of syllables per line. Quintain (English) is one such example; these are 5-line poems with an ABABB rhyme scheme, but with no syllabic requirements. Here is our poetry form description for the Quintain (English) poetry form (notice that the number 0 is used to indicate that there is no requirement on the number of syllables in the line):

    0 A
    0 B
    0 A
    0 B
    0 B
Here's an example of a Quintain (English) from Percy Bysshe Shelly's Ode To A Skylark:

    Teach us, Sprite or Bird,
    What sweet thoughts are thine:
    I have never heard
    Praise of love or wine
    That panted forth a flood of rapture so divine.
Your program will read a poetry form description file containing poetry form names and descriptions. For each poetry form in the file, the first line gives the name of the poetry form, and subsequent lines contain the number of syllables and rhyme scheme as described in this section. Each poetry form is separated from the next by a blank line. We have provided poetry_forms.txt as an example poetry form description file. (We will test with other poetry form descriptions as well.) You may assume that the poetry form names given in a poetry form description file are all different.

The poetry samples given in this assignment description, as well as some other poems, are posted on the Poetry Files webpage.



#4 Data Representation

##4.1 Poetry Pattern

A poetry pattern is our data structure for a poetry form description. It is a two-item tuple of:
a list of the number of syllables per line (a list of int)
the rhyme scheme (a list of str)
For example, here is the poetry pattern for a limerick:

([8, 8, 5, 5, 8], ['A', 'A', 'B', 'B', 'A'])

##4.2 Pronunciation Dictionary

A pronunciation dictionary is our data structure for mapping words to phonemes. It is a dict of {str: list of str}, where:
each key is a word (a str)
each value is a list of phonemes for that word (a list of str)
For example, here is a (very tiny) pronunciation dictionary:

{'DANIEL': ['D', 'AE1', 'N', 'Y', 'AH0', 'L'], 
 'IS': ['IH1', 'Z'], 
 'GOOFY': ['G', 'UW1', 'F', 'IY0']}

#5 Valid Input

For all poetry used for this assignment, you may assume that all words in the poetry will appear as keys in the pronunciation dictionary that is being used.

#6 Required Functions

In the starter code file poetry_functions.py, complete the following function definitions. In addition, you must add some helper functions to aid with the implementation of these required functions.

|Function name:<br> (Parameter types) ->Return type|	 Description|
|:----|:----|
| count_lines:<br> (list of str) -> int|   Return the number of non-blank, non-empty strings in the given list. (A blank string is a string that contains only whitespace.)  |
|get_poem_lines:<br> (str) -> list of str|The parameter represents a poem. Return a list of non-blank, non-empty lines from the poem with whitespace removed from the beginning and end of each line.|
|check_syllables:<br> (list of str, poetry pattern, pronunciation dictionary) -> list of str |A syllable is a phoneme whose last character is 0, 1, or 2. As examples, the word BEFORE (B IH0 F AO1 R) has two syllables and the word GAP (G AE1 P) has one syllable. <br>  The first parameter represents a poem as a list of lines (as produced by get_poem_lines), the second represents a poetry pattern, and the third represents a pronunciation dictionary. Return a list of the lines from the poem that do not have the right number of syllables for the poetry pattern. The lines should appear in the list in the same order as they appear in the poem. If all lines have the right number of syllables, return the empty list.|
|check_rhyme_scheme:<br> (list of str, poetry pattern, pronunciation dictionary) -> list of list of str|A syllable is a phoneme whose last character is 0, 1, or 2. We say that two lines rhyme iff their final syllables and all phonemes after those final syllables match.<br> For example:<br> **THE** (DH AH0) and **A** (AH0) rhyme <br>**TREETOPS** (T R IY1 T AO2 P S) and **TRICERATOPS** (T R AY2 S EH1 R AH0 T AO2 P S) rhyme <br>**ABSURD** (AH0 B S ER1 D) and **ADJOURNS** (AH0 JH ER1 N Z) do not rhyme<br>The first parameter represents a poem as a list of lines (as produced by get_poem_lines), the second represents a poetry pattern, and the third represents a pronunciation dictionary. Return a list of lists of lines in the poem that should rhyme with each other (according to the poetry pattern) but don't. If all lines rhyme as they should, return the empty list. Notes:<br>    The lines should appear in the inner lists in the same order as they appear in the poem.<br> If n lines are supposed to rhyme with each other and at least one line does not, all n lines should appear in the inner list.<br> For example: <br>if the rhyme scheme is ['A', 'A', 'B', 'B', 'A'],<br>and the lines are ['On the', 'plains, a', 'triceratops climbs treetops.', 'The day adjourns.', 'Absurd!'],<br>this function should return [['On the', 'plains, a', 'Absurd!'], ['triceratops climbs treetops', 'The day adjourns.']].|


In the starter code file poetry_reader.py, complete the following function definitions.

|Function name:<br> (Parameter types) ->Return type|	 Description|
|:----|:----|
|read_pronunciation:<br>(file open for reading) -> pronunciation dictionary| The parameter represents an open file in the format of the CMU Pronouncing Dictionary. Return the pronunciation dictionary based on the given file.|
|read_poetry_form_description:<br>(file open for reading) -> poetry pattern|The parameter represents a poetry form description file from which a poetry form name has just been read. Read the poetry form description that follows from the poetry form description file and return the corresponding poetry pattern.|
|read_poetry_form_descriptions: <br>(file open for reading) -> dict of {str: poetry pattern}| The parameter represents a poetry form description file. Return a dictionary where each key is a poetry form name and each value is the poetry pattern for that form based on the given file.|

#7 The main program

We have provided the main program file poetry_program.py which is complete and must not be changed. Place the poetry_program.py file in the same folder (directory) as your poetry_functions.py and poetry_reader.py files. Once you have correctly implemented the functions in poetry_functions.py and poetry_reader.py, execution of the main program will:

 1. Read our version of the CMU Pronouncing Dictionary (dictionary.txt)
 2. Read poetry_forms.txt
 3. Repeatedly ask the user for a poetry form to check and the name of a file containing a poem. The program will report on whether or not the poem satisfies the poetry form description for the chosen poetry form.

#8 Required Testing (unittest)

Write (and submit) a set of unittests for functions count_lines and check_syllables. Name these two files test_count_lines.py and test_check_syllables.py. For each test method, include a brief docstring description specifying what is being tested. For unittest methods, the docstring description should not include a type contract or example calls.

##8.1 a3_type_checker.py and doctest

**a3_type_checker.py**

We are providing a type-check module that can be used to test whether your functions in poetry_functions.py have the correct parameter and return types. To use the type checker, place a3_type_checker.py in the same folder (directory) as your poetry_functions.py and run it.

If the type-checks pass: the output will consist only of one thing: the word "okay". This means that the function parameters and return types match the assignment specification.

If the type-checks fail: Look carefully at the message provided. One or more of your parameter or return types does not match the assignment specification. Fix your code and re-run the tests. Make sure the tests pass before submitting.

**doctest**

Each function in poetry_functions.py has a doctest test in its docstring description. Be sure to run the doctests and make sure that they pass. With the functions in this assignment, there are many more possible cases to test (and cases where your code could go wrong). If you want to get a great mark on the correctness of your functions, do a great job of testing your functions under all possible conditions. Then we won't be able to find any errors that you haven't already fixed!

You may have noticed that there is an r before each of the opening docstring triple-quotes in the poetry_functions.py starter code. The r denotes a raw string and means that special characters like \ will not be treated as special. By using raw strings for doctests that include \n and other escape sequences, the docstrings will be runnable as doctests.

#9 Additional requirements

Do not change any of the existing code. Add to it as specified in the comments.
Do not call print, input, or open. (Notice that the three required functions in poetry_reader.py take an open file, not a string.)
Do not use any break or continue statements. Any functions that do will receive a mark of zero. We are imposing this restriction because they are very easy to "abuse," resulting in terrible code.
Do not import any Python modules, other than unittest and poetry_functions.
How to tackle this assignment

##9.1 Principles:

To avoid getting overwhelmed, deal with one function at a time. Start with functions that don't call any other functions; this will allow you to test them right away. The steps listed below give you a reasonable order in which to write the functions.
For each function that you write, start by adding at least one example call to the docstring before you write the function.
Keep in mind throughout that any function you have might be a useful helper for another function. Part of your marks will be for taking advantage of opportunities to call an existing function.
As you write each function, begin by designing it in English, using only a few sentences. If your design is longer than that, shorten it by describing the steps at a higher level that leaves out some of the details. When you translate your design into Python, look for steps that are described at such a high level that they don't translate directly into Python. Design a helper function for each of these, and put a call to the helpers into your code. Don't forget to write a great docstring for each helper!
Since you are required to write unittests for count_lines and check_syllables, write those tests before or as you write the functions themselves. That way you can execute the unittests to test the code you are writing.

##9.2 Steps:

Here is a good order in which to solve the pieces of this assignment.

- Read this handout thoroughly and carefully, making sure you understand everything in it.
- Read the poetry_functions.py starter code to get an overview of what you will be writing.
- Implement and test the required functions in poetry_functions.py, along with helper functions. Now is also a good time to write the unittest test files, test_count_lines.py and test_check_syllables.py.
- Next, read the starter code poetry_reader.py, and implement and test those functions.
- Read the code provided in poetry_program.py and run that program. If there are any problems with the results, try to identify which of your functions has issues, and go back to testing that function.

#10 Marking

These are the aspects of your work that we will focus on in the marking:

- Correctness (60%): The poetry_program.py program should run as described in the requirements section by using your functions from poetry_functions.py and poetry_reader.py. We will check the correctness of each of the required functions from poetry_functions.py and poetry_reader.py. Remember that spelling of file and function names, including case, is important, and that functions should have exactly the number of parameters required and be placed in the same order as specified. Correctness, as evaluated by our tests and the TAs, will count for 60% of the assignment marks.

- Testing (20%): We will evaluate the unittests that you submit based on whether the tests are implemented properly and based on the quality of the test case choices. Ideally, your tests should cover all relevant cases without redundant (unnecessary) tests. Testing will count for 20% of the assignment marks.

- Style and Design (20%): Your code should be well documented with docstrings as well as internal comments, and it should adhere to the Python style guidelines. Your program should be broken down into functions, both to avoid repetitive code and to make the program easier to read. If a function body is more than about 20 lines long, introduce helper functions to do some of the work -- even if they will only be called once. All helper functions should have complete docstring descriptions. Make sure that you read the Python style guidelines page for some important rules and guidelines about formatting your code. Also, your variable names should be meaningful and your code as simple and clear as possible. Style and design will count for 20% of the assignment marks.

# 11 Submitting your assignment

You must hand in your work electronically, using the MarkUs online system. Instructions for doing so are posted on the Assignments page of the course website.

**The very last thing you do before submitting should be to run a3_type_checker.py one last time.** Otherwise, you could make a small error in your final changes before submitting that causes your code to receive zero for correctness.

For this assignment, hand in four files:

 - poetry_reader.py
 - poetry_functions.py
 - test_count_lines.py
 - test_check_syllables.py
 
Once you have submitted, be sure to check that you have submitted the correct version; new or missing files will not be accepted after the due date. Remember that spelling of filenames, including case, counts. **If your files are not named exactly as above, your code will receive zero for correctness.**


