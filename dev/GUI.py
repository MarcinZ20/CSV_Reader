import PySimpleGUI as sg
from CsvReader import CSV_Reader


class GUI():

    def __init__(self, title: str, size: tuple, theme="lightgreen6") -> None:
        self.title = title
        self.size = size
        self.theme = theme

    def make_window_1(self) -> sg.Window:
        view =  [
                [sg.Text("Choose .csv file: "), sg.Input(key="-FILE_PATH-", change_submits=True), sg.FileBrowse()],
                [sg.Text("Choose delimeter: "), sg.OptionMenu(values=[",", ";", ":"], key="-DELIMETER-")],
                [sg.Button("Load")], 
                [sg.Button("Exit")],
                [sg.Text('', k="-OUTPUT-")]]

        return sg.Window(title=self.title, layout=view, size=self.size, finalize=True)

    def make_window_2(self) -> sg.Window:
        left_col =  [
                [sg.Text("Choose what to do with file:")],
                [sg.OptionMenu(values=["Get headers", "Check dimensions", "Get column by name", "Get column by index", "Get value", "Change columns order"], default_value="Get value", k="-OPTIONS-", size=(20,7)), sg.Button("Go")],
                [sg.Text('')],
                [sg.Button("Exit", key="Exit"), sg.Button("Go back", key="Back")]]
        
        right_col = [
                    [sg.Text("OUTPUT:", justification="center")],
                    [sg.Text(size=(25,7), k="-OUTPUT-")],
                    [sg.Text("Row (int): ", visible=False, k="t1"), sg.Text("Column (str): ", visible=False, k="t2")],
                    [sg.Input(key="-ROW-", visible=False, size=(5,1)), sg.Input(key="-COL-", visible=False, size=(20,1))],
                    [sg.Button("Get value",  visible=False, key="submit")]]


        view = [[sg.Column(left_col), sg.VSeparator(), sg.Column(right_col)]]

        return sg.Window(title=self.title, layout=view, size=self.size, finalize=True)

    def make_window_3(self) -> sg.Window:

        view =  [    
                [sg.Text("Here is the default order: ")],
                    [sg.Text(key="-OUTPUT-")],
                    [sg.Text('')],
                    [sg.Text("Write values separated with a coma ex: l1, l2, l3, l4")],
                    [sg.Input(key="-ORDER-")],
                    [sg.Text("Choose a folder to save new file:")],
                    [sg.Text("Choose directory: "), sg.Input(key="-FOLDER_PATH-", change_submits=True), sg.FolderBrowse()],
                    [sg.Text("Choose name for the file (without extension)")],
                    [sg.Input(key="-NAME-")],
                    [sg.Button("Reorder columns", key="order")],
                    [sg.Button("Exit", key="Exit"), sg.Button("Go back", key="Back")]]

        return sg.Window(title=self.title, layout=view, size=self.size, finalize=True)

    @staticmethod
    def multiple_elements_visibility(window: sg.Window, ids: list, show: bool) -> None:
        for index in range(len(ids)):
            window.find_element(ids[index]).update(visible=show)

    def run() -> int:
        gui = GUI("CSV EDITOR", (600, 300))
        csvr = CSV_Reader()
        
        window1, window2, window3 = gui.make_window_1(), None, None 

        while True:
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED or event == 'Exit':
                window.close()
                break

            elif event == "Load" and values["-FILE_PATH-"] == '':
                sg.popup("Warning!","You must first add file path!", non_blocking=False, keep_on_top=True)

            elif event == "Load" and not values["-FILE_PATH-"] == '' and not window2:
                window2 = gui.make_window_2()
                window1.hide()
                try:
                    csvr.file_path = values["-FILE_PATH-"]
                    csvr.delimeter = values["-DELIMETER-"] if values["-DELIMETER-"] != '' else ','
                except (TypeError, ValueError) as e:
                    print(e)
                finally:
                    csvr.load_file()
                
            elif event == "Go":
                if values["-OPTIONS-"] == "Get headers": 
                    window["-OUTPUT-"].update(csvr.to_string(csvr.get_headers()))
                elif values["-OPTIONS-"] == "Check dimensions":
                    window["-OUTPUT-"].update(csvr.get_dimensions())
                elif values["-OPTIONS-"] == "Get value":
                    window["-OUTPUT-"].update("Please fill in row number and column name number below!")
                    gui.multiple_elements_visibility(window, ["-ROW-", "-COL-", "t1", "t2", "submit"], True)
                elif values["-OPTIONS-"] == "Get column by name":
                    window["-OUTPUT-"].update("Please fill in column name below!")
                    gui.multiple_elements_visibility(window, ["-COL-", "t2", "submit"], True)
                    window["-OUTPUT-"].update({})
                elif values["-OPTIONS-"] == "Get column by index":
                    window["-OUTPUT-"].update("Please fill in column index below!")
                    gui.multiple_elements_visibility(window, ["-COL-", "t2", "submit"], True)
                    window["-OUTPUT-"].update({})
                elif values["-OPTIONS-"] == "Change columns order" and not window3:
                    window3 = gui.make_window_3()
                    window2.hide()
                    window3["-OUTPUT-"].update(csvr.to_string(csvr.get_headers()))

            elif event == "submit":
                window["-OUTPUT-"].update(csvr.get_value_at(values["-ROW-"], values["-COL-"]))
                gui.multiple_elements_visibility(window, ["-ROW-", "-COL-", "t1", "t2", "submit"], False)

            elif event == "order":
                csvr.change_order_of_cols(values["-ORDER-"], values["-FOLDER_PATH-"], values["-NAME-"])
            
            elif event == "Back":
                if window == window3:
                    window2.un_hide()
                    window3.hide()
                if window == window2:
                    window1.un_hide()
                    window2.hide()
                

            
                

            




                

                
                
