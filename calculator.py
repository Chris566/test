import sys

from PyQt6 import QtWidgets

from ui_Calculator import Ui_CaculatorWin


class w_Calculator(QtWidgets.QWidget, Ui_CaculatorWin):
    def __init__(self):
        super(w_Calculator, self).__init__()
        self.setupUi(self)
        self.expr = ''
        self.resultfinished = False
    def CalObjPressed(self):
        if  self.resultfinished:self.ClearInput()
        pButton = self.sender()
        char = pButton.text()
        self.CalculatorDisplay.insertPlainText(char)
        self.expr += char
    def ExecuteCalculate(self):
        self.CalculatorDisplay.append("=")
        globalArea = {}
        try: result = eval(self.expr, globalArea)
        except Exception as e:
            self.CalculatorDisplay.append(f"计算结果错误，错误原因：\n{e}")
        else: self.CalculatorDisplay.append(str(result))
        self.resultfinished = True
    def ClearInput(self):
        self.CalculatorDisplay.clear()
        self.expr = ''
        self.resultfinished = False
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # mainwin = MediaPlayerWin()
    # mainwin.show()
    W = w_Calculator()
    W.show()
    sys.exit(app.exec())