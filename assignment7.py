def get_5x5_neighbors(x, y):    #Assignment1
    neighbors = [
        (x - 2, y + 2), (x - 1, y + 2), (x, y + 2), (x + 1, y + 2), (x + 2, y + 2),
        (x - 2, y + 1), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 2, y + 1),
        (x - 2, y), (x - 1, y), (x, y), (x + 1, y), (x + 2, y),
        (x - 2, y - 1), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 2, y - 1),
        (x - 2, y - 2), (x - 1, y - 2), (x, y - 2), (x + 1, y - 2), (x + 2, y - 2),
    ]
    return neighbors


def get_average_neighbors(im, list_neighbors):  #Assignment1
    total = 0
    for point in list_neighbors:
        total += im[point[0], point[1]]
    average = total / len(list_neighbors)
    return average


def average_smoothing_5x5():        #Assignment 1
    from skimage import io
    from skimage.color import rgb2gray
    import matplotlib.pyplot as plt
    import numpy as np
    file_name = 'Me.jpg'

    im = io.imread(file_name)
    im = rgb2gray(im)
    im_gray_pad = np.pad(im, pad_width=1)

    n, m = im_gray_pad.shape[0], im_gray_pad.shape[1]
    im_filter = np.zeros(im_gray_pad.shape)

    for x in range(1, n-2):
        for y in range(1, m-2):
            neighbors = get_5x5_neighbors(x, y)
            im_filter[x, y] = get_average_neighbors(im_gray_pad, neighbors)

    fig, axs = plt.subplots(nrows=1, ncols=2)
    axs[0].imshow(im_gray_pad, cmap='gray'), axs[1].imshow(im_filter, cmap='gray')
    axs[0].set_title('Original Image'), axs[1].set_title('5x5 Filter')
    plt.tight_layout()
    plt.show()


def gaussian_filter():          #Assignment 2
    import skimage.io
    import matplotlib.pyplot as plt
    import skimage.filters
    file_name = 'Me.jpg'
    image = skimage.io.imread(file_name)
    plt.title("Original Image"), plt.imshow(image), plt.show()
    sigmoids = [3, 9, 27, 81]

    for sigma in sigmoids:
        blurred = skimage.filters.gaussian(image, sigma=sigma, multichannel=True)
        plt.imshow(blurred), plt.title(f"gaussian filter, sigma={sigma}")
        plt.show()


def canny_edge_detection():     #Assignment3
    import matplotlib.pyplot as plt
    from skimage import feature
    import skimage.io
    from skimage.color import rgb2gray

    file_name = 'Me.jpg'
    im = rgb2gray(skimage.io.imread(file_name))

    sigmas = [1, 3, 5, 7, 9]
    for sigma in sigmas:
        edge_image = feature.canny(im, sigma=sigma)
        plt.imshow(edge_image, cmap='gray')
        plt.title(f"Sigma={sigma}")
        plt.show()


if __name__ == '__main__':
    canny_edge_detection()
