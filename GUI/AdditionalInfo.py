import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout


class AdditionalInfoWindow(QWidget):
    def __init__(self, image_path, logo_path):
        super().__init__()
        # Set the window icon
        self.setWindowIcon(QIcon(logo_path))
        self.setWindowTitle('Info')

        vlayout = QVBoxLayout(self)
        self.label = QLabel(self)
        self.pixmap = QPixmap(image_path)

        self.width = self.pixmap.width()
        self.height = self.pixmap.height()
        self.setMaximumSize(self.width,  self.height)
        self.setMinimumSize(self.width,  self.height)
        self.label.setPixmap(self.pixmap)

        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.addWidget(self.label)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # window = AdditionalInfoWindow(r'C:\Users\a.izmailov\PycharmProjects\FitForService\Images\image_L_msd.png', r'C:\Users\a.izmailov\PycharmProjects\FitForService\Icons\logo_api.png')
    window = AdditionalInfoWindow(r'C:\Users\a.izmailov\PycharmProjects\FitForService\Images\image_s_c.png', r'C:\Users\a.izmailov\PycharmProjects\FitForService\Icons\logo_api.png')
    sys.exit(app.exec_())
