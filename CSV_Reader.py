import pandas as pd
import os
from pathlib import Path

class CSV_Reader:

    data: pd.DataFrame

    def __init__(self, file_path: str, has_headers: bool) -> None:
        self.file_path = file_path
        self.headers = has_headers
        self.encoding = "ASCII"
        self.delimeter = ','

    def load_file(self) -> None:
        self.data = pd.read_csv(self.file_path)
    
    def get_headers(self) -> pd.DataFrame:
        return self.data.columns

    def get_column_by_name(self, col_name: str) -> pd.DataFrame:
        return self.data.loc[:, col_name]

    def get_column_by_index(self, col_index: int) -> pd.DataFrame:
            return self.data.iloc[:, col_index]

    def get_dimensions(self) -> tuple:
        return self.data.shape

    def get_value_at(self, row: int, col: str):
        try:
            return self.data.at(row, col)
        except (KeyError, ValueError) as err:
            print("Wrong value was submitted")
            return err

    def change_order_of_cols(self, new_order: list[str]) -> pd.DataFrame:
        df = self.data.copy(deep=True)
        return df[new_order]

    def print_file(self) -> None:
        print(self.data.to_string())


            
