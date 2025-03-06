from cryptography.fernet import Fernet
from django.conf import settings
#
#
# def enc(process1, process2, process3, file):
#     key = Fernet.generate_key()
#     process1 = enc_items(process1, key)
#     process2 = enc_items(process2, key)
#     process3 = enc_items(process3, key)
#     file = enc_file(file, key)
#     return process1, process2, process3, file, key
#
#
# def enc_file(files, key):
#     location = f'{settings.MEDIA_ROOT}/{files}'
#     fernet = Fernet(key)
#     with open(location, 'r') as fileread:
#         s = str(fileread.read())
#         l = bytes(s, 'utf-8')
#         en = fernet.encrypt(l)
#     with open(location, 'wb') as filewrite:
#         filewrite.write(en)
#         filewrite.close()
#     return files
#
#
# def enc_items(process1, key):
#     fernet = Fernet(key)
#     l = bytes(process1, 'utf-8')
#     en = fernet.encrypt(l)
#     return en
#
# def dec_file(file, key):
#     location = f'{settings.MEDIA_ROOT}/{file}'
#     fernet = Fernet(key)
#     with open(location, 'r') as fileread:
#         s = str(fileread.read())
#         l = bytes(s, 'utf-8')
#         en = fernet.decrypt(l)
#     # with open(location, 'wb') as filewrite:
#     #     filewrite.write(en)
#     #     filewrite.close()
#     return en
#
class Encryptor():

    def key_create(self):
        key = Fernet.generate_key()
        return key

    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key

    def file_encrypt(self, key, original_file, encrypted_file):
        f = Fernet(key)

        with open(original_file, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open(encrypted_file, 'wb') as file:
            file.write(encrypted)


    def file_decrypt(self, key, encrypted_file, decrypted_file):
        f = Fernet(key)

        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)
