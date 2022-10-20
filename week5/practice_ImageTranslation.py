def translate(img, x, y):
    from PIL import Image
    return img.transform(img.size, Image.AFFINE, (1, 0, x, 0, 1, y))


def translate_images():
    import matplotlib.pyplot as plt
    from PIL import Image

    file_name = '../Images/1-castle.png'
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


if __name__ == '__main__':
    translate_images()