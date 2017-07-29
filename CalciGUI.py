# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys 
from PyQt4.QtGui import *
from PyQt4.QtGui import *
from Calcibuttons import *
from MathematicalFunctions import *


class Calculator(QMainWindow):

    def __init__(self):
        super(Calculator,self).__init__()
        self.setWindowTitle("Calculator")
        self.resize(400,400)
        
        self.mainWidget = QWidget()  # Defining the Main layout on which other layout are added 
                   
        # A first vertical widget which contains < A display label + (First Horizonatal Layout) + Equal button
        self.verticalFirstLayout = QVBoxLayout()
        
        # Adding the display label
        self.testDisplayer = QLabel("0")
        
        # defining fonts and size of texts
        newFont = QFont("Times", 35, QFont.Bold)
        buttonFont = QFont("Times", 15, QFont.Bold)
        self.testDisplayer.setFont(newFont)
              
        # Adding the Display label to the First vertical layout 
        self.verticalFirstLayout.addWidget(self.testDisplayer)    
                
        # Definign a horizontal Layout which will contain < A grid layout + A vertical layout >
        self.horizontalFirstLayout = QHBoxLayout()
        
        # Defining the grid Layout 
        self.buttonGrid = QGridLayout()
        
        # Adding number buttons to grid layout
#        buttonValue = 1
#        for column in range(0,3):
#            for row in range(0,3):      
#                buttonLabel = str(buttonValue)
#                self.buttonGrid.addWidget(Calcbutton(buttonLabel),column,row)             
#                buttonValue = buttonValue +1    
        self.oneButton = QPushButton("1") 
        self.twoButton = QPushButton("2")   
        self.threeButton = QPushButton("3") 
        self.fourButton = QPushButton("4") 
        self.fiveButton = QPushButton("5") 
        self.sixButton = QPushButton("6") 
        self.sevenButton = QPushButton("7") 
        self.eightButton = QPushButton("8") 
        self.nineButton = QPushButton("9") 
        self.zeroButton = QPushButton("0") 
        self.dotButton = QPushButton(".")
        self.clearButton = QPushButton("CLEAR") 
        
        
        self.buttonGrid.addWidget(self.oneButton,0,0)    
        self.buttonGrid.addWidget(self.twoButton,0,1)
        self.buttonGrid.addWidget(self.threeButton,0,2)    
        self.buttonGrid.addWidget(self.fourButton,1,0)
        self.buttonGrid.addWidget(self.fiveButton,1,1)    
        self.buttonGrid.addWidget(self.sixButton,1,2)
        self.buttonGrid.addWidget(self.sevenButton,2,0)    
        self.buttonGrid.addWidget(self.eightButton,2,1)
        self.buttonGrid.addWidget(self.nineButton,2,2)    
        self.buttonGrid.addWidget(self.zeroButton,3,0)
        self.buttonGrid.addWidget(self.dotButton,3,1)
        self.buttonGrid.addWidget(self.clearButton,3,2)
        
        self.newValue = '0'
        self.oldValue = '0'
        self.dispText = '0'
        self.finalValue = 0
        self.wantedFunc = ' '
        
          
        # Defininf the vertical Second layout that will contain mathematical functions 
        self.verticalSecondLayout = QVBoxLayout()        
        buttonList = ['+','-','/','x']
        
        # Adding mathematical functions as buttons to layout 
