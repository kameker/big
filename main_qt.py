# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(966, 522)
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
        self.scale_text.setObjectName("scale_text")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(850, 70, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(850, 150, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(850, 230, 47, 13))
        self.label_3.setObjectName("label_3")
        self.sputnik = QtWidgets.QRadioButton(Form)
        self.sputnik.setGeometry(QtCore.QRect(800, 280, 82, 17))
        self.sputnik.setObjectName("sputnik")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(800, 310, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.show_button.setText(_translate("Form", "????????????????????"))
        self.label.setText(_translate("Form", "????????????"))
        self.label_2.setText(_translate("Form", "??????????????"))
        self.label_3.setText(_translate("Form", "??????????????"))
        self.sputnik.setText(_translate("Form", "??????????????"))
        self.radioButton_2.setText(_translate("Form", "??????????"))
