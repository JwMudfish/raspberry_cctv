import os
import cv2

cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FPS, 1)

def get_devices_list():
    devices_list = []

    result = os.popen('v4l2-ctl --list-devices').read()
    result_lists = result.split("\n\n")
    for result_list in result_lists:
        if result_list != '':
            result_list_2 = result_list.split('\n\t')
            devices_list.append(result_list_2[1][-1])
    print(devices_list)
    return devices_list

def get_img():
    while True:
        ret, frame = cap.read()

        if ret:
            cv2.imshow('video', frame)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

            if k == ord("c"):
                cv2.imwrite('cap.jpg', frame)
        
        else:
            print('error')

active_cam = get_devices_list()
print(f'현재 활성화 되어있는 카메라는 {active_cam} 입니다.')

get_img()