def hist_skimage_bychannels():
    from skimage import io
    import matplotlib.pyplot as plt
    file = '../Images/1-castle.png'
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


if __name__ =='__main__':
    hist_skimage_bychannels()