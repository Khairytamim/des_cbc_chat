import socket
import random
import string
from DES import *

q =353
a = 3

xa = input('Masukkan random key untuk alice (xa): ')
int_xa = int(xa)
ya = (a**int_xa)%q
jebret = str(ya)

xxx = 0

s = socket.socket()
host = socket.gethostname()
port = 12222
s.bind((host, port))
s.listen(5)
c = None

while True:
	xxx = xxx + 1
	if c is None:
		print 'menunggu koneksi dari server'
		c, addr = s.accept()
		print 'mendapatkan koneksi dari client dengan IP : ',addr
	else:
		if xxx == 2:
			yb = c.recv(10)
			print('ini yb-> ',yb)
			c.send(jebret)
			kab = (int(yb)**int_xa)%q
			print('ini kab-> ',kab)
			jebrets = str(kab)

			tambah_doang = 0

			if len(jebrets) < 8:
				temp_jebrets = len(jebrets)
				while temp_jebrets < 8:
					temp_jebrets = temp_jebrets + 1
					jebrets = jebrets + str(tambah_doang)
					print("cek isi-> ", jebrets)
			print jebrets
			with open('key_dh.txt','wb') as f:
				data = f.write(jebrets)
		print 'menunggu response'

		pesan_belum = c.recv(1024)
		print "yg belum di dekrip = ",pesan_belum
		pesan_client = decrypt(pesan_belum)
		print "Pesan dari client -> ",pesan_client
		q = raw_input("Tulis chat ke client: ")
		q_encrypt = encryptdua(q)
		c.send(q_encrypt)