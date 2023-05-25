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
    
    def crop(self): 
        return self.image[int(self.H/13):int(self.H/8), int(self.W/7):int(self.W/2-20)]
    
    def grayScale(self, img): 
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def binary(self, gray): 
        return cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
    def convert_binary(self, binary): 
        return cv2.bitwise_not(binary)
    
    def detect_ID(self): 
        image = self.crop()
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
        result = [extract[1], extract[2]]
        
        return result

def main():
    ocr = ExtractMark()
    result = [] 

    process = ImageProcessing('khaothi/demo1.jpg')

    ph = process.detect_ID()
    cv2.imshow('sophach', ph)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    result += ocr.read(ph)

    result.append(process.convert_base64())

    print(result)
    
    return result

if __name__ == '__main__': 
    main()








