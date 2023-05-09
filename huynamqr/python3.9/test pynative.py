import pymysql
from flask import Flask
import os
import base64


# app = Flask(__name__)
# app.secret_key = 'many random bytes'
# # Kết nối tới cơ sở dữ liệu
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='11092001Phanhuynam',
#                              db='qlpicture')

#
#
# def insertBLOB(emp_id, name, photo, biodataFile):
#     print("Inserting BLOB into python_employee table")
#     try:
#         connection = pymysql.connect(host='localhost',
#                                              database='qlpicture',
#                                              user='root',
#                                              password='11092001Phanhuynam')
#
#         cursor = connection.cursor()
#         sql_insert_blob_query = """ INSERT INTO python_employee
#                           (id, name, photo, biodata) VALUES (%s,%s,%s,%s)"""
#
#         empPicture = convertToBinaryData(photo)
#         file = convertToBinaryData(biodataFile)
#
#         # Convert data into tuple format
#         insert_blob_tuple = (emp_id, name, empPicture, file)
#         result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
#         connection.commit()
#         print("Image and file inserted successfully as a BLOB into python_employee table", result)
#
#     except pymysql.connect.Error as error:
#         print("Failed inserting BLOB data into MySQL table {}".format(error))

folder_path = 'D:/OneDrive - The Danang University of Economics/Nam 3 ki 2/NCKH/PICTURE'

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

# Lấy tất cả các file trong thư mục
file_list = os.listdir(folder_path)

# Lặp qua từng file
for x in file_list:
    # Nếu file không phải là thư mục
    z = os.listdir(folder_path+'/'+x)
    print(convertToBinaryData(z))
