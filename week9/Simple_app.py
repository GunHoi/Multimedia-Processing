from PyQt5.QtWidgets import QMainWindow, QApplication


class simple_app_class(QMainWindow):
    def __init__(self):
        from PyQt5.uic import loadUi
        super(simple_app_class, self).__init__()
        loadUi('simple_app.ui', self)


def simple_app():
    app = QApplication([])
    window = simple_app_class()
    window.show()
    app.exec()


if __name__ == '__main__':
    simple_app()
