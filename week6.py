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


def get_average_neighbors(im, list_neighbors):
    total = 0
    for point in list_neighbors:
        total += im[point[0], point[1]]
    average = total / len(list_neighbors)
    return average


def average_smoothing():        #3x3 Average filter 이미지가 부드러워짐(흐릿해짐) (p 32)
    from skimage import io
    from skimage.color import rgb2gray
    import matplotlib.pyplot as plt
    import numpy as np
    #file_name = 'Images/cameraman.jpg'
    file_name = 'Me.jpg'
    im = io.imread(file_name)
    im = rgb2gray(im)
    im_gray_pad = np.pad(im, pad_width=1)

    n, m = im_gray_pad.shape[0], im_gray_pad.shape[1]
    im_filter = np.zeros(im_gray_pad.shape)

    for x in range(1, n-1):
        for y in range(1, m-1):
            neighbors = get_3x3_neighbors(x, y)
            im_filter[x, y] = get_average_neighbors(im_gray_pad, neighbors)

    fig, axs = plt.subplots(nrows=1, ncols=2)
    axs[0].imshow(im_gray_pad, cmap='gray'), axs[1].imshow(im_filter, cmap='gray')
    axs[0].set_title('Original Image'), axs[1].set_title('3x3 Filter')
    plt.tight_layout()
    plt.show()


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


def matrix_smoothing():         #3x3 Matrix filter 이미지가 투명해짐(색이 사라지고 윤곽만 남음) (p 32)
    from skimage import io
    from skimage.color import rgb2gray
    import matplotlib.pyplot as plt
    import numpy as np
    file_name = 'Images/cameraman.jpg'
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


if __name__ == '__main__':
    average_smoothing()
