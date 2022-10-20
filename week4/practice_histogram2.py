def hist_skimage():
    from skimage import io
    from matplotlib import pyplot as plt
    file = '../Images/1-castle.png'
    im = io.imread(file)
    fig, axs = plt.subplots(nrows=2, ncols=1)
    axs[0].imshow(im)
    axs[1].hist(im.ravel(), bins=256)
    plt.show()


if __name__ == '__main__':
    hist_skimage()