import datetime
#from cryptography.fernet import Fernet

class Card:
    
    def __init__(self):
        self.__card_id = "";
        self.__student_id = "";
        self.__timestamp = "";
    
        # Encrption can be added at later stage
        # self.__fernet = Fernet(b'EhO3oCgiq1-xb3a-9YOKAIz8aGF0mBOB6c501DxJ2ZA=')
    
    def get_card_id(self):
        return self.__card_id
    
    def set_full_id(self, acid, asid):
        self.__card_id = acid
        self.__student_id = asid
        self.__full_id = (self.__card_id + self.__student_id)
        self.__timestamp = datetime.datetime.now()

    def get_full_id(self):
        return self.__full_id
   
    def get_student_id(self):
        return self.__student_id
    
    def get_timestamp(self):
        return self.__timestamp
    # Decryption Function    
"""    
    def get_d_full_id(self):
        return self.__fernet.decrypt(self.__full_id).decode()
"""

