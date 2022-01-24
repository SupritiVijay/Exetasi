import cv2
import numpy as np
from tqdm import trange

base = cv2.imread("raw_logo.png", cv2.IMREAD_UNCHANGED)
feathers = cv2.imread("raw_feathers.png", cv2.IMREAD_UNCHANGED)
img = base+feathers
cv2.imwrite("./rotating_images/angle_000.png", img)
(h, w) = feathers.shape[:2]
(cX, cY) = (w // 2, h // 2)
for angle in trange(0, 360, 5):
	path = "./rotating_images/angle_"+"0"*(3-len(str(angle)))+str(angle)+".png"
	M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
	rotated = cv2.warpAffine(feathers, M, (w, h))
	img = base+rotated
	cv2.imwrite(path, img)