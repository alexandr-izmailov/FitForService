import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PyQt5 import QtCore
from GUI.Tabs.CommonObjects import CommonObjects

class TabGC(CommonObjects):
    def __init__(self):
        super().__init__()
        self.setup_layout_objects()

        # DEFINING of Layout objects
        # =================================================================
        self.hlayout_t_amS = QHBoxLayout()
        self.hlayout_t_amC = QHBoxLayout()
        self.hlayout_pb = QHBoxLayout()


        # ADJUSTING of Label, ComboBox and lineEdit
        # =================================================================
        self.label_t_amS = QLabel('Avg measured longitudinal thickness, t_amS [mm]:')
        self.line_t_amS = QLineEdit()
        self.line_t_amS.setMinimumSize(self.line_min_w, self.line_min_h)
        self.line_t_amS.setMaximumSize(self.line_max_w, self.line_max_h)
        self.label_t_amS.setToolTip("Average measured wall thickness of the component based on the longitudinal CTP determined at the time of the inspection, t_amS")
        self.line_t_amS.setValidator(self.d_validator)

        self.label_t_amC = QLabel('Avg measured circumferential thickness, t_amC [mm]:')
        self.line_t_amC = QLineEdit()
        self.line_t_amC.setMinimumSize(self.line_min_w, self.line_min_h)
        self.line_t_amC.setMaximumSize(self.line_max_w, self.line_max_h)
        self.line_t_amC.setValidator(self.d_validator)

        self.pb_load_latest_input = QPushButton("Load Latest Input")
        self.pb_load_latest_input.setMinimumSize(280, self.pb_min_h)
        self.pb_load_latest_input.setMaximumSize(280, self.pb_max_h)
        self.pb_load_latest_input.setToolTip('Click here, if you want to load the latest input data for general corrosion')

        self.pb_calculate = QPushButton("Calculate FFS")
        self.pb_calculate.setMinimumSize(self.pb_min_w, self.pb_min_h)
        self.pb_calculate.setMaximumSize(self.pb_max_w, self.pb_max_h)


        # ADJUSTING of layout
        # =================================================================
        self.hlayout_t_amS.addWidget(self.label_t_amS)
        self.hlayout_t_amS.addWidget(self.line_t_amS)
        self.vlayout.addLayout(self.hlayout_t_amS)

        self.hlayout_t_amC.addWidget(self.label_t_amC)
        self.hlayout_t_amC.addWidget(self.line_t_amC)
        self.vlayout.addLayout(self.hlayout_t_amC)

        # self.vlayout.addWidget(self.pb_calculate, alignment=QtCore.Qt.AlignCenter)

        self.hlayout_pb.addWidget(self.pb_load_latest_input)
        self.hlayout_pb.addWidget(self.pb_calculate)
        self.vlayout.addLayout(self.hlayout_pb)

        self.setLayout(self.vlayout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TabGC()
    ex.show()
    sys.exit(app.exec_())
