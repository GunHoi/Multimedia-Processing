def opencv_open_image():
    import cv2
    file_name = '../Images/bunny.png'
    im = cv2.imread(file_name)
    cv2     #미완성
    cv2.waitKey(10000)


if __name__ == '__main__':
    opencv_open_image()
