#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sharedpreferences import SharedPreferences
from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.preferences = SharedPreferences("temp/config.txt")

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(565, 282)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 80, 242, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)

        self.w_note_color = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.w_note_color.setText(_fromUtf8(""))
        self.w_note_color.setObjectName(_fromUtf8("w_note_color"))
        self.w_note_color.clicked.connect(lambda:  self.select_color("wn")) #window note

        self.horizontalLayout.addWidget(self.w_note_color)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 120, 241, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)

        self.w_note_font = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.w_note_font.setObjectName(_fromUtf8("w_note_font"))
        self.horizontalLayout_2.addWidget(self.w_note_font)
        self.w_note_font.clicked.connect(lambda:  self.select_font("wn")) #window line


        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 20, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(310, 120, 242, 41))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_7 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)

        self.pushButton_5 = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        self.pushButton_5.clicked.connect(lambda: self.select_font("bn"))


        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(310, 80, 242, 41))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_8 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_6.addWidget(self.label_8)

        self.pushButton_6 = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_6.setText(_fromUtf8(""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_6.addWidget(self.pushButton_6)
        self.pushButton_6.clicked.connect(lambda:  self.select_color("bn")) #button note


        self.horizontalLayoutWidget_5 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(30, 210, 241, 41))
        self.horizontalLayoutWidget_5.setObjectName(_fromUtf8("horizontalLayoutWidget_5"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_9 = QtGui.QLabel(self.horizontalLayoutWidget_5)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_7.addWidget(self.label_9)

        self.w_line_font = QtGui.QPushButton(self.horizontalLayoutWidget_5)
        self.w_line_font.setObjectName(_fromUtf8("w_line_font"))
        self.horizontalLayout_7.addWidget(self.w_line_font)
        self.w_line_font.clicked.connect(lambda: self.select_font("wl"))


        self.horizontalLayoutWidget_6 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(30, 170, 242, 41))
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_10 = QtGui.QLabel(self.horizontalLayoutWidget_6)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_8.addWidget(self.label_10)

        self.w_line_color = QtGui.QPushButton(self.horizontalLayoutWidget_6)
        self.w_line_color.setText(_fromUtf8(""))
        self.w_line_color.setObjectName(_fromUtf8("w_line_color"))
        self.horizontalLayout_8.addWidget(self.w_line_color)
        self.w_line_color.clicked.connect(lambda:  self.select_color("wl")) #window line


        self.horizontalLayoutWidget_7 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(310, 210, 241, 41))
        self.horizontalLayoutWidget_7.setObjectName(_fromUtf8("horizontalLayoutWidget_7"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_11 = QtGui.QLabel(self.horizontalLayoutWidget_7)
        self.label_11.setObjectName(_fromUtf8("label_11"))

        self.horizontalLayout_9.addWidget(self.label_11)
        self.pushButton_9 = QtGui.QPushButton(self.horizontalLayoutWidget_7)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.horizontalLayout_9.addWidget(self.pushButton_9)
        self.pushButton_9.clicked.connect(lambda: self.select_font("bl"))

        self.horizontalLayoutWidget_8 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(310, 170, 242, 41))
        self.horizontalLayoutWidget_8.setObjectName(_fromUtf8("horizontalLayoutWidget_8"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_12 = QtGui.QLabel(self.horizontalLayoutWidget_8)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_10.addWidget(self.label_12)

        self.pushButton_10 = QtGui.QPushButton(self.horizontalLayoutWidget_8)
        self.pushButton_10.setText(_fromUtf8(""))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.horizontalLayout_10.addWidget(self.pushButton_10)
        self.pushButton_10.clicked.connect(lambda:  self.select_color("bl"))

        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.horizontalLayoutWidget_4.raise_()
        self.horizontalLayoutWidget_5.raise_()
        self.horizontalLayoutWidget_6.raise_()
        self.horizontalLayoutWidget_7.raise_()
        self.horizontalLayoutWidget_8.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.set_up_colors()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def select_color(self, caller):
        print("Caller:" + caller)
        color = QtGui.QColorDialog.getColor()

        if caller == "wn":
            self.preferences.setDataFromName("in-window_notes_color", color.name())
        elif caller == "wl":
            self.preferences.setDataFromName("in-window_line_color", color.name())
        elif caller == "bn":
            self.preferences.setDataFromName("in-browser_notes_color", color.name())
        elif caller == "bl":
            self.preferences.setDataFromName("in-browser_line_color", color.name())

        self.set_up_colors()

    def select_font(self, caller):
        print("Caller:" + caller)
        font, valid = QtGui.QFontDialog.getFont()
        caller_name = ""

        if caller == "wn":
            caller_name = "in-window_notes_font_"
        elif caller == "wl":
            caller_name = "in-window_line_font_"
        elif caller == "bn":
            caller_name = "in-browser_notes_font_"
        elif caller == "bl":
            caller_name = "in-browser_line_font_"

        print(caller_name)
        self.preferences.setDataFromName(caller_name + "size", str(font.pointSize()))
        self.preferences.setDataFromName(caller_name + "family", font.family())

    def set_up_colors(self):
        self.w_note_color.setStyleSheet("background-color: " + self.preferences.getDataFromName('in-window_notes_color'))
        self.w_line_color.setStyleSheet("background-color: " + self.preferences.getDataFromName('in-window_line_color'))
        self.pushButton_6.setStyleSheet("background-color: " + self.preferences.getDataFromName('in-browser_notes_color'))
        self.pushButton_10.setStyleSheet("background-color: " + self.preferences.getDataFromName('in-browser_line_color'))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Preferences", None))
        self.label.setText(_translate("MainWindow", "in-window note color      ", None))
        self.label_2.setText(_translate("MainWindow", "in-window note font       ", None))
        self.w_note_font.setText(_translate("MainWindow", "SELECT FONT", None))
        self.label_5.setText(_translate("MainWindow", "in-windows preferences", None))
        self.label_6.setText(_translate("MainWindow", "in-browser preferences", None))
        self.label_7.setText(_translate("MainWindow", "in-browser note font       ", None))
        self.pushButton_5.setText(_translate("MainWindow", "SELECT FONT", None))
        self.label_8.setText(_translate("MainWindow", "in-browser note color     ", None))
        self.label_9.setText(_translate("MainWindow", "in-window line font       ", None))
        self.w_line_font.setText(_translate("MainWindow", "SELECT FONT", None))
        self.label_10.setText(_translate("MainWindow", "in-window line color     ", None))
        self.label_11.setText(_translate("MainWindow", "in-browser line font       ", None))
        self.pushButton_9.setText(_translate("MainWindow", "SELECT FONT", None))
        self.label_12.setText(_translate("MainWindow", "in-browser line color     ", None))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())