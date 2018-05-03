import sys
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter, QTextBlock, QTextCursor
from compare import set_first_object, joinText,retResult
from time import sleep


def format(color, style='', bd_color='white'):
    """
    Return a QTextCharFormat with the given attributes.
    """
    _color = QColor()
    _bd_color = QColor()
    if type(color) is not str:
        _color.setRgb(color[0], color[1], color[2])
    else:
        _color.setNamedColor(color)
    if type(bd_color) is not str:
        _bd_color.setRgb(bd_color[0], bd_color[1], bd_color[2])
    else:
        _bd_color.setNamedColor(bd_color)

    _format = QTextCharFormat()
    _format.setForeground(_color)
    _format.setBackground(_bd_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)

    return _format


# Syntax styles that can be shared by all languages

STYLES = {
    'character': format([255, 0, 0], 'bold'),
    'line': format([0, 0, 0], 'bold', 'red'),
}


class Highlighter(QSyntaxHighlighter):
    temp_object = ""
    f_text, s_text = "", ""

    line = []


    allLine = []
    onlyChar = []

    keywords = ["T", "t", "s", "f"]

    # Python operators
    operators = [
        "\.", ",", "!"]

    result = []

    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)
        self.cursor = self.parent().parent().parent().textCursor()
        self.Line = QTextBlock(self.cursor.block())
        rules = []
        self.rules = []
        Highlighter.temp_object = self
        set_first_object(Highlighter.temp_object)

        # Keyword, operator, and brace rules
        for w in Highlighter.keywords:
            rules += [(r'%c' % w, 0, STYLES['character'])]
        for o in Highlighter.operators:
            rules += [(r'%s' % o, 0, STYLES['line'])]

            # Build a QRegExp for each pattern

        for (pat, index, fmt) in rules:
            self.rules.append([(QRegExp(pat), index, fmt)])

    # Get text editor from Window
    def returnParent(self):
        return self.parent().parent().parent()


    def getAllLine(self,ind):
        self.cursor.setBlockFormat(self.Line)




    def findLines(self):

        # self.cursor.setPosition()
        # print("SON",self.cursor.atBlockEnd())
        # print("BAŞ",self.cursor.atBlockStart())
        pass

    def highlightBlock(self, text):


        self.findLines()

        first, second = self.parent().parent().parent().parent().returnTextWindow()

        if Highlighter.temp_object is self:
            Highlighter.f_text = first.toPlainText()
            text = self.returnParent().toPlainText()
            joinText(text, Highlighter.temp_object)
        if Highlighter.temp_object is not self:
            Highlighter.s_text = second.toPlainText()
            text = self.returnParent().toPlainText()
            joinText(text)
        Highlighter.result = retResult()


        # print(Highlighter.result)



        # for ind, index in Highlighter.result:
        # self.cursor.setBlockFormat(self.Line)
        # self.setCurrentBlockState(0)
        # self.cursor.setPosition(0)
        print(self.Line.blockNumber())

        # print(self.cursor.positionInBlock())
        # print(self.cursor.position())
        # print(self.cursor.blockNumber())
        # if self.cursor.blockNumber() % 2 is 0:
        #     self.setFormat(0, 10, STYLES['line'])

        # for ind in range(0, 10):
        #     index = 0
        #     # print(ind,index)
        # if index == -2:
        #     length = len(text)
        #     # print(ind, index)
        #     self.setFormat(0, length, STYLES['line'])
        # else:
        #     self.setFormat(index, index, STYLES['character'])
        # # print(self.setCurrentBlockState(ind))
        # if self.currentBlockState()%2 is 0 :
        #     self.setFormat(0, 10, STYLES['line'])

        # for expression, nth, format in rules:
        #     # After unmatch line
        #     if expression == QRegExp("!"):
        #         index = expression.indexIn(text,0)
        #         if expression.cap(nth) == "!":
        #             # print(expression.cap(nth))
        #             length = len(text)
        #             self.setFormat(0,length,format)
        #     #Unmatch Char
        #     else:
        #         index = expression.indexIn(text, 0)
        #         while index >= 0:
        #             index = expression.pos(nth)
        #             length = len(expression.cap(nth))
        #             self.setFormat(index, length, format)
        #             index = expression.indexIn(text,index+length)

        # self.setCurrentBlockState(0)
