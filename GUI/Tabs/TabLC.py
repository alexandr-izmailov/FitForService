import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PyQt5 import QtCore
from GUI.Tabs.CommonObjects import CommonObjects

class TabLC(CommonObjects):
    def __init__(self):
        super().__init__()
        self.setup_layout_objects(add_EL_EC=True)

        # DEFINING of Layout objects
        # =================================================================
        self.hlayout_defect_type = QHBoxLayout()
        self.hlayout_g_r = QHBoxLayout()
        self.hlayout_s = QHBoxLayout()
        self.hlayout_c = QHBoxLayout()
        self.hlayout_L_msd = QHBoxLayout()
        self.hlayout_pb = QHBoxLayout()

        # ADJUSTING of Label, ComboBox and lineEdit
        # =================================================================
        self.label_defect_type = QLabel('Local metal loss defect type:')
        self.comboBox_defect_type = QComboBox()
        self.comboBox_defect_type.setMinimumSize(self.combo_box_min_w, self.combo_box_min_h)
        self.comboBox_defect_type.setMaximumSize(self.combo_box_max_w, self.combo_box_max_h)

        self.label_g_r = QLabel('Radius at the base of a Groove-Like Flaw, g_r [mm]:')
        self.line_g_r = QLineEdit()
        self.line_g_r.setMinimumSize(self.line_min_w, self.line_min_h)
        self.line_g_r.setMaximumSize(self.line_max_w, self.line_max_h)
        self.label_g_r.setToolTip("Radius at the base of a Groove-Like Flaw based on future corroded condition, g_r")
        self.line_g_r.setValidator(self.d_validator)

        self.label_s = QLabel('Longitudinal extent of local metal loss region, s [mm]:')
        self.line_s = QLineEdit()
        self.line_s.setMinimumSize(self.line_min_w, self.line_min_h)
        self.line_s.setMaximumSize(self.line_max_w, self.line_max_h)
        self.label_s.setToolTip("Longitudinal extent or length of the region of local metal loss based on future corroded thickness t_c, s")
        self.line_s.setValidator(self.d_validator)

        self.label_c = QLabel('Circumferential extent of local metal loss region, c [mm]:')
        self.line_c = QLineEdit()
        self.line_c.setMinimumSize(self.line_min_w, self.line_min_h)
        self.line_c.setMaximumSize(self.line_max_w, self.line_max_h)
        self.label_c.setToolTip("Circumferential extent or length of the region of local metal loss based on future corroded thickness  t_c, c")
        self.line_c.setValidator(self.d_validator)

        self.label_L_msd = QLabel('Distance to nearest major structural discontinuity, L_msd [mm]:')
        self.line_L_msd = QLineEdit()
        self.line_L_msd.setMinimumSize(self.line_min_w, self.line_min_h)
        self.line_L_msd.setMaximumSize(self.line_max_w, self.line_max_h)
        self.label_L_msd.setToolTip("Distance to the nearest major structural discontinuity, L_msd")
        self.line_L_msd.setValidator(self.d_validator)

        self.pb_load_latest_input = QPushButton("Load Latest Input")
        self.pb_load_latest_input.setMinimumSize(280, self.pb_min_h)
        self.pb_load_latest_input.setMaximumSize(280, self.pb_max_h)
        self.pb_load_latest_input.setToolTip('Click here, if you want to load the latest input data for local corrosion')

        self.pb_calculate = QPushButton("Calculate FFS")
        self.pb_calculate.setMinimumSize(self.pb_min_w, self.pb_min_h)
        self.pb_calculate.setMaximumSize(self.pb_max_w, self.pb_max_h)

        # ADJUSTING of layout
        # =================================================================
        self.hlayout_defect_type.addWidget(self.label_defect_type)
        self.hlayout_defect_type.addWidget(self.comboBox_defect_type)
        self.vlayout.addLayout(self.hlayout_defect_type)

        self.hlayout_g_r.addWidget(self.label_g_r)
        self.hlayout_g_r.addWidget(self.line_g_r)
        self.vlayout.addLayout(self.hlayout_g_r)

        self.hlayout_s.addWidget(self.label_s)
        self.hlayout_s.addWidget(self.line_s)
        self.vlayout.addLayout(self.hlayout_s)

        self.hlayout_c.addWidget(self.label_c)
        self.hlayout_c.addWidget(self.line_c)
        self.vlayout.addLayout(self.hlayout_c)

        self.hlayout_L_msd.addWidget(self.label_L_msd)
        self.hlayout_L_msd.addWidget(self.line_L_msd)
        self.vlayout.addLayout(self.hlayout_L_msd)

        # self.vlayout.addWidget(self.pb_calculate, alignment=QtCore.Qt.AlignCenter)

        self.hlayout_pb.addWidget(self.pb_load_latest_input)
        self.hlayout_pb.addWidget(self.pb_calculate)
        self.vlayout.addLayout(self.hlayout_pb)

        self.setLayout(self.vlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TabLC()
    ex.show()
    sys.exit(app.exec_())