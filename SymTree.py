from SymNode import SymNode
import nltk

class SymTree():
    def __init__(self, root=None):
        self.root = root

    def identify(self):
        self.root.identify()

    def expand(self):
        self.root.left.expand()
        self.root.right.expand()

    def __iter__(self):
        if self.root != None:
            return iter(self.root)
        else:
            return iter([])

    def __str__(self):
        return(str(self.root))

    def __repr__(self):
        # return "SymTree(" + repr(self.root) + ")"
        return repr(self.root)
