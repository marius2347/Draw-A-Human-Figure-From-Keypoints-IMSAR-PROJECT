# Drawing A Human Figure Using Keypoints

# imports
import cv2 
import numpy as np 

# define keypoints for the human body
keypoints = {
    'head': (250, 80),
    'left_shoulder': (200, 150),
    'right_shoulder': (300, 150),
    'left_elbow': (180, 200),
    'right_elbow': (320, 200),
    'left_wrist': (160, 250),
    'right_wrist': (340, 250),
    'left_hip': (220, 300),
    'right_hip': (280, 300),
    'left_knee': (210, 400),
    'right_knee': (290, 400),
    'left_ankle': (200, 500),
    'right_ankle': (300, 500),
}

# creating a blank image, tensor (x, y, channel)
image = np.zeros((600, 600, 3), dtype = "uint8")

# draw keypoints as small circlers
for key, point in keypoints.items():
    cv2.circle(image, point, 4, (0, 0, 255), -1) # red color circle

# draw lines to connect the keypoints

# head to shoulders
cv2.line(image, keypoints['head'], keypoints['left_shoulder'], (255, 255, 255), 2)
cv2.line(image, keypoints['head'], keypoints['right_shoulder'], (255, 255, 255), 2)

# shoulders to elbows
cv2.line(image, keypoints['left_shoulder'], keypoints['left_elbow'], (255, 255, 255), 2)
cv2.line(image, keypoints['right_shoulder'], keypoints['right_elbow'], (255, 255, 255), 2)

# elbows to wrists
cv2.line(image, keypoints['left_elbow'], keypoints['left_wrist'], (255, 255, 255), 2)
cv2.line(image, keypoints['right_elbow'], keypoints['right_wrist'], (255, 255, 255), 2)

# shoulders to hips
cv2.line(image, keypoints['left_shoulder'], keypoints['left_hip'], (255, 255, 255), 2)
cv2.line(image, keypoints['right_shoulder'], keypoints['right_hip'], (255, 255, 255), 2)

# hips to knees
cv2.line(image, keypoints['left_hip'], keypoints['left_knee'], (255, 255, 255), 2)
cv2.line(image, keypoints['right_hip'], keypoints['right_knee'], (255, 255, 255), 2)

# knees to ankles
cv2.line(image, keypoints['left_knee'], keypoints['left_ankle'], (255, 255, 255), 2)
cv2.line(image, keypoints['right_knee'], keypoints['right_ankle'], (255, 255, 255), 2)

# show the image
cv2.imshow("Human Figure", image)
cv2.waitKey(0)
cv2.destroyAllWindows()