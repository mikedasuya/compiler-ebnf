
'''expr = expr + expr;
expr = expr - expr;
expr = expr * expr;
expr = expr / expr;
expr = DIGIT | expr;
DIGIT = 0|1|2|3|4|5|6|7|8|9 '''
from enum import Enum


class LITERALS(Enum):
    DIGIT = 1,
    EXPRESSION = 2,
    SYMBOL = 3

class Node:
    def __init__(self, expr, literals):
        self.left = None
        self.right = None
        self.expr = expr
        self.literals = literals


class Parser:
    def __init__(self):
        self.rootNode =  None

    def ReturnSymBolNode(self, expr, symbolstring):
        loc = expr.findStr(symbolstring)
        if (loc != -1):
            node = Node(symbolstring, LITERALS.SYMBOL)
            rightStr = expr[:loc]
            leftStr = expr[loc:]
            node.left = Node(leftStr, LITERALS.EXPRESSION)
            node.right = Node(rightStr, LITERALS.EXPRESSION)
            return node
        return -1

    def AddRule(self, expr):
        return self.ReturnSymBolNode(expr, "+")

    def MinusRule(self, expr):
        return self.ReturnSymBolNode(expr, "-")

    def MultiplicationRule(self, expr):
        return self.ReturnSymBolNode(expr, "*")

    def DivisionRule(self, expr):
        return self.ReturnSymBolNode(expr, "*")

    def parse(self, expr):
        node = self.AddRule(expr)
        if (self.RootNode != None):
            self.RootNode = node
            self.RootNode.left = self.parse(node.left.expr)
            self.RootNode.right = self.parse(node.right.expr)

        node = self.MinusRule(expr)
        if (self.RootNode != None):
            self.RootNode = node
            self.RootNode.left = self.parse(node.left.expr)
            self.RootNode.right = self.parse(node.right.expr)

        node = self.MultiplicationRule(expr)
        if (self.RootNode != None):
            self.RootNode = node
            self.RootNode.left = self.parse(node.left.expr)
            self.RootNode.right = self.parse(node.right.expr)

        node = self.DivisionRule(expr)
        if (self.RootNode != None):
            self.RootNode = node
            self.RootNode.left = self.parse(node.left.expr)
            self.RootNode.right = self.parse(node.right.expr)

        if node != -1:
            return Node(expr, LITERALS.DIGIT)
        else:
            node.left = self.parse(node.left.expr)
            node.right = self.parse(node.right.expr)
            return node


