import cv2 as cv
# import pymysql
# import base64
import os
from PIL import Image
from pyzbar.pyzbar import decode

# Kết nối tới cơ sở dữ liệu
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='11092001Phanhuynam',
#                              db='qlpicture')

# Đường dẫn tới file ảnh
image_path = 'D:/OneDrive - The Danang University of Economics/Nam 3 ki 2/NCKH/NGHIÊN CỨU KHOA HỌC/python3.9/picture'
picture=os.listdir(image_path)
for i in picture:
    # Đọc ảnh từ file
    # img = cv.imread(picture+'/'+i)
    img = Image.open(image_path+'/'+i)
    dcode = decode(img)
    data = dcode[0].data.decode()
    print(data)

    # # Chuyển đổi ảnh sang base64
    # _, buffer = cv.imencode('.jpg', i)
    # encoded_string = base64.b64encode(buffer)
    # # Lưu base64 vào database
    # cur = connection.cursor()
    # cur.execute("INSERT INTO picture (picture_base64) VALUES (%s)", (encoded_string,))
    # cur.connection.commit()
    # cur.close()
