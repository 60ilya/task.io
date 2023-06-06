from Tabla import Table
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel

class TabWidget(QWidget):

    def __init__(self):
        super().__init__(self)

        self.setStyleSheet("background-color: #34fafa;\n"  "border: 1 px solid  # 000000;")

        # Кнопки +/- список
        self.plus_list = QtWidgets.QPushButton("+", self)
        self.plus_list.setGeometry(210, 0, 171, 161)
        self.plus_list.setFont(QtGui.QFont('Comic Sans MS', 30))
        self.plus_list.setStyleSheet("background-color: rgb(217, 0, 217);")

        self.minus_list = QtWidgets.QPushButton("-", self)
        self.minus_list.setGeometry(380, 0, 171, 161)
        self.minus_list.setFont(QtGui.QFont('Comic Sans MS', 30))
        self.minus_list.setStyleSheet("background-color: rgb(217, 0, 217);")

        # Текст под кнопками
        self.plus_label = QtWidgets.QLabel("Добавить таблицу", self)
        self.plus_label.setGeometry(220, 20, 151, 41)
        self.minus_label = QtWidgets.QLabel("Удалить таблицу", self)
        self.minus_label.setGeometry(390, 20, 151, 41)

        # Иконка
        self.icon = QLabel(self)
        self.icon.setGeometry(10, 10, 181, 141)

        # Таблицы
        self.table1 = Table(self)
        self.layout().addWidget(self.table1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    card = QtWidgets.QMainWindow()
    ui = TabWidget()
    ui.__init__(card)
    card.show()
    sys.exit(app.exec_())