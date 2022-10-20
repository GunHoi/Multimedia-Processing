def point_operation_process_multiplication():
    from skimage import io
    from skimage.color import rgb2gray
    import matplotlib.pyplot as plt
    file_name = 'Me.jpg'
    im = io.imread(file_name)
    im_gray = rgb2gray(im)
    ks = [0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2]
    rows = 2
    cols = int(len(ks)/rows)
    figure, axs = plt.subplots(nrows=rows, ncols=cols)
    row, col = 0, -1
    for k in ks:
        im_k = im_gray * k
        col += 1
        if col >= cols:
            row, col = 1, 0
        axs[row, col].imshow(im_k, cmap='gray', vmin=0, vmax=1)
        axs[row, col].title.set_text(f'k={k}'), axs[row, col].axis('off')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    point_operation_process_multiplication()
