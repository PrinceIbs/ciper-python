from closecode import ciper
from opencode import deciper
import fileinput


# decrypt the file content
def dec(file_content, key):
       decrypted = deciper(file_content, key)
       print(decrypted)
       with open(filename, 'w') as f:
              f.write(decrypted)

              
# encrypt the file content
def enc(file_content, key):
       encrypted = ciper(file_content, key)
       print(encrypted)
       with open(filename, 'w') as f:
              f.write(encrypted)


def main():
       # Take user decision
       action = int(input("1. Decrypt \n2. Encrypt\n>>> "))
       
       global filename

       filename = input("Enter file name: ")
                 
       with open(filename, 'r') as f:
              file_content = f.read()
              
       if action == 1:
              # get encryption key from user
              key = int(input(">>>Key: "))
              dec(file_content, key)

       elif action == 2:
              # get encryption key from the user
              key = int(input(">>>Key: "))
              enc(file_content, key)

       else:
              print("Invalid input")
       

main()
