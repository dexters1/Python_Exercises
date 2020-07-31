from xlrd import open_workbook,cellname

book = open_workbook("zadatak_excel.xls")
sheet = book.sheet_by_index(0)

print sheet.name
print sheet.nrows
print sheet.ncols

def writeRows(row_list):
    with open("movies_excel.txt", "w") as f:
        for row_index in range(len(row_list)):
            L = []
            for col_index in range(sheet.ncols):
                L.append(sheet.cell(row_list[row_index], col_index).value)
            f.write("%s, %s, %s\n" %(L[0], L[1], L[2]))
        
row_list = []

for row_index in range(sheet.nrows):
    for col_index in range(sheet.ncols):
        print sheet.cell(row_index, col_index).value
        if "Terry Jones" in str(sheet.cell(row_index, col_index).value):
            row_list.append(row_index)
            
writeRows(row_list)