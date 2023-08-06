from openpyxl import load_workbook

from car.models import items

work_book = load_workbook('./ph.xlsx')


work_sheet = work_book['Sheet2']

for row in range(2,22):
    row = str(row)
    water_pomp = work_sheet[f'B{row}'].value
    code = work_sheet[f'C{row}'].value
    price = work_sheet[f'D{row}'].value
    # items(title=water_pomp, product_code=code, price=price, brand_id=8)
    # items.save()
    print(f'succesfull {water_pomp}')


    # print(f'water_pomp==> {water_pomp}', f'code==> {code}', f'price==> {price}')


