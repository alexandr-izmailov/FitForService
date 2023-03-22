import sys
from loguru import logger
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QIcon
from GUI.UI import UI
from GUI.ShortReportWindow import ShortReportWindow
from GUI.AdditionalInfo import AdditionalInfoWindow
from GUI.WarningDialog import WarningDialog
from Classes.DataLayer import DataLayer, InputDataStaging, LatestInputData
from Algorithm_GC import gc_algorithm
from Algorithm_LC import lc_algorithm
from Document.DocumentProccess import save_new_report_file

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.directory_for_report = ''

        # LOADING DATA
        # =================================================================
        self.dl = DataLayer()

        # FULFILLING comboBoxes initially
        # =================================================================
        self.ui = UI()
        self.ui.setWindowIcon(QIcon('Icons\icon_240_240.png'))
        self.warning_dialog = WarningDialog()
        # self.gc_algorithm = Algorithm_GC.gc_algorithm
        self.add_items()

        # HANDLING comboBoxes
        # =================================================================
        self.gc_input = InputDataStaging()
        self.lc_input = InputDataStaging()

        self.gc_latest = LatestInputData('gc')
        self.lc_latest = LatestInputData('lc')

        # handle material selection for updating steel type
        self.ui.tab_gc.comboBox_material.currentIndexChanged.connect(self.update_comboBox_steel_type)
        self.ui.tab_lc.comboBox_material.currentIndexChanged.connect(self.update_comboBox_steel_type)

        # handle material and temperature selection for updating allowable stress
        self.ui.tab_gc.comboBox_material.currentIndexChanged.connect(self.update_comboBox_stress)
        self.ui.tab_gc.comboBox_temperature.currentIndexChanged.connect(self.update_comboBox_stress)
        self.ui.tab_lc.comboBox_material.currentIndexChanged.connect(self.update_comboBox_stress)
        self.ui.tab_lc.comboBox_temperature.currentIndexChanged.connect(self.update_comboBox_stress)

        # handle Nominal pipe size selection for updating Outside diameter of pipe
        self.ui.tab_gc.comboBox_nominal_pipe_size.currentIndexChanged.connect(self.update_comboBox_outside_diameter)
        self.ui.tab_lc.comboBox_nominal_pipe_size.currentIndexChanged.connect(self.update_comboBox_outside_diameter)

        # handle Steel type and Nominal pipe size selection for updating Schedule
        self.ui.tab_gc.comboBox_steel_type.currentIndexChanged.connect(self.update_comboBox_schedule)
        self.ui.tab_gc.comboBox_nominal_pipe_size.currentIndexChanged.connect(self.update_comboBox_schedule)
        self.ui.tab_lc.comboBox_steel_type.currentIndexChanged.connect(self.update_comboBox_schedule)
        self.ui.tab_lc.comboBox_nominal_pipe_size.currentIndexChanged.connect(self.update_comboBox_schedule)

        # handle Nominal pipe size selection for updating Wall thickness
        self.ui.tab_gc.comboBox_nominal_pipe_size.currentIndexChanged.connect(self.update_comboBox_thickness)
        self.ui.tab_lc.comboBox_nominal_pipe_size.currentIndexChanged.connect(self.update_comboBox_thickness)

        # handle Steel type selection for updating Wall thickness
        self.ui.tab_gc.comboBox_steel_type.currentIndexChanged.connect(self.update_comboBox_thickness)
        self.ui.tab_lc.comboBox_steel_type.currentIndexChanged.connect(self.update_comboBox_thickness)

        # handle Nominal pipe size, Steel type and Schedule  selection for updating Wall thickness
        self.ui.tab_gc.comboBox_nominal_pipe_size.currentIndexChanged.connect(self.update_comboBox_thickness)
        self.ui.tab_gc.comboBox_steel_type.currentIndexChanged.connect(self.update_comboBox_thickness)
        self.ui.tab_gc.comboBox_schedule.currentIndexChanged.connect(self.update_comboBox_thickness)
        self.ui.tab_lc.comboBox_nominal_pipe_size.currentIndexChanged.connect(self.update_comboBox_thickness)
        self.ui.tab_lc.comboBox_steel_type.currentIndexChanged.connect(self.update_comboBox_thickness)
        self.ui.tab_lc.comboBox_schedule.currentIndexChanged.connect(self.update_comboBox_thickness)

        # handle Pipe type selection for updating Mill under tolerance
        self.ui.tab_gc.comboBox_pipe_type.currentIndexChanged.connect(self.update_comboBox_mill_under_tolerance)
        self.ui.tab_lc.comboBox_pipe_type.currentIndexChanged.connect(self.update_comboBox_mill_under_tolerance)

        self.ui.tab_lc.comboBox_defect_type.currentIndexChanged.connect(self.update_line_g_r)

        self.ui.tab_gc.comboBox_schedule.currentIndexChanged.connect(self.thickness_locker)
        self.ui.tab_lc.comboBox_schedule.currentIndexChanged.connect(self.thickness_locker)



        # HANDLING pushButtons
        # =================================================================
        self.ui.tab_gc.pb_calculate.clicked.connect(self.pb_calculate_clicked)
        self.ui.tab_lc.pb_calculate.clicked.connect(self.pb_calculate_clicked)

        self.ui.tab_gc.pb_load_latest_input.clicked.connect(self.load_latest_input_data)
        self.ui.tab_lc.pb_load_latest_input.clicked.connect(self.load_latest_input_data)

        self.ui.tab_lc.pb_s_info.clicked.connect(self.show_s_or_c_info)

        self.ui.tab_lc.pb_L_msd_info.clicked.connect(self.show_L_msd_info)

        self.ui.show()

    def thickness_locker(self):
        if self.ui.tab.currentIndex() == 0:
            if self.ui.tab_gc.comboBox_schedule.currentText().lower() == 'user defined':
                self.ui.tab_gc.comboBox_thickness.setEditable(True)
                self.ui.tab_gc.comboBox_thickness.clear()
                self.ui.tab_gc.comboBox_thickness.setValidator(self.ui.tab_gc.d_validator)
            else:
                self.ui.tab_gc.comboBox_thickness.setEditable(False)
        else:
            if self.ui.tab_lc.comboBox_schedule.currentText().lower() == 'user defined':
                self.ui.tab_lc.comboBox_thickness.setEditable(True)
                print('HI*10')
                self.ui.tab_lc.comboBox_thickness.clear()
                self.ui.tab_lc.comboBox_thickness.setValidator(self.ui.tab_lc.d_validator)
            else:
                self.ui.tab_lc.comboBox_thickness.setEditable(False)

    def update_line_g_r(self):
        if self.ui.tab_lc.comboBox_defect_type.currentText().lower() == 'groove':
            self.ui.tab_lc.line_g_r.setValidator(self.ui.tab_lc.d_validator)
            self.ui.tab_lc.line_g_r.clear()
            self.ui.tab_lc.line_g_r.setEnabled(True)
        elif self.ui.tab_lc.comboBox_defect_type.currentText().lower() == 'local metal loss':
            self.ui.tab_lc.line_g_r.setValidator(self.ui.tab_lc.d_validator)
            self.ui.tab_lc.line_g_r.setText('Not required')
            self.ui.tab_lc.line_g_r.setEnabled(False)

    def show_file_dialog(self):
        # Create a file dialog to let the user select a directory
        file_dialog = QFileDialog(self, 'Select Directory')

        # file_dialog.show()

        # Open the file dialog and get the selected directory
        self.directory_for_report = file_dialog.getExistingDirectory()

        if self.directory_for_report != '':
            # save_new_report_file(self.directory_for_report, self.gc_document, gc_or_lc='GC')
            print('print from show_file_dialog: directory is: ', self.directory_for_report)
            save_new_report_file(self.directory_for_report, self.document, gc_or_lc = self.gc_or_lc_report)
            print('report saved to directory ', self.directory_for_report)
        else:
            print('directory was not chosen')


    def show_s_or_c_info(self):
        self.s_or_c_info_window = AdditionalInfoWindow(image_path='Images/image_s_c.png', logo_path='Icons/logo_api.png')

    def show_L_msd_info(self):
        self.L_msd_info_window = AdditionalInfoWindow(image_path='Images/image_L_msd.png', logo_path='Icons/logo_api.png')

    def pb_calculate_clicked(self):
        if self.ui.tab.currentIndex() == 0:
            input_data_dict = self.create_input_data_dict('gc')
            is_all_input_entered = self.check_all_input_entered(input_data_dict)

            if  is_all_input_entered:
                if input_data_dict['RSF_a'] == '0':
                    self.warning_dialog.show_warning_dialog("RSF_a parameter can't be 0")
                else:
                    self.gc_latest.save_input_data_dict_to_file(input_data_dict)

                    self.gc_input.asset = input_data_dict['asset']
                    self.gc_input.line_number = input_data_dict['line_number']
                    self.gc_input.monitoring_location = input_data_dict['monitoring_location']
                    self.gc_input.wall_loss_type = input_data_dict['wall_loss_type']
                    self.gc_input.material = input_data_dict['material']
                    self.gc_input.steel_type = input_data_dict['steel_type']
                    self.gc_input.temperature = input_data_dict['temperature']
                    self.gc_input.stress = float(input_data_dict['stress'])
                    self.gc_input.nominal_pipe_size = input_data_dict['nominal_pipe_size']
                    self.gc_input.outside_diameter = float(input_data_dict['outside_diameter'])
                    self.gc_input.schedule = input_data_dict['schedule']
                    self.gc_input.thickness = float(input_data_dict['thickness'].strip())
                    self.gc_input.pipe_type = input_data_dict['pipe_type']
                    self.gc_input.mill_under_tolerance = float(input_data_dict['mill_under_tolerance'])
                    self.gc_input.P = float(input_data_dict['P'])
                    self.gc_input.Y_B31 = float(input_data_dict['Y_B31'])
                    self.gc_input.E = float(input_data_dict['E'])
                    self.gc_input.RSF_a = float(input_data_dict['RSF_a'])
                    self.gc_input.MA = float(input_data_dict['MA'])
                    self.gc_input.t_sl = float(input_data_dict['t_sl'])
                    self.gc_input.LOSS = float(input_data_dict['LOSS'])
                    self.gc_input.FCA = float(input_data_dict['FCA'])
                    self.gc_input.FCA_ml = float(input_data_dict['FCA_ml'])
                    self.gc_input.t_mm = float(input_data_dict['t_mm'])
                    self.gc_input.t_amS = float(input_data_dict['t_amS'])
                    self.gc_input.t_amC = float(input_data_dict['t_amC'])

                    self.short_report_text, self.document = gc_algorithm(self.gc_input)

                    self.gc_or_lc_report = 'gc'

                    print(self.short_report_text)

                    self.short_report_window = ShortReportWindow(self.short_report_text)

                    self.short_report_window.pb_full_report.clicked.connect(self.show_file_dialog)

            else:
                self.warning_dialog.show_warning_dialog("Please, enter all the input data\nto calculate Fitness-For-Service")
        else:
            input_data_dict = self.create_input_data_dict('lc')
            is_all_input_entered = self.check_all_input_entered(input_data_dict)

            if is_all_input_entered:
                if input_data_dict['RSF_a'] == '0':
                    self.warning_dialog.show_warning_dialog("RSF_a parameter can't be 0")
                else:
                    self.lc_latest.save_input_data_dict_to_file(input_data_dict)

                    self.lc_input.asset = input_data_dict['asset']
                    self.lc_input.line_number = input_data_dict['line_number']
                    self.lc_input.monitoring_location = input_data_dict['monitoring_location']
                    self.lc_input.material = input_data_dict['material']
                    self.lc_input.steel_type = input_data_dict['steel_type']
                    self.lc_input.temperature = input_data_dict['temperature']
                    self.lc_input.stress = float(input_data_dict['stress'])
                    self.lc_input.nominal_pipe_size = input_data_dict['nominal_pipe_size']
                    self.lc_input.outside_diameter = float(input_data_dict['outside_diameter'])
                    self.lc_input.schedule = input_data_dict['schedule']
                    self.lc_input.thickness = float(input_data_dict['thickness'].strip())
                    self.lc_input.pipe_type = input_data_dict['pipe_type']
                    self.lc_input.mill_under_tolerance = float(input_data_dict['mill_under_tolerance'])
                    self.lc_input.P = float(input_data_dict['P'])
                    self.lc_input.Y_B31 = float(input_data_dict['Y_B31'])
                    self.lc_input.E = float(input_data_dict['E'])
                    self.lc_input.EC = float(input_data_dict['EC'])
                    self.lc_input.EL = float(input_data_dict['EL'])
                    self.lc_input.RSF_a = float(input_data_dict['RSF_a'])
                    self.lc_input.MA = float(input_data_dict['MA'])
                    self.lc_input.t_sl = float(input_data_dict['t_sl'])
                    self.lc_input.LOSS = float(input_data_dict['LOSS'])
                    self.lc_input.FCA = float(input_data_dict['FCA'])
                    self.lc_input.FCA_ml = float(input_data_dict['FCA_ml'])
                    self.lc_input.t_mm = float(input_data_dict['t_mm'])
                    self.lc_input.defect_type = input_data_dict['defect_type']
                    if self.lc_input.defect_type.lower() == 'local metal loss':
                        pass
                    else:
                        self.lc_input.g_r = float(input_data_dict['g_r'])
                    self.lc_input.s = float(input_data_dict['s'])
                    self.lc_input.c = float(input_data_dict['c'])
                    self.lc_input.L_msd = float(input_data_dict['L_msd'])

                    self.short_report_text, self.document = lc_algorithm(self.lc_input)

                    self.gc_or_lc_report = 'lc'

                    print(self.short_report_text)

                    self.short_report_window = ShortReportWindow(self.short_report_text)

                    self.short_report_window.pb_full_report.clicked.connect(self.show_file_dialog)

            else:
                self.warning_dialog.show_warning_dialog(
                    "Please, enter all the input data\nto calculate Fitness-For-Service")

    def create_input_data_dict(self, gc_or_lc):
        """
        :return: List of all input parameters (empty and not empty)
        """
        input_data_dict = {}

        if gc_or_lc == 'gc':
            input_data_dict['asset'] = self.ui.tab_gc.line_asset.text()
            input_data_dict['line_number'] = self.ui.tab_gc.line_line_number.text()
            input_data_dict['monitoring_location'] = self.ui.tab_gc.line_monitoring_location.text()
            input_data_dict['wall_loss_type'] = self.ui.tab_gc.comboBox_wall_loss_type.currentText()
            input_data_dict['material'] = self.ui.tab_gc.comboBox_material.currentText()
            input_data_dict['steel_type'] = self.ui.tab_gc.comboBox_steel_type.currentText()
            input_data_dict['temperature'] = self.ui.tab_gc.comboBox_temperature.currentText()
            input_data_dict['stress'] = self.ui.tab_gc.comboBox_stress.currentText()
            input_data_dict['nominal_pipe_size'] = self.ui.tab_gc.comboBox_nominal_pipe_size.currentText()
            input_data_dict['outside_diameter'] = self.ui.tab_gc.comboBox_outside_diameter.currentText()
            input_data_dict['schedule'] = self.ui.tab_gc.comboBox_schedule.currentText()
            input_data_dict['thickness'] = self.ui.tab_gc.comboBox_thickness.currentText()
            input_data_dict['pipe_type'] = self.ui.tab_gc.comboBox_pipe_type.currentText()
            input_data_dict['mill_under_tolerance'] = self.ui.tab_gc.comboBox_mill_under_tolerance.currentText()
            input_data_dict['P'] = self.ui.tab_gc.line_P.text()
            input_data_dict['Y_B31'] = self.ui.tab_gc.line_Y_B31.text()
            input_data_dict['E'] = self.ui.tab_gc.line_E.text()
            input_data_dict['RSF_a'] = self.ui.tab_gc.line_RSF_a.text()
            input_data_dict['MA'] = self.ui.tab_gc.line_MA.text()
            input_data_dict['t_sl'] = self.ui.tab_gc.line_t_sl.text()
            input_data_dict['LOSS'] = self.ui.tab_gc.line_LOSS.text()
            input_data_dict['FCA'] = self.ui.tab_gc.line_FCA.text()
            input_data_dict['FCA_ml'] = self.ui.tab_gc.line_FCA_ml.text()
            input_data_dict['t_mm'] = self.ui.tab_gc.line_t_mm.text()
            input_data_dict['t_amS'] = self.ui.tab_gc.line_t_amS.text()
            input_data_dict['t_amC'] = self.ui.tab_gc.line_t_amC.text()
        else:
            input_data_dict['asset'] = self.ui.tab_lc.line_asset.text()
            input_data_dict['line_number'] = self.ui.tab_lc.line_line_number.text()
            input_data_dict['monitoring_location'] = self.ui.tab_lc.line_monitoring_location.text()
            input_data_dict['material'] = self.ui.tab_lc.comboBox_material.currentText()
            input_data_dict['steel_type'] = self.ui.tab_lc.comboBox_steel_type.currentText()
            input_data_dict['temperature'] = self.ui.tab_lc.comboBox_temperature.currentText()
            input_data_dict['stress'] = self.ui.tab_lc.comboBox_stress.currentText()
            input_data_dict['nominal_pipe_size'] = self.ui.tab_lc.comboBox_nominal_pipe_size.currentText()
            input_data_dict['outside_diameter'] = self.ui.tab_lc.comboBox_outside_diameter.currentText()
            input_data_dict['schedule'] = self.ui.tab_lc.comboBox_schedule.currentText()
            input_data_dict['thickness'] = self.ui.tab_lc.comboBox_thickness.currentText()
            input_data_dict['pipe_type'] = self.ui.tab_lc.comboBox_pipe_type.currentText()
            input_data_dict['mill_under_tolerance'] = self.ui.tab_lc.comboBox_mill_under_tolerance.currentText()
            input_data_dict['P'] = self.ui.tab_lc.line_P.text()
            input_data_dict['Y_B31'] = self.ui.tab_lc.line_Y_B31.text()
            input_data_dict['E'] = self.ui.tab_lc.line_E.text()
            input_data_dict['EC'] = self.ui.tab_lc.line_EC.text()
            input_data_dict['EL'] = self.ui.tab_lc.line_EL.text()
            input_data_dict['RSF_a'] = self.ui.tab_lc.line_RSF_a.text()
            input_data_dict['MA'] = self.ui.tab_lc.line_MA.text()
            input_data_dict['t_sl'] = self.ui.tab_lc.line_t_sl.text()
            input_data_dict['LOSS'] = self.ui.tab_lc.line_LOSS.text()
            input_data_dict['FCA'] = self.ui.tab_lc.line_FCA.text()
            input_data_dict['FCA_ml'] = self.ui.tab_lc.line_FCA_ml.text()
            input_data_dict['t_mm'] = self.ui.tab_lc.line_t_mm.text()
            input_data_dict['defect_type'] = self.ui.tab_lc.comboBox_defect_type.currentText()
            input_data_dict['g_r'] = self.ui.tab_lc.line_g_r.text()
            input_data_dict['s'] = self.ui.tab_lc.line_s.text()
            input_data_dict['c'] = self.ui.tab_lc.line_c.text()
            input_data_dict['L_msd'] = self.ui.tab_lc.line_L_msd.text()

        return input_data_dict

    def check_all_input_entered(self, input_data_dict:dict):
        return '' not in input_data_dict.values()

    def load_latest_input_data(self):

        if self.ui.tab.currentIndex() == 0:
            gc_latest_input_data_dict = self.gc_latest.load_latest_input_data_dict_from_file()

            if type(gc_latest_input_data_dict) == str:
                # if true it means that the latest input data couldn't be loaded because of Exception
                self.warning_dialog.show_warning_dialog(gc_latest_input_data_dict)
            else:
                self.ui.tab_gc.line_asset.setText(gc_latest_input_data_dict.get('asset'))
                self.ui.tab_gc.line_line_number.setText(gc_latest_input_data_dict.get('line_number'))
                self.ui.tab_gc.line_monitoring_location.setText(gc_latest_input_data_dict.get('monitoring_location'))
                self.ui.tab_gc.comboBox_wall_loss_type.setCurrentText(gc_latest_input_data_dict.get('wall_loss_type'))
                self.ui.tab_gc.comboBox_material.setCurrentText(gc_latest_input_data_dict.get('material'))
                self.ui.tab_gc.comboBox_steel_type.setCurrentText(gc_latest_input_data_dict.get('steel_type'))
                self.ui.tab_gc.comboBox_temperature.setCurrentText(gc_latest_input_data_dict.get('temperature'))
                self.ui.tab_gc.comboBox_stress.setCurrentText(gc_latest_input_data_dict.get('stress'))
                self.ui.tab_gc.comboBox_nominal_pipe_size.setCurrentText(gc_latest_input_data_dict.get('nominal_pipe_size'))
                self.ui.tab_gc.comboBox_outside_diameter.setCurrentText(gc_latest_input_data_dict.get('outside_diameter'))
                self.ui.tab_gc.comboBox_schedule.setCurrentText(gc_latest_input_data_dict.get('schedule'))
                self.ui.tab_gc.comboBox_thickness.setCurrentText(gc_latest_input_data_dict.get('thickness'))
                self.ui.tab_gc.comboBox_pipe_type.setCurrentText(gc_latest_input_data_dict.get('pipe_type'))
                self.ui.tab_gc.comboBox_mill_under_tolerance.setCurrentText(gc_latest_input_data_dict.get('mill_under_tolerance'))
                self.ui.tab_gc.line_P.setText(gc_latest_input_data_dict.get('P'))
                self.ui.tab_gc.line_Y_B31.setText(gc_latest_input_data_dict.get('Y_B31'))
                self.ui.tab_gc.line_E.setText(gc_latest_input_data_dict.get('E'))
                self.ui.tab_gc.line_RSF_a.setText(gc_latest_input_data_dict.get('RSF_a'))
                self.ui.tab_gc.line_MA.setText(gc_latest_input_data_dict.get('MA'))
                self.ui.tab_gc.line_t_sl.setText(gc_latest_input_data_dict.get('t_sl'))
                self.ui.tab_gc.line_LOSS.setText(gc_latest_input_data_dict.get('LOSS'))
                self.ui.tab_gc.line_FCA.setText(gc_latest_input_data_dict.get('FCA'))
                self.ui.tab_gc.line_FCA_ml.setText(gc_latest_input_data_dict.get('FCA_ml'))
                self.ui.tab_gc.line_t_mm.setText(gc_latest_input_data_dict.get('t_mm'))
                self.ui.tab_gc.line_t_amS.setText(gc_latest_input_data_dict.get('t_amS'))
                self.ui.tab_gc.line_t_amC.setText(gc_latest_input_data_dict.get('t_amC'))
        else:
            lc_latest_input_data_dict = self.lc_latest.load_latest_input_data_dict_from_file()

            if type(lc_latest_input_data_dict) == str:
                # if true it means that the latest input data couldn't be loaded because of Exception
                self.warning_dialog.show_warning_dialog(lc_latest_input_data_dict)
            else:
                self.ui.tab_lc.line_asset.setText(lc_latest_input_data_dict.get('asset'))
                self.ui.tab_lc.line_line_number.setText(lc_latest_input_data_dict.get('line_number'))
                self.ui.tab_lc.line_monitoring_location.setText(lc_latest_input_data_dict.get('monitoring_location'))
                self.ui.tab_lc.comboBox_material.setCurrentText(lc_latest_input_data_dict.get('material'))
                self.ui.tab_lc.comboBox_steel_type.setCurrentText(lc_latest_input_data_dict.get('steel_type'))
                self.ui.tab_lc.comboBox_temperature.setCurrentText(lc_latest_input_data_dict.get('temperature'))
                self.ui.tab_lc.comboBox_stress.setCurrentText(lc_latest_input_data_dict.get('stress'))
                self.ui.tab_lc.comboBox_nominal_pipe_size.setCurrentText(lc_latest_input_data_dict.get('nominal_pipe_size'))
                self.ui.tab_lc.comboBox_outside_diameter.setCurrentText(lc_latest_input_data_dict.get('outside_diameter'))
                self.ui.tab_lc.comboBox_schedule.setCurrentText(lc_latest_input_data_dict.get('schedule'))
                self.ui.tab_lc.comboBox_thickness.setCurrentText(lc_latest_input_data_dict.get('thickness'))
                self.ui.tab_lc.comboBox_pipe_type.setCurrentText(lc_latest_input_data_dict.get('pipe_type'))
                self.ui.tab_lc.comboBox_mill_under_tolerance.setCurrentText(lc_latest_input_data_dict.get('mill_under_tolerance'))
                self.ui.tab_lc.line_P.setText(lc_latest_input_data_dict.get('P'))
                self.ui.tab_lc.line_Y_B31.setText(lc_latest_input_data_dict.get('Y_B31'))
                self.ui.tab_lc.line_E.setText(lc_latest_input_data_dict.get('E'))
                self.ui.tab_lc.line_EC.setText(lc_latest_input_data_dict.get('EC'))
                self.ui.tab_lc.line_EL.setText(lc_latest_input_data_dict.get('EL'))
                self.ui.tab_lc.line_RSF_a.setText(lc_latest_input_data_dict.get('RSF_a'))
                self.ui.tab_lc.line_MA.setText(lc_latest_input_data_dict.get('MA'))
                self.ui.tab_lc.line_t_sl.setText(lc_latest_input_data_dict.get('t_sl'))
                self.ui.tab_lc.line_LOSS.setText(lc_latest_input_data_dict.get('LOSS'))
                self.ui.tab_lc.line_FCA.setText(lc_latest_input_data_dict.get('FCA'))
                self.ui.tab_lc.line_FCA_ml.setText(lc_latest_input_data_dict.get('FCA_ml'))
                self.ui.tab_lc.line_t_mm.setText(lc_latest_input_data_dict.get('t_mm'))
                self.ui.tab_lc.comboBox_defect_type.setCurrentText(lc_latest_input_data_dict.get('defect_type'))
                if lc_latest_input_data_dict['defect_type'].lower() == 'local metal loss':
                    # self.ui.tab_lc.line_g_r.setText('not required')
                    pass
                else:
                    self.ui.tab_lc.line_g_r.setText(lc_latest_input_data_dict.get('g_r'))
                self.ui.tab_lc.line_s.setText(lc_latest_input_data_dict.get('s'))
                self.ui.tab_lc.line_c.setText(lc_latest_input_data_dict.get('c'))
                self.ui.tab_lc.line_L_msd.setText(lc_latest_input_data_dict.get('L_msd'))

    def add_items(self):
        self.ui.tab_gc.comboBox_material.addItems(self.dl.df_material['material'])
        self.ui.tab_lc.comboBox_material.addItems(self.dl.df_material['material'])

        self.ui.tab_gc.comboBox_steel_type.addItems(self.filter_material(self.dl.df_material)['steel type'])
        self.ui.tab_lc.comboBox_steel_type.addItems(self.filter_material(self.dl.df_material)['steel type'])

        self.ui.tab_gc.comboBox_temperature.addItems(self.dl.df_stress['temperature'].unique())
        self.ui.tab_lc.comboBox_temperature.addItems(self.dl.df_stress['temperature'].unique())

        self.ui.tab_gc.comboBox_stress.addItems(self.filter_stress(self.dl.df_stress)['stress'])
        self.ui.tab_lc.comboBox_stress.addItems(self.filter_stress(self.dl.df_stress)['stress'])

        self.ui.tab_gc.comboBox_nominal_pipe_size.addItems(self.dl.df_pipe['nominal pipe size'])
        self.ui.tab_lc.comboBox_nominal_pipe_size.addItems(self.dl.df_pipe['nominal pipe size'])

        self.ui.tab_gc.comboBox_outside_diameter.addItems(self.filter_pipe(self.dl.df_pipe)['outside diameter'])
        self.ui.tab_lc.comboBox_outside_diameter.addItems(self.filter_pipe(self.dl.df_pipe)['outside diameter'])

        self.ui.tab_gc.comboBox_schedule.addItems(self.filter_schedule(self.dl.df_thickness)['schedule'])
        self.ui.tab_lc.comboBox_schedule.addItems(self.filter_schedule(self.dl.df_thickness)['schedule'])

        self.ui.tab_gc.comboBox_thickness.addItems(self.filter_thickness(self.dl.df_thickness)['wall thickness'])
        self.ui.tab_lc.comboBox_thickness.addItems(self.filter_thickness(self.dl.df_thickness)['wall thickness'])
        self.ui.tab_gc.comboBox_thickness.setEditable(False)
        self.ui.tab_lc.comboBox_thickness.setEditable(False)

        self.ui.tab_gc.comboBox_wall_loss_type.addItems(self.dl.df_wall_loss_type['type of wall loss'])

        self.ui.tab_gc.comboBox_pipe_type.addItems(self.dl.df_mill_under_tolerance['pipe type'])
        self.ui.tab_lc.comboBox_pipe_type.addItems(self.dl.df_mill_under_tolerance['pipe type'])

        self.ui.tab_gc.comboBox_mill_under_tolerance.addItems(self.filter_mill_under_tolerance(self.dl.df_mill_under_tolerance)['mill under tolerance'])
        self.ui.tab_lc.comboBox_mill_under_tolerance.addItems(self.filter_mill_under_tolerance(self.dl.df_mill_under_tolerance)['mill under tolerance'])

        self.ui.tab_lc.comboBox_defect_type.addItems(self.dl.df_defect_type['defect type'])

        self.ui.tab_gc.line_Y_B31.setText('0.4')
        self.ui.tab_lc.line_Y_B31.setText('0.4')

        self.ui.tab_gc.line_E.setText('1.0')
        self.ui.tab_lc.line_E.setText('1.0')

        self.ui.tab_gc.line_RSF_a.setText('0.9')
        self.ui.tab_lc.line_RSF_a.setText('0.9')

        self.ui.tab_gc.line_MA.setText('0')
        self.ui.tab_lc.line_MA.setText('0')

        self.ui.tab_gc.line_t_sl.setText('0')
        self.ui.tab_lc.line_t_sl.setText('0')

        self.ui.tab_gc.line_LOSS.setText('0')
        self.ui.tab_lc.line_LOSS.setText('0')

        self.ui.tab_gc.line_FCA.setText('0')
        self.ui.tab_lc.line_FCA.setText('0')

        self.ui.tab_lc.line_EC.setText('1.0')

        self.ui.tab_lc.line_EL.setText('1.0')




    # FILTERING of DataFrames
    # =================================================================
    def filter_material(self, df_material):
        if self.ui.tab.currentIndex() == 0:
            selected_material = self.ui.tab_gc.comboBox_material.currentText()
        else:
            selected_material = self.ui.tab_lc.comboBox_material.currentText()
        return df_material[df_material['material'] == selected_material]

    def filter_stress(self, df_stress):
        if self.ui.tab.currentIndex() == 0:
            selected_material = self.ui.tab_gc.comboBox_material.currentText()
            selected_temperature = self.ui.tab_gc.comboBox_temperature.currentText()
        else:
            selected_material = self.ui.tab_lc.comboBox_material.currentText()
            selected_temperature = self.ui.tab_lc.comboBox_temperature.currentText()
        return df_stress[
            (df_stress['material'] == selected_material) & (df_stress['temperature'] == selected_temperature)]

    def filter_pipe(self,  df_pipe):
        if self.ui.tab.currentIndex() == 0:
            selected_pipe = self.ui.tab_gc.comboBox_nominal_pipe_size.currentText()
        else:
            selected_pipe = self.ui.tab_lc.comboBox_nominal_pipe_size.currentText()
        return df_pipe[df_pipe['nominal pipe size'] == selected_pipe]

    def filter_schedule(self, df_thickness):
        if self.ui.tab.currentIndex() == 0:
            selected_steel_type = self.ui.tab_gc.comboBox_steel_type.currentText()
            selected_nominal_pipe_size = self.ui.tab_gc.comboBox_nominal_pipe_size.currentText()
        else:
            selected_steel_type = self.ui.tab_lc.comboBox_steel_type.currentText()
            selected_nominal_pipe_size = self.ui.tab_lc.comboBox_nominal_pipe_size.currentText()
        return df_thickness[(df_thickness['steel type'] == selected_steel_type) & (df_thickness['nominal pipe size'] == selected_nominal_pipe_size)]

    def filter_thickness(self, df_thickness):
        if self.ui.tab.currentIndex() == 0:
            selected_nominal_pipe_size = self.ui.tab_gc.comboBox_nominal_pipe_size.currentText()
            selected_steel_type = self.ui.tab_gc.comboBox_steel_type.currentText()
            selected_schedule = self.ui.tab_gc.comboBox_schedule.currentText()
        else:
            selected_nominal_pipe_size = self.ui.tab_lc.comboBox_nominal_pipe_size.currentText()
            selected_steel_type = self.ui.tab_lc.comboBox_steel_type.currentText()
            selected_schedule = self.ui.tab_lc.comboBox_schedule.currentText()
        return df_thickness[
            (df_thickness['nominal pipe size'] == selected_nominal_pipe_size) & (df_thickness['steel type'] == selected_steel_type) & (df_thickness['schedule'] == selected_schedule)]

    def filter_mill_under_tolerance(self, df_mill_under_tolerance):
        if self.ui.tab.currentIndex() == 0:
            selected_pipe_type = self.ui.tab_gc.comboBox_pipe_type.currentText()
        else:
            selected_pipe_type = self.ui.tab_lc.comboBox_pipe_type.currentText()
        return df_mill_under_tolerance[df_mill_under_tolerance['pipe type'] == selected_pipe_type]

    # UPDATING of comboBoxes
    # =================================================================
    def update_comboBox_steel_type(self):
        # Filter steel type data based on the selected material
        df_steel_type_filtered = self.filter_material(self.dl.df_material)

        if self.ui.tab.currentIndex() == 0:
            self.ui.tab_gc.comboBox_steel_type.clear()
            self.ui.tab_gc.comboBox_steel_type.addItems(df_steel_type_filtered['steel type'])
        else:
            self.ui.tab_lc.comboBox_steel_type.clear()
            self.ui.tab_lc.comboBox_steel_type.addItems(df_steel_type_filtered['steel type'])

    def update_comboBox_stress(self):
        # Filter stress data based on the selected material and temperature
        df_stress_filtered = self.filter_stress(self.dl.df_stress)

        if self.ui.tab.currentIndex() == 0:
            self.ui.tab_gc.comboBox_stress.clear()
            self.ui.tab_gc.comboBox_stress.addItems(df_stress_filtered['stress'])
        else:
            self.ui.tab_lc.comboBox_stress.clear()
            self.ui.tab_lc.comboBox_stress.addItems(df_stress_filtered['stress'])

    def update_comboBox_outside_diameter(self):
        # Filter pipe data based on the selected nominal pipe size
        df_pipe_filtered = self.filter_pipe(self.dl.df_pipe)

        if self.ui.tab.currentIndex() == 0:
            self.ui.tab_gc.comboBox_outside_diameter.clear()
            self.ui.tab_gc.comboBox_outside_diameter.addItems(df_pipe_filtered['outside diameter'])
        else:
            self.ui.tab_lc.comboBox_outside_diameter.clear()
            self.ui.tab_lc.comboBox_outside_diameter.addItems(df_pipe_filtered['outside diameter'])

    def update_comboBox_schedule(self):
        # Filter schedule data based on the selected Steel type and Nominal pipe size
        df_schedule_filtered = self.filter_schedule(self.dl.df_thickness)

        if self.ui.tab.currentIndex() == 0:
            self.ui.tab_gc.comboBox_schedule.clear()
            self.ui.tab_gc.comboBox_schedule.addItems(df_schedule_filtered['schedule'])
        else:
            self.ui.tab_lc.comboBox_schedule.clear()
            self.ui.tab_lc.comboBox_schedule.addItems(df_schedule_filtered['schedule'])

    def update_comboBox_thickness(self):
        # Filter thickness data based on the selected nominal pipe size, steel type and schedule
        df_thickness_filtered = self.filter_thickness(self.dl.df_thickness)

        if self.ui.tab.currentIndex() == 0:
            self.ui.tab_gc.comboBox_thickness.clear()
            self.ui.tab_gc.comboBox_thickness.addItems(df_thickness_filtered['wall thickness'])
        else:
            self.ui.tab_lc.comboBox_thickness.clear()
            self.ui.tab_lc.comboBox_thickness.addItems(df_thickness_filtered['wall thickness'])

    def update_comboBox_mill_under_tolerance(self):
        # Filter mill under tolerance data based on the selected pipe type
        df_mill_under_tolerance_filtered = self.filter_mill_under_tolerance(self.dl.df_mill_under_tolerance)

        if self.ui.tab.currentIndex() == 0:
            self.ui.tab_gc.comboBox_mill_under_tolerance.clear()
            self.ui.tab_gc.comboBox_mill_under_tolerance.addItems(df_mill_under_tolerance_filtered['mill under tolerance'])
        else:
            self.ui.tab_lc.comboBox_mill_under_tolerance.clear()
            self.ui.tab_lc.comboBox_mill_under_tolerance.addItems(df_mill_under_tolerance_filtered['mill under tolerance'])

# if __name__ == '__main__':
#     import time
#     start_time = time.time()
#     app = QApplication(sys.argv)
#     ex = App()
#     diff = time.time() - start_time
#     print(f'Длительность запуска всей программы - {diff}')
#     sys.exit(app.exec_())

def logging_excepthook(type_, value, traceback):
    logger.opt(exception=(type_, value, traceback)).error("Unhandled Qt error")

logger.add('logger_logs.log', rotation="5 MB", compression="zip")

sys.excepthook = logging_excepthook
app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
