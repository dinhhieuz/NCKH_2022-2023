import cv2 
import numpy as np 
from pyzbar.pyzbar import decode
import base64

class ImageProcessing: 
    def __init__(self, filename) -> None:
        self.filename = filename
        
        self.image = self.readImage()
        self.H, self.W, self.C = self.image.shape
        return

    def readImage(self): 
        return cv2.imread(self.filename)
    
    def crop(self, object_name): 
        if object_name == 'marking': 
            return self.image[int(self.H/5.2):int(self.H/3.2), 30:int(self.W/6)]
        return self.image[100:int(self.H/6), int(self.W*2.2/5):int(self.W-100)]
    
    def grayScale(self, img): 
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def binary(self, gray): 
        return cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
    def convert_binary(self, binary): 
        return cv2.bitwise_not(binary)

    def detect_marking(self): 
        image = self.crop(object_name = 'marking')
        grayImage = self.grayScale(image)
        binary = self.binary(grayImage)
        image = self.convert_binary(binary)
        return image
    
    def detect_ID(self): 
        image = self.crop(object_name = 'ID')
        grayImage = self.grayScale(image)
        binary = self.binary(grayImage)
        image = self.convert_binary(binary)
        return image

    def get_qrcode(self): 
        qr = DetectQR()
        return qr.extract(self.image)

    def convert_base64(self):
        _, buffer = cv2.imencode('.jpg', self.image)
        encoded_string = base64.b64encode(buffer)
        return encoded_string

class ExtractMark: 
    def __init__(self, fileModel) -> None:
        self.fileModel = fileModel

        from tensorflow.keras.models import load_model
        self.model = load_model(self.fileModel)

        return
    
    def read(self, image):

        img = np.reshape(cv2.resize(image.astype(float), (28, 28)), (-1, 28, 28, 1)) / 255.0

        pred = self.model.predict(img)
        mark = np.argmax(pred)
        confidence = np.max(pred) * 100

        result = [mark, confidence]

        return result

class DetectQR: 
    def __init__(self) -> None:
        pass

    def extract(self, img):
        dcode = decode(img)
        data = dcode[0].data.decode()
        return data



if __name__ == '__main__': 

    pred = ExtractMark('model.h5')

    mark = ImageProcessing('anh1.jpg')
    result_marking = [mark.get_qrcode()]

    mark_cell = mark.detect_marking()
    result_marking += pred.read(mark_cell)
    result_marking += [mark.convert_base64()[:5]]
    print(result_marking)

    ###### 

    id = ImageProcessing('anh2.jpg')
    result_id = [id.get_qrcode()]

    id_cell = id.detect_ID()
    result_id += pred.read(id_cell)
    result_id += [id.convert_base64()[:5]]
    print(result_id)