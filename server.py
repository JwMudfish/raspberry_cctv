# -*- coding: utf-8 -*-

'''  
   https://www.pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/
   원격으로 웹캠 라이브 스트리밍 보는 방법
   라즈베리에서 실행하는 소스. 노트북에서 원격으로 보기 전 라즈베리에서 sender.send_image를 쏘고 있어야된다.
'''
import socket
import time
from imutils.video import VideoStream
import imagezmq

sender = imagezmq.ImageSender(connect_to='tcp://localhost:5555') # 클라이언트 아이피: 5555(아마 default인거 같음)
 
rpi_name = socket.gethostname() # send RPi hostname with each image

# 해상도 변경이 안되는거 같음 해결 해야됨
# picam = VideoStream(src=2, resolution=(960, 720)).start()
picam = VideoStream(src=2).start()

# warm up 필요없을지도.. 테스트 해봐야됨
print("warm up")
time.sleep(2.0)  # allow camera sensor to warm up
print("warm up done")
print("start ..")

while True:  # send images as stream until Ctrl-C

   '''
      라즈베리에서 카메라 읽어서 클라이언트(노트북)에게 계속 쏴주는 로직
   '''
   image = picam.read()
   sender.send_image(rpi_name, image) # 첫번째 인자는 ip 넣어줘도 되고 호스트 네임 적어줘도됨. 그냥 별칭 넣어주는거