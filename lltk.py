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
    print("Language Logic Toolkit v0.2\n")
    print("This project is an exploration into the compatibility between language and computation. The goal of the Language-Logic application is to create an application where, when given a sentence can identify prepositional phrases and breakdown its structure in order to output the symbolic logic of the statement. Currently, this program is only prepared to tackle simple conditional argument structure.\n")
    print("USAGE:")
    print("python3 lltk.py [-options] [sentence]")
    print("options:\n\t-r\tRepeat Input\n\t-s\tIsolate Subject\n\t-c\tShow Conditional Type\n\t-d\tDemo")
    print("sentence: Can only be recognized if it includes some sort of if-then or if-and-only-if conditional statement. ex. If I have the time to study then I will get an A.")

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        usage()
    else:
        sentence = ""
        options = ""
        if sys.argv[1][0] == "-":
            options = sys.argv[1]
            if len(sys.argv) == 3:
                sentence = sys.argv[2]
        else:
            sentence = sys.argv[1]
        tk.run(sentence,options)
