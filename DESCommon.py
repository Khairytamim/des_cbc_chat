
from DESConstant import *
from DESUtil import get_column, get_row, to_binary, left_shift



def apply_IP(block):
    #menambahkan isi block yang telah di permutasi dengan IP
    r = []
    r.extend(block)
    for i in range(0, 64):
        r[i] = block[IP[i]]

    return r


def apply_FP(block):
    """final permutaion
    """
    r = []
    r.extend(block)
    for i in range(0, 64):
        r[i] = block[(FP[i])]
    return r


def e_box(block):
    #memperbesar block yang dari 32 bit menjadi 48 bit
    dummy = []
    for i in range(48):
        dummy.append(block[E[i]])

    r = []
    for i in range(0, 48, 6):
        j = i + 6
        r.append(dummy[i:j])
    return r

#ngerubah 6 bit block jadi 4 bit. totalnya jadi 32 bit
def s_box(block):
    #menyimpelkan blok 48bit menjadi 32bit dengan cara membuat tabelnya
    #yang bisa paling pinggirnya
    for i in range(0, 8):
        row = str(block[i][0]) + str(block[i][-1])
        column = ''
        for j in range(1, 5):
            column += str(block[i][j])
        a = 16 * get_row(row)
        a += get_column(column)
        block.pop(i)
        block.insert(i, to_binary(ord(chr(s[i][a]))))
    r = []
    for i in block:
        r.extend(i[4:8])
    return r


def p_box(block):
    r = []
    r.extend(block)
    for i in range(32):
        r[i] = block[P[i]]
    return r


def iterate(left_block, right_block, keys, CIPHERS_FOR_EACH_ROUND):
    for j in range(0, 16):
        change_array = [] #change array diisi dengan right block
        #right block diisi oleh 
        change_array.extend(right_block)
        right_block = e_box(right_block)
        #ngerubah dari 32bits ke 48bits
        #chipper function
        for i in range(0, 8):
            di = i * 6
            for k in range(0, 6):
                #di xor sama keys
                right_block[i][k] ^= keys[j][di + k]
        right_block = s_box(right_block)
        right_block = p_box(right_block)
        for i in range(0, 32):
            right_block[i] ^= left_block[i]

        left_block = []
        left_block.extend(change_array)

        if CIPHERS_FOR_EACH_ROUND is not None:
            t = left_block
            t.extend(right_block)
            CIPHERS_FOR_EACH_ROUND.append(t)

    return left_block, right_block


def DES(text_bits, start, end, keys, CIPHERS_FOR_EACH_ROUND=None):
    #penggabungan 
    block = []
    for i in range(start, end):
        block.append(text_bits[i])

    block = apply_IP(block)
    #isi block sudah di permutasi dan akan dibagi menjadi 2 bagian

    left_block = block[0:32]
    right_block = block[32:64]

    left_block, right_block = iterate(left_block, right_block, keys, CIPHERS_FOR_EACH_ROUND)

    block = []
    block.extend(right_block)
    block.extend(left_block)

    block = apply_FP(block)

    cipher_block = ''
    for i in block:
        cipher_block += str(i)
    return cipher_block


def generate_keys(key_text):
    #merubah key menjadi biner
    key = []
    for i in key_text:
        key.extend(to_binary(ord(i)))
    # print
    # print key

    C = []
    D = []
    r = []
    # iv_new = []
    for i in range(28):
        C.append(key[PC1_C[i]])
    # print "array C = "
    # print C
    # print "==="
    for i in range(28):
        D.append(key[PC1_D[i]])
    for i in range(0, 16):
        if i in [0, 1, 8, 15]:
            C = left_shift(C, 1)
            D = left_shift(D, 1)
        else:
            C = left_shift(C, 2)
            D = left_shift(D, 2)
        CD = []
        CD.extend(C)
        CD.extend(D)
        dummy = []
        for i in range(48):
            dummy.append(CD[PC2[i]])
        r.append(dummy)
    return r
