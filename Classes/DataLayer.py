import time
import json
import pandas as pd


class DataLayer:
    def __init__(self):

        self.df_material = None
        self.df_stress = None
        self.df_pipe = None
        self.df_schedule = None
        self.df_thickness = None
        self.df_wall_loss_type = pd.DataFrame({'type of wall loss': ('Internal', 'External')})
        self.df_mill_under_tolerance = pd.DataFrame(
            {'pipe type': ('seamless %', 'welded mm', 'user defined %', 'user defined mm'),
             'mill under tolerance': ('12.50', '0.25', '', '')})
        self.df_defect_type = pd.DataFrame({'defect type': ('Local metal loss','Groove')})

        self.load_data()

    def load_data(self):
        # start = time.time()

        # Load data from material.xlsx
        self.df_material = pd.read_excel('source_tables/material.xlsx',
                                         dtype={'material': str, 'steel type': str})

        # Load data from stress.xlsx
        self.df_stress = pd.read_excel('source_tables/stress.xlsx',
                                       dtype={'material': str, 'temperature': str, 'stress': str})

        # Load data from pipe.xlsx
        self.df_pipe = pd.read_excel('source_tables/pipe.xlsx',
                                       dtype={'nominal pipe size': str, 'outside diameter': str})

        # Load data from schedule.xlsx
        self.df_schedule = pd.read_excel('source_tables/schedule.xlsx',
                                     dtype={'steel type': str, 'schedule': str})

        # Load data from thickness.xlsx
        self.df_thickness = pd.read_excel('source_tables/thickness.xlsx',
                                     dtype={'nominal pipe size': str, 'steel type': str, 'schedule': str, 'wall thickness': str})

    def __str__(self):
        return f'{self.df_material} \n{self.df_stress} \n{self.df_pipe} \n{self.df_wall_loss_type} \n{self.df_mill_under_tolerance} \n{self.df_thickness} \n{self.df_schedule}  \n{self.df_defect_type}'

class InputDataStaging:
    def __init__(self):
        self.asset = None
        self.line_number = None
        self.monitoring_location = None
        self.wall_loss_type = None
        self.material = None
        self.steel_type = None
        self.temperature = None
        self.stress = None
        self.nominal_pipe_size = None
        self.outside_diameter = None
        self.schedule = None
        self.thickness = None
        self.pipe_type = None
        self.mill_under_tolerance = None
        self.P = None
        self.Y_B31 = None
        self.E = None
        self.RSF_a = None
        self.MA = None
        self.t_sl = None
        self.LOSS = None
        self.FCA = None
        self.FCA_ml = None
        self.NDE_type = None
        self.t_mm = None
        self.t_amS = None
        self.t_amC = None

        self.EC = None
        self.EL = None
        self.defect_type = None
        self.g_r = None
        self.s = None
        self.c = None
        self.L_msd = None



class LatestInputData:
    def __init__(self, gc_or_lc):
        self.gc_or_lc = gc_or_lc
    def save_input_data_dict_to_file(self, input_data_dict):
        try:
            with open(f"{self.gc_or_lc}_latest_input_data.txt", "w") as f:
                json.dump(input_data_dict, f)
                print("Info: InputData saved to file successfully")
        except IOError:
            print("Error: Failed to save data to file (IOError).")
        return


    def load_latest_input_data_dict_from_file(self):
        """
        :return: dictionary of the latest input data, loaded from .txt file
        """
        try:
            with open(f"{self.gc_or_lc}_latest_input_data.txt", "r") as f:
                latest_input_data_dict = json.load(f)
                print("Info: the latest_input_data loaded to dictionary successfully")
                print(latest_input_data_dict)
                return latest_input_data_dict
        except FileNotFoundError:
            exception_text = f"Couldn't load the latest input data:\nFile with the latest input not found"
        except (json.JSONDecodeError):
            exception_text = f"Couldn't load the latest input data: \n{self.gc_or_lc}_latest_input_data.txt file decoding error happened"
        return exception_text

if __name__ == '__main__':

    start = time.time()
    dl = DataLayer()
    diff = time.time() - start
    print(dl)


    print(f'\nВремя выполнения класса слоя данных {diff}')

    latest_input_data = LatestInputData()
    dict = {
    "lineEdit_2": "value2",
    "lineEdit_3": "value3",
    "lineEdit_4": "value4",
    "lineEdit_5": "value5",
}
    latest_input_data.save_input_data_to_file(dict, gc_or_lc = 'gc')
    print(latest_input_data.load_latest_input_data_from_file(gc_or_lc = 'gc'))


