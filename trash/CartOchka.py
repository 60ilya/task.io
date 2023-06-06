from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Card(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.count = 0

    def setup(self):
        self.setObjectName(f"card_{self.count}")
        self.setGeometry(0, 80 + self.count * 166, 371, 168)
        self.setStyleSheet("background-color: rgb(0,255,255);\
                             border: 2px solid #000000;\
                             padding: 10px;")

    def create_card(self):
        self.setup()

        # Создаем QPlainTextEdit
        text_edit = QPlainTextEdit(self)
        text_edit.setGeometry(10, 17, 351, 133)
        font = QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        text_edit.setFont(font)
        text_edit.setStyleSheet("background-color: rgb(255, 255, 255);")

        # Устанавливаем начальный текст
        text_edit.setPlainText("название карточки")

        # Кнопка настроек
        option_btn = QPushButton(self)
        option_btn.setGeometry(330, 120, 31, 31)
        option_btn.setFont(font)
        option_btn.setStyleSheet("background-color: rgb(255,0, 255);")

        # Устанавливаем объекты вレйаут
        layout = QVBoxLayout(self)
        layout.addWidget(text_edit)
        layout.addWidget(option_btn)

        self.count += 1

        self.show()

    def remove_card(self):
        self.deleteLater()

