import xlrd
import xlwt

wb = xlrd.open_workbook("documents/data.xls")
sheet1 = wb.sheet_by_index(0)
sheet2 = wb.sheet_by_index(1)

n1rows = sheet1.nrows
n1cols = sheet1.ncols
n2rows = sheet2.nrows
n2cols = sheet2.ncols

def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")

book_name_xls = '导出.xls'
sheet_name_xls = '表二减表一'

sheet1 = wb.sheet_by_index(0)
sheet2 = wb.sheet_by_index(1)

x = 0
y = 0

for x in range(0,401):
    for y in range(0,239):
        sub = sheet2.cell_value(x,y)-sheet1.cell_value(x,y)
        print(sub)
        # print(sub)
    print("###################")
w,h = 402,240
Matrix = [[0 for y in range(w)] for x in range[h]]

# for x in range(0,401):
#     for y in range(0,239):
#         sub = sheet1.cell_value(x,y)-sheet2.cell_value(x,y)
#         print(sub)
value = []


if __name__== '__main__':
    write_excel_xls(book_name_xls,sheet_name_xls,value)

