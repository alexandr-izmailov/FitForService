import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTextBrowser, QPushButton, QFileDialog, QHBoxLayout, QGridLayout


class ShortReportWindow(QMainWindow):
    def __init__(self, short_report_text):
        super().__init__()
        self.directory_for_report = ''

        # Set the window icon
        self.setWindowIcon(QIcon('Icons\icon_240_240.png'))
        self.setWindowTitle('Calculations')
        self.resize(900, 400)
        self.setMaximumSize(1100, 700)
        self.setMinimumSize(700, 300)

        # Create a central widget for the main window
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QGridLayout(central_widget)

        # Create a horizontal layout for the button
        hlayout_pb_full_report = QHBoxLayout()
        hlayout_pb_full_report.setAlignment(Qt.AlignCenter)

        # Create a text browser and add it to the layout
        text_browser = QTextBrowser()
        text_browser.setText(short_report_text)
        layout.addWidget(text_browser, 0, 0)

        # Create a button and add it to the button layout
        self.pb_full_report = QPushButton('Full Report')
        self.pb_full_report.setMaximumSize(350, 150)
        hlayout_pb_full_report.addWidget(self.pb_full_report)

        # Add the button layout to the grid layout
        layout.addLayout(hlayout_pb_full_report, 1, 0)

        # Handling pushButton the button's clicked signal to a slot that opens a file dialog
        # =================================================================================
        # self.pb_full_report.clicked.connect(self.show_file_dialog)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShortReportWindow('dsd')
    sys.exit(app.exec_())

