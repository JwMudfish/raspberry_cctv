# -*- coding: utf-8 -*-
'''  
   https://www.pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/
   원격으로 웹캠 라이브 스트리밍 보는 방법
   노트북에서 실행하는 소스, 라즈베리에서 이미지를 쏘면 읽어들이고 화면에 출력.
'''

import imagezmq
import cv2
import os

imageHub = imagezmq.ImageHub()

while True:
    (rpiName, frame) = imageHub.recv_image()
    imageHub.send_reply(b'OK')
    #print("[INFO] receiving data from {}...".format(rpiName))
    try:
        cv2.imshow('video', frame)
        
        if cv2.waitKey(1) == ord('q'):
            break
    except:
        pass

#os.system('sh kill_server.sh')

