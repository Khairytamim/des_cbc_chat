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

if __name__ == "__main__":
    main()
