from server import constants
import pandas as pd


class Server:
    def __init__(self):
        self.data_table = pd.read_csv(constants.server_data_adress)
        self.messages_table = pd.read_csv(constants.server_data_adress)

    def aggregate_all(self):
        pass

