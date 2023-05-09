import pymysql
from flask import Flask
import base64
from PIL import Image
from io import BytesIO
app = Flask(__name__)
app.secret_key = 'many random bytes'
# Kết nối tới cơ sở dữ liệu
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='11092001Phanhuynam',
                             db='qlpicture')
cur=connection.cursor()
cur.execute("select picture_base64 from picture where Idpicture =2")
result = cur.fetchone()
picture_base64 = result[0]
image_data = base64.b64decode(bytes(picture_base64, 'utf-8'))
img = Image.open(BytesIO(image_data))
img.show()

# for i in data:
#     print(i)
#     print()
# for i in data:
#     image_data = base64.b64decode(i)

