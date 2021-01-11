import sys
import st2
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = st2.Ui_MainWindow()
ui.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec_())
