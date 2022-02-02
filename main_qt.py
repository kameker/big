from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(852, 522)
        self.pictureLabel = QtWidgets.QLabel(Form)
        self.pictureLabel.setGeometry(QtCore.QRect(20, 10, 491, 491))
        self.pictureLabel.setText("")
        self.pictureLabel.setObjectName("pictureLabel")
        self.x_text = QtWidgets.QTextEdit(Form)
        self.x_text.setGeometry(QtCore.QRect(560, 60, 281, 31))
        self.x_text.setObjectName("x_text")
        self.show_button = QtWidgets.QPushButton(Form)
        self.show_button.setGeometry(QtCore.QRect(560, 440, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.show_button.setFont(font)
        self.show_button.setObjectName("show_button")
        self.y_text = QtWidgets.QTextEdit(Form)
        self.y_text.setGeometry(QtCore.QRect(560, 140, 281, 31))
        self.y_text.setObjectName("y_text")
        self.scale_text = QtWidgets.QTextEdit(Form)
        self.scale_text.setGeometry(QtCore.QRect(560, 220, 281, 31))
        self.scale_text.setObjectName("textEdit_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.show_button.setText(_translate("Form", "Отобразить"))
