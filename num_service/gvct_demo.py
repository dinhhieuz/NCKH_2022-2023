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
        if object_name == 'marking': 
            return self.image[int(self.H/4.5):int(self.H/3.6), 30:int(self.W/6.2)]
        return self.image[120:int(self.H/7.5), int(self.W*4.1/5):int(self.W-50)]
    
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
        result = [extract[1].replace(' ', '').replace(',', ''), round(extract[2], 2)]
        
        return result

def main():
    ocr = ExtractMark()
    result = [] 

    process = ImageProcessing('chamthi/demo5.jpg')
    mark = process.detect_marking()
    cv2.imshow('image', mark)
    result += ocr.read(mark)

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







