def skimage_open_image():   #Open an Image
    from skimage import io
    file_name = 'Images/0-colors-image.jpg'

    im = io.imread(file_name)
    io.imshow(im)
    io.show()


def skimage_save_image():   #Save an Image
    from skimage import io
    import os
    file_name = 'Images/lena.jpg'

    im = io.imread(file_name)
    io.imshow(im)
    io.show()
    cwd = os.getcwd()
    new_image_file = os.path.join(cwd, 'new-lena.jpg')
    io.imsave(new_image_file, im)


def pillow_open_image():    #Open an Image
    from PIL import Image
    file_name = 'Images/1-castle.png'
    im = Image.open(file_name)
    im.show()


def pillow_save_image():    #Save an Image
    from PIL import Image
    file_name = 'Images/1-castle.png'
    im = Image.open(file_name)
    im.save('new-castle-image.jpg')


def opencv_open_image():    #Open an Image
    import cv2
    file_name = 'Images/bunny.png'
    im = cv2.imread(file_name)
    cv2.imshow(file_name, im)
    cv2.waitKey(10000)


def opencv_open_image():    #Save an Image
    import cv2
    file_name = 'Images/bunny.png'
    im = cv2.imread(file_name)
    cv2.imshow(file_name, im)
    cv2.waitKey(10000)


def matplotlib_open_image():    #Open an Image
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    file_name = 'Images/cheetah.png'
    im = mpimg.imread(file_name)
    plt.imshow(im)
    plt.show()


def matplotlib_save_image():    #Sava an Image
    import matplotlib.image as mpimg

    file_name = 'Images/cheetah.png'
    im = mpimg.imread(file_name)
    mpimg.imsave('new-cheetahaaaaaa.png', im)


def matplotlib_show_images():   #Open and show multiple Images
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    file_name1 = 'Images/cheetah.png'
    im1 = mpimg.imread(file_name1)

    file_name2 = 'Images/duck_rgb.png'
    im2 = mpimg.imread(file_name2)

    fig, axs = plt.subplots(1, 2)   # 1 row , 2 cols
    axs[0].imshow(im1)
    axs[0].axis('off')  #주변 눈금이 사라진다.
    axs[1].imshow(im2)
    plt.show()
    # 2 row , 2 cols 면 axs[0,0] ~ axs[1,1]


def numpy_create_image():   #Create an Image
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


def view_image_by_channels():
    from skimage import io
    from skimage.color import rgb2gray
    import matplotlib.pyplot as plt
    file_name = 'Images/1-castle.png'

    im = io.imread(file_name)
    print(type(im), im.shape)   # <class 'numpy.ndarry'>

    im_red = im[:, :, 0]
    im_green = im[:, :, 1]
    im_blue = im[:, :, 2]
    im_gray = rgb2gray(im)

    figure, axs = plt.subplots(nrows=2, ncols=3)
    axs[0, 0].imshow(im_red, cmap='Reds'), axs[0, 0].title.set_text('Reds')
    axs[0, 1].imshow(im_green, cmap='Greens'), axs[0, 1].title.set_text('Greens')
    axs[0, 2].imshow(im_blue, cmap='Blues'), axs[0, 2].title.set_text('Blues')
    axs[1, 0].imshow(im_gray, cmap='gray'), axs[1, 0].title.set_text('Gray')
    axs[1, 1].imshow(im), axs[1, 1].title.set_text('Original image')
    axs[1, 2].title.set_text('Blank')

    plt.tight_layout()
    plt.show()


def numpy_create_image_p46():   #Practice create Image p 46 색 바 만들기
    import numpy as np
    import matplotlib.pyplot as plt

    fig, axs = plt.subplots(1, 4)

    img_r = np.zeros((255, 25))
    for i in range(255):
        img_r[i] = i

    my_cmap = 'viridis' #Default : virids
    axs[0].imshow(img_r, cmap='Reds', vmin=0, vmax=255)
    axs[1].imshow(img_r, cmap='Greens', vmin=0, vmax=255)
    axs[2].imshow(img_r, cmap='Blues', vmin=0, vmax=255)
    axs[3].imshow(img_r, cmap='gray', vmin=0, vmax=255)

    axs[0].title.set_text('Reds'), axs[1].title.set_text('Greens')
    axs[2].title.set_text('Blues'), axs[3].title.set_text('gray')
    plt.show()


def numpy_create_image_p47_p48():   #Practice create Image p 47 네모판에 흰 동그라미
    import numpy as np
    import matplotlib.pyplot as plt
    import random

    shape =(8, 8)
    im = np.zeros(shape)

    im1 = np.zeros(shape)
    im2 = np.zeros(shape)
    im1.fill(255)
    im2.fill(128)

    fig, axs = plt.subplots(1, 5)

    img_r = np.zeros((9, 9))    # 8x8 칸 만들고 ( 동그라미)
    #img_r.fill(0)               # 배경 검정색으로 색칠 0 - black / 255 - white

    for i in range(9):
        for j in range(9):
            if i == 1 or i == 7:
                if j == 3 or j == 4 or j == 5:
                    img_r[i][j] = 255       # 색칠할 칸만 흰색으로 색칠
            elif i == 2 or i == 6:
                if j == 2 or j == 6:
                    img_r[i][j] = 255
            elif i == 3 or i == 4 or i == 5:
                if j == 1 or j == 7:
                    img_r[i][j] = 255
            else:   #i==0 / i==8 일 때 (생략가능)
                img_r[i][j] = 0

    img_chess = np.zeros((8, 8))    #chess 판 만들기
    #img_chess.fill(0)

    for i in range(8):
        for j in range(8):
            if i%2 != 0 and j%2 == 0:
                img_chess[i][j] = 255
            elif i%2 == 0 and j%2 != 0:
                img_chess[i][j] = 255
            else:
                img_chess[i][j] = 0

    img_rand = np.zeros((8, 8)) #random한 수를 위해 import random

    for i in range(8):           #randrange(0, 256)은 0 이상 256 미만의 숫자 중 random
        for j in range(8):
            img_rand[i][j] = random.randrange(0, 256)

    my_cmap = 'gray' #Default : virids  #0 : 검정  / 255 : 흰색
    axs[0].imshow(im, cmap=my_cmap, vmin=0, vmax=255)
    axs[1].imshow(im1, cmap=my_cmap, vmin=0, vmax=255)
    axs[2].imshow(img_r, cmap=my_cmap, vmin=0, vmax=255)
    axs[3].imshow(img_chess, cmap=my_cmap, vmin=0, vmax=255)
    axs[4].imshow(img_rand, cmap=my_cmap, vmin=0, vmax=255)
    axs[0].title.set_text('0 values'), axs[1].title.set_text('255 values')
    plt.show()


if __name__ == '__main__':
    numpy_create_image_p47_p48()

