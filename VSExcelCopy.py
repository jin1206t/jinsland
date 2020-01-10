import xlrd 
import xlwt

''' 
copy sheet
in all column >=2, plus 1
except column A
'''

def copy_excel():
    # read file
    sheetRe = xlrd.open_workbook('sample.xls')
    sheetRe = sheetRe.sheets()[0]
    columnN = sheetRe.ncols
    rowN = sheetRe.nrows

    # write file
    Wr = xlwt.Workbook()
    sheet1 = Wr.add_sheet('RawData',True) #add sheet name later

    for row in range(rowN):
        cell = sheetRe.cell_value(row,0)
        type(cell)
        sheet1.write(row,0,cell)
        for column in range(1,columnN):
            sheet1.write(row,column,sheetRe.cell_value(row,column) + '1')

    Wr.save('exCopied.xls')

if __name__ == '__main__':
    copy_excel()