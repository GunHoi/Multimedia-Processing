def numpy_create_image():
    import numpy as np
    import matplotlib.pyplot as plt
    shape =(8, 8)
    im = np.zeros(shape)
    im1 = np.zeros(shape)
    im2 = np.zeros(shape)
    im1.fill(255)
    im2.fill(128)

    fig, axs = plt.subplots(1, 4)

    img_r = np.zeros((255, 50))
    for i in range(255):
        img_r[i] = i

    my_cmap = 'viridis' #Default : virids
    axs[0].imshow(im, cmap=my_cmap, vmin=0, vmax=255)
    axs[1].imshow(im1, cmap=my_cmap, vmin=0, vmax=255)
    axs[2].imshow(img_r, cmap=my_cmap, vmin=0, vmax=255)
    axs[3].imshow(im2, cmap=my_cmap, vmin=0, vmax=255)

    axs[0].title.set_text('0 values'), axs[1].title.set_text('255 values')
    plt.show()


if __name__ == '__main__':
    numpy_create_image()