#        for item in buttonList:
#            self.verticalSecondLayout.addWidget(Calcbutton(item))       
        self.plusButton = QPushButton('+')
        self.minusButton = QPushButton('-')
        self.divButton = QPushButton('/')
        self.mulButton = QPushButton('*')
        
        
        self.verticalSecondLayout.addWidget(self.plusButton)
        self.verticalSecondLayout.addWidget(self.minusButton)
        self.verticalSecondLayout.addWidget(self.divButton)
        self.verticalSecondLayout.addWidget(self.mulButton)
        # Adding grid layout and vertical second layout to vertical second layout  
        self.horizontalFirstLayout.addLayout(self.buttonGrid) 
        self.horizontalFirstLayout.addLayout(self.verticalSecondLayout)
        
        # Adding horizontal layout to the first vertical layout
        self.verticalFirstLayout.addLayout(self.horizontalFirstLayout)
        
        # Addding a equal button to the vertical button 
        self.equalButton = QPushButton("=")
        self.equalButton.setFont(buttonFont)
        self.verticalFirstLayout.addWidget(self.equalButton)
        
        # Adding vertical first layout to mainWidget 
        self.mainWidget.setLayout(self.verticalFirstLayout)
        
        # making the main widget as cental widget
        self.setCentralWidget(self.mainWidget)
  

    def run(self):
        self.oneButton.clicked.connect(lambda: self._updateValue(1))
        self.twoButton.clicked.connect(lambda: self._updateValue(2))
        self.threeButton.clicked.connect(lambda: self._updateValue(3))
        self.fourButton.clicked.connect(lambda: self._updateValue(4))
        self.fiveButton.clicked.connect(lambda: self._updateValue(5))
        self.sixButton.clicked.connect(lambda: self._updateValue(6))
        self.sevenButton.clicked.connect(lambda: self._updateValue(7))
        self.eightButton.clicked.connect(lambda: self._updateValue(8))
        self.nineButton.clicked.connect(lambda: self._updateValue(9))
        self.zeroButton.clicked.connect(lambda: self._updateValue(0))
        
        self.plusButton.clicked.connect(lambda: self._mathfunc('+'))
        self.minusButton.clicked.connect(lambda: self._mathfunc('-'))
        self.divButton.clicked.connect(lambda: self._mathfunc('/'))
        self.mulButton.clicked.connect(lambda: self._mathfunc('x'))
        
        
        
        self.equalButton.clicked.connect(lambda: self._equalfunc())
        
        self.clearButton.clicked.connect(lambda: self._clearVariable())

    def _updateValue(self,buttonValue):  
        
        if len(self.newValue) == 1 and self.newValue == '0':
            self.newValue = str(buttonValue)
        else:
            self.newValue = str(self.newValue) + str(buttonValue)

                        
        if len(self.dispText) == 1 and self.dispText == '0':
            self.dispText = str(buttonValue)
        else:
            self.dispText = self.dispText + str(buttonValue)  
        

        self.testDisplayer.setText(self.dispText)
        
    def _mathfunc(self,mfunction):
           
        if self.oldValue == '0':
            self.oldValue = self.newValue
        else:
            self.oldValue = str(self.finalValue)

            
        self.newValue = '0'     
        self.dispText = self.dispText+mfunction
        self.wantedFunc = mfunction
        self.testDisplayer.setText(self.dispText)



    def _equalfunc(self):

        if self.wantedFunc == '+':
            self.finalValue =int(self.oldValue) + int(self.newValue)
     
        elif self.wantedFunc == '-':
            self.finalValue =int(self.oldValue) - int(self.newValue)
        
        elif self.wantedFunc == '/':
            self.finalValue =int(self.oldValue) / int(self.newValue)
        
        elif self.wantedFunc == 'x':
            self.finalValue =int(self.oldValue) * int(self.newValue)
            
        self.testDisplayer.setText(str(self.finalValue))
        self.dispText = str(self.finalValue)
#        self.oldValue = str(self.finalValue)
        self.newValue = '0'
        
    
    def _clearVariable(self):
        self.oldValue = '0'
        self.newValue = '0'
        self.finalValue = 0
        self.dispText = '0'
        
        self.testDisplayer.setText(self.dispText)
             

def main():
    field_simulation = QApplication(sys.argv) #create new application
    field_window = Calculator() #create new instance of main window
    field_window.show() #make instance visible
    field_window.run()
    field_window.raise_() #raise instance to top of window stack
    field_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()