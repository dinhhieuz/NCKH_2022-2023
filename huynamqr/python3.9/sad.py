import pymysql
from flask import Flask
import os
import base64

folder_path = 'D:/OneDrive - The Danang University of Economics/Nam 3 ki 2/NCKH/PICTURE/A201_1_MIS2001_201121521128'

# Lấy tất cả các file trong thư mục
file_list = os.listdir(folder_path)
# print(file_list)
# Lặp qua từng file
for x in file_list:

        # Đọc tất cả các giá trị trong file và chuyển đổi sang base64
        png=folder_path+'/'+x
        with open(png, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            print(encoded_string)