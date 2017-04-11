import socket
from DES import *

s = socket.socket()
host = socket.gethostname()
# host = '10.151.36.25'
port = 12228
s.bind((host, port))

s.listen(5)
c = None

while True:
   if c is None:
       # Halts
       print 'menunggu koneksi dari server'
       c, addr = s.accept()
       print 'mendapatkan koneksi dari client dengan IP : ', addr
   else:
       print 'Menunggu response'

       pesan_belum = c.recv(1024)
       print "yg belum di dekrip = ", pesan_belum
       pesan_client = decrypt(pesan_belum)
       print "Pesan dari client -> ", pesan_client
       q = raw_input("Tulis chat ke client: ")
       q_encrypt = encryptdua(q)
       c.send(q_encrypt)