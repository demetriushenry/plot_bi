import sys

from PySide2.QtWidgets import (QApplication, QFormLayout, QMainWindow,
                               QPushButton, QSpinBox, QVBoxLayout, QWidget)


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Plot BI')

        # main widget
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # layout initialize
        g_layout = QVBoxLayout()
        layout = QFormLayout()
        main_widget.setLayout(g_layout)

        # Add Widgets
        self.parm = QSpinBox()
        self.parm.setValue(30)
        layout.addRow('Parameter', self.parm)
        self.exec_btn = QPushButton('Execute')

        # global layout setting
        g_layout.addLayout(layout)
        g_layout.addWidget(self.exec_btn)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
    del main
