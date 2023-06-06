from PyQt5.QtWidgets import QWidget

from CartOchka import Card
from PyQt5 import QtCore, QtGui, QtWidgets
class Table(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.setStyleSheet("border:2px solid #000000;\n" "background-color: rgb(0, 255, 255);")
        self.setParent(parent)
        self.card_count = 0
        self.plus_card.clicked.connect(self.add_card)
        self.minus_card.clicked.connect(self.remove_card)

        # Кнопки добавить/удалить карточку
        self.plus_card = QtWidgets.QPushButton("+ ", self)
        self.plus_card.setGeometry(0, 0, 171, 81)
        self.plus_card.setFont(QtGui.QFont('Comic Sans MS', 30))
        self.plus_card.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.minus_card = QtWidgets.QPushButton("-", self)
        self.minus_card.setGeometry(170, 0, 201, 81)
        self.minus_card.setFont(QtGui.QFont('Comic Sans MS', 30))
        self.minus_card.setStyleSheet("background-color: rgb(255, 255, 255);")

        # Текст под кнопками
        self.plus_label = QtWidgets.QLabel("Добавить карточку", self)
        self.plus_label.setGeometry(20, 5, 141, 21)
        self.plus_label.setFont(QtGui.QFont('Comic Sans MS', 8))
        self.minus_label = QtWidgets.QLabel("Удалить карточку", self)
        self.minus_label.setGeometry(210, 5, 141, 21)


    def add_card(self):
        card = Card(self.Table)
        card.setGeometry(0, 80 + self.card_count * 166, 371, 168)
        card.setObjectName(f"card_{self.card_count}")
        self.card_count += 1


    def remove_card(self, card_number):
        card = self.findChild(QtWidgets.QWidget, f"card_{card_number}")
        card.remove_card()


    def reset_cards(self):
        self.card_count = 0