# program to encrypt and decrypt user entered data

from msvcrt import getch
from os import system
import hashlib

class joker:
    def __init__(self):
        All_algorithm = ["BLAKE2b512, BLAKE2s256, MD4, MD5, MD5-SHA1, RIPEMD160, SHA1,", "SHA224, SHA256, SHA384, SHA512, blake2b, blake2b512, blake2s,",
                         "blake2s256, md4, md5, md5-sha1, ripemd160, sha1, sha224, sha256,", "sha384, sha3_224, sha3_256, sha3_384, sha3_512, sha512,", "shake_128, shake_256, whirlpool"]

    def menu(self):
        while True:
            system("cls")
            print(f"\t\t <-------- Welcome To Main Menu  --------> ")
            print(f"\t\t <------------------------------------------> ")
            print(f"\t\t <-----  1 . Encrypt  -----> ")
            # print(f"\t\t <-----  2 . Decrypt  -----> ")
            print(f"\t\t <-----  10. About    -----> ")
            print(f"\t\t <-----  99. Exit     -----> ")
            ch = int(input())
            if ch == 1:
                self.encrypt()
            elif ch == 2:
                pass
            elif ch == 10:
                pass
            elif ch == 99:
                print(f"\t\t <------ Thanks for using our program -----> ")
                break
        getch()
    def encrypt(self):
        print(f"\t\t <------- Welcome to Encrypt Section -----> ")
        str = input("\t\t Enter String -----> ")
        ha = hashlib.sha1()
        ha.update(str.encode('utf-8'))
        print(f"\t\t Encrpted string ----> {ha.hexdigest()} ")
        getch()

def choose():
    lo = ["BLAKE2b512", "BLAKE2s256", "MD4", "MD5", "MD5-SHA1", "RIPEMD160", "SHA1",
          "SHA224", "SHA256", "SHA384", "SHA512", "blake2b", "blake2b512", "blake2s",
          "blake2s256", "md4", "md5", "md5-sha1", "ripemd160", "sha1", "sha224", "sha256",
          "sha384", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "sha512", "shake_128",
          "shake_256", "whirlpool", "BLAKE2b512", "BLAKE2s256", "MD4", "MD5", "MD5-SHA1", "RIPEMD160",
          "SHA1",
          "SHA224", "SHA256", "SHA384", "SHA512", "blake2b", "blake2b512", "blake2s",
          "blake2s256", "md4", "md5", "md5-sha1", "ripemd160", "sha1", "sha224", "sha256",
          "sha384", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "sha512",
          "shake_128", "shake_256", "whirlpool"]
    
    e=1
    for var in lo:
        print(f"\t\t {e} -----> {var} ")
        e+=1

    str=int(input("\t\t Select Alogithm -----> "))
    print(f"\t\t Algorithm ----> {lo[str-1]} ")
    return lo[str-1]






joke=joker()
joke.menu()
