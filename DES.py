import math
from DESCommon import DES, generate_keys
from DESUtil import to_binary, add_pads_if_necessary, hex_to_bin, bin_to_hex, bin_to_text

try:
    input = raw_input
except NameError:
    pass

def get_bits(plaintext):
    text_bits = []
    for i in plaintext:
        text_bits.extend(to_binary(ord(i)))
    return text_bits

def encryptdua(plaintext):
	key_text = 'kij12345'
    #hahhaha
	keys = generate_keys(key_text)
	text_bits = get_bits(plaintext)
	text_bits = add_pads_if_necessary(text_bits)
	
	iv_bits = '0000000000000000000000000000000000000000000000000000000000000000'
	results = map(int, iv_bits)	

	print "ini results -> ",results

	for i in text_bits:
		text_bits[i] ^= results[i]

	final_cipher = ''
	for i in range (0, len(text_bits), 64):
		final_cipher += DES(text_bits, i, (i+64), keys)

	hex_cipher = ''
	i = 0
	while i < len(final_cipher):
		hex_cipher += bin_to_hex(final_cipher[i:i+4])
		i = i+4
	return hex_cipher

def encrypt(plaintext, iv_bits):
	key_text = "kij12345"
	keys = generate_keys(key_text)
	text_bits = get_bits(plaintext)
	text_bits = add_pads_if_necessary(text_bits)
	print "ini lemparan dari iv bits-> ",iv_bits

	print "iv -> ",iv_bits

	results = map(int, iv_bits)

	print "map iv ->",results

	for i in text_bits:
		text_bits[i] ^= results[i]

	print "text_bits setelah di XOR->",text_bits

	final_cipher = ''
	for i in range(0, len(text_bits), 64):
		final_cipher += DES(text_bits, i, (i+64), keys)

	hex_cipher = ''
	i = 0
	while i < len(final_cipher):
		hex_cipher += bin_to_hex(final_cipher[i:i+4])
		i = i+4
	return hex_cipher, final_cipher

def decrypt_cbc(cipher, iv_bits): #cipher hexadecimal dan key 8 character\
	key_text = "kij12345"
	keys = generate_keys(key_text) # key dirubah ke biner
	text_bits = [] 
	ciphertext = ''
	cipher_iv = ''
	for i in cipher:
		cipher_iv += hex_to_bin(i)
	print "text hexa dari",cipher,"sudah dirubah ke",cipher_iv

	# print "ini lemparan dari iv bits-> ",iv_bits
	results = map(int, iv_bits)
	# print "ini results -> ",results

	ciphertemp = []
	for i in cipher: 
		# conversion of hex-decimal form to binary form
		ciphertext += hex_to_bin(i)
	ciphertemp = str(ciphertext)
	# print "ini ciphertext -> ",ciphertext
	# print "ini ciphertemp -> ",ciphertemp
	for i in ciphertemp:
		text_bits.append(i)
	# print "ini textbits -> ",text_bits
	xx = 0
	text_temp = []

	for xx in range(0,len(text_bits)/64):
		# print "masuk for xx"
		ho = len(text_bits)/64
		temp = []
		aa = 0
		while aa < 64:
			temp += text_bits.pop(0)
			aa = aa + 1
		temp_new = []
		for i in temp:
			temp_new.append(int(i))		
		
		if xx == 0:
			keys.reverse()
		bin_mess = ''
		for i in range(0, len(temp_new), 64):
			bin_mess += DES(temp_new, i, (i+64), keys)

		print "ini bin sebelum xor ->",bin_mess

		bin_mess = map(int, bin_mess) #ubah jadi integer 


		# #xor antara iv_new dan bi miss
		for i in bin_mess:
			bin_mess[i] ^= results[i]

		print "new fvking bin sete;ah xor -> ",bin_mess
		bin_str = str(bin_mess)
		print bin_str
		bin_baru = []
		bin_baru = ''.join(str(e) for e in bin_mess)
		print "ini boi bin joinnya", bin_baru
		i = 0
		text_mess = ''
		while i < len(bin_baru):
			text_mess += bin_to_text(bin_baru[i:i+8])
			i = i+8
		print "ini text mess bawah->", text_mess
		text_temp.append(text_mess)
		# print "text temp ==",text_temp
		final_temp = ''.join(text_temp)
		# print "final temp ==",final_temp
	return final_temp.rstrip('\x00'), cipher_iv

def decrypt(cipher): #cipher hexadecimal dan key 8 character
	key_text = "kij12345"
	keys = generate_keys(key_text) # key dirubah ke biner
	text_bits = [] 
	ciphertext = ''

	ciphertemp = []
	for i in cipher: 
		# conversion of hex-decimal form to binary form
		ciphertext += hex_to_bin(i)
	ciphertemp = str(ciphertext)
	for i in ciphertemp:
		text_bits.append(i)
	xx = 0
	text_temp = []
	for xx in range(0,len(text_bits)/64):
		ho = len(text_bits)/64
		temp = []
		aa = 0
		while aa < 64:
			temp += text_bits.pop(0)
			aa = aa + 1
		temp_new = []
		for i in temp:
			temp_new.append(int(i))
		#print "keys sebelum reverse->",keys		
		
		if xx == 0:
			keys.reverse()
		bin_mess = ''
		for i in range(0, len(temp_new), 64):
			bin_mess += DES(temp_new, i, (i+64), keys)
		i = 0
		text_mess = ''
		while i < len(bin_mess):
			text_mess += bin_to_text(bin_mess[i:i+8])
			i = i+8
		# print "ini text mess bawah->", text_mess
		final_gan = []
		final_gan.append(text_mess.rstrip('\x1c'))
		#print "ini hasil iterasi ke ", xx+1, final_gan
		text_temp.append(text_mess)
		final_temp = ''.join(text_temp)
	return final_temp.rstrip('\x00')

	for i in temp:
		# conversion of hex-decimal form to binary form
		ciphertext += hex_to_bin(i)
	for i in ciphertext:
		text_bits.append(int(i))

	text_bits = add_pads_if_necessary(text_bits)
	keys.reverse()
	bin_mess = ''
	for i in range(0, len(text_bits), 64):
		bin_mess += DES(text_bits, i, (i+64), keys)

	i = 0
	text_mess = ''
	while i < len(bin_mess):
		text_mess  += bin_to_text(bin_mess[i:i+8])
		i = i+8
	return text_mess.rstrip('\x00')

