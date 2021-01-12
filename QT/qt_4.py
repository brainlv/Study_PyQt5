import sys
import st4
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = st4.Ui_MainWindow()
ui.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec_())
