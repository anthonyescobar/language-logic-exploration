import nltk

syms = ['A','B','C','D','E','F','G','H','I','J']
i = 0

class SymNode():
    def __init__(self,val,left=None,right=None,sym=None):
        self.val = val
        self.left = left
        self.right = right
        self.op = ""
        self.sym = sym
        self.sbls = {"CON":"⇒","BCON":"⇔","AND":"∧","OR":"∨","NOT":"¬"}

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

    def remove(self,arg):
        for a in arg:
            if a in self.val:
                self.val.remove(a)

    # def upSymI(self):
    #     self.i += 1

    def identify(self):
        # loop through and look for if_then, _if/wh_, _iff_

        # if-then
        if self.val[0] == "If":
            if "then" in self.val:
                self.setLeft(SymNode(self.val[1:self.val.index("then")]))
                self.left.setSym()
                self.setRight(SymNode(self.val[self.val.index("then")+1:]))
                self.right.setSym()
                self.setVal("CON")
                self.sym = self.sbls[self.val]
            elif "," in self.val:
                self.setLeft(SymNode(self.val[1:self.val.index(",")]))
                self.left.setSym()
                self.setRight(SymNode(self.val[self.val.index(",")+1:]))
                self.right.setSym()
                self.setVal("CON")
                self.sym = self.sbls[self.val]
            elif "when" in self.val:
                self.setLeft(SymNode(self.val[1:self.val.index("when")]))
                self.left.setSym()
                self.setRight(SymNode(self.val[self.val.index("when")+1:]))
                self.right.setSym()
                self.setVal("CON")
            elif "where" in self.val:
                self.setLeft(SymNode(self.val[1:self.val.index("where")]))
                self.left.setSym()
                self.setRight(SymNode(self.val[self.val.index("where")+1:]))
                self.right.setSym()
                self.setVal("CON")

        # _iff_
        elif all(x in self.val for x in ["if",'and',"only","if"]):
            # print("_iff_")
            # print(self.val.index("if"))
            self.setLeft(SymNode(self.val[:self.val.index("if")]))
            self.left.setSym()
            self.setRight(SymNode(self.val[self.val.index("if")+4:]))
            self.right.setSym()
            self.setVal("BCON")
            self.sym = self.sbls[self.val]

        # _if_
        elif "if" in self.val:
            self.setLeft(SymNode(self.val[self.val.index("if")+1:]))
            self.left.setSym()
            self.setRight(SymNode(self.val[:self.val.index("if")]))
            self.right.setSym()
            self.setVal("CON")
            self.sym = self.sbls[self.val]

        else:
            self.setVal("ERROR")
            return

    def expand(self):
        if "n't" in self.val:
            self.op = self.sbls["NOT"]
            # del self.val[self.val.index("n't")-1]
            # del self.val[self.val.index("n't")]
            self.val.remove("n't")
        elif "not" in self.val:
            self.op = self.sbls["NOT"]
            # del self.val[self.val.index("not")]
            self.val.remove("n't")

        if "and" in self.val:
            # print("AND")
            self.setLeft(SymNode(self.val[:self.val.index("and")]))
            self.left.setSym()
            self.setRight(SymNode(self.val[self.val.index("and")+1:]))
            self.right.setSym()
            self.setVal("AND")
            self.sym = self.sbls[self.val]

            self.left.expand()
            self.right.expand()
        elif "or" in self.val:
            # print("OR")
            self.setLeft(SymNode(self.val[:self.val.index("or")]))
            self.left.setSym()
            self.setRight(SymNode(self.val[self.val.index("or")+1:]))
            self.right.setSym()
            self.setVal("OR")
            self.sym = self.sbls[self.val]

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
        else: # if not isinstance(self.val,list):
            return self.sym + ": " + " ".join(self.val)
