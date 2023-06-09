# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page5.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1643, 797)
        self.Table = QtWidgets.QWidget(Form)
        self.Table.setGeometry(QtCore.QRect(30, 100, 371, 591))
        self.Table.setStyleSheet("border:2px solid #000000;\n"
                                 "background-color: rgb(0, 255, 255);")
        self.Table.setObjectName("Table")
        self.plus_card_Button = QtWidgets.QPushButton(self.Table)
        self.plus_card_Button.setGeometry(QtCore.QRect(0, 160, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.plus_card_Button.setFont(font)
        self.plus_card_Button.setStyleSheet("border:2px solid #000000;\n"
                                            "background-color: rgb(255, 255, 255);")
        self.plus_card_Button.setObjectName("plus_card_Button")
        self.minus_card_Button = QtWidgets.QPushButton(self.Table)
        self.minus_card_Button.setGeometry(QtCore.QRect(170, 160, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.minus_card_Button.setFont(font)
        self.minus_card_Button.setStyleSheet("border:2px solid #000000;\n"
                                             "background-color: rgb(255, 255, 255);")
        self.minus_card_Button.setObjectName("minus_card_Button")

        self.scroll_area = QtWidgets.QScrollArea(self.Table)
        self.scroll_area.setGeometry(QtCore.QRect(0, 0, 371, 161))
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")

        self.cards_widget = QtWidgets.QWidget()
        self.cards_widget.setGeometry(QtCore.QRect(0, 0, 361, 1000))
        self.cards_widget.setObjectName("cards_widget")

        self.cards_layout = QtWidgets.QVBoxLayout(self.cards_widget)
        self.cards_layout.setSpacing(10)
        self.cards_layout.setObjectName("cards_layout")

        self.scroll_area.setWidget(self.cards_widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect buttons
        self.plus_card_Button.clicked.connect(self.add_card)
        self.minus_card_Button.clicked.connect(self.remove_card)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.plus_card_Button.setText(_translate("Form", "+"))
        self.minus_card_Button.setText(_translate("Form", "-"))

    def add_card(self):
        new_card = QtWidgets.QPlainTextEdit()
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        new_card.setFont(font)
        new_card.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cards_layout.addWidget(new_card)

    def remove_card(self):
        if self.cards_layout.count() > 0:
            card_to_remove = self.cards_layout.takeAt(self.cards_layout.count() - 1)
            card_to_remove.widget().deleteLater()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())