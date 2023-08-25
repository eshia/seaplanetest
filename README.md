# seaplanetest
My submission for the technical assessment for Seaplane.

### Technical Assessment Description 

Design and implement a function in Python that takes two words and a dictionary of words as input. 
Your function should return the shortest possible path between the two words by changing one letter at a time. Each change is one path step.

You can assume that:

* Both the start and end words are lowercase strings of varying lengths.
* The start and end words can be different lengths.
* Only one letter can be changed, added, or deleted at a time.
* Each intermediate word must exist in the dictionary of words

### This repo

1. `func.py` file: The main function **`shortestWordPath()`** exists in this file. The function takes in 3 parameters `(startWord: string, endWord: string, wordDict: Dictionary)`
    * Outputs the shortest path as: "do - dog - dig", (as a string separated by dashes)
    * Outputs None if there is no path to be found.
    * NOTE: I assumed `wordDict` to be a dictionary where the key is the word, and the value = True (it exists), so all the keys in this dictionary will have value of True
2. `testsuite.py` file: I included some simple tests for my function, just to show edge cases and also expected output for all cases.
    * If you run the testsuite.py as is, it runs all the small tests I wrote. Run it like: `python3 testsuite.py`
3. `IMPLEMENTATION.md` file: I included a small explanation of my implementation of the function (thought process, assumptions made)
