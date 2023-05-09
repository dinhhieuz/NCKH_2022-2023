import cv2 as cv
import pymysql
from flask import Flask
from pyzbar import pyzbar
import base64

app = Flask(__name__)
app.secret_key = 'many random bytes'
# Kết nối tới cơ sở dữ liệu
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='11092001Phanhuynam',
                             db='qlpicture')

cap = cv.VideoCapture(0)
found = False

while not found:
    ret, frame = cap.read()
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text = "{} . {}".format(barcodeData, barcodeType)
        print(text)
        cv.putText(frame, text, (x - 10, y - 10), cv.FONT_HERSHEY_SIMPLEX,
                   0.5, (0, 0, 255), 1)

        # hiển thị ảnh
        cv.imshow('QR Code', frame)
        #chuyển ảnh sang base64 và lưu vào DB

        _, buffer = cv.imencode('.jpg', frame)
        encoded_string = base64.b64encode(buffer)
        cur = connection.cursor()
        cur.execute("insert into picture(picture_base64) VALUES ( %s)",( encoded_string))
        cur.connection.commit()
        cur.close()
        # đóng tất cả các cửa sổ khi tìm thấy mã QR
        cv.waitKey(0)
        cv.destroyAllWindows()
        found = True
        break

    cv.imshow('qrcode - Ma QR', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
