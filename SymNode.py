import nltk

syms = ['A','B','C','D','E','F','G','H','I','J']
i = 0

class SymNode():

    def __init__(self,val,left=None,right=None,sym=None):
        self.val = val
        self.left = left
        self.right = right
        self.sym = sym

    def getVal(self):
        return self.val

    def setVal(self,arg):
        self.val = arg

    def getLeft(self,arg):
        return self.left

    def setLeft(self,arg):
        self.left = arg

    def getRight(self,arg):
        return self.right

    def setRight(self,arg):
        self.right = arg

    def getSym(self):
        return self.sym

    def setSym(self):
        global syms
        global i
        self.sym = syms[i]
        i += 1
        if i >= len(syms):
            i = 0

    # def upSymI(self):
    #     self.i += 1

    def identify(self):
        # loop through and look for if_then, _if/wh_, _iff_

        # if-then
        if self.val[0] == "If":
            print("if_then")
            if "then" in self.val:
                self.setLeft(SymNode(self.val[1:self.val.index("then")]))
                self.left.setSym()
                self.setRight(SymNode(self.val[self.val.index("then")+1:]))
                self.right.setSym()
                self.setVal("TF")
                self.sym = "⇒"
            if "," in self.val:
                self.setLeft(SymNode(self.val[1:self.val.index(",")]))
                self.left.setSym()
                self.setRight(SymNode(self.val[self.val.index(",")+1:]))
                self.right.setSym()
                self.setVal("TF")
                self.sym = "⇒"

        # _iff_
        if all(x in self.val for x in ["if",'and',"only","if"]):
            print("_iff_")
            # print(self.val.index("if"))
            self.setLeft(SymNode(self.val[:self.val.index("if")]))
            self.left.setSym()
            self.setRight(SymNode(self.val[self.val.index("if")+4:]))
            self.right.setSym()
            self.setVal("bc")
            self.sym = "⇔"

        # _if_
        if "if" in self.val:
            self.setLeft(SymNode(self.val[self.val.index("if")+1:]))
            self.left.setSym()
            self.setRight(SymNode(self.val[:self.val.index("if")]))
            self.right.setSym()
            self.setVal("TF")
            self.sym = "⇒"

    def expand(self):
        if "and" in self.val:
            print("AND")
            self.setLeft(SymNode(self.val[:self.val.index("and")]))
            self.left.setSym()
            self.setRight(SymNode(self.val[self.val.index("and")+1:]))
            self.right.setSym()
            self.setVal("AND")
            self.sym = "∧"

            self.left.expand()
            self.right.expand()
        elif "or" in self.val:
            print("OR")
            self.setLeft(SymNode(self.val[:self.val.index("or")]))
            self.left.setSym()
            self.setRight(SymNode(self.val[self.val.index("or")+1:]))
            self.right.setSym()
            self.setVal("OR")
            self.sym = "∨"

            self.left.expand()
            self.right.expand()
        # else:
        #     print("")

    # inorder traversal
    def _iter_(self):
        if self.left != None:
            for elem in self.left:
                yield elem

        yield self.val

        if self.right != None:
            for elem in self.right:
                yield elem

    def __str__(self):
        if self.left != None and self.right != None:
            return " " + str(self.left) + " " + str(self.sym) + " " + str(self.right)
        return self.sym

    def __repr__(self):
        # return "\n\tSymNode(" + repr(self.sym) + "," + repr(self.val) + "," + repr(self.left) + "," + repr(self.right) + ")"
        if self.left != None and self.right != None:
            return repr(self.left) + "\n" + repr(self.right)
        if len(self.val) > 2:
            return self.sym + ": " + " ".join(self.val)
