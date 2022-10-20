def flip_images():
    from PIL import Image
    import matplotlib.pyplot as plt

    file_name = '../Images/messi.png'
    im = Image.open(file_name)

    im_flip_left_right = im.transpose(Image.FLIP_LEFT_RIGHT)
    im_flip_top_bottom = im.transpose(Image.FLIP_TOP_BOTTOM)

    fig, axs = plt.subplots(nrows=1, ncols=3)
    axs[0].imshow(im), axs[0].title.set_text('Original Image')
    axs[1].imshow(im_flip_left_right), axs[1].title.set_text('Flip Left Right')
    axs[2].imshow(im_flip_top_bottom), axs[2].title.set_text('Flip Top Bottom')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    flip_images()