def main():

    print('Encrypt = 1')
    print('Decrypt = 2')
    # buat milih mau encrypt atau decrypt
    choice = int(input())

    #jika yang dipilih adalah encrypt
    if(choice == 1):
    	#intputkan teks yang akan kita encrypt
		plaintext = str(input('Text yang mau encrypt: \n'))
		
		#isi dari array plaintext, dicopykan ke array new_plaintext
		new_plaintext = []
		new_plaintext.extend(plaintext)
		
		xx = 0
		aa = 0
		temp = []
		iv_new = []
		temp_jebret = []

		#jika panjang dari plainteks kurang dari 8, maka proses enkripsi hanya dilakukan sekali saja
		if len(plaintext) < 8:
			cipher = encryptdua(plaintext)
			print "Hasil enkripsi dari",plaintext,"adalah: "

			file = open("hasil.txt","w")
			file.write(cipher)
			# file.write("\n")
			file.close()

			print(cipher)

		#jika panjang dari plainteks lebih dari 8, maka proses enkripsi dilakukan sebanyak jumlah teks yang diinputkan
		else: 
			putaran = 1
			#dibaca sampe plaintextnya habis
			while xx < math.ceil(len(plaintext)/8.0): 

				if xx == 0:
					iv_bits = '0000000000000000000000000000000000000000000000000000000000000000'
				else:	
					#mengganti iv_bits dengan hasil binary dari enkrispi putaran pertama
					iv_bits = iv_new
				
				aa = 0
				temp=[]
				print "ini new_plaintext ->", new_plaintext
				while aa < 8:
					#kalo di new_plaintext masih ada isinya
					if new_plaintext:
						#mengeluarkan isi dari array new_plainteks dari index ke 0, dan memasukkannya ke dalam array temp dari index ke 0
						temp += new_plaintext.pop(0)
						aa = aa + 1
					#kalo di new_plaintext sudah kosong
					else:
						break
					
				print "keluar while"
				print temp
				xx = xx + 1

				cipher = encrypt(temp, iv_bits)

				#nilai cipher di index ke 0 merupakan hasil enkripsi, dipindahkan ke array jebret
				jebret = cipher[0]
				print "Hasil enkripsi putaran ke ",putaran,"adalah: "
				print jebret

				#hasil jebret, dimasukkan ke dalam array temp_jebret supaya nanti dapat digabungkan
				temp_jebret.append(jebret)
				putaran = putaran + 1

				#nilai cipher di index ke 1 merupakan binary dari hasil enkripsi, dipindahkan ke array iv_new supaya nanti dapat dipindah ke array iv_bits
				iv_new = cipher[1]

			print "Maka hasil enkripsi dari text",plaintext,"adalah: "

			#hasil dari array temp_jebret yang masih terpisah2 oleh index digabungkan ke array final_banget dengan menghilangkan spasinya
			final_banget = ''.join(temp_jebret)

			file = open("hasil.txt","w")

			file.write(final_banget)
			# file.write("\n")
			file.close()

			print final_banget
			
    elif (choice == 2):

    	putaran = 1

        file = open("hasil.txt","r")
        cipher = file.read()
        
        backup_cipher = cipher
        temp_cipher = []

        panjang_cipher = len(cipher)
        print "panjang cipher text adalah: ", panjang_cipher

        hasil = []
        hasil.extend(backup_cipher)

        iv_new = []
        temp_jebret = []

        aa = 0
        xx = 0

        while xx < panjang_cipher / 16:
        	if xx == 0:
        		iv_bits = '0000000000000000000000000000000000000000000000000000000000000000'
        	else:
        		#ngerubah c1 jadi iv_new
        		iv_bits = iv_new

        	aa = 0
        	temp_cipher = []

        	while aa < 16:
        		if backup_cipher:
        			temp_cipher += hasil.pop(0)
        			aa = aa + 1
        			#print temp_cipher
        		else:
        			break

        	#print "kirim temp -> ", temp_cipher

        	xx = xx + 1
        	plaintext = decrypt_cbc(temp_cipher, iv_bits)

        	jebret = plaintext[0]
        	iv_new = plaintext[1]
        	print "Hasil dekrip putaran ke ",putaran, " adalah: "
        	print "ini hasil text-> ",jebret
        	print "ini iv_new-> ",iv_new
        	print "======================="

        	temp_jebret.append(jebret)
        	putaran = putaran + 1
        	# iv_new = plaintext[1]



    	print "Maka hasil dekripsi dari text",cipher,"adalah: "

    	final_banget = ''.join(temp_jebret)
    	file = open("hasil2.txt","w")

    	file.write(final_banget)
    	file.close()
    	print(final_banget)

    print('exiting...')
    return

if __name__ == "__main__":
    main()
