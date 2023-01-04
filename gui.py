import PySimpleGUI as sg
from CSV_Reader import CSV_Reader


layouts = {
        "loading_file_window": [
                [sg.Text("Choose .csv file: "), sg.Input(), sg.FileBrowse(key="-FILE_PATH-")],
                [sg.Text("Choose delimeter: "), sg.OptionMenu(values=[",", ";", ":"], key="-DELIMETER_")],
                [sg.Button("Load")], 
                [sg.Button("Exit")]],
        "working_with_files_window": [
                [sg.Text("Choose what to do with file"), sg.OptionMenu(values=["Get headers", "Check dimensions", "Get column by name", "Get column by index", "Get value"])],
                [sg.Text("To switch order of columns, first get headers, go to your favourite text editor, change the order, paste it below and click change order")],
                [sg.Input(), sg.Button("Change order")]]
    }


class GUI():

    def __init__(self, title: str, size: tuple(int, int), layouts: dict, theme="lightgreen6") -> None:
        self.title = title
        self.size = size
        self.layouts = layouts
        self.theme = theme

    def create_window(self, layout: str) -> sg.Window:
        return sg.Window(title=self.title, layout=self.layouts.get(layout), size=self.size)

    def get_layout_names(self) -> list:
        return list(self.layouts.keys())

        
        

