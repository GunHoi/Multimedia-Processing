from PyQt5.QtWidgets import QMainWindow, QApplication


def get_3x3_neighbors(x, y):
    neighbors = [(x - 1, y - 1),
                 (x, y - 1),
                 (x + 1, y - 1),
                 (x - 1, y),
                 (x, y),
                 (x + 1, y),
                 (x - 1, y + 1),
                 (x, y + 1),
                 (x + 1, y + 1)]
    return neighbors


def get_neighbor_values(im, list_neighbors):
    list_value = []
    for point in list_neighbors:
        list_value.append(im[point[0], point[1]])
    return list_value


def get_matrix_33_filtering(matrix1, matrix2):
    import numpy as np
    matrix1, matrix2 = np.asarray(matrix1), np.asarray(matrix2)
    total = 0
    for i in range(3):
        for j in range(3):
            total += matrix1[i, j] * matrix2[i, j]
    return total / 9


class Apply_matrix_image_class(QMainWindow):
    def __init__(self):
        from PyQt5.uic import loadUi
        super(Apply_matrix_image_class, self).__init__()
        loadUi('Assignment9a_app.ui', self)
        self.btnBrowse.clicked.connect(lambda: self.open_image())
        self.btnApply.clicked.connect(lambda: self.matrix_smoothing())
        self.image = None

    def matrix_smoothing(self):
        from skimage import io
        from skimage.color import rgb2gray
        import matplotlib.pyplot as plt
        import numpy as np

        try:
            im = rgb2gray(self.image)
            im_gray_pad = np.pad(im, pad_width=1)
            n, m = im_gray_pad.shape[0], im_gray_pad.shape[1]
            im_filter = np.zeros(im_gray_pad.shape)

            w1 = int(self.textEdit_1.toPlainText())
            w2 = int(self.textEdit_2.toPlainText())
            w3 = int(self.textEdit_3.toPlainText())
            w4 = int(self.textEdit_4.toPlainText())
            w5 = int(self.textEdit_5.toPlainText())
            w6 = int(self.textEdit_6.toPlainText())
            w7 = int(self.textEdit_7.toPlainText())
            w8 = int(self.textEdit_8.toPlainText())
            w9 = int(self.textEdit_9.toPlainText())

            weight = [[w1, w2, w3],
                      [w4, w5, w6],
                      [w7, w8, w9]]

            for x in range(1, n - 1):
                for y in range(1, m - 1):
                    neighbors = get_3x3_neighbors(x, y)
                    neighbors_value = get_neighbor_values(im_gray_pad, neighbors)
                    neighbors_33 = np.asarray(neighbors_value).reshape((3, 3))
                    im_filter[x, y] = get_matrix_33_filtering(neighbors_33, weight)

            io.imsave('GrayImage.png', im_gray_pad)
            io.imsave('FilterImage.png', im_filter)
            image2 = io.imread('GrayImage.png')
            image3 = io.imread('FilterImage.png')
            self.show_image(self.lblImage2, image2)
            self.show_image(self.lblImage3, image3)
        except Exception as e:
            print('Error: {}'.format(e))

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


    def show_image(self, label, image):
        import qimage2ndarray
        from PyQt5 import QtGui

        image = qimage2ndarray.array2qimage(image)
        qpixmap = QtGui.QPixmap.fromImage(image)
        label.setPixmap(qpixmap)


def Apply_matrix_image_app():
    app = QApplication([])
    window = Apply_matrix_image_class()
    window.show()
    app.exec()


if __name__ == '__main__':
    Apply_matrix_image_app()
