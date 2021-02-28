import PyQt5

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)


class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

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

        layout = QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(radioButton3)
        layout.addWidget(checkBox)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)    

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Some sample buttons")

        nameLabel_1 = QLabel(self)
        nameLabel_1.setText('Read Braille:')
        line_1 = QLineEdit(self)
        line_1.setText("test")

        nameLabel_2 = QLabel(self)
        nameLabel_2.setText('Activate Arduino:')
        line_2 = QLineEdit(self)

        nameLabel_3 = QLabel(self)
        nameLabel_3.setText('Navgiation:')
        line_3 = QLineEdit(self)

        nameLabel_4 = QLabel(self)
        nameLabel_4.setText('Acccessibility:')
        line_4 = QLineEdit(self)
        
        nameLabel_5 = QLabel(self)
        nameLabel_5.setText('Hierarchy:')
        line_5 = QLineEdit(self)

        nameLabel_6 = QLabel(self)
        nameLabel_6.setText('Minus Index:')
        line_6 = QLineEdit(self)

        nameLabel_7 = QLabel(self)
        nameLabel_7.setText('Plus Index:')
        line_7 = QLineEdit(self)

        nameLabel_8 = QLabel(self)
        nameLabel_8.setText('Speak:')
        line_8 = QLineEdit(self)

        
        nameLabel_9 = QLabel(self)
        nameLabel_9.setText('Braille Read Quit:')
        line_9 = QLineEdit(self)


        nameLabel_10 = QLabel(self)
        nameLabel_10.setText('Braille Read Contiue:')
        line_10 = QLineEdit(self)

        layout = QVBoxLayout()
        layout.addWidget(nameLabel_1)
        layout.addWidget(line_1)
        layout.addWidget(nameLabel_2)
        layout.addWidget(line_2)
        layout.addWidget(nameLabel_3)
        layout.addWidget(line_3)
        layout.addWidget(nameLabel_4)
        layout.addWidget(line_4)
        layout.addWidget(nameLabel_5)
        layout.addWidget(line_5)
        layout.addWidget(nameLabel_6)
        layout.addWidget(line_6)
        layout.addWidget(nameLabel_7)
        layout.addWidget(line_7)
        layout.addWidget(nameLabel_8)
        layout.addWidget(line_8)
        layout.addWidget(nameLabel_9)
        layout.addWidget(line_9)
        layout.addWidget(nameLabel_10)
        layout.addWidget(line_10)
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Ignored)

        tab1 = QWidget()
        tableWidget = QTableWidget(10, 10)

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)

        tab2 = QWidget()
        textEdit = QTextEdit()

        textEdit.setPlainText("Test your Braille display and audio output. \n Enter sample text here.\n")

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

        self.bottomLeftTabWidget.addTab(tab2, "Calibrate")

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Audio Speed")


        lineEdit = QLineEdit('s3cRe7')
        lineEdit.setEchoMode(QLineEdit.Password)

        spinBox = QSpinBox(self.bottomRightGroupBox)
        spinBox.setValue(50)

        slider = QSlider(Qt.Horizontal, self.bottomRightGroupBox)
        slider.setValue(40)

        scrollBar = QScrollBar(Qt.Horizontal, self.bottomRightGroupBox)
        scrollBar.setValue(60)

        dial = QDial(self.bottomRightGroupBox)
        dial.setValue(30)
        dial.setNotchesVisible(True)

        layout = QGridLayout()
        layout.addWidget(spinBox, 1, 0, 1, 2)
        layout.addWidget(slider, 3, 0)
        layout.addWidget(scrollBar, 4, 0)
        layout.addWidget(dial, 3, 1, 2, 1)
        self.bottomRightGroupBox.setLayout(layout)

    



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_()) 