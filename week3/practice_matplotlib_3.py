def matplotlib_show_images():
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    file_name1 = '../Images/cheetah.png'
    im1 = mpimg.imread(file_name1)

    file_name2 = '../Images/duck_rgb.png'
    im2 = mpimg.imread(file_name2)

    fig, axs = plt.subplots(1, 2)   # 1 row , 2 cols
    axs[0].imshow(im1)
    axs[0].axis('off')  #주변 눈금이 사라진다.
    axs[1].imshow(im2)
    plt.show()
    # 2 row , 2 cols 면 axs[0,0] ~ axs[1,1]


if __name__ == '__main__':
    matplotlib_show_images()
