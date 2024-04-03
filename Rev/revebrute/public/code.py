import hashlib
import random

flag = "Redacted"

def my_encode(flag):
    li = []
    l = []
    for i in range(0,len(flag),4):
        l.append(flag[i:i+4])
    for k in l:
        ele = 0
        for j in range(0,len(k)):
            ele = ele + (ord(k[j])<<8*(3-j))
        li.append(ele)
    enc = ''
    for num in li:
        n0 = chr(int(((num/pow(85,4)) % 85) + 33))
        n1 = chr(int(((num/pow(85,3)) % 85) + 33))
        n2 = chr(int(((num/pow(85,2)) % 85) + 33))
        n3 = chr(int(((num/pow(85,1)) % 85) + 33))
        n4 = chr(int(((num/pow(85,0)) % 85) + 33))
        key = n0 + n1 + n2 + n3 + n4
        enc += key
    return enc

def my_encrypt(flag_val):
	result = (hashlib.sha256(flag_val.encode())).hexdigest()
	new_val = int(str(result),16)
	str_new_val = str(new_val)
	charact = ''
	for i in range(0,len(str_new_val),2):
		char = chr(int(str_new_val[i]+str_new_val[i+1]))
		if char.isalpha():
			charact+=char
		else:
			charact+=str_new_val[i]+str_new_val[i+1]
	return charact

def binary_to_text(binary_string):
    binary_values = binary_string.split()
    text_result = ''.join(chr(int(bin_val, 2)) for bin_val in binary_values)
    return text_result

def string_to_binary(input_string):
    binary_representation = ' '.join(format(ord(char), '08b') for char in input_string)
    #print("These are binary represent.",binary_representation)
    return binary_representation

def xor_binary_strings(binary_str1, binary_str2):
    result = ''
    for bit1, bit2 in zip(binary_str1, binary_str2):
        #print(bit1,bit2)
        result += '1' if bit1 != bit2 else '0'
        #print("result is",result)
    return result

def encode(s,key):
    if key == "":
        key = 10 #Default Key

    key = int(key)
    text_binary = string_to_binary(s)
    key_binary = format(key, '08b')

    result_fina = []
    for char in text_binary.split():
        result_binary = ''.join(xor_binary_strings(char, key_binary))
        result_fina.append(result_binary)
    
    result_fina = ' '.join(result_fina)
    b2t = binary_to_text(result_fina)
    return(b2t)

def main():
	flag_value = flag 
	encoded_flag = my_encode(flag_value)
	inter_flag = my_encrypt(flag_value)
	xored_flag = encode(inter_flag,random.randrange(1,255))
	final_flag = str(inter_flag)
	print(final_flag)
if __name__=="__main__":
	main()