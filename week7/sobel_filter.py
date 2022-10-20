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
    return total/9

def matrix_smoothing():
    from skimage import io
    from skimage.color import rgb2gray
    import matplotlib.pyplot as plt
    import numpy as np
    file_name = '../Images/cameraman.jpg'
    im = io.imread(file_name)
    im = rgb2gray(im)
    im_gray_pad = np.pad(im, pad_width=1)
    n, m = im_gray_pad.shape[0], im_gray_pad.shape[1]
    im_filter = np.zeros(im_gray_pad.shape)

    weight = [[-1, 0, 1],
         [-2, 0, 2],
         [-1, 0, 1]]
    for x in range(1, n - 1):
        for y in range(1, m - 1):
            neighbors = get_3x3_neighbors(x, y)
            neighbors_value = get_neighbor_values(im_gray_pad, neighbors)
            neighbors_33 = np.asarray(neighbors_value).reshape((3, 3))
            im_filter[x, y] = get_matrix_33_filtering(neighbors_33, weight)

    fig, axs = plt.subplots(nrows=1, ncols=2)
    fig.suptitle(f'Weight matrix: {weight}')
    axs[0].imshow(im_gray_pad, cmap='gray'), axs[1].imshow(im_filter, cmap='gray')
    plt.tight_layout()
    plt.show()


def sobel_filter_manual():
    from skimage import io
    from skimage.color import rgb2gray
    import matplotlib.pyplot as plt
    import numpy as np
    import math
    file_name = '../Images/1-castle.png'
    im = rgb2gray(io.imread(file_name))
    im_gray_pad = np.pad(im, pad_width=1)
    n, m = im_gray_pad.shape[0], im_gray_pad.shape[1]
    im_filter_x, im_filter_y = np.zeros(im_gray_pad.shape), np.zeros(im_gray_pad.shape)
    sobel_image = np.zeros(im_gray_pad.shape)

    Gx = [[-1, 0, 1],
         [-2, 0, 2],
         [-1, 0, 1]]
    Gy = [[1, 2, 1],
          [0, 0, 0],
          [-1, -2, -1]]

    for x in range(1, n - 1):
        for y in range(1, m - 1):
            neighbors = get_3x3_neighbors(x, y)
            neighbors_value = get_neighbor_values(im_gray_pad, neighbors)
            neighbors_33 = np.asarray(neighbors_value).reshape((3, 3))
            im_filter_x[x, y] = get_matrix_33_filtering(neighbors_33, Gx)
            im_filter_y[x, y] = get_matrix_33_filtering(neighbors_33, Gy)

    for i in range(n):
        for j in range(m):
            sobel_image[i, j] = math.sqrt(im_filter_x[i, j] ** 2 + im_filter_y[i, j] ** 2)

    fig, axs = plt.subplots(ncols=2)
    axs[0].imshow(im, cmap='gray'), axs[0].set_title('Original image')
    axs[1].imshow(sobel_image, cmap='gray'), axs[1].set_title('Sobel filter image')
    plt.tight_layout(), plt.show()


def sobel_filter_skimage():
    import matplotlib.pyplot as plt
    from skimage import filters
    from skimage.color import rgb2gray
    from skimage import io

    file_name = '../Images/1-castle.png'
    image = rgb2gray(io.imread(file_name))
    edge_sobel = filters.sobel(image)

    fig, axes = plt.subplots(ncols=2)
    axes[0].imshow(image, cmap='gray'), axes[0].set_title('Original Image')
    axes[1].imshow(edge_sobel, cmap='gray'), axes[1].set_title('Sobel Edge Detection')
    plt.tight_layout(), plt.show()


def canny_edge_detection():
    import matplotlib.pyplot as plt
    from skimage import feature
    import skimage.io
    from skimage.color import rgb2gray

    file_name = '../Images/1-castle.png'
    im = rgb2gray(skimage.io.imread(file_name))

    sigmas = [1, 2, 3, 4, 5]
    for sigma in sigmas:
        edge_image = feature.canny(im, sigma=sigma)
        plt.imshow(edge_image, cmap='gray')
        plt.title(f"Sigma={sigma}")
        plt.show()


def region_processing():
    import numpy as np
    import matplotlib.pyplot as plt
    from skimage import io
    from skimage.color import rgb2gray
    from skimage.segmentation import watershed
    from skimage.filters import sobel

    file_name = '../Images/cameraman.jpg'
    img = rgb2gray(io.imread(file_name))
    sobel_img = sobel(img)
    markers = np.zeros_like(img)
    markers[img < 30/255] = 1
    markers[img > 150/255] = 2
    region_img = watershed(sobel_img, markers)

    fig, axs = plt.subplots(nrows=2, ncols=2)
    axs[0, 0].imshow(img, cmap='gray'), axs[0, 0].title.set_text('Original image')
    axs[0, 1].imshow(sobel_img, cmap='gray'), axs[0, 1].title.set_text('Sobel filter')
    axs[1, 0].imshow(markers, cmap='gray'), axs[1, 0].title.set_text('marker image')
    axs[1, 1].imshow(region_img, cmap='gray'), axs[1, 1].title.set_text('region image')
    [ax.axis('off') for ax in axs.ravel()]

    plt.show()
    plt.tight_layout()


if __name__ == '__main__':
    matrix_smoothing()

