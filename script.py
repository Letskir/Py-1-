from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton , QLabel , QVBoxLayout , QHBoxLayout
from time import sleep
from random import  randint
app=QApplication([])
main_win=QWidget()

main_win.setWindowTitle("XD")
main_win.move(randint(100,500),randint(50,500))
main_win.show()

winner = QLabel("Push to button")
winner_num=QLabel("???")
button=QPushButton("Generate")
line_v=QVBoxLayout()
line_v.addWidget(winner,alignment=Qt.AlignCenter)
line_v.addWidget(winner_num, alignment=Qt.AlignCenter)
line_v.addWidget(button, alignment=Qt.AlignCenter)
main_win.setLayout(line_v)
def show_winner():
    num=str(randint(1,100))
    winner_num.setText(num)
    winner.setText("Winner🕳")
button.clicked.connect(show_winner)



app.exec_()
