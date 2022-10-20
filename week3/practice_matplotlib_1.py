def matplotlib_open_image():
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    file_name = '../Images/cheetah.png'
    im = mpimg.imread(file_name)
    plt.imshow(im)
    plt.show()


if __name__ == '__main__':
    matplotlib_open_image()
