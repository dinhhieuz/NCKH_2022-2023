import cv2


class ImageProcessing:

    def __init__(self, filename, W=547, H=447, C=3) -> None:
        self.filename = filename
        self.W = W
        self.H = H
        self.C = C

        image = self.readImage()
        image = self.resize(image)
        self.image = image
        return

    def readImage(self):
        return cv2.imread(self.filename)

    def resize(self, img):
        return cv2.resize(img, (self.H, self.W))

    def crop(self, img, object_name):
        if object_name == 'marking':
            return img[50:int(self.H / 3), :int(self.W / 4)]
        return img[int(self.H * 0.5 / 7):int(self.H / 5), int(self.W * 4 / 6):int(self.W * 4.5 / 6)]

    def grayScale(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def threshOld(self, gray):
        return cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    def binary(self, gray):
        return cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

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
        w, y = int(w / 2.5), int(h / 1.5)
        return img[y:y + h, x:x + w]

    def gaussianBlur(self, image):
        ksize = (5, 5)
        sigmaX = 0
        blur = cv2.GaussianBlur(image, ksize, sigmaX)
        return blur

    def convert_binary(self, binary):
        return cv2.bitwise_not(binary)

    def detect_marking(self):
        image = self.crop(self.image, object_name='marking')
        grayImage = self.grayScale(image)
        thresh = self.threshOld(grayImage)
        contours, hierarchy = self.findContour(thresh)
        rects = self.filterContour(contours)
        image = self.getCoordinates(grayImage, rects)
        binary = self.binary(image)
        image = self.convert_binary(binary)

        cv2.imshow('Marking', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return image

    def detect_ID(self):
        image = self.crop(self.image, object_name='ID')
        grayImage = self.grayScale(image)
        binary = self.binary(grayImage)
        image = self.convert_binary(binary)

        cv2.imshow('ID', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return image


class ExtractMark:
    def __init__(self, fileModel, list_image) -> None:
        self.fileModel = fileModel
        self.list_image = list_image
        from tensorflow.keras.models import load_model
        self.model = load_model(self.fileModel)

        return

    def readMark(self):
        import numpy as np
        fields = ['marking', 'confidence_1', 'id', 'confidence_2']
        info = []
        for image in self.list_image:
            img = np.reshape(cv2.resize(image.astype(float), (28, 28)), (-1, 28, 28, 1)) / 255.0

            result = self.model.predict(img)
            mark = np.argmax(result)
            confidence = np.max(result) * 100
            info += [mark, confidence]

        record = dict(zip(fields, info))
        print(record)
        return record


def main():
    processing = ImageProcessing('test.jpg')
    marking = processing.detect_marking()
    id = processing.detect_ID()
    image = [marking, id]

    model = ExtractMark('model.h5', image)
    info = model.readMark()


if __name__ == '__main__':
    main()