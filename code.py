from closecode import ciper
from opencode import deciper
import fileinput



def dec(file_content):
       decrypted = deciper(file_content, 12)
       print(decrypted)
       with open(filename, 'w') as f:
              f.write(decrypted)


def enc(file_content):
       encrypted = ciper(file_content, 12)
       print(encrypted)
       with open(filename, 'w') as f:
              f.write(encrypted)


def main():

       global filename
       filename = 'myfile.txt'
                 
       with open(filename, 'r') as f:
              file_content = f.read()
              
       action = int(input("1. Decrypt \n2. Encrypt\n>>> "))
       if action == 1:
              dec(file_content)
              enc(file_content)
       elif action == 2:
              enc(file_content)
       else:
              print("Invalid input")
       

main()
