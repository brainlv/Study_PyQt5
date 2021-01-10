import sys
import st1
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = st1.Ui_MainWindow()
ui.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec_())
