import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTabWidget, QToolBar, QAction, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Интерфейс")
        self.setGeometry(100, 100, 800, 600)

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

    def on_my_tables(self):
        # Здесь добавьте функциональность кнопки "Мои таблицы"
        pass

    def on_exit(self):
        self.close()

    def add_tab(self):
        new_tab = Tab()
        self.tabs.addTab(new_tab, f"Лист {self.tabs.count() + 1}")

    def remove_tab(self):
        if self.tabs.count() > 0:
            self.tabs.removeTab(self.tabs.currentIndex())


class Tab(QWidget):
    def __init__(self):
        super(Tab, self).__init__()

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