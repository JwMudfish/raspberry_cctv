import pexpect

ssh_newkey = 'ls'
conn = 'ssh pi@192.168.0.42'
passwd = '1234'
p = pexpect.spawn(conn)
index = p.expect( [ssh_newkey, 'password:', pexpect.EOF, pexpect.TIMEOUT], 1 )

if index == 0:
    print('index == 0')
    p.sendline('yes')
    index = p.expect( [ssh_newkey, 'password:', pexpect.EOF, pexpect.TIMEOUT], 1 )
if index == 1:
	print ('index == 1')
	p.sendline(passwd)
	index = p.expect( [pexpect.EOF, pexpect.TIMEOUT], 1 )
elif index == 2:
	print ("Cannot connect to " + conn)
	sys.exit(0)