import cv2
import numpy as np
import os

path = './rotating_images/'
images = np.stack([cv2.imread(path+i, cv2.IMREAD_UNCHANGED) for i in os.listdir(path)])
print(images.shape)
video = cv2.VideoWriter('record.mov', 0, 24, (images.shape[2], images.shape[1])) 
for image in images:
	video.write(image) 
cv2.destroyAllWindows() 
video.release() 