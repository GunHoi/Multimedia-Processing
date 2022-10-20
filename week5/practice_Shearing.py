def shear(img, bx, by):
    from PIL import Image
    shear_img = img.transform(img.size, Image.AFFINE, (bx, by, 0, 0, 1, 0))
    return shear_img


def shear_images():
    from PIL import Image
    import matplotlib.pyplot as plt

    file_name = '../Images/1-castle.png'
    im = Image.open(file_name)

    bxs = [0.8, 1]
    bys = [0.8, 1]
    for bx in bxs:
        for by in bys:
            shear_img = shear(im, bx, by)
            plt.imshow(shear_img), plt.title(f'bx, by = ({bx, by})')
            plt.tight_layout()
            plt.show()


if __name__ == '__main__':
    shear_images()
