import xlrd

wb = xlrd.open_workbook("documents/b.xlsx")
#
sheet1 = wb.sheet_by_index(0)
sheet2 = wb.sheet_by_index(1)
sheet3 = wb.sheet_by_index(2)

T3 = T6 = T2 = T8 = T4 = T1 = T7 = T5 = []

x = 0
for x in