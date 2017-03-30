#This program is written by Uday Sagar Shiramshetty, studying 3rd year CSE, at MANIT-Bhopal
#It is written according to the python 3 syntax. Just run this program and follow the instructions 
#for encryption and decryption
#Any comments may be addressed to udaysagar.2177@gmail.com
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

def encryptdua(plaintext, key_text):
	keys = generate_keys(key_text)
	text_bits = get_bits(plaintext)
	text_bits = add_pads_if_necessary(text_bits)
	
	iv_bits = '0000000000000000000000000000000000000000000000000000000000000000'
	results = map(int, iv_bits)	

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

def encrypt(plaintext, key_text, iv_bits):
	keys = generate_keys(key_text)
	text_bits = get_bits(plaintext)
	text_bits = add_pads_if_necessary(text_bits)
	results = map(int, iv_bits)

	for i in text_bits:
		text_bits[i] ^= results[i]
	final_cipher = ''
	for i in range(0, len(text_bits), 64):
		final_cipher += DES(text_bits, i, (i+64), keys)
	# conversion of binary cipher into hex-decimal form
	# print "ini final ciper"
	# print final_cipher
	# print "========"
	hex_cipher = ''
	i = 0
	while i < len(final_cipher):
		hex_cipher += bin_to_hex(final_cipher[i:i+4])
		i = i+4
	return hex_cipher, final_cipher

def decrypt(cipher, key_text):
	keys = generate_keys(key_text)

	text_bits = []
	ciphertext = ''
	for i in cipher:
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
		text_mess += bin_to_text(bin_mess[i:i+8])
		i = i+8
	return text_mess.rstrip('\x00')

def main():
    print('Encrypt = 1')
    print('Decrypt = 2')
    choice = int(input())

    key_text = str(input('Enter the key\n'))

    if(len(key_text) < 8):
    	print('Key must be 8 characters in length. Exiting...')
    	return

    if(choice == 1):
		plaintext = str(input('Enter the message(in Text-form)\n'))
		#print plaintext
		#ambil 8 karakter awal
		new_plaintext = []
		new_plaintext.extend(plaintext)
		#print new_plaintext		
		xx = 0
		aa = 0
		temp = []
		iv_new = []
		temp_jebret = []

		if len(plaintext) < 8:
			cipher = encryptdua(plaintext, key_text)
			print('the cipher is(in hex-decimal form)')
			print(cipher)

		else:
			putaran = 1
			while xx < math.ceil(len(plaintext)/8.0): #dibaca sampe plaintextnya habis

				if xx == 0:
					iv_bits = '0000000000000000000000000000000000000000000000000000000000000000'
				else:
					iv_bits = iv_new
				# print "ini iv_bits di def main"
				# print iv_bits
				aa = 0
				# print new_plaintext
				temp=[]
				while aa < 8:
					temp += new_plaintext.pop(0)
					aa = aa + 1			
				xx = xx + 1
				# print temp
				cipher = encrypt(temp, key_text, iv_bits)
				# print('the cipher is(in hex-decimal fform)')
				# print(cipher)

				jebret = cipher[0]
				print "Hasil enkripsi putaran ke ",putaran,"adalah: "
				print jebret
				temp_jebret.append(jebret)
				putaran = putaran + 1

				iv_new = cipher[1]
				# print iv_new
				#print iv_new

		print "Maka hasil enkripsi dari text",plaintext,"adalah: "
		final_banget = ''.join(temp_jebret)
		print final_banget

    else:
        cipher = str(input('Enter the message(in hex-decimal form)\n'))
        plaintext = decrypt(cipher, key_text)
        print('the original text is')
        print(plaintext)

    print('exiting...')
    return

if __name__ == "__main__":
    main()
