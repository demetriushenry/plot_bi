import sys

from PySide2 import QtWidgets
from PySide2.QtCore import QFile, Qt
from PySide2.QtUiTools import QUiLoader


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.window = None
        self.setup_ui()

    def setup_ui(self):
        loader = QUiLoader()
        file = QFile('layouts/mainwindow.ui')
        file.open(QFile.ReadOnly)
        self.window = loader.load(file, self)
        file.close()
        self.window.show()


if __name__ == "__main__":
    QtWidgets.QApplication.setQuitOnLastWindowClosed(False)
    QtWidgets.QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    res = app.exec_()
    # ensure window destruction
    del window
    sys.exit(res)
