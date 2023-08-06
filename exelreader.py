from openpyxl import load_workbook

from youre_app.models import youre model

work_book = load_workbook('./ph.xlsx')

# if you have only one sheet Enter "Sheet1"
# if you have more than sheets look at buttom right of your Exel Project and see Which Sheet is Active Or Wichone you want to work with
work_sheet = work_book['Your_Sheet_Name']
# columns in exel is text --->  A B C D E F G 
# columns number ------------>  1 2 3 4 5 6 7

# loop inside first row
for row in range(number_of_your_column, End_Rows_Number+1):
    row = str(row)

    #_______________________________________
    # in this Case Ive got 3 Column
    column1_name = work_sheet[f'B{row}'].value
    column2_name = work_sheet[f'C{row}'].value
    column3_name = work_sheet[f'D{row}'].value
    #if You have more columns add it like top and Change the column name example:
    # column_name = work_sheet[f'colum_text{row}'].value 
    #_______________________________________
    
    #if you have more columns in database add it here
    model = items(model_field1=column1_name, model_field2=column2_name, model_field3=column3_name)
    model.save()
    print(f'succesfull {column1_name}')


    # print(f'column1_name==> {column1_name}', f'column2_name==> {column2_name}', f'column3_name==> {column3_name}')


