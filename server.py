import socket
import random
import string
import cPickle
import pickle
from DES import *
from rsa import *

s = socket.socket()
host = socket.gethostname()
port = 12229
s.bind((host, port))
s.listen(5)
c = None

index_rsa = 0



while True:
	if c is None:
		print("Menunggu koneksi dari server")
		c, addr = s.accept()
		print("Mendapatkan koneksi dari client dengan IP : ",addr)

		if index_rsa == 0:
			prima_1 = int(raw_input("Masukkan bilangan prima: "))
			prima_2 = int(raw_input("Masukkan bilangan prima: (harus berbeda dengan prima 1)"))
			print("Membuat public key + private key ")
			public,  private = generate_keypair(prima_1, prima_2)
			print("Public key -> ",public," dan Private key -> ",private)
			# pickle.dump(public, open("save.pub","wb"))
			pub1, pub2 = public
			c.send(str(pub1))
			c.recv(1024)
			c.send(str(pub2))
			c.recv(1024)
			# dataKirim = pickle.dumps(public)
			# print("Cek data kirim -> ",dataKirim)
			# c.sendall(str(dataKirim))
			print("Masukkan nilai q dan a, dipisahkan dengan spasi")
			qdana = raw_input()
			qdana_split = qdana.split(' ')
			q = qdana_split[0]
			a = qdana_split[1]
			enkrip_q = encrypt_rsa(private, q)
			print "====", enkrip_q
			pickle.dump(enkrip_q, open("save.q","wb"))
			c.sendall("sudah ditulis")
			enkrip_a = encrypt_rsa(private, a)
			pickle.dump(enkrip_a, open("save.a","wb"))
			c.sendall("sudah ditulis juga")

			# enkrip_qFinal = ''.join(map(lambda x: str(x), enkrip_q))
			# enkrip_aFinal = ''.join(map(lambda x: str(x), enkrip_a))
			# print("ini enrkip q -> ",enkrip_qFinal,"ini enrkip a -> ",enkrip_aFinal)
			# print("Dekrip dengan public key ",public)
			# print("q -> ",decrypt_rsa(public, enkrip_q))
			# print("a -> ",decrypt_rsa(public, enkrip_a))

			index_rsa = index_rsa + 1
	else:
		terimaQ = c.recv(1024)
		c.sendall("sudah diterima")
		terimaA = c.recv(1024)
		c.sendall("sudah diterima juga")

		q = int(terimaQ)
		a = int(terimaA)
		
		# elif index_rsa == 1:
		xa = input('Masukkan random key untuk alice (xa): ')
		int_xa = int(xa)
		ya = (a**int_xa)%q
		jebret = str(ya)

		xxx = 0

		# s = socket.socket()
		# host = socket.gethostname()
		# port = 12222
		# s.bind((host, port))
		# s.listen(5)
		# c = None

		while True:
			xxx = xxx + 1
			
				#diffie-hellman
				# if xxx == 2:
					#rsa

				# elif xxx == 2:
			if xxx == 1:
				#diffie-hellman
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
				xxx = xxx + 1
			else:
				print("ini xxx di dalam else -> ",xxx)
				print 'menunggu response'

				pesan_belum = c.recv(1024)
				print "yg belum di dekrip = ",pesan_belum
				pesan_client = decrypt(pesan_belum)
				print "Pesan dari client -> ",pesan_client
				q = raw_input("Tulis chat ke client: ")
				q_encrypt = encryptdua(q)
				c.send(q_encrypt)