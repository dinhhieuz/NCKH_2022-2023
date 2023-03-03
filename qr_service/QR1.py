
file_open = open('myqrcode.txt', 'a')
import cv2
from pyzbar.pyzbar import decode
import numpy as np
cam = cv2.VideoCapture(0)
#neu 0 là camara laptop của mình, thiết lập mạng nội bộ và check camara.
while True:
    ok, frame = cam.read()
    for code in decode(frame):
        '''print(code) #type --> cách dùng code/ thuộc tính rect
        x = code.rect.left
        y = code.rect.top
        w = code.rect.width
        h = code.rect.height'''

        '''cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 3)'''

        pts = np. array([code.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines (frame, [pts], True, (255, 0, 255), 3)

    cv2.imshow('QRcode Frame', frame)
    '''polylines: Vì có lấy đc 4 cặp điểm, polylines'''
    '''đọc dữ liệu, xác nhận enter, ghi thành một tập tin, imshow, waitkey: chờ khoá'''
    key_pressed = cv2.waitKey(1)
    if key_pressed == 13:
        data = code.data.decode('utf -8')
        print (data)
        file_open.write(data + '\n')
    if key_pressed == 113:
        break

file_open.close()
cam.release()
cv2.destroyAllWindown()




