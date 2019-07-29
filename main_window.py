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

        self._setup_slots()

        # attributes
        self._data = None

    def _setup_slots(self):
        self.window.actionOpen.triggered.connect(self.load_csv_file)
        self.window.actionQuit.triggered.connect(self.exit_application)
        self.window.cb_heads.currentTextChanged.connect(self.on_heads_changed)
        self.window.bt_plot.clicked.connect(self.on_plot_graphs_click)

    @Slot()
    def exit_application(self):
        QtWidgets.QApplication.exit()

    @Slot()
    def load_csv_file(self):
        file_path = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open CSV file', '', 'CSV (*.csv);;All file (*)')
        if file_path:
            self._data = pd.read_csv(file_path[0], sep=';')
            heads = [i for i in self._data.head(0)]
            self._popupate_fields(heads)

    @Slot(str)
    def on_heads_changed(self, text):
        series = self._data[text]
        value_list = [str(value) for value in series.values]
        self.window.lw_values.clear()
        self.window.lw_values.addItems(value_list)

    @Slot()
    def on_plot_graphs_click(self):
        self._get_item_from_dialog()

    def _popupate_fields(self, heads):
        self.window.cb_heads.addItems(heads)

    def _get_item_from_dialog(self):
        heads = [i for i in self._data.head(0)]
        value1, ok1 = QtWidgets.QInputDialog().getItem(
            self, 'First graph', 'Select the first graph.', heads, 0,
            False
        )
        value2, ok2 = QtWidgets.QInputDialog().getItem(
            self, 'Second graph', 'Select the second graph.', heads, 0,
            False
        )
        if ok1 and ok2:
            # generate graph
            pass
        else:
            # it must need to select two items
            pass


if __name__ == "__main__":
    QtWidgets.QApplication.setQuitOnLastWindowClosed(False)
    QtWidgets.QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    res = app.exec_()
    # ensure window destruction
    del window
    sys.exit(res)
