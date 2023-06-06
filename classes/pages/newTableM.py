import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTabWidget, QToolBar, QAction, QTextEdit, QHBoxLayout, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Интерфейс")
        self.setGeometry(500, 200, 1000, 600)

        self.toolbar = QToolBar()
        self.toolbar.setMovable(False)
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)

        self.my_tables_button = QAction(QIcon(), "Мои таблицы", self)
        self.my_tables_button.setShortcut("Ctrl+T")
        self.my_tables_button.triggered.connect(self.on_my_tables)

        self.exit_button = QAction(QIcon(), "Выход", self)
        self.exit_button.setShortcut("Ctrl+Q")
        self.exit_button.triggered.connect(self.on_exit)

        self.toolbar.addAction(self.my_tables_button)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.exit_button)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.add_tab_button = QPushButton("Добавить лист", self)
        self.add_tab_button.setStyleSheet("background-color: purple; color: black;")
        self.add_tab_button.clicked.connect(self.add_tab)

        self.remove_tab_button = QPushButton("Удалить лист", self)
        self.remove_tab_button.setStyleSheet("background-color: purple; color: black;")
        self.remove_tab_button.clicked.connect(self.remove_tab)

        self.toolbar.addWidget(self.add_tab_button)
        self.toolbar.addWidget(self.remove_tab_button)

        iconM = QtGui.QIcon()
        iconM.addPixmap(QtGui.QPixmap("img/coolhat.png"),
        QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(iconM)

    def on_my_tables(self):
        # Здесь добавьте функциональность кнопки "Мои таблицы"
        pass

    def on_exit(self):
        self.close()

    def add_tab(self):
        new_tab = UI_table()
        self.tabs.addTab(new_tab, f"Лист {self.tabs.count() + 1}")

    def remove_tab(self):
        if self.tabs.count() > 0:
            self.tabs.removeTab(self.tabs.currentIndex())


class UI_table(QWidget):
    def __init__(self):
        super(Tab, self).__init__()

        self.layout = QHBoxLayout()

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_contents = QWidget()
        self.scroll_area.setWidget(self.scroll_area_contents)

        self.columns_layout = QHBoxLayout()
        self.scroll_area_contents.setLayout(self.columns_layout)

        self.add_column_button = QPushButton("Добавить столбец", self)
        self.add_column_button.clicked.connect(self.add_column)

        self.remove_column_button = QPushButton("Удалить столбец", self)
        self.remove_column_button.clicked.connect(self.remove_column)

        self.layout.addWidget(self.scroll_area)
        self.layout.addWidget(self.add_column_button)
        self.layout.addWidget(self.remove_column_button)

        self.setLayout(self.layout)

    def add_column(self):
        column = Column()
        self.columns_layout.addWidget(column)

    def remove_column(self):
        if self.columns_layout.count() > 0:
            column = self.columns_layout.itemAt(self.columns_layout.count() - 1).widget()
            self.columns_layout.removeWidget(column)
            column.deleteLater()


class Column(QWidget):
    def __init__(self):
        super(Column, self).__init__()

        self.layout = QVBoxLayout()

        self.add_card_button = QPushButton("Добавить карточку", self)
        self.add_card_button.clicked.connect(self.add_card)

        self.remove_card_button = QPushButton("Удалить карточку", self)
        self.remove_card_button.clicked.connect(self.remove_card)

        self.layout.addWidget(self.add_card_button)
        self.layout.addWidget(self.remove_card_button)

        self.setLayout(self.layout)

    def add_card(self):
        card = QTextEdit()
        card.setStyleSheet("background-color: cyan;")
        self.layout.addWidget(card)

    def remove_card(self):
        if self.layout.count() > 2:
            card = self.layout.itemAt(self.layout.count() - 1).widget()
            self.layout.removeWidget(card)
            card.deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())