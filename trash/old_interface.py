import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from mainMenu import Ui_MainMenu
from SingUp import Ui_SingUp
from SingIn import Ui_MainWindow3
from Surprise import Ui_Surprise
from CreateTable import Ui_CreateTable
from page6 import Ui_MainWindow6
from Card import Ui_Card
from Settings import Ui_SettingsWindow
from mytable import Ui_MainWindow7

app = QtWidgets.QApplication(sys.argv)
MainMenu = QtWidgets.QMainWindow()
ui = Ui_MainMenu()
ui.setupUi(MainMenu)
MainMenu.show()

        
def singUp():
    global SingUp
    SingUp = QtWidgets.QMainWindow()
    ui = Ui_SingUp()
    ui.setupUi(SingUp)
    MainMenu.close()
    SingUp.show()

    def openMainMenuBack():
        SingUp.close()
        MainMenu.show()

    ui.backButton.clicked.connect(openMainMenuBack)
  
    ui.surpriseButton.clicked.connect(surprise)
        
    ui.continueButton.clicked.connect(openPage6)

    
def singIn():
    global SingIn
    SingIn = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(SingIn)
    MainMenu.close()
    SingIn.show()

    def openMainMenuBack():
        SingIn.close()
        MainMenu.show()

    ui.backButton.clicked.connect(openMainMenuBack)


    ui.surpriseButton.clicked.connect(surprise)       

    ui.continueButton.clicked.connect(openPage6)


def openPage6():
        global MainWindow6
        MainWindow6 = QtWidgets.QMainWindow()
        ui = Ui_MainWindow6()
        ui.setupUi(MainWindow6)

        SingIn.close() #Починить!!! ( Сделать и на SingUp )

        MainWindow6.show()

        def openMainMenuBack():
            MainWindow6.close()
            MainMenu.show()

        ui.backButton.clicked.connect(openMainMenuBack)
    
        ui.surpriseButton.clicked.connect(openPage4_2)
            
        ui.mytableButton.clicked.connect(openMyTables)

        ui.create_tableButton.clicked.connect(Table)

def Table():
    global CreateTable
    CreateTable = QtWidgets.QMainWindow()
    ui = Ui_CreateTable()
    ui.setupUi(CreateTable)
    MainWindow6.close()
    CreateTable.show()

    def createTableBack():
        CreateTable.close()
        MainWindow6.show()

    ui.EscapeButton.clicked.connect(createTableBack)
        
    ui.myTablesButton.clicked.connect(openMylistBack)

    # ui.card_option.clicked.connect(card)

    ui.plus_card_Button.clicked.connect(card)

def openMylistBack():
    global MainWindow7
    MainWindow7 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow7()
    ui.setupUi(MainWindow7)
    CreateTable.close()
    MainWindow7.show()

def card():
    global Card
    Card = QtWidgets.QMainWindow()
    ui = Ui_Card()
    ui.setupUi(Card)
    Card.show()
    
    def closeCard():
        Card.close()

    ui.nextButton.clicked.connect(closeCard)
        
    ui.SettingsButton.clicked.connect(settings)

def settings():
    global SettingsWindow
    SettingsWindow = QtWidgets.QMainWindow()
    ui = Ui_SettingsWindow()
    ui.setupUi(SettingsWindow)
    SettingsWindow.show()

    def closeSettings():
        SettingsWindow.close()

    ui.settingscontinue.clicked.connect(closeSettings)

def openMyTables():
            
    global MainWindow7
    MainWindow7 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow7()
    ui.setupUi(MainWindow7)
    MainWindow6.close()
    MainWindow7.show()

def openPage4_2():
            global surprise
            surprise = QtWidgets.QMainWindow()
            ui = Ui_Surprise()
            ui.setupUi(surprise)
            MainWindow6.close()
            surprise.show()

            def openPage6Back2():
                surprise.close()
                MainWindow6.show()

            ui.backButton.clicked.connect(openPage6Back2)

def surprise():
    global Surprise
    Surprise = QtWidgets.QMainWindow()
    ui = Ui_Surprise()
    ui.setupUi(Surprise)

    SingIn.close()
    Surprise.show()

    def openMainMenuBack():
        Surprise.close()
        MainMenu.show()

    ui.backButton.clicked.connect(openMainMenuBack)


ui.registrationButton.clicked.connect(singUp)
ui.authorizationButton.clicked.connect(singIn)   

# Выход
sys.exit(app.exec_())
