#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import cPickle
import pickle
import string
from DES import *
from rsa import *

s = socket.socket()                   
s.connect(('10.151.43.191', 8820))
print 'Sudah terhubung'

index_rsa = 0

while True:
	if index_rsa == 0:
		pub1 = s.recv(1024)
		s.sendall("Pub1 sudah diterima")
		pub2 = s.recv(1024)
		s.sendall("Pub2 sudah diterima")
		a = s.recv(1024)
		print a, pub1, pub2
		favoriteq = pickle.load(open("save.q","rb"))
		print("ini enkrip q -> ",favoriteq)
		kirimQ = decrypt_rsa(int(pub1), int(pub2), favoriteq)
		print pub1, pub2, favoriteq
		print("kirim Q ->"), kirimQ
		b = s.recv(1024)
		print b
		favoritea = pickle.load(open("save.a","rb"))
		print("ini enkrip a -> ",favoriteq)
		kirimA = decrypt_rsa(int(pub1), int(pub2), favoritea)
		print kirimA
		s.send(str(kirimQ))
		s.recv(1024)
		s.send(str(kirimA))
		s.recv(1024)

		q = int(kirimQ)
		a = int(kirimA)
	
	xb = input('masukkan random key untuk bob (xb) : ')
	int_xb = int(xb)
	yb = (a**int_xb)%q
	jebret = str(yb)
	print('ini yb-> ', yb)

	xxx = 0

	# s = socket.socket()
	# host = socket.gethostname()
	# port = 12222

	# s.connect((host, port))
	# print 'Terhubung dengan server dengan IP : ', host

	while True:
		xxx = xxx + 1

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

