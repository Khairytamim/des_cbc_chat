import socket
from DES import *

q = 353
a = 3

xb = input('masukkan random key untuk bob (xb) : ')
int_xb = int(xb)
yb = (a**int_xb)%q
jebret = str(yb)
print('ini yb-> ', yb)

xxx = 0

s = socket.socket()
host = socket.gethostname()
port = 12222

s.connect((host, port))
print 'Terhubung dengan server dengan IP : ', host

while True:
	xxx = xxx + 1

	print ("jembut-> ", xxx)
	if xxx == 1:
		s.sendall(jebret)
		ya = s.recv(10)
		print ('ini ya->', ya)
		kab = (int(ya)**int_xb)%q
		print ('ini kab->', kab)
		jebrets = str(kab)

		tambah_doang = 0

		if len(jebrets) < 8:
			temp_jebrets = len(jebrets)
			while temp_jebrets < 8:
				temp_jebrets = temp_jebrets + 1
				jebrets = jebrets + str(tambah_doang)
		print jebrets
		with open('key_dh.txt','wb') as f:
			data = f.write(jebrets)
		print ("jebrets, sudah ditulis ke key_dh-> ", jebrets)


	z = raw_input("Tulis chat ke server: ")
	z_encrypt = encryptdua(z)
	s.send(z_encrypt)
	print 'Menunggu response'

	x = s.recv(1024)
	print "yg blm di dekrip = ", x

	pesan_server = decrypt(x)
	print "Pesan dari server -> ", pesan_server

