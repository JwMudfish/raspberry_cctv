cd ~/Desktop/personal_project/cctv_test
# ARR=42
# echo $ARR
USER=pi
PW=1234
# for IPS in $ARR;
# do
#echo $IPS
#IP=192.168.0.$IPS
IP=192.168.0.42
expect<<EOF
  set timeout 1
  spawn ssh $USER@$IP "pkill -f pi_server.py -9"
  expect "password"
  send "$PW\r"
  expect eof
EOF
#done