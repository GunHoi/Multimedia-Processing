def gaussian_filter():
    import skimage.io
    import matplotlib.pyplot as plt
    import skimage.filters
    file_name = '../Images/1-castle.png'
    image = skimage.io.imread(file_name)
    plt.title("Original Image"), plt.imshow(image), plt.show()
    sigmoids = [3, 5, 7, 9]

    for sigma in sigmoids:
        blurred = skimage.filters.gaussian(image, sigma=sigma, multichannel=True)
        plt.imshow(blurred), plt.title(f"gaussian filter, sigma={sigma}")
        plt.show()


if __name__ == '__main__':
    gaussian_filter()
