def detect_new_object():
    from skimage import io
    import matplotlib.pyplot as plt
    file1, file2 = 'No.jpg', 'Yes.jpg'

    im1, im2 = io.imread(file1), io.imread(file2)
    im = im2 - im1
    a_max = 125
    im = im - a_max

    fig, axs = plt.subplots(nrows=1, ncols=3)
    [ax.set_axis_off() for ax in axs.ravel()]
    axs[0].imshow(im1), axs[1].imshow(im2), axs[2].imshow(im)

    plt.tight_layout(), plt.show()
    plt.imshow(im), plt.axis('off'), plt.show()


if __name__ == '__main__':
    detect_new_object()