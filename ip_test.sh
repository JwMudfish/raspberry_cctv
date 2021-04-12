ARR=$(python3 get_ip.py)
echo $ARR
echo 'python3 $SAVE_DIR/pi_server.py -i' $ARR