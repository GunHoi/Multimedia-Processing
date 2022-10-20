def calculate_hist_of_image():
    from skimage import io
    import matplotlib.pyplot as plt
    import numpy as np
    file = 'Tree.jpg'
    im = io.imread(file)
    im_flatten = im.flatten()
    hist = np.zeros(256)
    for i in im_flatten:
        hist[i] += 1
    x = [i for i in range(0, 256)]
    fig, axs = plt.subplots(nrows=2, ncols=1)
    axs[0].imshow(im)
    axs[1].bar(x, hist)
    plt.show()


if __name__ == '__main__':
    calculate_hist_of_image()