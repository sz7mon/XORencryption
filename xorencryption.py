#!/usr/bin/env python3
import sys
import os
import base64

def xor(data, key):
    key_bytes = key.encode()
    key_length = len(key_bytes)
    xor_data = []
    for i in range(len(data)):
        xor_byte = data[i] ^ key_bytes[i % key_length]
        xor_data.append(xor_byte)
    return bytes(xor_data)

if len(sys.argv) < 2 or sys.argv[1] == "help":
    print("Usage: ")
    print("python3 xorencryption.py <file_path> [-k <key>]")
    print("Options: ")
    print(" -k <key>    Specify the encryption key. If not specified, a default key is used.")
    print("Example:")
    print("python3 xorencryption.py myfile.txt -k key")
    sys.exit()
file_path = sys.argv[1]
key = "default key"
if "-k" in sys.argv:
    key_index = sys.argv.index("-k") + 1
    if key_index < len(sys.argv):
        key = sys.argv[key_index]
if not os.path.exists(file_path):
    print("File does not exist.")
    sys.exit()
with open(file_path, 'rb') as file:
    file_data = file.read()
encrypted_data = xor(file_data, key)
encrypted_file_path = os.path.splitext(file_path)[0] + "_enc" + os.path.splitext(file_path)[1]
with open(encrypted_file_path, 'wb') as file:
    file.write(encrypted_data)
encrypted_base64 = base64.b64encode(encrypted_data).decode()
encrypted_base64_file_path = os.path.splitext(file_path)[0] + "_enc_b64"
with open(encrypted_base64_file_path, 'w') as file:
    file.write(encrypted_base64)