import xlrd
import xlwt
import random

wb = xlrd.open_workbook("documents/supply.xlsx")

sheet1 = wb.sheet_by_index(0)

n1rows = sheet1.nrows
n1cols = sheet1.ncols

x,y = 1,1
for x in range(1,403):
    max = sheet1.cell_value(x,y)
    x += 1
    int(max)
    # print(type(int(max)))
    print(random.uniform(0,int(max)))

# print(type(random.uniform(0,max)))
