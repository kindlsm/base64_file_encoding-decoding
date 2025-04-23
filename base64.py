import base64
import os

def encode_file(file_path):
    with open(file_path, 'rb') as file_to_encode:
        file_data = file_to_encode.read()
        encoded_data = base64.b64encode(file_data)
    
    with open(file_path, 'wb') as encoded_file:
        encoded_file.write(encoded_data)

def decode_file(file_path):
    with open(file_path, 'rb') as file_to_decode:
        encoded_data = file_to_decode.read()
        decoded_data = base64.b64decode(encoded_data)
    
    with open(file_path, 'wb') as decoded_file:
        decoded_file.write(decoded_data)

def main():
    choice = input("1. Base64 encoding\n2. Base64 decoding\n#Input: ")
    
    file_name = input("#Input2(filename) : ")
    file_path = os.path.join(os.getcwd(), file_name)
    
    
    if choice == '1':
        encode_file(file_path)
    elif choice == '2':
        decode_file(file_path)

if __name__ == "__main__":
    main()