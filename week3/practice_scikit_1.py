def skimage_open_image():
    from skimage import io
    file_name = '../Images/0-colors-image.jpg'

    im = io.imread(file_name)
    io.imshow(im)
    io.show()


if __name__ == '__main__':
    skimage_open_image()
