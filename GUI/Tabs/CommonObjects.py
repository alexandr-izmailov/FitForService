import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PyQt5 import QtCore
from PyQt5.QtGui import QDoubleValidator,QRegExpValidator

class CommonObjects(QWidget):
    def __init__(self):
        super().__init__()

        # DEFINING of Validator parameters
        # =================================================================
        self.regex = QtCore.QRegExp("^(?!0\d)\d{1,11}(?:\.\d{1,4})?$")
        self.d_validator  = QRegExpValidator(self.regex)

        # DEFINING of Size parameters
        # =================================================================
        self.combo_box_min_w = 160
        self.combo_box_max_w = self.combo_box_min_w
        self.combo_box_min_h = 25
        self.combo_box_max_h = self.combo_box_min_w


        self.line_min_w = 160
        self.line_max_w = self.line_min_w
        self.line_min_h = 25
        self.line_max_h = self.line_min_w

        self.label_max_h = 19
        self.label_min_h = self.label_max_h

        self.pb_max_w = 300
        self.pb_min_w = self.pb_max_w
        self.pb_max_h = 33
        self.pb_min_h = self.pb_max_h

    def setup_layout_objects(self, add_EL_EC = False):
        # DEFINING of Layout objects
        # =================================================================
        self.vlayout = QVBoxLayout()

        self.hlayout_asset = QHBoxLayout()
        self.hlayout_line_number = QHBoxLayout()
        self.hlayout_monitoring_location = QHBoxLayout()

        self.hlayout_material = QHBoxLayout()
        self.hlayout_steel_type = QHBoxLayout()
        self.hlayout_temperature = QHBoxLayout()
        self.hlayout_stress = QHBoxLayout()
        self.hlayout_nominal_pipe_size = QHBoxLayout()
        self.hlayout_outside_diameter = QHBoxLayout()
        self.hlayout_schedule = QHBoxLayout()
        self.hlayout_thickness = QHBoxLayout()
        self.hlayout_wall_loss_type = QHBoxLayout()
        self.hlayout_pipe_type = QHBoxLayout()
        self.hlayout_mill_under_tolerance = QHBoxLayout()
        self.hlayout_P = QHBoxLayout()
        self.hlayout_Y_B31 = QHBoxLayout()
        self.hlayout_E = QHBoxLayout()
        self.hlayout_EC = QHBoxLayout()
        self.hlayout_EL = QHBoxLayout()
        self.hlayout_RSF_a = QHBoxLayout()

        self.hlayout_MA = QHBoxLayout()
        self.hlayout_t_sl = QHBoxLayout()
        self.hlayout_LOSS = QHBoxLayout()
        self.hlayout_FCA = QHBoxLayout()
        self.hlayout_FCA_ml = QHBoxLayout()

        self.hlayout_NDE_type = QHBoxLayout()
        self.hlayout_t_mm = QHBoxLayout()

        # ADJUSTING of Label, ComboBox and lineEdit
        # =================================================================
        self.label_asset = QLabel('Asset:')
        self.line_asset = QLineEdit()
        self.line_asset.setMinimumSize(320, self.line_min_h)
        self.line_asset.setMaximumSize(320, self.line_max_h)

        self.label_line_number = QLabel('Line number:')
        self.line_line_number = QLineEdit()
        self.line_line_number.setMinimumSize(320, self.line_min_h)
        self.line_line_number.setMaximumSize(320, self.line_max_h)

        self.label_monitoring_location = QLabel('Corrosion monitoring location:')
        self.line_monitoring_location = QLineEdit()
        self.line_monitoring_location.setMinimumSize(320, self.line_min_h)
        self.line_monitoring_location.setMaximumSize(320, self.line_max_h)

        self.label_wall_loss_type = QLabel('Type of wall loss:')
        self.comboBox_wall_loss_type = QComboBox()
        self.comboBox_wall_loss_type.setMinimumSize(320, self.combo_box_min_h)
        self.comboBox_wall_loss_type.setMaximumSize(320, self.combo_box_max_h)

        self.label_design_parameters = QLabel('Design parameters')
        self.label_design_parameters.setAlignment(QtCore.Qt.AlignCenter)
        self.label_design_parameters.setMaximumHeight(self.label_max_h)
        self.label_design_parameters.setMinimumHeight(self.label_min_h)

        self.label_material = QLabel('Pipe material:')
        self.comboBox_material = QComboBox()
        self.comboBox_material.setEditable(True)
        self.comboBox_material.setMinimumSize(self.combo_box_min_w, self.combo_box_min_h)
        self.comboBox_material.setMaximumSize(self.combo_box_max_w, self.combo_box_max_h)

        self.label_steel_type = QLabel('Steel type:')
        self.comboBox_steel_type = QComboBox()
        self.comboBox_steel_type.setMinimumSize(self.combo_box_min_w, self.combo_box_min_h)
        self.comboBox_steel_type.setMaximumSize(self.combo_box_max_w, self.combo_box_max_h)

        self.label_temperature = QLabel('Designed temperature [°C]:')
        self.comboBox_temperature = QComboBox()
        self.comboBox_temperature.setEditable(True)
        self.comboBox_temperature.setMaxVisibleItems(350)
        self.comboBox_temperature.setMinimumSize(self.combo_box_min_w, self.combo_box_min_h)
        self.comboBox_temperature.setMaximumSize(self.combo_box_max_w, self.combo_box_max_h)
        self.comboBox_temperature.setValidator(self.d_validator)

        self.label_stress = QLabel('Allowable stress, S [MPa]:')
        self.comboBox_stress = QComboBox()
        self.comboBox_stress.setEditable(True)
        self.comboBox_stress.setMinimumSize(self.combo_box_min_w, self.combo_box_min_h)
        self.comboBox_stress.setMaximumSize(self.combo_box_max_w, self.combo_box_max_h)
        self.comboBox_stress.setValidator(self.d_validator)

        self.label_nominal_pipe_size = QLabel('Nominal pipe size:')
        self.comboBox_nominal_pipe_size = QComboBox()
        self.comboBox_nominal_pipe_size.setEditable(True)
        self.comboBox_nominal_pipe_size.setMinimumSize(self.combo_box_min_w, self.combo_box_min_h)
        self.comboBox_nominal_pipe_size.setMaximumSize(self.combo_box_max_w, self.combo_box_max_h)

        self.label_outside_diameter = QLabel('Outside diameter of pipe, D_o [mm]:')
        self.comboBox_outside_diameter = QComboBox()
        self.comboBox_outside_diameter.setEditable(True)
        self.comboBox_outside_diameter.setMinimumSize(self.combo_box_min_w, self.combo_box_min_h)
        self.comboBox_outside_diameter.setMaximumSize(self.combo_box_max_w, self.combo_box_max_h)
        self.comboBox_outside_diameter.setValidator(self.d_validator)

        self.label_schedule = QLabel('Schedule:')
        self.comboBox_schedule = QComboBox()
        self.comboBox_schedule.setEditable(True)
        self.comboBox_schedule.setMinimumSize(self.combo_box_min_w, self.combo_box_min_h)
        self.comboBox_schedule.setMaximumSize(self.combo_box_max_w, self.combo_box_max_h)

        self.label_thickness = QLabel('Wall thickness, t [mm]:')
        self.comboBox_thickness = QComboBox()
        self.comboBox_thickness.setEditable(True)
        self.comboBox_thickness.setMinimumSize(self.combo_box_min_w, self.combo_box_min_h)
        self.comboBox_thickness.setMaximumSize(self.combo_box_max_w, self.combo_box_max_h)
        self.comboBox_thickness.setValidator(self.d_validator)

        self.label_pipe_type = QLabel('Pipe type:')
        self.comboBox_pipe_type = QComboBox()
        self.comboBox_pipe_type.setEditable(True)
        self.comboBox_pipe_type.setMinimumSize(self.combo_box_min_w, self.combo_box_min_h)
        self.comboBox_pipe_type.setMaximumSize(self.combo_box_max_w, self.combo_box_max_h)

        self.label_mill_under_tolerance = QLabel('Mill under tolerance, M_ut:')
        self.comboBox_mill_under_tolerance = QComboBox()
        self.comboBox_mill_under_tolerance.setEditable(True)
        self.comboBox_mill_under_tolerance.setMinimumSize(self.combo_box_min_w, self.combo_box_min_h)
        self.comboBox_mill_under_tolerance.setMaximumSize(self.combo_box_max_w, self.combo_box_max_h)
        self.comboBox_mill_under_tolerance.setValidator(self.d_validator)

        self.label_P = QLabel('Internal design pressure, P [bar]:')
        self.line_P = QLineEdit()
        self.line_P.setMinimumSize(self.line_min_w, self.line_min_h)
        self.line_P.setMaximumSize(self.line_max_w, self.line_max_h)
        self.line_P.setValidator(self.d_validator)

        self.label_Y_B31 = QLabel('Coefficient ASME B31.3, YB31:')
        self.line_Y_B31 = QLineEdit()
        self.line_Y_B31.setMinimumSize(self.line_min_w, self.line_min_h)
        self.line_Y_B31.setMaximumSize(self.line_max_w, self.line_max_h)
        self.line_Y_B31.setValidator(self.d_validator)

        self.label_E = QLabel('Weld joint efficiency factor, E:')
        self.line_E = QLineEdit()
        self.line_E.setMinimumSize(self.line_min_w, self.line_min_h)
        self.line_E.setMaximumSize(self.line_max_w, self.line_max_h)
        self.line_E.setValidator(self.d_validator)

        if add_EL_EC:
            self.label_EC = QLabel('Longitudinal weld joint efficiency, EC:')
            self.line_EC = QLineEdit()
            self.line_EC.setMinimumSize(self.line_min_w, self.line_min_h)
            self.line_EC.setMaximumSize(self.line_max_w, self.line_max_h)
            self.line_EC.setValidator(self.d_validator)

            self.label_EL = QLabel('Circumferential weld joint efficiency, EL:')
            self.line_EL = QLineEdit()
            self.line_EL.setMinimumSize(self.line_min_w, self.line_min_h)
            self.line_EL.setMaximumSize(self.line_max_w, self.line_max_h)
            self.line_EL.setValidator(self.d_validator)

        self.label_RSF_a = QLabel('Remaining strength factor, RSF_a:')
        self.line_RSF_a = QLineEdit()
        self.line_RSF_a.setMinimumSize(self.line_min_w, self.line_min_h)
        self.line_RSF_a.setMaximumSize(self.line_max_w, self.line_max_h)
        self.line_RSF_a.setValidator(self.d_validator)

        self.label_wall_thickness_allowances = QLabel('Wall thickness allowances')
        self.label_wall_thickness_allowances.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wall_thickness_allowances.setMinimumHeight(self.label_min_h)
        self.label_wall_thickness_allowances.setMaximumHeight(self.label_max_h)


        self.label_MA = QLabel('Mechanical allowances, MA [mm]:')
        self.line_MA = QLineEdit()
        self.line_MA.setMinimumSize(self.line_min_w, self.line_min_h)
        self.line_MA.setMaximumSize(self.line_max_w, self.line_max_h)
        self.label_MA.setToolTip("Mechanical allowances (thread or groove depth), MA")
        self.line_MA.setValidator(self.d_validator)

        self.label_t_sl = QLabel('Supplemental thickness, t_sl [mm]:')
        self.line_t_sl = QLineEdit()
        self.line_t_sl.setMinimumSize(self.line_min_w, self.line_min_h)
        self.line_t_sl.setMaximumSize(self.line_max_w, self.line_max_h)
        self.line_t_sl.setValidator(self.d_validator)

        self.label_LOSS = QLabel('Uniform metal loss away from local metal loss, LOSS [mm]:')
        self.line_LOSS = QLineEdit()
        self.line_LOSS.setMinimumSize(self.line_min_w, self.line_min_h)
        self.line_LOSS.setMaximumSize(self.line_max_w, self.line_max_h)
        self.label_LOSS.setToolTip("Uniform metal loss away from the local metal loss, LOSS")
        self.line_LOSS.setValidator(self.d_validator)

        self.label_FCA = QLabel('FCA away from the local metal loss area, FCA [mm]:')
        self.line_FCA = QLineEdit()
        self.line_FCA.setMinimumSize(self.line_min_w, self.line_min_h)
        self.line_FCA.setMaximumSize(self.line_max_w, self.line_max_h)
        self.label_FCA.setToolTip("Future corrosion allowance away from the local metal loss area, FCA [mm]")
        self.line_FCA.setValidator(self.d_validator)

        self.label_FCA_ml = QLabel('FCA for local metal loss area, FCA_ml [mm]:')
        self.line_FCA_ml = QLineEdit()
        self.line_FCA_ml.setMinimumSize(self.line_min_w, self.line_min_h)
        self.line_FCA_ml.setMaximumSize(self.line_max_w, self.line_max_h)
        self.label_FCA_ml.setToolTip("Future corrosion allowance for local metal loss area, FCA_ml")
        self.line_FCA_ml.setValidator(self.d_validator)

        self.label_wall_thickness_measurements = QLabel('Wall thickness measurements')
        self.label_wall_thickness_measurements.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wall_thickness_measurements.setMaximumHeight(self.label_max_h)
        self.label_wall_thickness_measurements.setMinimumHeight(self.label_min_h)

        self.label_NDE_type = QLabel('Type of NDE:')
        self.line_NDE_type = QLineEdit()
        self.line_NDE_type.setMinimumSize(self.line_min_w, self.line_min_h)
        self.line_NDE_type.setMaximumSize(self.line_max_w, self.line_max_h)

        self.label_t_mm = QLabel('Min measured thickness, t_mm [mm]:')
        self.line_t_mm = QLineEdit()
        self.line_t_mm.setMinimumSize(self.line_min_w, self.line_min_h)
        self.line_t_mm.setMaximumSize(self.line_max_w, self.line_max_h)
        self.label_t_mm.setToolTip("Minimum measured thickness at the time of the assessment, t_mm")
        self.line_t_mm.setValidator(self.d_validator)

        # ADJUSTING of layout
        # =================================================================
        self.hlayout_asset.addWidget(self.label_asset)
        self.hlayout_asset.addWidget(self.line_asset)
        self.vlayout.addLayout(self.hlayout_asset)

        self.hlayout_line_number.addWidget(self.label_line_number)
        self.hlayout_line_number.addWidget(self.line_line_number)
        self.vlayout.addLayout(self.hlayout_line_number)

        self.hlayout_monitoring_location.addWidget(self.label_monitoring_location)
        self.hlayout_monitoring_location.addWidget(self.line_monitoring_location)
        self.vlayout.addLayout(self.hlayout_monitoring_location)

        self.hlayout_wall_loss_type.addWidget(self.label_wall_loss_type)
        self.hlayout_wall_loss_type.addWidget(self.comboBox_wall_loss_type)
        self.vlayout.addLayout(self.hlayout_wall_loss_type)

        self.vlayout.addWidget(self.label_design_parameters)

        self.hlayout_material.addWidget(self.label_material)
        self.hlayout_material.addWidget(self.comboBox_material)
        self.vlayout.addLayout(self.hlayout_material)

        self.hlayout_steel_type.addWidget(self.label_steel_type)
        self.hlayout_steel_type.addWidget(self.comboBox_steel_type)
        self.vlayout.addLayout(self.hlayout_steel_type)

        self.hlayout_temperature.addWidget(self.label_temperature)
        self.hlayout_temperature.addWidget(self.comboBox_temperature)
        self.vlayout.addLayout(self.hlayout_temperature)

        self.hlayout_stress.addWidget(self.label_stress)
        self.hlayout_stress.addWidget(self.comboBox_stress)
        self.vlayout.addLayout(self.hlayout_stress)

        self.hlayout_nominal_pipe_size.addWidget(self.label_nominal_pipe_size)
        self.hlayout_nominal_pipe_size.addWidget(self.comboBox_nominal_pipe_size)
        self.vlayout.addLayout(self.hlayout_nominal_pipe_size)

        self.hlayout_outside_diameter.addWidget(self.label_outside_diameter)
        self.hlayout_outside_diameter.addWidget(self.comboBox_outside_diameter)
        self.vlayout.addLayout(self.hlayout_outside_diameter)

        self.hlayout_schedule.addWidget(self.label_schedule)
        self.hlayout_schedule.addWidget(self.comboBox_schedule)
        self.vlayout.addLayout(self.hlayout_schedule)

        self.hlayout_thickness.addWidget(self.label_thickness)
        self.hlayout_thickness.addWidget(self.comboBox_thickness)
        self.vlayout.addLayout(self.hlayout_thickness)

        self.hlayout_pipe_type.addWidget(self.label_pipe_type)
        self.hlayout_pipe_type.addWidget(self.comboBox_pipe_type)
        self.vlayout.addLayout(self.hlayout_pipe_type)

        self.hlayout_mill_under_tolerance.addWidget(self.label_mill_under_tolerance)
        self.hlayout_mill_under_tolerance.addWidget(self.comboBox_mill_under_tolerance)
        self.vlayout.addLayout(self.hlayout_mill_under_tolerance)

        self.hlayout_P.addWidget(self.label_P)
        self.hlayout_P.addWidget(self.line_P)
        self.vlayout.addLayout(self.hlayout_P)

        self.hlayout_Y_B31.addWidget(self.label_Y_B31)
        self.hlayout_Y_B31.addWidget(self.line_Y_B31)
        self.vlayout.addLayout(self.hlayout_Y_B31)

        self.hlayout_E.addWidget(self.label_E)
        self.hlayout_E.addWidget(self.line_E)
        self.vlayout.addLayout(self.hlayout_E)

        if add_EL_EC:
            self.hlayout_EC.addWidget(self.label_EC)
            self.hlayout_EC.addWidget(self.line_EC)
            self.vlayout.addLayout(self.hlayout_EC)

            self.hlayout_EL.addWidget(self.label_EL)
            self.hlayout_EL.addWidget(self.line_EL)
            self.vlayout.addLayout(self.hlayout_EL)

        self.hlayout_RSF_a.addWidget(self.label_RSF_a)
        self.hlayout_RSF_a.addWidget(self.line_RSF_a)
        self.vlayout.addLayout(self.hlayout_RSF_a)

        self.vlayout.addWidget(self.label_wall_thickness_allowances)

        self.hlayout_MA.addWidget(self.label_MA)
        self.hlayout_MA.addWidget(self.line_MA)
        self.vlayout.addLayout(self.hlayout_MA)

        self.hlayout_t_sl.addWidget(self.label_t_sl)
        self.hlayout_t_sl.addWidget(self.line_t_sl)
        self.vlayout.addLayout(self.hlayout_t_sl)

        self.hlayout_LOSS.addWidget(self.label_LOSS)
        self.hlayout_LOSS.addWidget(self.line_LOSS)
        self.vlayout.addLayout(self.hlayout_LOSS)

        self.hlayout_FCA.addWidget(self.label_FCA)
        self.hlayout_FCA.addWidget(self.line_FCA)
        self.vlayout.addLayout(self.hlayout_FCA)

        self.hlayout_FCA_ml.addWidget(self.label_FCA_ml)
        self.hlayout_FCA_ml.addWidget(self.line_FCA_ml)
        self.vlayout.addLayout(self.hlayout_FCA_ml)

        self.vlayout.addWidget(self.label_wall_thickness_measurements)

        self.hlayout_NDE_type.addWidget(self.label_NDE_type)
        self.hlayout_NDE_type.addWidget(self.line_NDE_type)
        self.vlayout.addLayout(self.hlayout_NDE_type)

        self.hlayout_t_mm.addWidget(self.label_t_mm)
        self.hlayout_t_mm.addWidget(self.line_t_mm)
        self.vlayout.addLayout(self.hlayout_t_mm)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CommonObjects()
    ex.show()
    sys.exit(app.exec_())