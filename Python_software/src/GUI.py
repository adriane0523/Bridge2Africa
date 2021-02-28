import PyQt5

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)
from util import *
from shortcuts import *
import json

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)
        
        self.line_1 = None
        self.line_2 = None
        self.line_3 = None
        self.line_4 = None
        self.line_5 = None
        self.line_6 = None
        self.line_7 = None
        self.line_8 = None
        self.line_9 = None
        self.line_10 = None
        self.speed = 0


        # when you want to destroy the dialog set this to True
        self._want_to_close = False
        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        styleLabel = QLabel("&Style:")
        styleLabel.setBuddy(styleComboBox)

        self.useStylePaletteCheckBox = QCheckBox("&Use style's standard palette")
        self.useStylePaletteCheckBox.setChecked(True)

        disableWidgetsCheckBox = QCheckBox("&Disable widgets")

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()


        mainLayout = QGridLayout()
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Bridge2Africa")
        self.changeStyle('Windows')

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()

    def changePalette(self):
        if (self.useStylePaletteCheckBox.isChecked()):
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(self.originalPalette)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Select Mode")

        radioButton1 = QRadioButton("Tutorial Mode")
        radioButton2 = QRadioButton("Active Mode: Both audio and Braille")
        radioButton3 = QRadioButton("Passive Mode: Braille")
        radioButton1.setChecked(True)

        checkBox = QCheckBox("Include Assessibility Rating in Search Results")
        checkBox.setTristate(True)
        checkBox.setCheckState(Qt.PartiallyChecked)

        button = QPushButton('Open Browser', self)
        button.clicked.connect(self.on_click2)

        layout = QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(radioButton3)
        layout.addWidget(button)
        layout.addWidget(checkBox)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)    

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Some sample buttons")

        shortcut  = read_shortcut()
        nameLabel_1 = QLabel(self)
        nameLabel_1.setText('Read Braille:')
        self.line_1 = QLineEdit(self)
        self.line_1.setText(shortcut["readBraille"])
 
        nameLabel_2 = QLabel(self)
        nameLabel_2.setText('Activate Arduino:')
        self.line_2 = QLineEdit(self)
        self.line_2.setText(shortcut["activateArduino"])

        nameLabel_3 = QLabel(self)
        nameLabel_3.setText('Navgiation:')
        self.line_3 = QLineEdit(self)
        self.line_3.setText(shortcut["navigation"])

        nameLabel_4 = QLabel(self)
        nameLabel_4.setText('Acccessibility:')
        self.line_4 = QLineEdit(self)
        self.line_4.setText(shortcut["accessibility"])

        nameLabel_5 = QLabel(self)
        nameLabel_5.setText('Hierarchy:')
        self.line_5 = QLineEdit(self)
        self.line_5.setText(shortcut["hierarchy"])

        nameLabel_6 = QLabel(self)
        nameLabel_6.setText('Minus Index:')
        self.line_6 = QLineEdit(self)
        self.line_6.setText(shortcut["indexMinus"])

        nameLabel_7 = QLabel(self)
        nameLabel_7.setText('Plus Index:')
        self.line_7 = QLineEdit(self)
        self.line_7.setText(shortcut["indexPlus"])

        nameLabel_8 = QLabel(self)
        nameLabel_8.setText('Speak:')
        self.line_8 = QLineEdit(self)
        self.line_8.setText(shortcut["speak"])
        
        nameLabel_9 = QLabel(self)
        nameLabel_9.setText('Braille Read Quit:')
        self.line_9 = QLineEdit(self)
        self.line_9.setText(shortcut["brailleQuit"])

        nameLabel_10 = QLabel(self)
        nameLabel_10.setText('Braille Read Continue:')
        self.line_10 = QLineEdit(self)
        self.line_10.setText(shortcut["brailleContiue"])

        layout = QVBoxLayout()
        layout.addWidget(nameLabel_1)
        layout.addWidget(self.line_1)
        layout.addWidget(nameLabel_2)
        layout.addWidget(self.line_2)
        layout.addWidget(nameLabel_3)
        layout.addWidget(self.line_3)
        layout.addWidget(nameLabel_4)
        layout.addWidget(self.line_4)
        layout.addWidget(nameLabel_5)
        layout.addWidget(self.line_5)
        layout.addWidget(nameLabel_6)
        layout.addWidget(self.line_6)
        layout.addWidget(nameLabel_7)
        layout.addWidget(self.line_7)
        layout.addWidget(nameLabel_8)
        layout.addWidget(self.line_8)
        layout.addWidget(nameLabel_9)
        layout.addWidget(self.line_9)
        layout.addWidget(nameLabel_10)
        layout.addWidget(self.line_10)
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Ignored)
                
        button = QPushButton('Save settings', self)
        button.move(100,70)
        button.clicked.connect(self.on_click)
  
        self.bottomLeftTabWidget.addTab(button, "save")

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Audio Speed")
        shortcut  = read_shortcut()

        speed_label = QLabel(self)
        speed_label.setText('Set Speed:')
        self.speed = QLineEdit(self)
        self.speed.setText(shortcut["speed"])

        layout = QVBoxLayout()
        layout.addWidget(speed_label)
        layout.addWidget(self.speed)
        self.bottomRightGroupBox.setLayout(layout)
    
    def on_click2(self):
        print(getBrowserOpen())
        if (getBrowserOpen() == False):
            on_triggered()



    def on_click(self):
        print(self.line_1.text())

        data = {
            "readBraille" : self.line_1.text(), 
            "activateArduino" : self.line_2.text(),
            "navigation": self.line_3.text(),
            "accessibility": self.line_4.text(),
            "hierarchy" : self.line_5.text(),
            "indexMinus" : self.line_6.text(),
            "indexPlus": self.line_7.text(),
            "speak" : self.line_8.text(),
            "brailleQuit" : self.line_9.text(),
            "brailleContiue":self.line_10.text(),
            "speed": self.speed.text()
            }
    
        write_json(data)
        self.close()

    # overriding the closeEvent method
    def closeEvent(self, event):
        close_driver()
        # setting text to the label
        print("Close Event Called")

      
      
