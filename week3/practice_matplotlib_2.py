def matplotlib_save_image():
    import matplotlib.image as mpimg

    file_name = '../Images/cheetah.png'
    im = mpimg.imread(file_name)
    mpimg.imsave('new-cheetahaaaaaa.png', im)


if __name__ == '__main__':
    matplotlib_save_image()
