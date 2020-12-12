import xlrd3

wk = xlrd3.open_workbook('testdata.xlsx')
sheet = wk.sheet_by_name('Sheet1')

print(sheet.cell_value(1,3))
print(sheet.merged_cells)

a=sheet.row_values(0)
print(a)

