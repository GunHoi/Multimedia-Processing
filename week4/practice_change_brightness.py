def point_operation_process_addition():
    from skimage import io
    from skimage.color import rgb2gray
    import matplotlib.pyplot as plt
    file_name = 'Coffee.jpg'

    im = io.imread(file_name)
    im_gray = rgb2gray(im)

    ks_add_bright = [0, 0.1, 0.2, 0.4, 0.6, 0.8, 0.9, 1]
    # ks_add_bright=[0,-0.1,-0.2,-0.4,-0.6,-0.8,-0.9,-1]
    ks_reduce_bright = [-1 for i in ks_add_bright]

    ks = ks_add_bright
    figure, axs = plt.subplots(nrows=1, ncols=len(ks_add_bright))
    for idx,k in enumerate(ks):
        im_k = im_gray+k
        axs[idx].imshow(im_k, cmap='gray', vmin=0, vmax=1)
        axs[idx].title.set_text(f'k={k}'), axs[idx].axis('off')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    point_operation_process_addition()
