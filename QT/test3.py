from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
import random

app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('电赛上位机')

labelEdit_1 = QLabel(window)
labelEdit_1.setText("温度:")
labelEdit_1.move(10, 25)

textEdit_1 = QLineEdit(window)
textEdit_1.setText(str(random.randint(0, 9)))
textEdit_1.move(50, 25)

labelEdit_2 = QLabel(window)
labelEdit_2.setText("距离:")
labelEdit_2.move(10, 125)

textEdit_2 = QLineEdit(window)
# tEdit.setPlaceholderText("请输入薪资表")
textEdit_2.setText(str(random.randint(0, 9)))
textEdit_2.move(50, 125)

labelEdit_2 = QLabel(window)
labelEdit_2.setText("步数:")
labelEdit_2.move(10, 225)

textEdit_2 = QLineEdit(window)
# tEdit.setPlaceholderText("请输入薪资表")
textEdit_2.setText(str(random.randint(0, 9)))
textEdit_2.move(50, 225)

labelEdit_2 = QLabel(window)
labelEdit_2.setText("心率:")
labelEdit_2.move(10, 325)

textEdit_2 = QLineEdit(window)
# tEdit.setPlaceholderText("请输入薪资表")
textEdit_2.setText(str(random.randint(0, 9)))
textEdit_2.move(50, 325)

window.show()

app.exec_()
