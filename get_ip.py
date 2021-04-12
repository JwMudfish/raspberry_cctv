#-*- coding: utf-8 -*-
import sys
import os
import socket


sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import config

# check master ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #3 
s.connect(('8.8.8.8', 0)) 
ip = s.getsockname()[0]
#ip = ip.split(".")[-1]

print(ip)
# device_list = config.refrigerators["device_list"]
# # 마스터 파이가 가장 마지막에 실행 되어야 함
# # 재부팅을 마스터 파이 먼저 하면 나머지는 실행이 안됨
# # 마스터 ip가 포함되어 있다면 가장 마지막에 실행 시키는 로직 
# master_pi_check = False
# for device in device_list:
#     for ip_key in device["ips"].keys():
#         if ip_key == ip:
#             master_pi_check = True
#             continue
#         print(int(ip_key))

# if master_pi_check:
#     print(ip)

# def ipcheck():
#     return socket.gethostbyname(socket.getfqdn())

# #print(ipcheck())
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(('8.8.8.8', 0))
# ip = s.getsockname()[0]
# print(ip)

