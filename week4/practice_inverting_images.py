def inverting_image():
    from skimage import io
    from skimage.color import rgb2gray
    import matplotlib.pyplot as plt
    file_name = 'Me.jpg'
    im = io.imread(file_name)
    im_gray = rgb2gray(im)

    a_max = 0.5
    im_invert = a_max - im_gray
    figure, axs = plt.subplots(nrows=1, ncols=2)
    axs[0].imshow(im_gray, cmap='gray', vmin=0, vmax=1)
    axs[0].title.set_text('original gray scale image')
    axs[1].imshow(im_invert, cmap='gray', vmin=0, vmax=1)
    axs[1].title.set_text(f'invert image, a_max={a_max}')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    inverting_image()