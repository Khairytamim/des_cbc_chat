#permutation function
def permutation(table, binary):
    permutation_result = []
    for i in table:
        permutation_result.append(binary[i - 1])
    return b''.join(permutation_result)

#left shifting function
def left_shift(table, binary_list):
    x = 0
    for i in table:
        binary_list.append(binary_list[x][i:] + binary_list[x][0:i])
        x = x + 1
    return binary_list

#compute xor from 2 binary number
def xor(num1, num2):
    result = ""
    for i in range(0,len(num1)):
        if bool(int(num1[i])) != bool(int(num2[i])):
            result += '1'
        else:
            result += '0'
    return result

#s-box operation
def check_s_box(key1, key2, table, num):
    num1 = num[0:1] + num[-1:]
    num2 = num[1:5]
    index1 = key1.index(num1)
    index2 = key2.index(num2)
    return table[index1][index2]

#encrypting text with DES algorithm
def encrypt(plaintext, key):
    #main variable

    #table for permutation
    ip_table = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
    pc_1_table = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 45, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    left_shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    pc_2_table = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    e_table = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    p_box_table = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
    ip_inverse_table = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

    #s-box table
    #vertical
    s_box_key_1 = ['00', '01', '10', '11']
    #horizontal
    s_box_key_2 = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    #list of list
    s1_table = []
    s1_table.append([14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7])
    s1_table.append([0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8])
    s1_table.append([4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0])
    s1_table.append([15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13])
    s2_table = []
    s2_table.append([15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10])
    s2_table.append([3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5])
    s2_table.append([0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15])
    s2_table.append([13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9])
    s3_table = []
    s3_table.append([10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8])
    s3_table.append([13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1])
    s3_table.append([13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7])
    s3_table.append([1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12])
    s4_table = []
    s4_table.append([7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15])
    s4_table.append([13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9])
    s4_table.append([10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4])
    s4_table.append([3, 15, 0, 6, 10, 1, 13, 18, 9, 4, 5, 11, 12, 7, 2, 14])
    s5_table = []
    s5_table.append([2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9])
    s5_table.append([14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 15])
    s5_table.append([4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14])
    s5_table.append([11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3])
    s6_table = []
    s6_table.append([12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11])
    s6_table.append([10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8])
    s6_table.append([9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6])
    s6_table.append([4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13])
    s7_table = []
    s7_table.append([4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1])
    s7_table.append([13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6])
    s7_table.append([1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2])
    s7_table.append([6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12])
    s8_table = []
    s8_table.append([13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7])
    s8_table.append([1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2])
    s8_table.append([7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8])
    s8_table.append([2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11])

    #convert s-box into binary
    for i in range(0,4):
        for j in range(0,16):
            s1_table[i][j] = '{0:04b}'.format(s1_table[i][j])
            s2_table[i][j] = '{0:04b}'.format(s2_table[i][j])
            s3_table[i][j] = '{0:04b}'.format(s3_table[i][j])
            s4_table[i][j] = '{0:04b}'.format(s4_table[i][j])
            s5_table[i][j] = '{0:04b}'.format(s5_table[i][j])
            s6_table[i][j] = '{0:04b}'.format(s6_table[i][j])
            s7_table[i][j] = '{0:04b}'.format(s7_table[i][j])
            s8_table[i][j] = '{0:04b}'.format(s8_table[i][j])

    #initialize plain text and key
    plaintext_bin = plaintext
    key_bin = key

    #generate initial permutation
    ip = permutation(ip_table, plaintext_bin)
    left = []
    right = []
    left.append(ip[0:32])
    right.append(ip[32:64])

    #key permutation and splitting
    cd = permutation(pc_1_table, key_bin)
    c = []
    d = []
    c.append(cd[0:28])
    d.append(cd[28:56])

    #shifting splitted key to left
    c = left_shift(left_shift_table, c)
    d = left_shift(left_shift_table, d)

    #join splitted key
    cd = []
    k = []
    for i in range(0, 17):
        cd.append(c[i] + d[i])
        k.append(permutation(pc_2_table, cd[i]))
        #print 'c:'+c[i]
        #print 'd:'+d[i]
    #print cd

    #do 16 stage xor operation on expanded right-splitted plain text with variable K
    er = []
    a = []
    a.append('')
    for i in range(0, 16):
        er.append(permutation(e_table, right[i]))
        a.append(xor(er[i], k[i+1]))

        #s-box operation
        b_temp = []
        for j in range(0, 8):
            b_temp.append(a[i+1][j*6:j*6+6])
        b = check_s_box(s_box_key_1, s_box_key_2, s1_table, b_temp[0])
        b += check_s_box(s_box_key_1, s_box_key_2, s2_table, b_temp[1])
        b += check_s_box(s_box_key_1, s_box_key_2, s3_table, b_temp[2])
        b += check_s_box(s_box_key_1, s_box_key_2, s4_table, b_temp[3])
        b += check_s_box(s_box_key_1, s_box_key_2, s5_table, b_temp[4])
        b += check_s_box(s_box_key_1, s_box_key_2, s6_table, b_temp[5])
        b += check_s_box(s_box_key_1, s_box_key_2, s7_table, b_temp[6])
        b += check_s_box(s_box_key_1, s_box_key_2, s8_table, b_temp[7])

        #p-box permutation
        p = permutation(p_box_table, b)
        right.append(xor(p, left[i]))
        left.append(right[i])

    # join right and left splitted plaintext into chiper text
    rl = right[16]+left[16]
    chiper_text = permutation(ip_inverse_table, rl)
    return chiper_text

#get input from user
print "Enter Text to be Encrypted"
plaintext = raw_input()
key = ''
#looping until user input the right key format
while len(key) != 8:
    print "Enter Key (must be exactly 8 character)"
    key = raw_input()

#convert plaintext and key into binary
plaintext_bin = ''.join(format(x, 'b').zfill(8) for x in bytearray(plaintext))
key_bin = ''.join(format(x, 'b').zfill(8) for x in bytearray(key))

text_length = len(plaintext)
chiper = ''
iv = '0000000000000000000000000000000000000000000000000000000000000000'
i = 0

#start chiper block chaining encryption with DES
while text_length > 0:
    if(text_length < 8):
        p_text = plaintext_bin[i * 64:i*64 + 8*text_length]
        for i in range(0, 8 - text_length):
            p_text = '00000000' + p_text
    else:
        p_text = plaintext_bin[i * 64:i * 64 + 64]
    p = xor(iv, p_text)
    chiper = encrypt(p, key_bin)
    iv = chiper
    i+=1
    text_length -= 8

chiper_bin = []
chiper_text = ''
for i in range(0, 8):
    chiper_bin.append(int(chiper[i*8:i*8+8], 2))
    # chiper_text += chiper_bin[i]
    print chr(chiper_bin)