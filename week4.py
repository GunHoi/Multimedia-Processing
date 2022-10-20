def point_operation_process_addition():                 #점점 밝아져서 완전 하얗게 변함 (p 24)
    from skimage import io
    from skimage.color import rgb2gray
    import matplotlib.pyplot as plt
    file_name = './Images/cameraman.jpg'

    im = io.imread(file_name)
    im_gray = rgb2gray(im)

    ks_add_bright = [0, 0.1, 0.2, 0.4, 0.6, 0.8, 0.9, 1]        #bright
    # ks_add_bright=[0,-0.1,-0.2,-0.4,-0.6,-0.8,-0.9,-1]       #dark
    ks_reduce_bright = [-1 for i in ks_add_bright]

    ks = ks_add_bright
    figure, axs = plt.subplots(nrows=1, ncols=len(ks_add_bright))
    for idx,k in enumerate(ks):
        im_k = im_gray+k
        axs[idx].imshow(im_k, cmap='gray', vmin=0, vmax=1)
        axs[idx].title.set_text(f'k={k}'), axs[idx].axis('off')

    plt.tight_layout()
    plt.show()


def point_operation_process_multiplication():       #점점 밝아지는데 위와 다르게 인물과 배경이 구분되어 인물이 뚜렷하게 보임 (p 27)
    from skimage import io
    from skimage.color import rgb2gray
    import matplotlib.pyplot as plt
    file_name = 'Images/cameraman.jpg'
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


def inverting_image():              #색이 반전됨 (p 28)
    from skimage import io
    from skimage.color import rgb2gray
    import matplotlib.pyplot as plt
    file_name = 'Images/cameraman.jpg'
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


def detect_new_object():           #두 사진을 비교해서 2번사진 - 1번사진 해서 물체 탐지 (p 37)
    from skimage import io
    import matplotlib.pyplot as plt
    file1, file2 = './week4/No.jpg', './week4/Yes.jpg'

    im1, im2 = io.imread(file1), io.imread(file2)
    im = im2 - im1
    a_max = 125
    im = im - a_max

    fig, axs = plt.subplots(nrows=1, ncols=3)
    [ax.set_axis_off() for ax in axs.ravel()]
    axs[0].imshow(im1), axs[1].imshow(im2), axs[2].imshow(im)

    plt.tight_layout(), plt.show()
    plt.imshow(im), plt.axis('off'), plt.show()


def calculate_hist_of_image():      # Histogram 출력(선이 그려져있는) (p 42)
    from skimage import io
    import matplotlib.pyplot as plt
    import numpy as np
    file = 'Images/1-castle.png'
    im = io.imread(file)
    im_flatten = im.flatten()
    hist = np.zeros(256)
    for i in im_flatten:
        hist[i] += 1
    x = [i for i in range(0, 256)]
    fig, axs = plt.subplots(nrows=2, ncols=1)
    axs[0].imshow(im)
    axs[1].bar(x, hist)
    plt.show()


def hist_skimage():           #Histogram 출력(꽉 색칠 되어있는) (p 44)
    from skimage import io
    from matplotlib import pyplot as plt
    file = 'Images/1-castle.png'
    im = io.imread(file)
    fig, axs = plt.subplots(nrows=2, ncols=1)
    axs[0].imshow(im)
    axs[1].hist(im.ravel(), bins=256)
    plt.show()


def hist_skimage_bychannels():  #Histogram 출력 (R, G, B, Total 채널 별) (p 46)
    from skimage import io
    import matplotlib.pyplot as plt
    file = 'Images/1-castle.png'
    im = io.imread(file)

    fig, axs = plt.subplots(nrows=2, ncols=1)
    axs[0].imshow(im)
    axs[1].hist(im.ravel(), bins=256, color='orange', )
    axs[1].hist(im[:, :, 0].ravel(), bins=256, color='red', alpha=0.5)
    axs[1].hist(im[:, :, 1].ravel(), bins=256, color='Green', alpha=0.5)
    axs[1].hist(im[:, :, 2].ravel(), bins=256, color='Blue', alpha=0.5)
    plt.xlabel('Intensity Value')
    plt.ylabel('Count')
    plt.legend(['Total', 'Red_Channel', 'Green_Channel', 'Blue Channel'])
    plt.show()


def hist_equalization():    #Histogram 동등화
    from skimage import io, exposure
    from matplotlib import pyplot as plt

    file = 'Images/flowers.png'
    im = io.imread(file)
    im_equalization = exposure.equalize_hist(im)
    fig, axs = plt .subplots(nrows=2, ncols=2)
    axs[1, 0].hist(im.ravel(), bins=256), axs[0, 0].imshow(im)
    axs[0, 1].imshow(im_equalization), axs[1, 1].hist(im_equalization.ravel(), bins=256)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    hist_equalization()

