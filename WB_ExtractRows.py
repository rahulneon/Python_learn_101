import xlrd
loc="F:\SampleData.xlsx"

wb = xlrd.open_workbook(loc)

# here the sample shet has nuber of sheets so the index value identifies the sheet that is to be utilized
sheet = wb.sheet_by_index(1)
sheet.cell_value(0,0)



# extracting number of rows
print(sheet.nrows)


# extrating number of columns
print(sheet.ncols)

# print first row

print(sheet.row_values(2,0))

# extracting all column names

for i in range(sheet.ncols):
    print(sheet.cell_value(0,i))



#extracting first column.
"""
assert isinstance(sheet.nrows, object)
for i in range(sheet.nrows):
     print(sheet.cell_value(i,0))
     

"""

