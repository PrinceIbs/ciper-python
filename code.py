from closecode import ciper
from opencode import deciper
import fileinput



def dec(file_content, key):
       decrypted = deciper(file_content, key)
       print(decrypted)
       with open(filename, 'w') as f:
              f.write(decrypted)


def enc(file_content, key):
       encrypted = ciper(file_content, key)
       print(encrypted)
       with open(filename, 'w') as f:
              f.write(encrypted)


def main():

       global filename
       filename = "myfile.txt"
                 
       with open(filename, 'r') as f:
              file_content = f.read()
              
       action = int(input("1. Decrypt \n2. Encrypt\n>>> "))
       if action == 1:
              key = int(input("Key>>> "))
              dec(file_content, key)

       elif action == 2:
              key = int(input("Key>>> "))
              enc(file_content, key)

       else:
              print("Invalid input")
       

main()
