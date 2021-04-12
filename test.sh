#!/bin/sh

cd ~/Desktop/personal_project/raspberry_cctv
# ARR=$(python3 config.py | jq '.device_list | .[] | .ips | keys | .[]')
# ARR=$(echo $ARR | tr -d '"')

ARR=$(python3 get_ip.py)
#$ARR = 42
echo 'local_ip : ' $ARR

USER=ubuntu
PW=1234
FILE1=/home/perth/Desktop/personal_project/raspberry_cctv/pi_server.py
#FOLDER1=/home/pi/cctv_test
SAVE_DIR=/home/pi/cctv_test
#MAKE_LOGS_DIR=/home/pi/Desktop/logs

#for IPS in $ARR;
#do

# you should be install expect
# sudo apt install expect
IP=192.168.0.153
echo $IP

expect<<EOF
  set timeout 2
  spawn ssh server1 "scp -o StrictHostKeyChecking=no $USER@$IP:~/tst/tst.py perth@192.168.0.153:~/Desktop/personal_project/raspberry_cctv/"
  expect "password:"
  send "$PW\r"
  expect eof
EOF

# expect<<EOF
#   set timeout 2
#   spawn scp -o StrictHostKeyChecking=no $FILE1 $USER@$IP:$SAVE_DIR
#   expect "password:"
#   send "$PW\r"
#   expect eof
# EOF

# expect<<EOF
#   set timeout 1
#   spawn ssh $USER@$IP "python3 $SAVE_DIR/pi_server.py -i " $ARR
#   expect "password"
#   send "$PW\r"
#   expect eof
# EOF