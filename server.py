import socket
import random
import string
import cPickle
import pickle
from DES import *
from rsa import *

s = socket.socket()
host = socket.gethostname()
port = 12226
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
			c.send(str(prima_1))
			c.recv(1024)
			c.send(str(prima_2))
			c.recv(1024)
			print("Membuat public key + private key ")
			public,  private = generate_keypair(prima_1, prima_2)
			print("Public key -> ",public," dan Private key -> ",private)
			# with open('pubKey.txt','wb') as f:
			# 	data = f.write(str(public))
			# data_string = cPickle.dumps(public)
			# print data_string
			# c.send(str(data_string))
			# terima1 = c.recv(1024)
			# print terima1
			print("Masukkan nilai q dan a, dipisahkan dengan spasi")
			qdana = raw_input()
			qdana_split = qdana.split(' ')
			q = qdana_split[0]
			a = qdana_split[1]
			enkrip_q = encrypt_rsa(private, q)
			print enkrip_q
			with open('enkrip_q.txt','wb') as f:
				data_1 = pickle.dump(enkrip_q, f)
				print ("ini data 1 -> ",data_1)
				data_2 = f.write(data_1)
			enkrip_a = encrypt_rsa(private, a)
			c.sendall("Server : OK client. semua udah ditulis")
			enkrip_qFinal = ''.join(map(lambda x: str(x), enkrip_q))
			c.send(enkrip_qFinal)
			c.recv(2014)
			enkrip_aFinal = ''.join(map(lambda x: str(x), enkrip_a))
			print("ini enrkip q -> ",enkrip_qFinal,"ini enrkip a -> ",enkrip_aFinal)
			print("Dekrip dengan public key ",public)
			print("q -> ",decrypt_rsa(public, enkrip_q))
			print("a -> ",decrypt_rsa(public, enkrip_a))

			index_rsa = index_rsa + 1
	else:

		q = 353
		a = 3

		
		
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