import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Crosshair(QtWidgets.QWidget):
    def __init__(self, parent=None, windowSize=24, penWidth=2):
        QtWidgets.QWidget.__init__(self, parent)
        self.ws = windowSize
        self.resize(windowSize+1, windowSize+1)
        self.pen = QtGui.QPen(QtGui.QColor(255,0,0)) #Adjust RGB values for a different colour https://www.rapidtables.com/web/color/RGB_Color.html
        self.pen.setWidth(penWidth)                                            
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowTransparentForInput)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.move(QtWidgets.QApplication.desktop().screen().rect().center() - self.rect().center() + QtCore.QPoint(1,1))

    def paintEvent(self, event):
        crosshairlength = 3 #Adjust the spacing of the crosshair
        ws = self.ws
        res = int(ws/2)
        red = int(ws/crosshairlength)
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        painter.drawLine(res, 0, res, res - red)
        painter.drawLine(res, res + red+1, res, ws)
        painter.drawLine(0, res, res - red, res)
        painter.drawLine(res + red, res, ws - 0.5, res)

app = QtWidgets.QApplication(sys.argv)
widget = Crosshair(windowSize=16, penWidth=2) #Adjust the windowSize to make the whole crosshair larger, Adjust the penWidth to adjust the thickness of the crosshair
widget.show()
sys.exit(app.exec_())