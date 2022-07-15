initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]
expansion_perm = [32, 1 , 2 , 3 , 4 , 5 , 4 , 5,
         6 , 7 , 8 , 9 , 8 , 9 , 10, 11,
         12, 13, 12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21, 20, 21,
         22, 23, 24, 25, 24, 25, 26, 27,
         28, 29, 28, 29, 30, 31, 32, 1 ]
perm_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
s_box = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],
            
         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
           [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],
   
         [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
           [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
           [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],
       
          [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
           [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
           [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ],
        
          [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
           [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
           [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],
       
         [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
           [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ],
         
          [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
           [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ],
        
         [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]
final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
                39, 7, 47, 15, 55, 23, 63, 31,
                38, 6, 46, 14, 54, 22, 62, 30,
                37, 5, 45, 13, 53, 21, 61, 29,
                36, 4, 44, 12, 52, 20, 60, 28,
                35, 3, 43, 11, 51, 19, 59, 27,
                34, 2, 42, 10, 50, 18, 58, 26,
                33, 1, 41, 9, 49, 17, 57, 25]
per = [ 16,  7, 20, 21,
        29, 12, 28, 17,
         1, 15, 23, 26,
         5, 18, 31, 10,
         2,  8, 24, 14,
        32, 27,  3,  9,
        19, 13, 30,  6,
        22, 11,  4, 25 ]
perm_1 = [ 57, 49, 41 , 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19,11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4]
def hex2bin(text):
    my_hexdata = text
    scale = 16 # equal to hexadecimal
    return bin(int(my_hexdata, scale))[2:].zfill(len(my_hexdata)*4)
def bin2hex(s):
    mp = {"0000" : '0',
          "0001" : '1',
          "0010" : '2',
          "0011" : '3',
          "0100" : '4',
          "0101" : '5',
          "0110" : '6',
          "0111" : '7',
          "1000" : '8',
          "1001" : '9',
          "1010" : 'A',
          "1011" : 'B',
          "1100" : 'C',
          "1101" : 'D',
          "1110" : 'E',
          "1111" : 'F' }
    hex = ""
    for i in range(0,len(s),4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex = hex + mp[ch]
    return hex

def leftshift(k_text, n):
    return k_text[n:] + k_text[:n]
        
def S_box(xor):
    #s box value calculation
        j = 0
        k = 0
        s_box_val = ''
        for i in range(6, len(xor) + 1, 6):
            row = xor[j:i][0] + xor[j:i][-1]
            row = int(row, 2) #binary to decimal
            col = xor[j:i][1:-1]
            col = int(col, 2)
            j = i          
            if len("{0:b}".format(s_box[k][row][col])) < 4:
                binary = "{0:b}".format(s_box[k][row][col])
                binary =  '0' * (4 - len("{0:b}".format(s_box[k][row][col]))) + binary
                s_box_val += binary
            else:
                s_box_val += "{0:b}".format(s_box[k][row][col])
            k += 1
        return s_box_val
def encrypt(left, right, left_k, right_k):
    l_16 = ''
    r_16 = ''
    for i in range(16):
        #text
        left_k = ''.join(left_k)
        right_k = ''.join(right_k)
        original_right = right[:32]
        right = ''.join([right[x - 1] for x in expansion_perm])
        #key
        if i == 0 or i == 1 or i == 8 or i == 15:
            left_k = leftshift(left_k, 1)
            right_k = leftshift(right_k, 1)
        else:
            left_k = leftshift(left_k, 2)
            right_k = leftshift(right_k, 2)
        new_key = ''.join(left_k) + ''.join(right_k)
        #permuted choice 2
        new_key = ''.join([new_key[perm_2[x] - 1] for x in range(len(perm_2))])
        #xor with right and new_key
        xor = ''.join([str(int(right[i]) ^ int(new_key[i])) for i in range(len(new_key))])
        #S-BOX value calculation
        s_box_value = S_box(xor)
        s_box_value = [s_box_value[per[x] - 1] for x in range(len(per))]
        s_box_value = ''.join(s_box_value)
        #second xor value
        xor_1 = ''.join([str(int(left[i]) ^ int(s_box_value[i])) for i in range(len(left))])
        left = original_right
        right = xor_1
        if i == 14:
            l_16 = xor_1
        if i == 15:
            r_16 = xor_1
    bit_swap = r_16 + l_16
    iip = ''.join([bit_swap[final_perm[x] - 1] for x in range(len(final_perm))])
    return bin2hex(iip)
#des main
def main():
    text = "123456ABCD132536"
    key = "AABB09182736CCDD"
    #text = text.encode("utf-8").hex()
    #key = key.encode("utf-8").hex()
    text = hex2bin(text)
    key = hex2bin(key)
    text = ''.join([text[x - 1] for x in initial_perm]) #initial permutation
    key = [key[perm_1[x] - 1] for x in range(len(perm_1))] #permuted choice - 1
    left = text[:32]
    right = text[32:]
    left_k = key[:28]
    right_k = key[28:]
    ciphertext = encrypt(left,right, left_k, right_k)
    print(ciphertext)
main()