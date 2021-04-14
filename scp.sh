#!/bin/sh

cd ~/Desktop/personal_project/raspberry_cctv
# ARR=$(python3 config.py | jq '.device_list | .[] | .ips | keys | .[]')
# ARR=$(echo $ARR | tr -d '"')

ARR=$(python3 get_ip.py)
#$ARR = 42
echo 'local_ip : ' $ARR

USER=pi
PW=1234
FILE1=/home/perth/Desktop/personal_project/raspberry_cctv/pi_server.py
#FOLDER1=/home/pi/cctv_test
SAVE_DIR=/home/pi/cctv_test
#MAKE_LOGS_DIR=/home/pi/Desktop/logs

#for IPS in $ARR;
#do

# you should be install expect
# sudo apt install expect
read -p '라즈베리 IP를 입력하시오 (ex> 192.168.0.42): ' IP
#echo "<${last_name}> 성입니다."
#IP=192.168.0.42
echo $IP

expect<<EOF
  set timeout 2
  spawn ssh $USER@$IP "mkdir $SAVE_DIR"
  expect "password:"
  send "$PW\r"
  expect eof
EOF

echo '폴더 생성 완료'

expect<<EOF
  set timeout 2
  spawn scp -o StrictHostKeyChecking=no $FILE1 $USER@$IP:$SAVE_DIR
  expect "password:"
  send "$PW\r"
  expect eof
EOF

echo 'server 파일 전송 완료'

expect<<EOF
  set timeout 1
  spawn ssh $USER@$IP "python3 $SAVE_DIR/pi_server.py -i " $ARR
  expect "password"
  send "$PW\r"
  expect eof
EOF

echo 'pi_server.py 실행 완료'

python3 client.py
#done