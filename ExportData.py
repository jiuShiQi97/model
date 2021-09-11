import xlrd
import xlwt
import random

#需求：1。求出合作天数 2. 求出供应比并按行求平均 3. 表二按行求和
wb = xlrd.open_workbook("documents/a.xlsx")
#
sheet1 = wb.sheet_by_index(0)
sheet2 = wb.sheet_by_index(1)
sheet3 = wb.sheet_by_index(2)

n1rows = sheet1.nrows
n1cols = sheet1.ncols
n2rows = sheet2.nrows
n2cols = sheet2.ncols
n3rows = sheet3.nrows
n3cols = sheet3.ncols

# def write_excel_xls(path, sheet_name, value):
#     index = len(value)  # 获取需要写入数据的行数
#     workbook = xlwt.Workbook()  # 新建一个工作簿
#     sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
#     for i in range(0, index):
#         for j in range(0, len(value)):
#             sheet.write(i, j, value[i])  # 像表格中写入数据（对应的行和列）
#     workbook.save(path)  # 保存工作簿
#     print("xls格式表格写入数据成功！")


# def write_excel_xls_append(path, value):
#     index = len(value)  # 获取需要写入数据的行数
#     workbook = xlrd.open_workbook(path)  # 打开工作簿
#     sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
#     worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
#     rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
#     # new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
#     new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
#     for i in range(0, index):
#         for j in range(0, len(value[i])):
#             new_worksheet.write(i+rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
#     new_workbook.save(path)  # 保存工作簿
#     print("xls格式表格【追加】写入数据成功！")

book_name_xls = 'ques.xls'

sheet1_xls = 'ques1'
sheet2_xls = 'ques2'
sheet3_xls = 'ques3'


value1 = []
value2 = []
value3 = []

x = 0
y = 0
sum = 0
for y in range(2,24):
    ran = random.uniform(0.8,1.2)
    for x in range(6,407):
        data = sheet1.cell_value(x,1)
        if type(data)==float:
            value = int(data*ran)
            value1.append(value)
            sum = sum + value
        else:
            value = 0
            value1.append(value)
    print(value1)
    print("第"+str(y)+"周的总量： "+str(sum))
    sum = 0
    value1 = []


print("################")
for y in range(2,24):
    ran = random.uniform(0.8,1.2)
    for x in range(6,407):
        data = sheet2.cell_value(x,1)
        if type(data)==float:
            value = int(data*ran)
            value2.append(value)
            sum = sum + value
        else:
            value = 0
            value1.append(value)
    print(value2)
    print("第"+str(y)+"周的总量： "+str(sum))
    sum = 0
    value2 = []
print("################")
for y in range(2,24):
    ran = random.uniform(0.8,1.2)
    for x in range(6,407):
        data = sheet3.cell_value(x,1)
        if type(data)==float:
            value = int(data*ran)
            value3.append(value)
            sum = sum + value
        else:
            value = 0
            value3.append(value)
    print(value3)
    print("第"+str(y)+"周的总量： "+str(sum))
    sum = 0
    value3 = []


# write_excel_xls(book_name_xls, sheet1_xls, value1)
# write_excel_xls(book_name_xls, sheet2_xls, value2)
# write_excel_xls(book_name_xls, sheet3_xls, value3)


