import cv2
import os
 
# 视频的帧数为30，那么60s的视频一共有1800帧，选择60张照片，则选择每隔30帧选一张
 
path_video = "/labelimg_SaveDir/polar_winding/MP4Videos/Videos/"
save_pictures = "/labelimg_SaveDir/polar_winding/MP4Videos/JPEGImages/"
 
count = 0
num = 0
for path_cv in os.listdir(path_video):
    # 视频数量一共是9个
    vc = cv2.VideoCapture(os.path.join(path_video,path_cv))
    i = 0
    while vc.isOpened():
        rval, img = vc.read()
        
        frame_count = vc.get(cv2.CAP_PROP_FRAME_COUNT)  # 视频文件的帧数
        frame_fps = vc.get(cv2.CAP_PROP_FPS)  # 视频文件的帧率
        
        if i==frame_count:  
            break
        else:
            i=i+1
            if i % int(frame_count/60) == 0:  #选取60照片
                count = count + 1
                # 图片命名及保存路径
                filename=str(count)+".jpg"
                cv2.imwrite(save_pictures+filename,img)
    num = num +1
    print("第{}个视频截取图片完毕！".format(num))
        
    # 释放资源
    vc.release()
    cv2.destroyAllWindows()        
 
