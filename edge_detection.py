import cv2
import os
rootdir=r'D:\pycharm_community\python_workspace\canny_detection\img1'
desdir='D:\pycharm_community\python_workspace\canny_detection\canny5_100/'
path=os.listdir(rootdir)
for file in path:
    img=os.path.join(rootdir,file)
    original_img=cv2.imread(img)
    edge_img=cv2.Canny(original_img,5,100,apertureSize=3)
    cv2.imwrite(desdir+file,edge_img)


