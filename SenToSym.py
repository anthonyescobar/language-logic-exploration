'''
Anthony Escobar

SenToSym.py

 A Simple tool to convert a sentance into it's symbolic logic.

 Citation:
 Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
'''
import nltk

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

if __name__ == "__main__":
    playingAround()
