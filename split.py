import cPickle
from rsa import *

prima_1 = int(raw_input("Masukkan bilangan prima: "))
prima_2 = int(raw_input("Masukkan bilangan prima: (harus berbeda dengan prima 1)"))
print("Membuat public key + private key ")
public,  private = generate_keypair(prima_1, prima_2)
print("Public key -> ",public," dan Private key -> ",private)
data_string = cPickle.dumps(public)
print data_string
data_arr = cPickle.loads(data_string)
print("=============")
print data_arr
print("Masukkan nilai q dan a, dipisahkan dengan spasi")
qdana = raw_input()
qdana_split = qdana.split(' ')
q = qdana_split[0]
a = qdana_split[1]
enkrip_q = encrypt_rsa(private, q)
enkrip_a = encrypt_rsa(private, a)
enrkip_qFinal = ''.join(map(lambda x: str(x), enkrip_q))
enrkip_aFinal = ''.join(map(lambda x: str(x), enkrip_a))
print("ini enrkip q -> ",enrkip_qFinal,"ini enrkip a -> ",enrkip_aFinal)
print("Dekrip dengan public key ",public)
print("q -> ",decrypt_rsa(public, enkrip_q))
print("a -> ",decrypt_rsa(public, enkrip_a))