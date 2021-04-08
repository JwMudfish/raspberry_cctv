# -*- coding: utf-8 -*-
import os
from subprocess import PIPE, Popen
import argparse


def cam_list():
    '''
        /dev/video? 숫자 변경 될 경우에도 층 정보 변경되지 않게 물리적 포트 고정
        포트 1 = cap0, 2 = cap1      물리적 포트 숫자
        -----------------------    -----------------------
        -          -   cam2   -    -     2    -     3    -
        -----------------------    -----------------------
        -   lc1    -   cam1   -    -     3    -     2    -
        -----------------------    -----------------------
    '''
    camera_list = {}
    splited = [] # output : ['/dev/video0']c
    get_all_device_list = Popen(["v4l2-ctl --list-devices"], shell=True, stdout=PIPE, stderr=PIPE, encoding='utf-8')
    stdout, stderr = get_all_device_list.communicate()
    get_all_device_list = stdout.split('\n\n')
    print(get_all_device_list)
    for i in get_all_device_list:
        # 라즈베리에서 자동으로 잡히는거 빼내기
        if "bcm2835-codec-decode" in i or "bcm2835-isp" in i:
            continue
        if "bcm2835-isp" in i:
            continue

        if i != '':
            item = i.split('\n\t')
            splited.append(item[1])
    print(splited)
    for i in splited:
        if i != '':
            tmp = (f"udevadm info -a -n {i} | grep 'looking at device'")
            loc = os.popen(tmp).read().split(':1.0')[0][-1]
            camera_list[loc] = i
    return camera_list

print(cam_list())
