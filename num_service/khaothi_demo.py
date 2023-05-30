import cv2 
import numpy as np 
import base64
import easyocr

class ImageProcessing: 
    def __init__(self, filename) -> None:
        self.filename = filename
        
        self.image = self.readImage()
        self.H, self.W, self.C = self.image.shape
        return

    def readImage(self): 
        return cv2.imread(self.filename)
    
    def crop(self, object_name): 
        if object_name == 'id':
            return self.image[int(self.H/13):int(self.H/8), int(self.W/7):int(self.W/2-20)]
        return self.image[int(self.H/13):int(self.H/8), int(self.W/2-20):]
    
    def grayScale(self, img): 
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def binary(self, gray): 
        return cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
    def convert_binary(self, binary): 
        return cv2.bitwise_not(binary)
    
    def detect_ID(self): 
        image = self.crop('id')
        grayImage = self.grayScale(image)
        binary = self.binary(grayImage)
        image = self.convert_binary(binary)
        return image

    def detect_sbd(self): 
        image = self.crop('sbd')
        grayImage = self.grayScale(image)
        binary = self.binary(grayImage)
        image = self.convert_binary(binary)
        return image

    def convert_base64(self):
        _, buffer = cv2.imencode('.jpg', self.image)
        encoded_string = base64.b64encode(buffer)
        return encoded_string[:5]
    
class ExtractMark: 
    def __init__(self) -> None:
        self.reader = easyocr.Reader(['en'])
        return
    
    def read(self, image):
        extract = self.reader.readtext(image)[0]
        result = [extract[1].replace(' ', ''), round(extract[2], 2)]
        
        return result

def main():
    ocr = ExtractMark()
    result = [] 

    process = ImageProcessing('khaothi/demo5.jpg')

    ph = process.detect_ID()
    cv2.imshow('sophach', ph)
    result += ocr.read(ph)

    sbd = process.detect_sbd()
    cv2.imshow('sbd', sbd)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    result += ocr.read(sbd)

    result.append(process.convert_base64())

    print(result)
    
    return result

if __name__ == '__main__': 
    main()








