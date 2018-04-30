'''
Anthony Escobar

lltk.py

 A Simple tool to convert a sentance into it's symbolic logic.

 Citation:
 Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
'''
import nltk
import SenToSym as tk
import sys

def usage():
    print("USAGE HERE")

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        usage()
        # tk.theProcess2()
    else:
        if sys.argv[1][0] == "-":
            sentence = sys.argv[2]
            options = sys.argv[1]
        else:
            sentence = sys.argv[1]
            options = ""
        # print("\n" + sentence)
        tk.run(sentence,options)
