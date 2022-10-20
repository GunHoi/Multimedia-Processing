def pillow_open_image():
    from PIL import Image
    file_name = '../Images/1-castle.png'
    im = Image.open(file_name)
    im.show()


if __name__ == '__main__':
    pillow_open_image()
