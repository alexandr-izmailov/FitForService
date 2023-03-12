import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import QtGui

class WarningDialog:
    def show_warning_dialog(self, warning_text = 'I forgot to set up a warning text:-)',  gc_or_lc = ''):
        dialog = QMessageBox()
        dialog.setWindowTitle("Warning")
        dialog.setText(warning_text)
        dialog.setIconPixmap(QtGui.QIcon("Icons/warning_64.png").pixmap(64, 64))
        dialog.addButton(QMessageBox.Ok)
        dialog.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    warning_dialog = WarningDialog()
    warning_dialog.show_warning_dialog()
