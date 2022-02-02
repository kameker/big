import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_qt import Ui_Form


# Создание главного стартового окна
class Main(QMainWindow, Ui_Form):
    # инициальзация
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show_button.clicked.connect(self.show_fun)

    def show_fun(self):
        data = (self.x_text.toPlainText(), self.y_text.toPlainText(), self.scale_text.toPlainText())
        return data



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# запуск
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
