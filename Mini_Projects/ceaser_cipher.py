import string;
import re;

class CaesarCipher:
    def __init__(self):
        self.letters = list(string.ascii_lowercase);
        self.encryptedList = []
        self.decryptedList = []

    def get_message(self,encrypt = True):
        #Get encrypting/decrypting key
        key = self.get_key()
        if encrypt == False:
            message = input("Enter message to decrypt: ")
            result = self.decrypt_message(message,key)
        else:
            message = input("Enter message to encrypt: ")
            result = self.encrypt_message(message,key)
        return self.print_result(result)
    
    def get_key(self):
        while True:
            key = input("Enter key: ")
            if key.isdigit() == False:
                print("Invalid key value, please enter a valid key as a number!");
            else: return int(key)
            
    def encrypt_message(self,message,key = 3):
        for a,b in list(enumerate(message) ):
            encryptChar = b
            # Encode letters
            if encryptChar.isalpha():
                encryptIndex = self.letters.index(encryptChar.lower()) + key
                if encryptIndex > len(self.letters) - 1:
                    encryptChar = self.letters[encryptIndex - len(self.letters)]
                else: encryptChar = self.letters[encryptIndex]
                
            self.encryptedList.append(encryptChar)
            
        encrypted_message = "".join(self.encryptedList);
        # Find all numbers in the message and encrypt them
        encryptedNumbers =  self.find_numbers(encrypted_message)
        for i in encryptedNumbers:
            encrypted_message = encrypted_message.replace(str(i), str( int(i * key) ))
        
        return encrypted_message  
    
    def decrypt_message(self,encrypted_message,key):        
        for a,b in list(enumerate(encrypted_message)):
            decryptChar = b
            if decryptChar.isalpha():
                decryptIndex = self.letters.index(decryptChar) - key
                decryptChar = self.letters[decryptIndex]
            
            self.decryptedList.append(decryptChar)
            
        decryptedMessage = "".join(self.decryptedList)
        decryptedNumbers = self.find_numbers(decryptedMessage)
        
        for i in decryptedNumbers:
            decryptedMessage = decryptedMessage.replace(str(i), str( int(i / key) ));
        return decryptedMessage;        


    def find_numbers(self,message):
        return list(map(int, re.findall(r'\d+', message)))
    
    def print_result(self,message):
        print(message);

caesar_cipher = CaesarCipher();
caesar_cipher.get_message();
caesar_cipher.get_message(False);
#enMessage = caesar_cipher.encrypt_message("Hello my name is Jon Doe and I was born in 1904",3);
#deMessage = caesar_cipher.decrypt_message(enMessage,3);

