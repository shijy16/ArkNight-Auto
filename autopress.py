import cv2
from ScreenShot import Screenshot
import numpy as np
import random
import subprocess
from PIL import Image

def compare(img1,img2):
    MIN_MATCH_COUNT = 34

    sift = cv2.xfeatures2d.SIFT_create()

    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    index_params = dict(algorithm=1, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1, des2, k=2)


    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)

    if len(good) >= MIN_MATCH_COUNT:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

        matchesMask = mask.ravel().tolist()

        h, w = img1.shape

        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)

        dst = cv2.perspectiveTransform(pts, M)

    else:      
        matchesMask = None
        dst = None

    return dst

def get_click_range(box):
    x1 = box[0][0][0]
    y1 = box[0][0][1]

    x2 = box[2][0][0]
    y2 = box[2][0][1]

    return x1, y1, x2, y2

def find_pos(picDir,press=True):
    print('finding ' + picDir)
    shoter = Screenshot()
    shoter.shot()
    screenImg = cv2.imread("temp/cur.png",0)
    screenImg = np.rot90(screenImg)
    screenImg = np.rot90(screenImg)
    screenImg = np.rot90(screenImg)
    cv2.imwrite("temp/cur.png",screenImg)
    dstImg = cv2.imread('res/'+picDir,0)
    try:
        res = compare(dstImg,screenImg)
    except:
        return False
    if res is None:
        return False
    else:
        if(press):
            x1,y1,x2,y2 = get_click_range(res)
            x_offset = random.randint(0,1000)
            x_offset = float(x_offset)/float(1000)
            y_offset = random.randint(0,1000)
            y_offset = float(y_offset)/float(1000)
            x1 += (x2 - x1)*x_offset
            y1 += (y2 - y1)*y_offset
            cmd = "\tadb shell input tap " + str(x1) + " "+ str(y1)
            print(cmd)
            connect=subprocess.Popen(cmd,stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        return True