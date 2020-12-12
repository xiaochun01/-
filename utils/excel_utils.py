import xlrd3

class ExcelUtils:
    def __init__(self,excel_file_path,sheel_name):
        self.excel_file_path = excel_file_path
        self.sheel_name = sheel_name
        self.sheet = self.get_sheet()

    def get_sheet(self):
        work_book  = xlrd3.open_workbook(self.excel_file_path)
        sheet = work_book.sheet_by_name(self.sheel_name)
        return sheet

    def get_max_row_number(self):
        max_row_number = self.sheet.nrows
        return max_row_number

    def get_column_count(self):
        column_count =self.sheet.ncols
        return column_count
    def ger_merget_cell_value(self):
        merget_info = self.sheet.merged_cells
        return merget_info
    def get_merge_cell_value(self,row_index,col_index):
        cell_value = None
        for (min_row,max_row,min_col,max_clo) in self.ger_merget_cell_value():
            if min_row<= row_index and max_row>row_index:
                if min_col <= col_index and max_clo>col_index:
                    cell_value = self.sheet.cell_value(min_row,min_col)
                    break
                else:
                    cell_value = self.sheet.cell_value(row_index, col_index)
            else:
                cell_value =self.sheet.cell_value(row_index,col_index)
        return cell_value

    def get_all_data(self):
        execl_list_data = []
        row_head = self.sheet.row_values(0)
        for i in range(1,self.get_max_row_number()):
            row_dict = {}
            for j in range(self.get_column_count()):
                row_dict[row_head[j]] = self.get_merge_cell_value(i,j)
            execl_list_data.append(row_dict)
        return execl_list_data











