import socket
import cPickle
import pickle
import string
from DES import *
from rsa import *

s = socket.socket()
host = socket.gethostname()
port = 12226

s.connect((host, port))
print 'Terhubung dengan server dengan IP : ', host

index_rsa = 0

while True:
	if index_rsa == 0:
		prima_1 = s.recv(1024)
		print prima_1
		s.sendall("Client : OK. prima 1 sudah diterima")
		print("==========")
		prima_2 = s.recv(1024)
		print prima_2
		s.sendall("Client : OK. prima 2 sudah diterima")
		public,  private = generate_keypair(int(prima_1), int(prima_2))
		print("Public key -> ",public," dan Private key -> ",private)
		s.recv(1024)
		with open('enkrip_q.txt','wb') as f:
			data_1 = pickle.load(f)
			print ("ini data 1 -> ",data_1)
		# q = decrypt_rsa(public, enkrip_q)
		# print q

	# pubKey = s.recv(1024)
	# print("ini pubKey -> ", pubKey)
	# satu = pubKey.split('\n')
	# print satu[0]
	# dua = satu[0].split('I')
	# fix_dua = int(dua[1])
	# print("ini fix dua -> ",fix_dua)
	# tiga = satu[1].split('I')
	# fix_tiga = int(tiga[1])
	# print("ini fix tiga -> ",fix_tiga)
	# gabung = []
	# gabung.append(fix_dua)
	# gabung.append(fix_tiga)
	# print gabung
	# s.sendall("Client : OK. Public key sudah diterima")
	# s.recv(1024)
	# baca_satu = open('pubKey.txt','rb')
	# pubKey = baca_satu.read()
	# print pubKey
	# enkrip_q = open('enkrip_q.txt','rb')
	# berhasil_dong = enkrip_q.read()
	# print berhasil_dong
	# qAsli = decrypt_rsa(berhasil_dong, pubKey)
	# print qAsli
	# a = gabung.replace("[", "(")
	# print a
	# gabungStr = str(gabung)
	# tup = str(tuple(gabungStr))
	# trans = tup.translate(tup,"'")
	# print trans
	# data_arr = ', 'join(dua, tiga)
	# print data_arr
	# dua = satu.split('(I')
	
	

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

