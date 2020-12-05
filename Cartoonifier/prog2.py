import cv2
initialImage = cv2.imread("sumedh.jpg")
blurredImage = gaussianBlur(copy.deepcopy(initialImage))
cv2.imwrite("blurred.jpg", blurredImage)

def sharpen(image):
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)

def sepia(image):
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    return cv2.filter2D(image, -1, kernel)


def gaussianBlur(image):
    return cv2.GaussianBlur(image, (35, 35), 0)

def emboss(image):
    kernel = np.array([[0,-1,-1],
                            [1,0,-1],
                            [1,1,0]])
    return cv2.filter2D(image, -1, kernel)


