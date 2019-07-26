import sys

from PySide2 import QtWidgets
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        ui_file = QFile("layouts/mainwindow.ui")
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        window = loader.load(ui_file)
        ui_file.close()
        window.showFullScreen()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    # main.show()
    sys.exit(app.exec_())
    del main
