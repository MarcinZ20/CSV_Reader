import pandas as pd
import os
from pathlib import Path

class CSV_Reader:

    _data: pd.DataFrame

    def __init__(self, file_path = '', has_headers = True) -> None:
        self._file_path = file_path
        self._headers = has_headers
        self._encoding = "utf-8"
        self._delimeter = ','

    @property
    def file_path(self) -> str:
        return self._file_path

    @file_path.setter
    def file_path(self, path: str) -> None:
        if not Path(path).exists() or not path.endswith('.csv'):
            raise TypeError("Path doesn't exist or is not .csv!")
        self._file_path = path

    @property
    def headers(self) -> bool:
        return self._headers

    @headers.setter
    def headers(self, has_headers: bool) -> None:
        self._headers = has_headers

    @property
    def encoding(self) -> str:
        return self._encoding

    @encoding.setter
    def encoding(self, encoding: str) -> None:
        if encoding not in ("ASCII", "utf-8"):
            raise ValueError("Wrong encoding type!")
        self._encoding = encoding

    @property
    def delimeter(self) -> str:
        return self._delimeter

    @delimeter.setter
    def delimeter(self, delimeter: str) -> None:
        if delimeter not in (',', ';', ':'):
            raise ValueError("Unsupported delimeter!")
        self._delimeter = delimeter

    def load_file(self) -> None:
        self._data = pd.read_csv(self._file_path)
    
    def get_headers(self) -> pd.DataFrame:
        return self._data.columns

    def get_column_by_name(self, col_name: str) -> pd.DataFrame:
        return self.__data.loc[:, col_name]

    def get_column_by_index(self, col_index: int) -> pd.DataFrame:
            return self._data.iloc[:, col_index]

    def get_dimensions(self) -> str:
        return f'Rows: {self._data.shape[0]}\nColumns: {self._data.shape[1]}'

    def get_value_at(self, row: int, col: str) -> str:
        try:
            return str(self._data.at[int(row), col])
        except (KeyError, ValueError) as err:
            print("Wrong value was submitted", err)
            return err

    def change_order_of_cols(self, new_order: list, dir_path: str, file_name: str) -> None:
        
        extension = ".csv"
        path = dir_path + '/' + file_name + extension 

        if not Path(dir_path).exists():
            raise ValueError("Path doesn't exist ...")
      
        df = self._data.copy(deep=True)
        df = df[new_order.split(sep=',')]
        df.to_csv(path)      

    def print_file(self) -> None:
        print(self._data.to_string())

    @staticmethod
    def to_string(df: pd.DataFrame) -> str:
        return str(list(df))


            
