# -*- coding: utf-8 -*-

import socket
import time
from imutils.video import VideoStream
import imagezmq
import cv2
import os
import argparse
from subprocess import PIPE, Popen

# def get_devices_list():
#     devices_list = []

#     result = os.popen('v4l2-ctl --list-devices').read()
#     result_lists = result.split("\n\n")
#     for result_list in result_lists:
#         if result_list != '':
#             result_list_2 = result_list.split('\n\t')
#             devices_list.append(result_list_2[1][-1])
#     print(devices_list)
#     return devices_list

def get_devices_list():
    camera_list = {}
    splited = [] # output : ['/dev/video0']c
    get_all_device_list = Popen(["v4l2-ctl --list-devices"], shell=True, stdout=PIPE, stderr=PIPE, encoding='utf-8')
    stdout, stderr = get_all_device_list.communicate()
    get_all_device_list = stdout.split('\n\n')
    for i in get_all_device_list:

        if "bcm2835-codec-decode" in i or "bcm2835-isp" in i:
            continue
        if "bcm2835-isp" in i:
            continue

        if i != '':
            item = i.split('\n\t')
            #splited.append(item[1])
            splited.append(item[1])

    for i in splited:
        if i != '':
            tmp = (f"udevadm info -a -n {i} | grep 'looking at device'")
            loc = os.popen(tmp).read().split(':1.0')[0][-1]
            camera_list[loc] = i
    #return camera_list
    print('splited : ', splited)
    return splited 

def get_ip():
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #3 
   s.connect(('8.8.8.8', 0)) 
   ip = s.getsockname()[0]
   #ip = ip.split(".")[-1]
   return ip

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", dest="ip", action="store")          # extra value
args = parser.parse_args()

#local_ip = get_ip()
local_ip = args.ip
print(local_ip)
#local_ip = '192.168.0.153'
sender = imagezmq.ImageSender(connect_to=f'tcp://{local_ip}:5555') # 클라이언트 아이피: 5555(아마 default인거 같음)
 
rpi_name = socket.gethostname() # send RPi hostname with each image

# 해상도 변경이 안되는거 같음 해결 해야됨
# picam = VideoStream(src=2, resolution=(960, 720)).start()
#picam_1 = VideoStream(src=0).start()
#picam_2 = VideoStream(src=2).start()
active_cam = get_devices_list()
active_cam = sorted(list(set(active_cam)))

print(f'현재 활성화 되어있는 카메라는 {active_cam} 입니다.')

#first camera src
cap_1 = cv2.VideoCapture(int(active_cam[0][-1]))
# set the format into MJPG in the FourCC format 
cap_1.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G'))
#same for camera 2
cap_2 = cv2.VideoCapture(int(active_cam[1][-1]))
cap_2.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G'))


# cap_1 = cv2.VideoCapture(0)
# cap_2 = cv2.VideoCapture(2)

# warm up 필요없을지도.. 테스트 해봐야됨
print("warm up")
time.sleep(2.0)  # allow camera sensor to warm up
print("warm up done")
print("start ..")


while True:  # send images as stream until Ctrl-C

   ret, frame1 = cap_1.read()
   ret, frame2 = cap_2.read()
   #image_1 = picam_1.read()
   #print(image_1)
   #image_2 = picam_2.read()
   #print(image_2)
   #print(image_1, image_2)
   rst = cv2.hconcat([frame1, frame2])
   sender.send_image(rpi_name, rst) # 첫번째 인자는 ip 넣어줘도 되고 호스트 네임 적어줘도됨. 그냥 별칭 넣어주는거
