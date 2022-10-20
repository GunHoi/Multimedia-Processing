from PyQt5.QtWidgets import QMainWindow, QApplication


class image_processing_class(QMainWindow):
    def __init__(self):
        from PyQt5.uic import loadUi
        super(image_processing_class, self).__init__()
        loadUi('image_processing_app.ui', self)
        self.source_image = None
        self.btnOpenImage.clicked.connect(lambda: self.open_image())
        self.btnShowhist.clicked.connect(lambda: self.show_histogram())
        self.btnInvert.clicked.connect(lambda: self.invert_image())
        self.hsKValue.valueChanged.connect(lambda: self.change_kValue())
        self.btnEdgeDetection.clicked.connect(lambda: self.edgeDetection())

        self.btnConnectWebcam.clicked.connect(lambda: self.connectwebcam())
        self.btnStopWebcam.clicked.connect(lambda: self.stopwebcam())
        self.btnBlur.clicked.connect(lambda: self.set_blur())

        self.stop_webcam = False
        self.blur_flag = False

    def open_image(self):
        from PyQt5 import QtWidgets, QtCore
        from skimage import io
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                            'Open File',
                                                            QtCore.QDir.rootPath(),
                                                            '*.*')
        try:
            self.source_image = io.imread(fileName)
            self.show_image(self.lblImage1, self.source_image)
        except Exception as e:
            print('Error: {}'.format(e))

    def show_histogram(self):
        from matplotlib import pyplot as plt
        from skimage import io
        plt.figure(figsize=(5, 4))
        plt.hist(self.source_image.ravel(), bins=256)
        plt.savefig('hist.png')
        hist_img = io.imread('hist.png')
        self.show_image(self.lblImage2, hist_img)

    def invert_image(self):
        from skimage.color import rgb2gray
        from skimage.io import imread
        import matplotlib.pyplot as plt
        a_max = float(self.txtAlpha.toPlainText())
        gray_image = rgb2gray(self.source_image)
        im_invert = a_max - gray_image

        plt.figure(figsize=(5, 4)), plt.axis('off')
        plt.imshow(im_invert, cmap='gray', vmin=0, vmax=1)
        plt.savefig('invert.png')

        img2 = imread('invert.png')
        self.show_image(self.lblImage2, img2)

    def change_kValue(self):
        from skimage.io import imread
        import matplotlib.pyplot as plt
        import numpy as np
        k = self.hsKValue.value() / 100
        image_k = (self.source_image * k).astype(np.uint8)
        self.lblKvalue.setText(str(k))
        plt.axis('off')
        plt.imshow(image_k, vmin=0, vmax=255)
        plt.savefig('image_k.png')

        img2 = imread('image_k.png')
        self.show_image(self.lblImage2, img2)

    def edgeDetection(self):
        from skimage import feature
        import matplotlib.pyplot as plt
        from skimage.io import imread
        from skimage.color import rgb2gray
        sigma = int(self.txtSigma.toPlainText())
        gray_image = rgb2gray(self.source_image)
        edge_image = feature.canny(gray_image, sigma=sigma)
        plt.axis('off'), plt.imshow(edge_image, cmap='gray')
        plt.savefig('edge_image.png')

        img2 = imread('edge_image.png')
        self.show_image(self.lblImage2, img2)

    def connectwebcam(self):
        import cv2
        self.stop_webcam = False
        self.blur_flag = False
        # 0: WebcamId. If your computer doesn't have a webcam. Replace '0' by a Video Clip
        #cap = cv2.VideoCapture(0)
        cap = cv2.VideoCapture('examples.mp4')
        while True:
            ret, self.source_image = cap.read()
            self.source_image = cv2.cvtColor(self.source_image, cv2.COLOR_BGR2RGB)
            self.show_image(self.lblImage1, self.source_image)
            if self.blur_flag:
                Beta = int(self.txtBeta.toPlainText())
                blur_image = cv2.blur(self.source_image, (Beta, Beta))
                self.show_image(self.lblImage2, blur_image)
            cv2.waitKey(24)
            if self.stop_webcam:
                break
        cap.release()
        cv2.destroyAllWindows()

    def stopwebcam(self):
        self.stop_webcam = True

    def set_blur(self):
        self.blur_flag = True

    def show_image(self, label, image):
        import qimage2ndarray
        from PyQt5 import QtGui

        image = qimage2ndarray.array2qimage(image)
        qpixmap = QtGui.QPixmap.fromImage(image)
        label.setPixmap(qpixmap)


def image_processing_app():
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = image_processing_class()
    window.show()
    app.exec()


if __name__ == '__main__':
    image_processing_app()
