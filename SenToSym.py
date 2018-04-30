'''
Anthony Escobar

SenToSym.py

 A Simple tool to convert a sentance into it's symbolic logic.

 Citation:
 Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
'''
from SymTree import SymTree
from SymNode import SymNode
import nltk

def run(s,options=""):
    if "d" in options:
        demo()
        return
    t = SymTree(SymNode(nltk.word_tokenize(s)[:len(nltk.word_tokenize(s))-1]))
    if not t.poss():
        print("The sentence given cannot be identified.")
        return
    if "r" in options:
        print("Input: " + s)
    if "s" in options:
        t.isoSubject()
        for subj in t.getSubj():
            print("Subject: " + subj)
    t.identify()
    t.expand()
    print(repr(t))
    if "c" in options:
        print("Type: " + t.getCond())
    print(t)

######################## TESTING FUNCTIONS ####################################
def first():
    s = 'I will get an A when I have the time to study.'
    print(s)

    stt = nltk.pos_tag(nltk.word_tokenize(s))
    print(stt)

    sttne = nltk.chunk.ne_chunk(stt)
    print(sttne)

def theProcess1():
    sentence = "If I have the time to study then I will get an A."
    print("Input: " + sentence)
    tokens = nltk.word_tokenize(sentence)
    t = SymTree(SymNode(tokens[:len(tokens)-1]))
    # print(t)
    t.isoSubject()
    for subj in t.getSubj():
        print("Subject: " + subj)
    t.identify()
    t.expand()
    print(repr(t))
    print("Type: " + t.getCond())
    print(t)

def theProcess2():
    sentence = "Forneybots were found to malfumction if and only if they suffer water damage or overheard a logical paradox."
    print("Input: " + sentence)
    tokens = nltk.word_tokenize(sentence)
    t = SymTree(SymNode(tokens[:len(tokens)-1]))
    # print(t)
    t.isoSubject()
    for subj in t.getSubj():
        print("Subject: " + subj)
    t.identify()
    t.expand()
    print(repr(t))
    print("Type: " + t.getCond())
    print(t)

def theProcess3():
    sentence = "I will get an A if I have time to study."
    print(sentence)
    tokens = nltk.word_tokenize(sentence)
    print(tokens)
    t = SymTree(SymNode(tokens[:len(tokens)-1]))
    # print(t)
    t.identify()
    # print(t)
    t.expand()
    print(repr(t))
    print(t)

def playingAround():
    print("Testing the NLTK functions:\n")
    sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
    print(sentence)

    print("\nSentence Tokenized")
    tokens = nltk.word_tokenize(sentence)
    print(tokens)

    print("\nTokens Tagged")
    tagged = nltk.pos_tag(tokens)
    print(tagged)

    print("\nIdentify named entities")
    entities = nltk.chunk.ne_chunk(tagged)
    print(entities)

    print("\nMultipule Sentences now")
    sentences = '''Good muffins cost $3.88\nin New York.  Please buy me two of them.\n\nThanks.'''
    print(sentences)

    print("\nUse sent_tokenize(s)")
    sentTokens = nltk.sent_tokenize(sentences)
    print(sentTokens)

    print("Use word_tokenize(s) on each sentance in the array")
    arrTokens = []
    for s in sentTokens:
        arrTokens.append(nltk.word_tokenize(s))
    print(arrTokens)

def demo():
    theProcess1()
    print("")
    theProcess2()

    if __name__ == "__main__":
        playingAround()
        # print("\n---------------------")
        # first()
        # theProcess1("")
        # print("\n---------------------")
        # theProcess2("")
        # print("\n---------------------")
        # theProcess3("")
