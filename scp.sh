#!/bin/sh

cd ~/Desktop/auto_scp
# ARR=$(python3 config.py | jq '.device_list | .[] | .ips | keys | .[]')
# ARR=$(echo $ARR | tr -d '"')

ARR=$(python3 get_ips.py)
echo $ARR

USER=pi
PW=1234
FILE1=/home/pi/Desktop/config.py
FILE2=/home/pi/Desktop/cam.py
FILE3=/home/pi/Desktop/lc.py
FILE4=/home/pi/Desktop/log_adapter.py
FILE5=/home/pi/Desktop/logging.conf
FILE6=/home/pi/Desktop/lc_cali.json
FILE7=/home/pi/Desktop/temper.py
FILE8=/home/pi/Desktop/auto_start.sh
FILE9=/home/pi/Desktop/client1.domain.tld.crt
FILE10=/home/pi/Desktop/client1.domain.tld.key
FILE11=/home/pi/Desktop/downloaded-client-config.ovpn
FILE12=/home/pi/Desktop/vpn.py
FOLDER1=/home/pi/Desktop/keys
SAVE_DIR=/home/pi/Desktop/.
MAKE_LOGS_DIR=/home/pi/Desktop/logs
for IPS in $ARR;
do

# you should be install expect
# sudo apt install expect
IP=192.168.1.$IPS
echo $IP
expect<<EOF
  set timeout 2
  spawn scp -o StrictHostKeyChecking=no $FILE1 $FILE2 $FILE3 $FILE4 $FILE5 $FILE6 $FILE7 $FILE8 $FILE9 $FILE10 $FILE11 $FILE12 $USER@$IP:$SAVE_DIR
  expect "password:"
  send "$PW\r"
  expect eof
EOF
expect<<EOF
  set timeout 2
  spawn scp -r -o StrictHostKeyChecking=no $FOLDER1 $USER@$IP:$SAVE_DIR
  expect "password:"
  send "$PW\r"
  expect eof
EOF
expect<<EOF
  set timeout 2
  spawn ssh $USER@$IP "mkdir $MAKE_LOGS_DIR"
  expect "password:"
  send "$PW\r"
  expect eof
EOF
done