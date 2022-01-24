import shutil
import os
import xlrd

def mk_dir(path):
    if os.path.exists(path):
        return path
    else:
        os.mkdir(path)
        return path
path = r'/home/fst/桌面/shuji/临港9/0113/lg9'
img_path = path + '/' + 'moban1'
xlsx_path = path + '/' + 'car_result_2022-01-13.xlsx'



f = xlrd.open_workbook(xlsx_path)
sh = f.sheet_by_name('车型测试')

for i in range(sh.nrows):
    try:
        wheels = int(sh.row_values(i)[1])
        picture_name = int(sh.row_values(i)[2])
        picture = img_path + '/' + str(picture_name) + '.jpg'
        shutil.move(picture, os.path.join(mk_dir(img_path + '/' + str(wheels)),str(picture_name) + '.jpg'))
    except:
        print(i)
    # print(wheels, picture_name)