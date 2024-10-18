from Card import Card
from tkinter import messagebox
from ExcelWriter import ExcelWriter

import datetime

class HallPass:
    
    def __init__(self):
        self.__cardCount = 0
        self.__cardDictionary = {}
        self.writer = ExcelWriter()
        
    def check_card(self, card_id):
        return card_id in self.__cardDictionary
   
    def add_card(self, card):
        if(self.check_card(card.get_card_id())):
            messagebox.showerror("Error", "The card is already present")
        else:
            if(self.__cardCount < 2):
                self.__cardDictionary[card.get_card_id()] = card
                self.__cardCount += 1
                messagebox.showinfo("Information","Card Added for Student with Id: {id}".format(id = card.get_student_id()))
                print(self.__cardDictionary)
            else:
                messagebox.showerror("Error", "There are 2 cards already present in here")
                
    
    def return_card(self, card_id):
        if(not self.check_card(card_id)):
            messagebox.showerror("","The card is not present")
        else:
            total_time = datetime.datetime.now() - self.__cardDictionary[card_id].get_timestamp()
            ## Need to change the timer in minutes
            messagebox.showinfo("Information","Card Retrurned in {total_time} seconds".format(total_time = total_time.total_seconds()))
            self.writer.__writeSheet__(self.__cardDictionary[card_id].get_student_id(), '{total_time} seconds'.format(total_time = total_time.total_seconds())) 
            del self.__cardDictionary[card_id]
            self.__cardCount -= 1
            print(self.__cardDictionary)
            
            
