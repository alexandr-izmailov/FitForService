import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5 import QtCore,  QtWidgets
from GUI.Tabs.TabGC import TabGC
from GUI.Tabs.TabLC import TabLC

class UI(QWidget):
    def __init__(self):
        super().__init__()

        # ADJUSTING of Window
        # =================================================================
        self.setWindowTitle('FitForService')
        self.setGeometry(700, 40, 550, 1100)
        self.setMaximumSize(690, 1100)
        self.setMinimumSize(690, 1100)


        self.tab_gc = TabGC()
        self.tab_lc = TabLC()

        self.tab = QtWidgets.QTabWidget()
        self.tab.addTab(self.tab_gc, "General Corrosion Method")
        self.tab.addTab(self.tab_lc, "Local Corrosion Method")

        layout = QVBoxLayout()
        layout.addWidget(self.tab)
        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    ex.show()
    sys.exit(app.exec_())
