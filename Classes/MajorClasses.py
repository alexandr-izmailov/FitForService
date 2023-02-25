# definition of class, common for all functions, which is used to return result and text variables
class DataCalculated:
    def __init__(self, result, text):
        self.result = result
        self.text = text

    def __repr__(self):
        return f'Result: {self.result}\nText: {self.text}'
