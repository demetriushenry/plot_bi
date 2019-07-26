import sys
import pandas as pd

from PySide2 import QtWidgets
from PySide2.QtCore import QFile, Qt, Slot
from PySide2.QtUiTools import QUiLoader


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        loader = QUiLoader()
        file = QFile('layouts/mainwindow.ui')
        file.open(QFile.ReadOnly)
        self.window = loader.load(file, self)
        file.close()
        self.window.setWindowTitle('Plot BI')
        self.window.show()

        self.setup_slots()

        # attributes
        self._data = None

    def setup_slots(self):
        self.window.actionOpen.triggered.connect(self.load_csv_file)
        self.window.actionQuit.triggered.connect(self.exit_application)

    @Slot()
    def exit_application(self):
        QtWidgets.QApplication.exit()

    @Slot()
    def load_csv_file(self):
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open CSV file', '', 'CSV (*.csv);;All file (*)')
        if file_path:
            self._data = pd.read_csv(file_path[0], sep=';', encoding='latin1')
            heads = [i for i in self._data.head(0)]
            self._popupate_fields(heads)

    def _popupate_fields(self, heads):
        self.window.cb_heads.addItems(heads)


if __name__ == "__main__":
    QtWidgets.QApplication.setQuitOnLastWindowClosed(False)
    QtWidgets.QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    res = app.exec_()
    # ensure window destruction
    del window
    sys.exit(res)
