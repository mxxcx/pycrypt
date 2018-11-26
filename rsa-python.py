from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
# from Crypto.Hash import SHA256
import base64

# pip install pycrypto

class CryptoRSA:
    PRIVATE_KEY_FILE = "private_key.pem"
    PUBLIC_KEY_FILE = "public_key.pem"
    
    def __init__(self):
        return

    def __save_file(self, contents, file_name):
        f = open(file_name, 'w')
        f.write(contents)
        f.close()
        
    def __read_file(self, file_name):
        f = open(file_name,'r')
        contents = f.read()
        f.close()
        return contents  

    def generate_keys(self):
        keys = RSA.generate(4096)
        private_key = keys.exportKey("PEM")
        public_key = keys.publickey().exportKey("PEM")
        self.__save_file(private_key, self.PRIVATE_KEY_FILE)
        self.__save_file(public_key, self.PUBLIC_KEY_FILE)
        print "Public & Private Keys; generated & saved successfully!"  

    def encrypt(self,cleartext, public_keypath=None):
        if (public_keypath == None):
            public_keypath = self.PUBLIC_KEY_FILE
            
        public_key = RSA.importKey(self.__read_file(public_keypath))
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_data = cipher.encrypt(cleartext)
        return base64.b64encode(encrypted_data)    

    def decrypt(self,cipher_text, private_key_path=None):
        if private_key_path == None:
            private_key_path = self.PRIVATE_KEY_FILE
            
        cipher_text = base64.b64decode(cipher_text)
        private_key = RSA.importKey(self.__read_file(private_key_path))
        cipher = PKCS1_OAEP.new(private_key)
        return cipher.decrypt(cipher_text)   