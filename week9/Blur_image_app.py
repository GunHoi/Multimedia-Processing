from PyQt5.QtWidgets import QMainWindow, QApplication


class blur_image_class(QMainWindow):
    def __init__(self):
        from PyQt5.uic import loadUi
        super(blur_image_class, self).__init__()
        loadUi('Blur_image_app.ui', self)
        self.btnBrowse.clicked.connect(lambda: self.open_image())
        self.btnBlur.clicked.connect(lambda: self.blur_image())
        self.image = None

    def open_image(self):
        from PyQt5 import QtWidgets, QtCore
        from skimage import io
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                            'Open File',
                                                            QtCore.QDir.rootPath(),
                                                            '*.*')
        try:
            self.image = io.imread(fileName)
            self.show_image(self.lblImage1, self.image)
        except Exception as e:
            print('Error: {}'.format(e))

    def blur_image(self):
        from skimage import filters, io
        try:
            sigma = int(self.txtSigma.toPlainText())
            io.imsave('blurImage.png', filters.gaussian(self.image, sigma=sigma, multichannel=True))
            image2 = io.imread('blurImage.png')
            self.show_image(self.lblImage2, image2)
        except Exception as e:
            print('Error: {}'.format(e))

    def show_image(self, label, image):
        import qimage2ndarray
        from PyQt5 import QtGui

        image = qimage2ndarray.array2qimage(image)
        qpixmap = QtGui.QPixmap.fromImage(image)
        label.setPixmap(qpixmap)

def Blur_image_app():
    app = QApplication([])
    window = blur_image_class()
    window.show()
    app.exec()


if __name__ == '__main__':
    Blur_image_app()
