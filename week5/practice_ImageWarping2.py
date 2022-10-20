def warp_rows():
    import numpy as np
    from PIL import Image
    import math
    import matplotlib.pyplot as plt

    file_name = '../Images/1-castle.png'
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