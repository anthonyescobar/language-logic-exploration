'''
Anthony Escobar

SenToSym.py

 A Simple tool to convert a sentance into it's symbolic logic.

 Citation:
 Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
'''
import nltk
import SenToSym as tk
import sys

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        # Print Usage
        tk.theProcess2()
    else:
        print(sys.argv[1])
