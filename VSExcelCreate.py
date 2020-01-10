import xlwt

'''
# define table style
def set_style(name,height,bold=False):
    style = xlwt.XFStle()
    font = xlwt.Font()
    font.name = name
    # font.bold = bold
    font.color_index = 4
    font.height = height 
    style.font = font
    return style
'''

# write excel
'''
列： ID/name/location/volume
行: 1-100
'''
def write_excel():
    f = xlwt.Workbook()
    sheet1 = f.add_sheet("rawData",True)

    # initial value of row & column
    rowN = int(input('Input how many rows:'))
    column0 = ["A","B","C","D"]
    columnN = len(column0)

    # write row0
    for i in range(0,columnN):
        sheet1.col(i).width = 256 * 3
        sheet1.write(0,i,column0[i])

    # write other rows
    for row in range(1,rowN):
        for column in range(0,columnN):
            sheet1.write(row,column,column0[column] + str(row))
    
    f.save('exTest.xls')

if __name__ == '__main__':
    write_excel()
