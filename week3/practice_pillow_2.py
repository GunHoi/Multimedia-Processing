def pillow_save_image():
    from PIL import Image
    file_name = '../Images/1-castle.png'
    im = Image.open(file_name)
    im.save('new-castle-image.jpg')


if __name__ == '__main__':
    pillow_save_image()
