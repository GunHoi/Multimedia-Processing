def view_image_by_channels():
    from skimage import io
    from skimage.color import rgb2gray
    import matplotlib.pyplot as plt
    file_name = '../Images/1-castle.png'

    im = io.imread(file_name)
    print(type(im), im.shape) # <class 'numpy.ndarry'>

    im_red = im[:, :, 0]
    im_green = im[:, :, 1]
    im_blue = im[:, :, 2]
    im_gray = rgb2gray(im)

    figure, axs = plt.subplots(nrows=2, ncols=3)
    axs[0, 0].imshow(im_red, cmap='Reds'), axs[0, 0].title.set_text('Reds')
    axs[0, 1].imshow(im_green, cmap='Greens'), axs[0, 1].title.set_text('Greens')
    axs[0, 2].imshow(im_blue, cmap='Blues'), axs[0, 2].title.set_text('Blues')
    axs[1, 0].imshow(im_gray, cmap='gray'), axs[1, 0].title.set_text('Gray')
    axs[1, 1].imshow(im), axs[1, 1].title.set_text('Original image')
    axs[1, 2].title.set_text('Blank')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    view_image_by_channels()
