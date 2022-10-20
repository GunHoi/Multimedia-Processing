from PyQt5.QtWidgets import QMainWindow, QApplication

class image_compression_class(QMainWindow):
    def __init__(self):
        from PyQt5.uic import loadUi
        super(image_compression_class, self).__init__()
        loadUi('image_compression.ui', self)
        self.source_image = None
        self.btnOpenimage.clicked.connect(lambda: self.open_image())
        self.percent.valueChanged.connect(lambda: self.compress_image())

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
            self.show_file_size(fileName, self.lbl_size_image1)

        except Exception as e:
            print('Error: {}'.format(e))

    def show_image(self, label, image):
        import qimage2ndarray
        from PyQt5 import QtGui
        image = qimage2ndarray.array2qimage(image)
        qpixmap = QtGui.QPixmap.fromImage(image)
        label.setPixmap(qpixmap)

    def show_file_size(self, filename, label):
        import os
        file_size = os.path.getsize(filename)
        label.setText(f'{file_size / 1000} KB')

    def compress_image(self):
        from PIL import Image
        from skimage.io import imread

        try:
            percent = self.percent.value()
            self.quality_label.setText(f'{percent}%')
            image = Image.fromarray(self.source_image, 'RGB')
            compressed_file = 'compressed.jpeg'
            image.save(compressed_file, quality = percent)
            compressed_image = imread(compressed_file)
            self.show_image(self.lblImage2, compressed_image)
            self.show_file_size(compressed_file, self.lbl_size_image2)
        except Exception as e:
            print(f'Error: {e}')


def image_compression_app():
        import sys
        from PyQt5.QtWidgets import QApplication
        app = QApplication(sys.argv)
        window = image_compression_class()
        window.show()
        app.exec()


if __name__ == '__main__':
    image_compression_app()
