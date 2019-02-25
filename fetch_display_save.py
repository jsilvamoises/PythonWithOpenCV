import argparse
import cv2

# LOAD ARGS FROM PROMPT OR TERMINAL
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")

args = vars(ap.parse_args())

# LOAD IMAGE THIS IS IN ARGS
image = cv2.imread(args["image"])
# print(image)
print('width......: {} pixels '.format(image.shape[1]))
print('height.....: {} pixels '.format(image.shape[0]))
print('channels...: {}  '.format(image.shape[2]))

# DISPLAY IMAGE
cv2.imshow("Image Title",image)
cv2.waitKey(0)
# SALVA IMAGEM
cv2.imwrite("cat_XPTO.png",image)