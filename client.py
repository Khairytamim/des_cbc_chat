import socket
from DES import *

s = socket.socket()
host = socket.gethostname()
port = 12228

s.connect((host, port))
print 'Terhubung dengan server dengan IP : ', host

while True:
    z = raw_input("Tulis chat ke server: ")
    z_encrypt = encryptdua(z)
    s.send(z_encrypt)
    print 'Menunggu response'

    x = s.recv(1024)
    print "yg blm di dekrip = ", x

    pesan_server = decrypt(x)
    print "Pesan dari server -> ", pesan_server

