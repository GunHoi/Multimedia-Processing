def rotate_images():
    from PIL import Image
    import matplotlib.pyplot as plt

    file_name = '../Images/messi.png'
    im = Image.open(file_name)

    alphas = [45, 90, 135, 180, 225, 270, 315, 360]
    for alpha in alphas:
        im_rotated = im.rotate(alpha)
        plt.imshow(im_rotated)
        plt.title(f'Rotated angle: {alpha} ')
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    rotate_images()
