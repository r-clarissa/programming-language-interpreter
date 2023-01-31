from tkinter import *
from tkinter import filedialog, ttk
import re, sys, os, threading

# initialized as global variables
path = ""
dataTb = []
symbol = {}

# ========== LEXEMES DICTIONARY ========== 
lexemes = { 
        
}

# ========== LISTS OF VALID LEXEMES ==========


# ========== LEXICAL ANALYZER FUNCTIONS ==========
def arrange(tokens): # brute force
    pass

def lexicalAnalyzer():
    pass

# ========== SYNTAX ANALYZER FUNCTIONS ==========
def variableDeclaration(validTokens, varDeclaration, lexemes, index):
    pass

def outKeyword(validTokens, outputKeyword, index):
    pass

def arithOperators(validTokens, mathematicalOperators, logicalOperator, index):
    pass

def compareOperators(validTokens, comparisonOperators, logicalOperator, index):
    pass

def inpKeyword(validTokens, inputKeyword, index):
    pass

def typCasting(validTokens, typeCasting, typeLiteral, index): # change this one
    pass

def commentLine(validTokens, commentKeywords, index):
    pass

def condDelimiter(validTokens, conditionalDelimiters, conditionalKeywords, orly, yarly, nowai, mebbe, oic, index):
    pass

def concKeyword(validTokens, concatenationKeyword, logicalOperator, index):
    pass

def boolOperators(validTokens, booleanOperators, logicalOperator, operationDelimiter, index):
    pass

def switches(validTokens, switchKeywords, loopDelimiters, conditionalDelimiters, wtfCnt, omgCnt, breakCnt, oicCnt, index): 
    pass

def validateSwitches(wtfCnt, oicCnt, omgCnt, breakCnt):
    pass

def validateIfelse(orly, yarly, nowai, mebbe, oic):
    pass

def variableRAssignment(validTokens, varAssignment, logicalOperator, booleanValues, index):
    pass

def loops(validTokens, loopDelimiters, loopOperators, loopKeywords, loopFlag, index):
    pass

def syntaxAnalyzer():
    pass
                
   # ========== MAIN CONSTRUCT (HAI ... KTHXBYE)  ==========  
   # main algorithms here...

    # ========== SYNTAX ANALYZER OUTPUT  ==========
    print("\nValid Syntax:", validSyntax, errorMessage)

    return errorMessage, validSyntax

def varDecSemantics(validTokens, varDeclaration, lexemes, index):
    pass

def outputSemantics(validTokens, outputKeyword, index):
    pass

def semanticAnalyzer():
    pass

# ---------- GUI FUNCTIONS ----------
def openFile(): # open files
    pass
        
def runCode():  # runs file
    pass

def preventResize(event):   # function to make the columns unresizable
    pass
    
exitThread = False
exitSuccess = False

class outputRedirector(object):
    def __init__(self, widget):
        self.widget = widget
    def write(self, string):
        if not exitThread:
            self.widget.insert(END, string)
            self.widget.see(END)
        
def main():
    pass
    
if __name__ == '__main__':
    main()
