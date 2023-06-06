
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from page import Ui_MainWindow
from page2 import Ui_MainWindow2
from page3 import Ui_MainWindow3
from page4 import Ui_MainWindow4
from page5 import Ui_MainWindow5
from page6 import Ui_MainWindow6
from Card import Ui_card
from settings import Ui_SettingsWindow
from mytable import Ui_MainWindow7

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def openPage2():
    global MainWindow2
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow2)
    MainWindow.close()
    MainWindow2.show()

    def openPage1Back():
        MainWindow2.close()
        MainWindow.show()

    ui.backButton.clicked.connect(openPage1Back)

    def openPage4_1():
        global MainWindow4
        MainWindow4 = QtWidgets.QMainWindow()
        ui = Ui_MainWindow4()
        ui.setupUi(MainWindow4)
        MainWindow2.close()
        MainWindow4.show()

        def openPage2Back():
            MainWindow4.close()
            MainWindow2.show()

        ui.backButton.clicked.connect(openPage2Back)
    
    ui.surpriseButton.clicked.connect(openPage4_1)

    def openPage6():
        global MainWindow6
        MainWindow6 = QtWidgets.QMainWindow()
        ui = Ui_MainWindow6()
        ui.setupUi(MainWindow6)
        MainWindow2.close()
        MainWindow6.show()

        def openPage6Back():
            MainWindow6.close()
            MainWindow2.show()

        ui.backButton.clicked.connect(openPage6Back)

        def openPage4_2():
            global MainWindow4
            MainWindow4 = QtWidgets.QMainWindow()
            ui = Ui_MainWindow4()
            ui.setupUi(MainWindow4)
            MainWindow6.close()
            MainWindow4.show()

            def openPage6Back2():
                MainWindow4.close()
                MainWindow6.show()

            ui.backButton.clicked.connect(openPage6Back2)
    
        ui.surpriseButton.clicked.connect(openPage4_2)

        def openMyTables():
            
            global MainWindow7
            MainWindow7 = QtWidgets.QMainWindow()
            ui = Ui_MainWindow7()
            ui.setupUi(MainWindow7)
            MainWindow6.close()
            MainWindow7.show()
            
        ui.mytableButton.clicked.connect(openMyTables)

        def openPage5():
            global MainWindow5
            MainWindow5 = QtWidgets.QMainWindow()
            ui = Ui_MainWindow5()
            ui.setupUi(MainWindow5)
            MainWindow6.close()
            MainWindow5.show()

            def openPage5Back():
                MainWindow5.close()
                MainWindow6.show()

            ui.EscapeButton.clicked.connect(openPage5Back)

            def openMylistBack():
                global MainWindow7
                MainWindow7 = QtWidgets.QMainWindow()
                ui = Ui_MainWindow7()
                ui.setupUi(MainWindow7)
                MainWindow5.close()
                MainWindow7.show()
                
            ui.myTablesButton.clicked.connect(openMylistBack)

            def openCard():
                global card
                card = QtWidgets.QMainWindow()
                ui = Ui_card()
                ui.setupUi(card)
                card.show()
                
                def closeCard():
                    card.close()

                ui.nextButton.clicked.connect(closeCard)

                def openSettings():
                    global SettingsWindow
                    SettingsWindow = QtWidgets.QMainWindow()
                    ui = Ui_SettingsWindow()
                    ui.setupUi(SettingsWindow)
                    SettingsWindow.show()

                    def closeSettings():
                        SettingsWindow.close()

                    ui.settingscontinue.clicked.connect(closeSettings)
                    
                ui.SettingsButton.clicked.connect(openSettings)


            ui.card_option.clicked.connect(openCard)

        ui.create_tableButton.clicked.connect(openPage5)
        

    ui.continueButton.clicked.connect(openPage6)

    
def openPage3():
    global MainWindow3
    MainWindow3 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(MainWindow3)
    MainWindow.close()
    MainWindow3.show()

    def openPage1Back():
        MainWindow3.close()
        MainWindow.show()

    ui.backButton.clicked.connect(openPage1Back)

    def openPage4_1():
        global MainWindow4
        MainWindow4 = QtWidgets.QMainWindow()
        ui = Ui_MainWindow4()
        ui.setupUi(MainWindow4)
        MainWindow3.close()
        MainWindow4.show()

        def openPage3Back():
            MainWindow4.close()
            MainWindow3.show()

        ui.backButton.clicked.connect(openPage3Back)
    
    ui.surpriseButton.clicked.connect(openPage4_1)

    def openPage6():
        global MainWindow6
        MainWindow6 = QtWidgets.QMainWindow()
        ui = Ui_MainWindow6()
        ui.setupUi(MainWindow6)
        MainWindow3.close()
        MainWindow6.show()

        def openPage6Back():
            MainWindow6.close()
            MainWindow3.show()

        ui.backButton.clicked.connect(openPage6Back)

        def openPage4_2():
            global MainWindow4
            MainWindow4 = QtWidgets.QMainWindow()
            ui = Ui_MainWindow4()
            ui.setupUi(MainWindow4)
            MainWindow6.close()
            MainWindow4.show()

            def openPage6Back2():
                MainWindow4.close()
                MainWindow6.show()

            ui.backButton.clicked.connect(openPage6Back2)
    
        ui.surpriseButton.clicked.connect(openPage4_2)
        
        def openMyTables():
            
            global MainWindow7
            MainWindow7 = QtWidgets.QMainWindow()
            ui = Ui_MainWindow7()
            ui.setupUi(MainWindow7)
            MainWindow6.close()
            MainWindow7.show()
            
        ui.mytableButton.clicked.connect(openMyTables)
        def openPage5():
            global MainWindow5
            MainWindow5 = QtWidgets.QMainWindow()
            ui = Ui_MainWindow5()
            ui.setupUi(MainWindow5)
            MainWindow6.close()
            MainWindow5.show()

            def openPage5Back():
                MainWindow5.close()
                MainWindow6.show()

            ui.EscapeButton.clicked.connect(openPage5Back)

            def openMylistBack():
                global MainWindow7
                MainWindow7 = QtWidgets.QMainWindow()
                ui = Ui_MainWindow7()
                ui.setupUi(MainWindow7)
                MainWindow5.close()
                MainWindow7.show()
                
            ui.myTablesButton.clicked.connect(openMylistBack)

            def openCard():
                global card
                card = QtWidgets.QMainWindow()
                ui = Ui_card()
                ui.setupUi(card)
                card.show()
                
                def closeCard():
                    card.close()

                ui.nextButton.clicked.connect(closeCard)

                def openSettings():
                    global SettingsWindow
                    SettingsWindow = QtWidgets.QMainWindow()
                    ui = Ui_SettingsWindow()
                    ui.setupUi(SettingsWindow)
                    SettingsWindow.show()

                    def closeSettings():
                        SettingsWindow.close()

                    ui.settingscontinue.clicked.connect(closeSettings)
                    
                ui.SettingsButton.clicked.connect(openSettings)


            ui.card_option.clicked.connect(openCard)

        ui.create_tableButton.clicked.connect(openPage5)
        

    ui.continueButton.clicked.connect(openPage6)
    
ui.registrationButton.clicked.connect(openPage2)
ui.authorizationButton.clicked.connect(openPage3)

sys.exit(app.exec_())
