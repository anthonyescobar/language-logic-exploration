from SymNode import SymNode
import nltk

class SymTree():
    def __init__(self, root=None):
        self.root = root
        self.subj = None
        self.cond = None
        self.conds = {"BCON":"Biconditional","CON":"Conditional"}

    def identify(self):
        self.root.identify()
        self.cond = self.conds[self.root.getVal()]

    def expand(self):
        self.root.left.expand()
        self.root.right.expand()

    def isoSubject(self):
        self.subj = []
        pns = []
        # ent = nltk.chunk.ne_chunk(nltk.pos_tag(self.root.getVal())) # get entities, not necessary for now
        tag = nltk.pos_tag(self.root.getVal())
        for tup in tag:
            if tup[1] == "NNP" or tup[1] == "NNS":
                if tup[0] not in self.subj: self.subj.append(tup[0])
            elif tup[1] == "PRP":
                if tup[0] not in self.subj: self.subj.append(tup[0])
            elif tup[1] == "NNS":
                if tup[0] not in self.subj: self.subj.append(tup[0])
        self.root.remove(self.subj)
        self.root.remove(self.subj)
        # print(self.subj)

    def getSubj(self):
        return self.subj
    def getCond(self):
        return self.cond

    def poss(self):
        return "if" in self.root.val or "If" in self.root.val

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
