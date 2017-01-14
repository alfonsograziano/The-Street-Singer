#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from MusicConverter import MusicConverter
import webbrowser
from sharedpreferences import SharedPreferences
import os,sys
try:
    from PIL import Image
    import pytesseract
except ImportError:
    print("Warning, if you want to use OCR, please install PIL and pytesseract")

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


class UiMainWindow(object):
    """
    This is the main class. In this classs there are the GUI functions and the conversion functions
    The basic conversion function are read from the MusicConverter class
    """
    def setupUi(self, MainWindow):
        """
        This is the GUI setup
        Here python build all gui elements and make the MainWindow
        """
        self.preferences = SharedPreferences('temp/config.txt')
        self.converter = MusicConverter()

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(731, 758)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 731, 758))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))

        self.nameEdit = QtGui.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(10, 10, 461, 30))
        self.nameEdit.setObjectName("nameEdit")
        self.nameEdit.setPlaceholderText("Song title")

        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 461, 671))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.groupBox_7 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(500, 0, 221, 541))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))

        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 30, 131, 71))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        self.browseFromFile = QtGui.QPushButton(self.groupBox_2)
        self.browseFromFile.setGeometry(QtCore.QRect(40, 30, 88, 29))
        self.browseFromFile.setObjectName(_fromUtf8("browseFromFile"))

        # """""""""""""" SELECT FILE """"""""""""""
        self.browseFromFile.clicked.connect(self.select_file)

        self.groupBox = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox.setGeometry(QtCore.QRect(0, 100, 131, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.browseFromImage = QtGui.QPushButton(self.groupBox)
        self.browseFromImage.setGeometry(QtCore.QRect(40, 30, 88, 29))
        self.browseFromImage.setObjectName(_fromUtf8("browseFromImage"))
        self.browseFromImage.clicked.connect(self.select_image_file)

        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 180, 131, 71))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))

        self.notationComboBox = QtGui.QComboBox(self.groupBox_3)
        self.notationComboBox.setGeometry(QtCore.QRect(0, 30, 121, 25))
        self.notationComboBox.setObjectName(_fromUtf8("notationComboBox"))
        self.notationComboBox.addItem(_fromUtf8(""))
        self.notationComboBox.addItem(_fromUtf8(""))
        self.notationComboBox.addItem(_fromUtf8(""))

        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 250, 131, 71))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))

        self.sharpFlatComboBox = QtGui.QComboBox(self.groupBox_4)
        self.sharpFlatComboBox.setGeometry(QtCore.QRect(0, 30, 121, 25))
        self.sharpFlatComboBox.setObjectName(_fromUtf8("SharpFlatComboBox"))
        self.sharpFlatComboBox.addItem(_fromUtf8(""))
        self.sharpFlatComboBox.addItem(_fromUtf8(""))
        self.sharpFlatComboBox.addItem(_fromUtf8(""))

        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 350, 141, 51))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))

        self.toneComboBox = QtGui.QComboBox(self.groupBox_6)
        self.toneComboBox.setGeometry(QtCore.QRect(0, 20, 69, 25))
        self.toneComboBox.setObjectName(_fromUtf8("toneComboBox"))
        self.toneComboBox.addItem(_fromUtf8(""))
        self.toneComboBox.addItem(_fromUtf8(""))
        self.toneComboBox.addItem(_fromUtf8(""))
        self.toneComboBox.addItem(_fromUtf8(""))
        self.toneComboBox.addItem(_fromUtf8(""))
        self.toneComboBox.addItem(_fromUtf8(""))
        self.toneComboBox.addItem(_fromUtf8(""))
        self.toneComboBox.addItem(_fromUtf8(""))
        self.toneComboBox.addItem(_fromUtf8(""))
        self.toneComboBox.addItem(_fromUtf8(""))
        self.toneComboBox.addItem(_fromUtf8(""))
        self.toneComboBox.addItem(_fromUtf8(""))
        self.toneComboBox.addItem(_fromUtf8(""))

        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 440, 401, 1301))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))

        self.convert = QtGui.QPushButton(self.groupBox_5)
        self.convert.setGeometry(QtCore.QRect(0, 30, 88, 29))
        self.convert.setObjectName(_fromUtf8("convert"))

        # """""""""""""""" CONVERSION BUTTON """"""""""""""""
        self.convert.clicked.connect(self.conversion)

        self.saveIntoFile = QtGui.QPushButton(self.groupBox_5)
        self.saveIntoFile.setGeometry(QtCore.QRect(100, 30, 101, 29))
        self.saveIntoFile.setObjectName(_fromUtf8("saveIntoFile"))

        # """""""""""""""" SAVE INTO FILE BUTTON """"""""""""""""
        self.saveIntoFile.clicked.connect(self.save_into_file_func)

        self.readInBrowser = QtGui.QPushButton(self.groupBox_5)
        self.readInBrowser.setGeometry(QtCore.QRect(0, 70, 131, 29))
        self.readInBrowser.setObjectName(_fromUtf8("readInBrowser"))

        # """""""""""""""" VIEW INTO BROWSE BUTTON """"""""""""""""
        self.readInBrowser.clicked.connect(self.read_in_browser)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.triggered.connect(self.save_into_file_func)

        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionPreferences.setShortcut("Ctrl+P")
        self.actionPreferences.triggered.connect(self.start_preferences)

        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.triggered.connect(self.close_application)

        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "The Street Singer", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Properties", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Load from text file", None))
        self.browseFromFile.setText(_translate("MainWindow", "Browse...", None))
        self.groupBox.setTitle(_translate("MainWindow", "Load from image", None))
        self.browseFromImage.setText(_translate("MainWindow", "Browse...", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Convert notation into:", None))
        self.notationComboBox.setItemText(0, _translate("MainWindow", "null", None))
        self.notationComboBox.setItemText(1, _translate("MainWindow", "Italian notation", None))
        self.notationComboBox.setItemText(2, _translate("MainWindow", "English notation", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Convert into:", None))
        self.sharpFlatComboBox.setItemText(0, _translate("MainWindow", "null", None))
        self.sharpFlatComboBox.setItemText(1, _translate("MainWindow", "Sharp", None))
        self.sharpFlatComboBox.setItemText(2, _translate("MainWindow", "Flat", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Tone conversion", None))
        self.toneComboBox.setItemText(0, _translate("MainWindow", "null", None))
        self.toneComboBox.setItemText(1, _translate("MainWindow", "do", None))
        self.toneComboBox.setItemText(2, _translate("MainWindow", "do#", None))
        self.toneComboBox.setItemText(3, _translate("MainWindow", "re", None))
        self.toneComboBox.setItemText(4, _translate("MainWindow", "re#", None))
        self.toneComboBox.setItemText(5, _translate("MainWindow", "mi", None))
        self.toneComboBox.setItemText(6, _translate("MainWindow", "fa", None))
        self.toneComboBox.setItemText(7, _translate("MainWindow", "fa#", None))
        self.toneComboBox.setItemText(8, _translate("MainWindow", "sol", None))
        self.toneComboBox.setItemText(9, _translate("MainWindow", "sol#", None))
        self.toneComboBox.setItemText(10, _translate("MainWindow", "la", None))
        self.toneComboBox.setItemText(11, _translate("MainWindow", "la#", None))
        self.toneComboBox.setItemText(12, _translate("MainWindow", "si", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Convert and save", None))
        self.convert.setText(_translate("MainWindow", "CONVERT", None))
        self.saveIntoFile.setText(_translate("MainWindow", "SAVE INTO FILE", None))
        self.readInBrowser.setText(_translate("MainWindow", "READ IN BROWSER", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionSave.setText(_translate("MainWindow", "Save into file", None))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))

    def start_preferences(self):
        os.system("python preferences.py")

    def modifycss(self):
        note_color = self.preferences.getDataFromName("in-browser_notes_color")
        note_size = self.preferences.getDataFromName("in-browser_notes_font_size")

        line_color = self.preferences.getDataFromName("in-browser_line_color")
        line_size = self.preferences.getDataFromName("in-browser_line_font_size")

        with open("temp/style.css", "r+") as f:
            lines = f.read().splitlines()
            f.seek(0)

            lines[1] = "size: " + note_size + "px;"
            lines[2] = "color: " + note_color + ";"
            lines[8] = "size: " + line_size + "px;"
            lines[9] = "color: " + line_color + ";"

            text = ""
            for i in lines:
                text += i + "\n"

            f.write(text)

    def read_in_browser(self):
        print("I'm reading... wait")
        self.modifycss()
        new = 2
        url = os.path.dirname(os.path.abspath(__file__)) + "/temp/web-file.html"

        if self.nameEdit.text():
            title = str(self.nameEdit.text().toUtf8()).decode("utf-8")
        else:
            title = "Code generated by The Street Singer"

        opentext = """
        <html>
            <head>
                <meta charset="utf-8">
                <title>{}</title>
                <link rel="stylesheet" type="text/css" href="style.css">
            </head>
            <body>
                <pre>
        """.format(title.encode("utf-8"))

        endtext = """
                </pre>
            </body>
        </html>
        """

        mytext = str(self.textEdit.toPlainText().toUtf8()).decode("utf-8")
        text_list = mytext.encode('utf-8').splitlines()
        new_list = []

        for f in text_list:
            if self.converter.is_note_line(f):
                line = "<div class='note'>" + f + "</div>"
            else:
                line = "<div class='text'>" + f + "</div>"
            new_list.append(line)

        modtext = ""
        for f in new_list:
            modtext += f + "\n"

        with open(url, "w") as f:
            text = str(opentext + modtext + endtext).decode('utf-8')
            f.write(text.encode('utf-8'))

        webbrowser.open(url, new=new)

    def close_application(self):
        """
        This function close the program, you can close it by ckicking into the menu voice or with Ctrl + Q
        """
        sys.exit()

    def onResize(self, event):
        pass

    def conversion(self):
        firstline = True
        tonedifference = 0.00
        newtone = unicode(self.toneComboBox.currentText())
        mytext = unicode(self.textEdit.toPlainText())
        italian_english = unicode(self.notationComboBox.currentText())
        float_sharp = unicode(self.sharpFlatComboBox.currentText())
        mylist = mytext.splitlines()

        print("notation conversion: " + italian_english)
        print("sharp/flat conversion: " + float_sharp)
        print("######## START CONVERSION ########")

        convertedtext = []
        for f in mylist:
            if self.converter.is_note_line(f.lower()):
                line = f.lower()
                if firstline:
                    lasttone = self.converter.get_first_note(line.split(" "))  # trovo la prima nota
                    note1 = self.converter.convert_f_to_s(lasttone)
                    convertednote = self.converter.convert_english_to_italian(note1)

                    if newtone != "null":
                        tonedifference = self.converter.find_modifier(convertednote, newtone)
                    else:
                        tonedifference = 0.00

                    print("Current note: " + lasttone)
                    print("New tone: " + newtone)
                    print("Tone difference: " + str(tonedifference))
                    firstline = False

                list_line = self.converter.get_note_list(line)
                newlist = []
                for i in list_line:
                    newlist.append(self.converter.convert_english_to_italian(self.converter.convert_f_to_s(i)))

                convertednotelist = []

                for l in newlist:
                    if l == " ":
                        convertednotelist.append("  ")
                    if newtone != "null":
                        try:
                            convertednote = self.converter.convert(l.lower(), tonedifference)
                            convertednotelist.append(convertednote)
                            convertednotelist.append(" ")
                        except:
                            pass
                    else:
                        convertednotelist.append(l)
                        convertednotelist.append(" ")

                if unicode(self.notationComboBox.currentText()) == "Italian notation":
                    convertednotelist = self.converter.convert_list_into_italian_notation(convertednotelist)

                if unicode(self.notationComboBox.currentText()) == "English notation":
                    convertednotelist = self.converter.convert_list_into_english_notation(convertednotelist)

                if unicode(self.sharpFlatComboBox.currentText()) == "Sharp":
                    convertednotelist = self.converter.convert_list_into_sharp(convertednotelist)

                if unicode(self.sharpFlatComboBox.currentText()) == "Flat":
                    convertednotelist = self.converter.convert_list_into_flat(convertednotelist)

                newline = "".join(convertednotelist)  # rendo la lista una volta convertita nuovamente una stringa

                # aggiungi al testo convertito la linea modificata
                color = self.preferences.getDataFromName("in-window_notes_color")
                size = int(int(self.preferences.getDataFromName("in-window_notes_font_size"))/3)
                convertedtext.append('<font color="{}">'.format(color) +
                                     newline.replace(" ", "&nbsp;") + '</font><br></br>')

            else:
                color = self.preferences.getDataFromName("in-window_line_color")
                size = int(int(self.preferences.getDataFromName("in-window_notes_font_size")) / 3)
                convertedtext.append('<font color="{}">'.format(color) +
                                     f.replace(" ", "&nbsp;") + '</font><br></br>')

        self.textEdit.setHtml("".join(convertedtext))
        print("######## END CONVERSION ########")

    def save_into_file_func(self):
        """
        This funcion save into a file the text (converted or not).
        Text is taken from an editText.
        The filename is recommended by the program from the Song name
        """
        filename = str(self.nameEdit.text().toUtf8()).decode("utf-8")
        text = str(self.textEdit.toPlainText().toUtf8()).decode("utf-8")
        name = QtGui.QFileDialog.getSaveFileName(None, 'Save File',filename + ".txx")

        if name != "":
            with open(str(name.toUtf8()).decode("utf-8"), "w") as f:
                f.write(text.encode('utf-8'))

    def select_file(self):
        """
        This function select a file and put his content into a simple textEdit
        """
        filename = QtGui.QFileDialog.getOpenFileName()
        self.nameEdit.setText(os.path.basename(str(filename.toUtf8()).decode("utf-8")))
        with open(filename) as f:
            self.textEdit.setText(f.read())

    def select_image_file(self):
        """
        This function select an image and put the ocr result into a simple textEdit
        """
        try:
            filename = QtGui.QFileDialog.getOpenFileName()
            image = pytesseract.image_to_string(Image.open(str(filename)))
            self.textEdit.setText(image)
            print("Image correctly read")
        except:
            print("Error in load image, please install pytesseract and PIL")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.resizeEvent = ui.onResize
    MainWindow.show()
    sys.exit(app.exec_())