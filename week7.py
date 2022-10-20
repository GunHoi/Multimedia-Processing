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


def gaussian_filter():          #가우시안 필터 (점점 흐릿해진다) (p 25)
    import skimage.io
    import matplotlib.pyplot as plt
    import skimage.filters
    file_name = 'Images/1-castle.png'
    image = skimage.io.imread(file_name)
    plt.title("Original Image"), plt.imshow(image), plt.show()
    sigmoids = [3, 5, 7, 9]

    for sigma in sigmoids:
        blurred = skimage.filters.gaussian(image, sigma=sigma, multichannel=True)
        plt.imshow(blurred), plt.title(f"gaussian filter, sigma={sigma}")
        plt.show()


def sobel_filter_manual():      #edge detection (외곽선만 따준다) (p 30)
    from skimage import io
    from skimage.color import rgb2gray
    import matplotlib.pyplot as plt
    import numpy as np
    import math
    file_name = 'Images/1-castle.png'
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


def sobel_filter_skimage():     #edge detection (마찬가지로 외곽선만 따준다 but 코드 간결, 빠름) (p 32)
    import matplotlib.pyplot as plt
    from skimage import filters
    from skimage.color import rgb2gray
    from skimage import io

    file_name = 'Images/1-castle.png'
    image = rgb2gray(io.imread(file_name))
    edge_sobel = filters.sobel(image)

    fig, axes = plt.subplots(ncols=2)
    axes[0].imshow(image, cmap='gray'), axes[0].set_title('Original Image')
    axes[1].imshow(edge_sobel, cmap='gray'), axes[1].set_title('Sobel Edge Detection')
    plt.tight_layout(), plt.show()


def canny_edge_detection():     #edge detection (외곽선만 따주는데, 점점 퀼리티가 대충그린 느낌) (p 36)
    import matplotlib.pyplot as plt
    from skimage import feature
    import skimage.io
    from skimage.color import rgb2gray

    file_name = 'Images/1-castle.png'
    im = rgb2gray(skimage.io.imread(file_name))

    sigmas = [1, 2, 3, 4, 5]
    for sigma in sigmas:
        edge_image = feature.canny(im, sigma=sigma)
        plt.imshow(edge_image, cmap='gray')
        plt.title(f"Sigma={sigma}")
        plt.show()


def region_processing():    #Region processing with Watershed Algorithm ,
    import numpy as np
    import matplotlib.pyplot as plt
    from skimage import io
    from skimage.color import rgb2gray
    from skimage.segmentation import watershed
    from skimage.filters import sobel

    file_name = 'Images/cameraman.jpg'
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
    region_processing()
