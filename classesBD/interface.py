import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTabWidget, QToolBar, QAction, QTextEdit, QHBoxLayout, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from pages.authorisation import UI_authorisation
from pages.mainMenu import UI_mainMenu
from pages.registration import UI_registration
from pages.account import UI_account
from pages.surprise import UI_surprise
from pages.newTableM import UI_table
from pages.myTables import UI_myTables

from user import User


class MainMenu(QtWidgets.QMainWindow, UI_mainMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.registrationButton.clicked.connect(self.signUpPage)
        self.authorizationButton.clicked.connect(self.nextpage) 
    
    def nextpage(self):
        self.authorisationPage = SignInPage()
        self.authorisationPage.show()
        self.close()

    def signUpPage(self):
        self.signUp = SignUpPage()
        self.signUp.show()
        self.close()
    
class SignInPage(QtWidgets.QMainWindow, UI_authorisation):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushbutton_init()
        self.lineedit_init()
        self.backButton.clicked.connect(self.backPage)
        self.surpriseButton.clicked.connect(self.openSurprise)

    def pushbutton_init(self):
        self.continueButton.setEnabled(False)
        self.continueButton.clicked.connect(self.openPage6)

    def lineedit_init(self):
        self.emptyspace2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.emptyspace1.textChanged.connect(self.check_input_func)
        self.emptyspace2.textChanged.connect(self.check_input_func)

    def check_input_func(self):
        if self.emptyspace1.text() and \
           self.emptyspace2.text() :
            self.continueButton.setEnabled(True)
        else:
            self.continueButton.setEnabled(False)

    def openPage6(self):
        self.page6 = Page6(self.user_data())
        self.page6.show()
        self.close()
    
    def backPage(self):
        self.mainMenu = MainMenu()
        self.mainMenu.show()
        self.close()

    def openSurprise(self):
        self.s = Surprise()
        self.s.show()
        self.close()

class SignUpPage(QtWidgets.QMainWindow, UI_registration):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushbutton_init()
        self.lineedit_init()
        self.backButton.clicked.connect(self.backPage)
        self.surpriseButton.clicked.connect(self.openSurprise)

    def pushbutton_init(self):
        # self.continueButton.setEnabled(False)
        self.continueButton.clicked.connect(self.openPage6)

    def lineedit_init(self):
        self.emptyspace2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.emptyspace3.setEchoMode(QtWidgets.QLineEdit.Password)

        self.emptyspace1.textChanged.connect(self.check_input_func)
        self.emptyspace2.textChanged.connect(self.check_input_func)
        self.emptyspace3.textChanged.connect(self.check_input_func)
        self.emptyspace2.textChanged.connect(self.check_input_func)
        self.emptyspace5.textChanged.connect(self.check_input_func)

    def check_input_func(self):
        if self.emptyspace1.text() and \
           self.emptyspace2.text() and \
           self.emptyspace3.text() and \
           self.emptyspace4.text() and \
           self.emptyspace2.text() == self.emptyspace3.text() and \
           self.emptyspace5.text():
            self.continueButton.setEnabled(True)
        else:
            self.continueButton.setEnabled(False)

    def openPage6(self):
        self.page6 = Page6(self.user_data())
        self.page6.show()
        self.close()

    def user_data(self):
        user = User(self.emptyspace1.text(), self.emptyspace2.text(), self.emptyspace4.text(), self.emptyspace5.text())
        return user

    def backPage(self):
        self.mainMenu = MainMenu()
        self.mainMenu.show()
        self.close()

    def openSurprise(self):
        self.s = Surprise()
        self.s.show()
        self.close()

class Page6(QtWidgets.QMainWindow, UI_account):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setupUi(self)
        self.backButton.clicked.connect(self.backPage)
        self.surpriseButton.clicked.connect(self.openSurprise2)
        self.mytableButton.clicked.connect(self.openMyTables)
        self.create_tableButton.clicked.connect(self.openNewTable)

    def backPage(self):
        self.mainMenu = MainMenu()
        self.mainMenu.show()
        self.close()

    def openSurprise2(self):
        self.s = Surprise2(self.user)
        self.s.show()
        self.close()

    def openNewTable(self):
        self.t = NewTableM(self.user)
        # self.t = NewTable()
        self.t.show()
        self.close()

    def openMyTables(self):
        self.mt = MyTables(self.user)
        self.mt.show()
        self.close()

class MyTables(QtWidgets.QMainWindow, UI_myTables):

    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setupUi(self)
        self.EscapeButton.clicked.connect(self.openPage6)

    def openPage6(self):
        self.page6 = Page6(self.user)
        self.page6.show()
        self.close()
        

class NewTableM(QMainWindow):
    def __init__(self, user):
        super(NewTableM, self).__init__()

        self.user = user

        self.setWindowTitle("Шаманские карточки")
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

        iconM = QtGui.QIcon()
        iconM.addPixmap(QtGui.QPixmap("img/coolhat.png"),
        QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.setWindowIcon(iconM)

        self.toolbar.addWidget(self.add_tab_button)
        self.toolbar.addWidget(self.remove_tab_button)

    def on_my_tables(self):
        self.mt = MyTables(self.user)
        self.mt.show()
        self.close()

    def on_exit(self):
        self.page6 = Page6(self.user)
        self.page6.show()
        self.close()

    def add_tab(self):
        new_tab = UI_table()
        self.tabs.addTab(new_tab, f"Лист {self.tabs.count() + 1}")

    def remove_tab(self):
        if self.tabs.count() > 0:
            self.tabs.removeTab(self.tabs.currentIndex())

# class NewTable(QtWidgets.QMainWindow, newTable.Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.EscapeButton.clicked.connect(self.openPage6)        
#         self.myTablesButton.clicked.connect(self.openMyTables)
#         # self.plus_card_Button.clicked.connect(card)
#         # self.card_option.clicked.connect(card)

#     def openPage6(self):
#         self.page6 = Page6()
#         self.page6.show()
#         self.close()
    
#     def openMyTables(self):
#         self.mt = MyTables()
#         self.mt.show()
#         self.close()

class Surprise(QtWidgets.QMainWindow, UI_surprise):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.backPage)

    def backPage(self):
        self.mainMenu = MainMenu()
        self.mainMenu.show()
        self.close()

class Surprise2(QtWidgets.QMainWindow, UI_surprise):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setupUi(self)
        self.backButton.clicked.connect(self.backPage)

    def backPage(self):
        self.page6 = Page6(self.user)
        self.page6.show()
        self.close()





USER_PWD = {
    'userFrom@gmail.com': 'user',
    'admin@gmail.com': 'admin'
}


class SigninPage(QtWidgets.QDialog):
    def __init__(self):
        super(SigninPage, self).__init__()
        self.signin_user_label = QtWidgets.QLabel('E-mail:')
        self.signin_pwd_label = QtWidgets.QLabel('Password:')
        self.signin_pwd2_label = QtWidgets.QLabel('Password:')
        self.signin_user_line = QtWidgets.QLineEdit()
        self.signin_pwd_line = QtWidgets.QLineEdit()
        self.signin_pwd2_line = QtWidgets.QLineEdit()
        self.signin_button = QtWidgets.QPushButton('Sign in')

        self.user_h_layout = QtWidgets.QHBoxLayout()
        self.pwd_h_layout = QtWidgets.QHBoxLayout()
        self.pwd2_h_layout = QtWidgets.QHBoxLayout()
        self.all_v_layout = QtWidgets.QVBoxLayout()

        self.lineedit_init()
        self.pushbutton_init()
        self.layout_init()

    def layout_init(self):
        self.user_h_layout.addWidget(self.signin_user_label)
        self.user_h_layout.addWidget(self.signin_user_line)
        self.pwd_h_layout.addWidget(self.signin_pwd_label)
        self.pwd_h_layout.addWidget(self.signin_pwd_line)
        self.pwd2_h_layout.addWidget(self.signin_pwd2_label)
        self.pwd2_h_layout.addWidget(self.signin_pwd2_line)

        self.all_v_layout.addLayout(self.user_h_layout)
        self.all_v_layout.addLayout(self.pwd_h_layout)
        self.all_v_layout.addLayout(self.pwd2_h_layout)
        self.all_v_layout.addWidget(self.signin_button)

        self.setLayout(self.all_v_layout)

    def lineedit_init(self):
        self.signin_pwd_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signin_pwd2_line.setEchoMode(QtWidgets.QLineEdit.Password)

        self.signin_user_line.textChanged.connect(self.check_input_func)
        self.signin_pwd_line.textChanged.connect(self.check_input_func)
        self.signin_pwd2_line.textChanged.connect(self.check_input_func)

    def pushbutton_init(self):
        self.signin_button.setEnabled(False)
        self.signin_button.clicked.connect(self.check_signin_func)

    def check_input_func(self):
        if self.signin_user_line.text() and \
           self.signin_pwd_line.text() and \
           self.signin_pwd2_line.text():
            self.signin_button.setEnabled(True)
        else:
            self.signin_button.setEnabled(False)

    def check_signin_func(self):
        if self.signin_pwd_line.text() != self.signin_pwd2_line.text():
            QtWidgets.QMessageBox.critical(self, 'Wrong', 'Two Passwords Typed Are Not Same!')
        elif self.signin_user_line.text() not in USER_PWD:
            USER_PWD[self.signin_user_line.text()] = self.signin_pwd_line.text()
            QtWidgets.QMessageBox.information(self, 'Information', 'Register Successfully')
            self.close()
        else:
            QtWidgets.QMessageBox.critical(self, 'Wrong', 'This Username Has Been Registered!')

        self.signin_user_line.clear()
        self.signin_pwd_line.clear()
        self.signin_pwd2_line.clear()


class WindowAdmin(QtWidgets.QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)
        
        self.label = QtWidgets.QLabel(f'<h1>Привет, {name}!</h1>', alignment=QtCore.AlignCenter)
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        
class WindowUser(QtWidgets.QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.resize(640, 480)        
        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)
        
        self.label = QtWidgets.QLabel(f'<h1>Привет, {name}!</h1>')
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        

class Login(QtWidgets.QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.resize(300, 100)

        self.user_label = QtWidgets.QLabel('E-mail address:', self)
        self.pwd_label = QtWidgets.QLabel('Password:', self)
        self.user_line = QtWidgets.QLineEdit(self)
        self.user_line.setClearButtonEnabled(True)
        self.pwd_line = QtWidgets.QLineEdit(self)
        self.pwd_line.setClearButtonEnabled(True)
        self.login_button = QtWidgets.QPushButton('Войти', self)
        self.signin_button = QtWidgets.QPushButton('Зарегистрироватся', self)

        self.grid_layout = QtWidgets.QGridLayout()
        self.h_layout = QtWidgets.QHBoxLayout()
        self.v_layout = QtWidgets.QVBoxLayout()

        self.lineedit_init()
        self.pushbutton_init()
        self.layout_init()
        self.signin_page = SigninPage()            

    def layout_init(self):
        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.signin_button)
        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def lineedit_init(self):
        self.user_line.setPlaceholderText('Please enter your email')
        self.pwd_line.setPlaceholderText('Please enter your password')
        self.pwd_line.setEchoMode(QtWidgets.QLineEdit.Password)

        self.user_line.textChanged.connect(self.check_input_func)
        self.pwd_line.textChanged.connect(self.check_input_func)

    def pushbutton_init(self):
        self.login_button.setEnabled(False)
        self.login_button.clicked.connect(self.check_login_func)
        self.signin_button.clicked.connect(self.show_signin_page_func)

    def check_login_func(self):
        password = USER_PWD.get(self.user_line.text())
        if password != self.pwd_line.text():
            QtWidgets.QMessageBox.critical(self, 'Wrong', 'Wrong Username or Password!')
            return
        
        user = self.user_line.text().split('@')[0]
        if user == 'admin':
            self.windowAdmin = WindowAdmin(user)
            self.windowAdmin.show()
        else:
            self.windowUser = WindowUser(user)
            self.windowUser.show()
            
        self.close()   

    def show_signin_page_func(self):
        self.signin_page.exec_()

    def check_input_func(self):
        if self.user_line.text() and self.pwd_line.text():
            self.login_button.setEnabled(True)
        else:
            self.login_button.setEnabled(False)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainMenu()
    w.show()
    sys.exit(app.exec_())