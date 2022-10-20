def skimage_save_image():
    from skimage import io
    import os
    file_name = '../Images/lena.jpg'

    im = io.imread(file_name)
    io.imshow(im)
    io.show()
    cwd = os.getcwd()
    new_image_file = os.path.join(cwd, 'new-lena.jpg')
    io.imsave(new_image_file, im)


if __name__ == '__main__':
    skimage_save_image()
