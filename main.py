from PyQt5.QtWidgets import *

app = QApplication([])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")


main = MainWindow()
main.show()
app.exec()
