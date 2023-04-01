import cv2
import pickle

class ImageProcessing: 
    def __init__(self, filename, W=547, H=447, C=3) -> None:
        self.filename = filename
        self.W = W
        self.H = H 
        self.C = C
        return
    
    def readImage(self): 
        return cv2.imread(self.filename)
    
    def resize(self, img):
        return cv2.resize(img, (self.H, self.W))
    
    def crop(self, img): 
        return img[50:int(self.H/3), :int(self.W/4)]
    
    def grayScale(self, img): 
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    def threshOld(self, gray):
        return cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    
    def findContour(self, thresh): 
        return cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    def filterContour(self, contours): 
        rects = [] 
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < 1000 or area > 5000:
                continue
            rect = cv2.boundingRect(cnt)
            rects.append(rect)
        return rects
    
    def getCoordinates(self, img, rects): 
        x, y, w, h = rects[0]
        w, y = int(w/2.5), int(h/1.5)
        return img[y:y+h, x:x+w]
    
    def process(self): 
        image = self.readImage()
        image = self.resize(image)
        image = self.crop(image)
        grayImage = self.grayScale(image)
        thresh = self.threshOld(grayImage)
        contours, hierarchy = self.findContour(thresh)
        rects = self.filterContour(contours)
        image = self.getCoordinates(image, rects)
        cv2.imshow('output', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return image

class OCR: 
    def __init__(self, fileModel, image) -> None:
        self.fileModel = fileModel
        self.image = image
        return
    
    def readMark(self):
        with open(self.fileModel, 'rb') as f: 
            reader = pickle.load(f)
            result = reader.readtext(self.image)
            mark = ' '.join(detect[1] for detect in result)
        print(mark)
        return mark
    
    
def main(): 
    processing = ImageProcessing('tuluan5 - Copy.jpg')
    image = processing.process()
    model = OCR('OCR.pkl', image)
    model.readMark()                                     

if __name__ == '__main__': 
    main()