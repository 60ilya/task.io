# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(510, 343)
        SettingsWindow.setStyleSheet("")
        self.settingswidget = QtWidgets.QWidget(SettingsWindow)
        self.settingswidget.setStyleSheet("border: 10px solid #FF00FF;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.settingswidget.setObjectName("settingswidget")
        self.whiteradio = QtWidgets.QRadioButton(self.settingswidget)
        self.whiteradio.setGeometry(QtCore.QRect(30, 60, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.whiteradio.setFont(font)
        self.whiteradio.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.whiteradio.setObjectName("whiteradio")
        self.fioletradio = QtWidgets.QRadioButton(self.settingswidget)
        self.fioletradio.setGeometry(QtCore.QRect(160, 60, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.fioletradio.setFont(font)
        self.fioletradio.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.fioletradio.setObjectName("fioletradio")
        self.biruzradio = QtWidgets.QRadioButton(self.settingswidget)
        self.biruzradio.setGeometry(QtCore.QRect(340, 60, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.biruzradio.setFont(font)
        self.biruzradio.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.biruzradio.setObjectName("biruzradio")
        self.colorlabel = QtWidgets.QLabel(self.settingswidget)
        self.colorlabel.setGeometry(QtCore.QRect(10, 10, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.colorlabel.setFont(font)
        self.colorlabel.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.colorlabel.setObjectName("colorlabel")
        self.imagelabel = QtWidgets.QLabel(self.settingswidget)
        self.imagelabel.setGeometry(QtCore.QRect(10, 100, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.imagelabel.setFont(font)
        self.imagelabel.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.imagelabel.setObjectName("imagelabel")
        self.ImageButton = QtWidgets.QPushButton(self.settingswidget)
        self.ImageButton.setGeometry(QtCore.QRect(40, 150, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.ImageButton.setFont(font)
        self.ImageButton.setStyleSheet("border: 5px solid #FF00FF;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.ImageButton.setObjectName("ImageButton")
        self.personlabel = QtWidgets.QLabel(self.settingswidget)
        self.personlabel.setGeometry(QtCore.QRect(10, 216, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.personlabel.setFont(font)
        self.personlabel.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.personlabel.setObjectName("personlabel")
        self.person_text = QtWidgets.QTextEdit(self.settingswidget)
        self.person_text.setGeometry(QtCore.QRect(10, 260, 401, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.person_text.setFont(font)
        self.person_text.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.person_text.setObjectName("person_text")
        self.settingscontinue = QtWidgets.QPushButton(self.settingswidget)
        self.settingscontinue.setGeometry(QtCore.QRect(410, 260, 93, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.settingscontinue.setFont(font)
        self.settingscontinue.setObjectName("settingscontinue")
        SettingsWindow.setCentralWidget(self.settingswidget)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "MainWindow"))
        self.whiteradio.setText(_translate("SettingsWindow", "белый"))
        self.fioletradio.setText(_translate("SettingsWindow", "фиолетовый"))
        self.biruzradio.setText(_translate("SettingsWindow", "бирюзовый"))
        self.colorlabel.setText(_translate("SettingsWindow", "Выберите цвет"))
        self.imagelabel.setText(_translate("SettingsWindow", "Добавить изображение"))
        self.ImageButton.setText(_translate("SettingsWindow", "image"))
        self.personlabel.setText(_translate("SettingsWindow", "Автор карточки"))
        self.settingscontinue.setText(_translate("SettingsWindow", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsWindow = QtWidgets.QMainWindow()
    ui = Ui_SettingsWindow()
    ui.setupUi(SettingsWindow)
    SettingsWindow.show()
    sys.exit(app.exec_())