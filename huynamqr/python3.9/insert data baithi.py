import pymysql
from flask import Flask
import os
import base64


app = Flask(__name__)
app.secret_key = 'many random bytes'
# Kết nối tới cơ sở dữ liệu
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='11092001Phanhuynam',
                             db='qlpicture')

folder_path = 'D:/OneDrive - The Danang University of Economics/Nam 3 ki 2/NCKH/PICTURE'

# Lấy tất cả các file trong thư mục
file_list = os.listdir(folder_path)

# Lặp qua từng file
for x in file_list:
    tach=x.split('_')
    phongthi = tach[0]
    cathi = tach[1]
    monthi = tach[2]
    matkchamthi = tach[3]
    print('phongthi:', phongthi)
    print('cathi:', cathi)
    print('monthi:', monthi)
    print('matkchamthi:', matkchamthi)
    z = os.listdir(folder_path+'/'+x)
    for a in z:
        # Đọc tất cả các giá trị trong file và chuyển đổi sang base64
        png = folder_path+'/'+x +'/'+a
        # print(png)
        with open(png, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            cur = connection.cursor()
            cur.execute("insert into picture(picture_base64) VALUES ( %s)",( encoded_string))
            cur.connection.commit()
            cur.close()


# with open("image.png", "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read())
#     print(encoded_string)



# cur = connection.cursor()
# cur.execute("INSERT INTO baithi (picture) VALUES (%s)", (picture))
# cur.connection.commit()


