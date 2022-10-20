def translate(img, x, y):
    from PIL import Image
    return img.transform(img.size, Image.AFFINE, (1, 0, x, 0, 1, y))


def translate_images():     # image translation(이동) (p 39)
    import matplotlib.pyplot as plt
    from PIL import Image

    file_name = 'Images/1-castle.png'
    im = Image.open(file_name)
    fig, axs = plt.subplots(nrows=2, ncols=3)
    axs[0, 0].imshow(im), axs[0, 0].title.set_text("Original Image")
    axs[0, 1].imshow(translate(im, 100, 0)), axs[0, 1].title.set_text("Left")
    axs[0, 2].imshow(translate(im, -100, 0)), axs[0, 2].title.set_text("Right")
    axs[1, 0].imshow(translate(im, 0, 100)), axs[1, 0].title.set_text("Up")
    axs[1, 1].imshow(translate(im, 0, -100)), axs[1, 1].title.set_text("Down")
    axs[1, 2].imshow(translate(im, 100, 100)), axs[1, 2].title.set_text("Left Up")

    plt.tight_layout()
    plt.show()


def scaling():          #image scaling(크기 조절) (p 42)
    from PIL import Image
    import matplotlib.pyplot as plt

    file_name = 'Images/1-castle.png'
    im = Image.open(file_name)

    size0 = im.size[0], im.size[1]
    size1 = (1, 0.5)
    im_size1 = im.resize((round(size0[0] * size1[0]), round(size0[1] * size1[1])))
    size2 = (0.5, 1)
    im_size2 = im.resize((round(size0[0] * size2[0]), round(size0[1] * size2[1])))
    size3 = (0.1, 0.1)
    im_size3 = im.resize((round(size0[0] * size3[0]), round(size0[1] * size3[1])))
    fig, axs = plt.subplots(nrows=2, ncols=2)
    axs[0, 0].imshow(im), axs[0, 0].title.set_text("Original image")
    axs[0, 1].imshow(im_size1), axs[0, 1].title.set_text(f"size: ({size1}")
    axs[1, 0].imshow(im_size2), axs[1, 0].title.set_text(f"size: ({size2}")
    axs[1, 1].imshow(im_size3), axs[1, 1].title.set_text(f"size: ({size3}")

    plt.tight_layout()
    plt.show()


def shear(img, bx, by):
    from PIL import Image
    shear_img = img.transform(img.size, Image.AFFINE, (bx, by, 0, 0, 1, 0))
    return shear_img


def shear_images():     #image shearing(기울임) (p 45)
    from PIL import Image
    import matplotlib.pyplot as plt

    file_name = 'Images/1-castle.png'
    im = Image.open(file_name)

    bxs = [0.8, 1]
    bys = [0.8, 1]
    for bx in bxs:
        for by in bys:
            shear_img = shear(im, bx, by)
            plt.imshow(shear_img), plt.title(f'bx, by = ({bx, by})')
            plt.tight_layout()
            plt.show()


def rotate_images():        #image Roatation(회전) (p 48)
    from PIL import Image
    import matplotlib.pyplot as plt

    file_name = 'Images/messi.png'
    im = Image.open(file_name)

    alphas = [45, 90, 135, 180, 225, 270, 315, 360]
    for alpha in alphas:
        im_rotated = im.rotate(alpha)
        plt.imshow(im_rotated)
        plt.title(f'Rotated angle: {alpha} ')
        plt.tight_layout()
        plt.show()


def flip_images():      #image Flip(뒤집음) (p 51)
    from PIL import Image
    import matplotlib.pyplot as plt

    file_name = 'Images/messi.png'
    im = Image.open(file_name)

    im_flip_left_right = im.transpose(Image.FLIP_LEFT_RIGHT)
    im_flip_top_bottom = im.transpose(Image.FLIP_TOP_BOTTOM)

    fig, axs = plt.subplots(nrows=1, ncols=3)
    axs[0].imshow(im), axs[0].title.set_text('Original Image')
    axs[1].imshow(im_flip_left_right), axs[1].title.set_text('Flip Left Right')
    axs[2].imshow(im_flip_top_bottom), axs[2].title.set_text('Flip Top Bottom')

    plt.tight_layout()
    plt.show()


def warp_cols():    #image warping(흐물흐물 - 열(세로)) (p 52)
    import numpy as np
    from PIL import Image
    import math
    import matplotlib.pyplot as plt

    file_name = 'Images/1-castle.png'
    img = Image.open(file_name).convert("L")
    img = np.array(img)
    rows, cols = img.shape[0], img.shape[1]
    img_output = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            offset_x = int(40.0 * math.sin(2 * 3.14 * i / 180))
            if j + offset_x < rows:
                img_output[i, j] = img[i, (j + offset_x) % cols]
            else:
                img_output[i, j] = 0

    fig, axs = plt.subplots(nrows=1, ncols=2)
    axs[0].imshow(img, cmap='gray'), axs[0].title.set_text('Original Image')
    axs[1].imshow(img_output, cmap='gray'), axs[1].title.set_text('Warped image')
    plt.tight_layout()
    plt.show()


def warp_rows():    #image warping(흐물흐물 - 행(가로) : ~ 모양) (p 52)
    import numpy as np
    from PIL import Image
    import math
    import matplotlib.pyplot as plt

    file_name = 'img.png'
    img = Image.open(file_name).convert("L")
    img = np.array(img)
    rows, cols = img.shape[0], img.shape[1]
    img_output = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            offset_y = int(40.0 * math.sin(2 * 3.14 * j / 180))
            if i + offset_y < rows:
                img_output[i, j] = img[(i + offset_y) % rows, j]
            else:
                img_output[i, j] = 0
    fig, axs = plt.subplots(nrows=1, ncols=2)
    axs[0].imshow(img, cmap='gray'), axs[0].title.set_text('Original Image')
    axs[1].imshow(img_output, cmap='gray'), axs[1].title.set_text('Warped image')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    warp_rows()
