import random

from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(500, 500)

lbl = QLabel("Вікторина")
numberlbl = QLabel("Номер переможця")
startButton = QPushButton("дізнатись переможця")

main_line = QVBoxLayout()
main_line.addWidget(lbl)
main_line.addWidget(numberlbl)
main_line.addWidget(startButton)

window.setLayout(main_line)

def winner():
    a = random.randint(1, 10)
    numberlbl.setText(str(a))

startButton.clicked.connect(winner)

window.show()
app.exec()