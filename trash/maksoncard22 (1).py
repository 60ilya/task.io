from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1015, 758)
        self.Table = QtWidgets.QWidget(Form)
        self.Table.setGeometry(QtCore.QRect(30, 100, 371, 591))
        self.Table.setStyleSheet("border:2px solid #000000;\n"
                                 "background-color: rgb(0, 255, 255);")
        self.Table.setObjectName("Table")
        self.plus_card_Button = QtWidgets.QPushButton(self.Table)
        self.plus_card_Button.setGeometry(QtCore.QRect(0, 0, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.plus_card_Button.setFont(font)
        self.plus_card_Button.setStyleSheet("border:2px solid #000000;\n"
                                            "background-color: rgb(255, 255, 255);")
        self.plus_card_Button.setObjectName("plus_card_Button")
        self.minus_card_Button = QtWidgets.QPushButton(self.Table)
        self.minus_card_Button.setGeometry(QtCore.QRect(170, 0, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.minus_card_Button.setFont(font)
        self.minus_card_Button.setStyleSheet("border:2px solid #000000;\n"
                                             "background-color: rgb(255, 255, 255);")
        self.minus_card_Button.setObjectName("minus_card_Button")
        self.Card = QtWidgets.QWidget(self.Table)
        self.Card.setGeometry(QtCore.QRect(0, 80, 371, 161))
        self.Card.setObjectName("Card")
        self.card_label1 = QtWidgets.QLabel(self.Table)
        self.card_label1.setGeometry(QtCore.QRect(20, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        self.card_label1.setFont(font)
        self.card_label1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-color: rgb(255, 255, 255);")
        self.card_label1.setObjectName("card_label1")
        self.card_label2 = QtWidgets.QLabel(self.Table)
        self.card_label2.setGeometry(QtCore.QRect(200, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        self.card_label2.setFont(font)
        self.card_label2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-color: rgb(255, 255, 255);")
        self.card_label2.setObjectName("card_label2")


        self.card_count = 0


        self.plus_card_Button.clicked.connect(self.add_card)
        self.minus_card_Button.clicked.connect(self.delete_card)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.plus_card_Button.setText(_translate("Form", "+"))
        self.minus_card_Button.setText(_translate("Form", "-"))
        self.card_label1.setText(_translate("Form", "Добавить карточку"))
        self.card_label2.setText(_translate("Form", "Удалить карточку"))



    def add_card(self):

        card = QtWidgets.QWidget(self.Table)
        card.setGeometry(QtCore.QRect(0, 80 + self.card_count * 161, 371, 161))
        card.setObjectName(f"card_{self.card_count}")
        self.card_count += 1

        card.setStyleSheet("background-color: rgb(0, 255, 255);\n"
                           "border: 2px solid #000000;\n"
                           "padding: 10px;")

        text_edit = QtWidgets.QPlainTextEdit(card)
        text_edit.setGeometry(QtCore.QRect(10, 30, 351, 121))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        text_edit.setFont(font)
        text_edit.setStyleSheet("background-color: rgb(255, 255, 255);")

        card_option = QtWidgets.QPushButton(card)
        card_option.setGeometry(QtCore.QRect(330, 120, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        card_option.setFont(font)
        card_option.setStyleSheet("background-color: rgb(255, 0, 255);")
        card_option.setObjectName("card_option")
        card_option = QtWidgets.QPushButton(self.Card)
        card_option.setGeometry(QtCore.QRect(330, 120, 31, 31))

        card_option.setFont(font)
        card_option.setStyleSheet("background-color: rgb(255, 0, 255);")
        card_option.setObjectName("card_option")

        text_edit.setPlainText("название карточки")
        card_option.setText("?")

        card.show()

    def delete_card(self):
        if self.card_count > 0:
            card = self.Table.findChild(QtWidgets.QWidget, f"card_{self.card_count - 1}")
            if card:
                card.deleteLater()
                self.card_count -= 1


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())