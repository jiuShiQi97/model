import xlrd
import xlwt

#需求：1。求出合作天数 2. 求出供应比并按行求平均 3. 表二按行求和
wb = xlrd.open_workbook("documents/doc1.xlsx")
#
sheet1 = wb.sheet_by_index(0)
sheet2 = wb.sheet_by_index(1)

n1rows = sheet1.nrows
n1cols = sheet1.ncols
n2rows = sheet2.nrows
n2cols = sheet2.ncols

#表二按行求和

x = 0
y = 0
sum = 0

# while(x < n2rows):
#     while(y < n2cols):
#         sum = sum + sheet2.cell_value(x,y)
#         # print("s"+str(x)+"供应商在第"+str(y-1)+"周发货量:"+str(sheet2.cell_value(x,y)))
#         y += 1
#         print("S"+str(x)+"供应商供应总量为："+str(sum))
#     x+=1

# print(sheet1.cell_value(1,2))
# print(sheet2.cell_value(1,2))


