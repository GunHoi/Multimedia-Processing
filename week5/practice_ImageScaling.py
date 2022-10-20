def scaling():
    from PIL import Image
    import matplotlib.pyplot as plt

    file_name = '../Images/1-castle.png'
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


if __name__ == '__main__':
    scaling()
