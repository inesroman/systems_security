#!/usr/bin/python
import socket
import json
import hashlib

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
c_sqnr = 0
s_sqnr = 0
state = "CLOSED"

# our test system only has one user and one pin for it
s_user = "utz"
s_password = "1234"

print ("connecting to server")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	s.connect((TCP_IP, TCP_PORT))
except socket.error as err:
	print ("socket.error : %s" % err)
	quit()

print ("connected to server")

#print ("type :" , m_json['type'])

print ("--> sending HELLO")
m_json = {}
m_json['type'] = 'HELLO' 
c_sqnr += 1
m_json['sqnr'] = c_sqnr 
state = 'WAIT_HELLO_ACK'
s.send(json.dumps(m_json).encode())
print ("--> sent data: " , json.dumps(m_json))

while True:
	print ("waiting for message from server")
	m_str = s.recv(BUFFER_SIZE).decode()
	print ("<-- received data:", m_str)

	try:
		m_json = json.loads(m_str)
	except ValueError:
		print ('    received data is no JSON, exiting ...')
		s.close()
		quit()

	if m_json['sqnr'] > s_sqnr  :
		s_sqnr = m_json['sqnr']
	else:
		print ('    received message out of sequence, exiting ...')
		s.close()
		quit()

	if state == 'WAIT_HELLO_ACK' and m_json['type'] == 'HELLO_ACK' :
		state = 'CONNECTED'
		print ('<-- HELLO_ACK received, connected!')
		print ("--> sending DATA")
		challenge = m_json['data']
		hashed_result = hashlib.md5((s_password + challenge).encode('utf-8')).hexdigest()
		m_json = {}
		m_json['type'] = 'DATA' 
		c_sqnr += 1
		m_json['sqnr'] = c_sqnr 
		m_json['user'] = s_user
		m_json['secret'] = hashed_result
		m_json['data'] = 'DATADATADATA' 
		s.send(json.dumps(m_json).encode())
		print ("--> sent data: " , json.dumps(m_json))
	elif state == 'CONNECTED' and m_json['type'] == 'CLOSE': 
		state = 'CONNECTED'
		print ('<-- CLOSE received')
		s.close()
		print ("connection closed")
		quit()
	else:
		print ('--> received message of type %s ignored in state %s' % (m_json['type'],state))


