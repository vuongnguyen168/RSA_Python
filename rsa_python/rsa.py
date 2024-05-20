import random
import math
# kiểm tra số nguyên tố
def check_prime(n):
    if n<2:
        return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return True
# phép đảo ngược modulo cho phi
def mod_inverse(e,phi):
    for d in range(3,phi):
        if (d*e) % phi ==1:
            return d
# tạo khóa
def generate_key(p,q):
    n=p*q
    phi=(p-1)*(q-1)
    e=random.randint(2,phi-1)
    while math.gcd(e,phi) !=1:
        e=random.randint(2,phi-1)
    d=mod_inverse(e,phi)
    publickey=(e,n)
    privatekey=(d,n)
    return publickey,privatekey
# mã hóa
def encrypt(message,publickey):
    e,n=publickey
    encrypt_message=[pow(ord(x),e)%n for x in message]#hàm ord chuyển các kí tự thành số nguyên theo bảng mã asscii, hàm pow(x,y)%z tính x^y modulo z
    return encrypt_message
# giải mã
def decrypt(encrypt_message,privatekey):
    d,n=privatekey
    decrypt_message=''.join([chr(pow(x,d)%n) for x in encrypt_message])#hàm char chuyển các số nguyên thành kí tự theo bảng mã asscii, hàm pow(x,y)%z tính x^y modulo z
    return decrypt_message
# nhập p và giới hạn p có độ lớn ít nhất là 4 bit
print("Nhập p: ",end="")
p=int(input())
while check_prime(p)==False or p.bit_length() < 4:
    print("p không phải nguyên tố hoặc không đủ lớn, nhập lại: ", end="")
    p=int(input())
# nhập q và giới hạn q có độ lớn ít nhất là 4 bit
print("Nhập q: ",end="")
q=int(input())
while check_prime(q)==False or q.bit_length() < 4:
    print("q không phải nguyên tố hoặc không đủ lớn, nhập lại: ", end="")
    q=int(input())
# tạo khóa
publickey,privatekey=generate_key(p,q)
print("Khóa công khai: {}".format(publickey))
print("Khóa bí mật: {}".format(privatekey))
# nhập thông điệp
print("Nhập thông điệp: ",end="")
message=input()
encrypt_message=encrypt(message,publickey)
decrypt_message=decrypt(encrypt_message,privatekey)
print("Thông điệp đã mã hóa:",encrypt_message)
print("Thông điệp đã giải mã:",decrypt_message)


# 1 số test
#số nguyên tố nhỏ p = 61, q = 53
#số nguyên tố lớn p = 102673, q = 102677