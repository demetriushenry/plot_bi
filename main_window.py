import sys
import pandas as pd
import matplotlib.pyplot as plt

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
        if file_path[0]:
            self._data = pd.read_csv(file_path[0], sep=';')
            heads = [i for i in self._data.head(0)]
            self._popupate_fields(heads)

    @Slot(str)
    def on_heads_changed(self, text):
        series = self._data[text]
        value_list = [str(value) for value in series.values]
        self.window.lw_values.clear()
        self.window.lw_values.addItems(value_list)
        self.window.bt_plot.setEnabled(len(value_list) > 0)

    @Slot()
    def on_plot_graphs_click(self):
        self._get_item_from_dialog()

    def _popupate_fields(self, heads):
        self.window.cb_heads.addItems(heads)

    def _get_item_from_dialog(self):
        heads = [i for i in self._data.head(0)]
        head1, ok1 = QtWidgets.QInputDialog().getItem(
            self, 'First graph', 'Select the first graph.', heads, 0,
            False
        )
        head2, ok2 = QtWidgets.QInputDialog().getItem(
            self, 'Second graph', 'Select the second graph.', heads, 0,
            False
        )
        if ok1 and ok2:
            # generate graph
            self._generate_graph(head1, head2)
        else:
            # it must need to select two items
            pass

    def _generate_graph(self, column1, column2):
        fig, axes = plt.subplots(1, 2)

        # graph1
        graph1 = self._data.groupby(column1)
        graph1[column1].describe()
        self._data[column1].drop_duplicates()
        chart1 = graph1[column1].aggregate(['count'])
        df1 = pd.DataFrame(chart1.sort_values(
            ['count'], ascending=False).head())

        # graph2
        graph2 = self._data.groupby(column2)
        graph2[column2].describe()
        self._data[column2].drop_duplicates()
        chart2 = graph2[column2].aggregate(['count'])
        df2 = pd.DataFrame(chart2.sort_values(
            ['count'], ascending=False).head())

        ax1 = df1.plot.bar(ax=axes[0, 0], rot=0)
        ax1.legend([column1])
        ax2 = df2.plot.bar(ax=axes[0, 1], rot=0)
        ax2.legend([column2])

        plt.show()


if __name__ == "__main__":
    QtWidgets.QApplication.setQuitOnLastWindowClosed(False)
    QtWidgets.QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    res = app.exec_()
    # ensure window destruction
    del window
    sys.exit(res)
