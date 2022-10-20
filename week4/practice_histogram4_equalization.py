def hist_equalization():
    from skimage import io, exposure
    from matplotlib import pyplot as plt

    file = 'Tree.jpg'
    im = io.imread(file)
    im_equalization = exposure.equalize_hist(im)
    fig, axs = plt .subplots(nrows=2, ncols=2)
    axs[1, 0].hist(im.ravel(), bins=256), axs[0, 0].imshow(im)
    axs[0, 1].imshow(im_equalization), axs[1, 1].hist(im_equalization.ravel(), bins=256)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    hist_equalization()