from HallPass import HallPass
from Card import Card

from tkinter import *
from tkinter import messagebox

class Main:
    
    def __init__(self):
        self.hall_pass = HallPass()
        
    def add_card(self):
        self.card.set_full_id(self.cardid, self.asid.get())
        self.hall_pass.add_card(self.card)
        self.root3.destroy()
        
    def return_card(self):
        self.hall_pass.return_card(self.cardid)
        
    def submit(self):
        choice = self.check_card()
        self.cardid = self.cid.get()
        print(choice)
        self.root1.destroy()
        if choice == False:
            self.card = Card()
            self.root3 = Tk()
            self.root3.title("Hall Pass")
            self.root3.minsize(200, 150)  # corrected to self.root.minsize
            empty = Label(self.root3)
            empty.grid(row=0)

            empty = Label(self.root3)
            empty.grid(row=1, padx=(12,10))

            label_card = Label(self.root3, text="Enter Student Id")
            label_card.grid(row=2, padx=(12,10))

            self.asid = Entry(self.root3)
            self.asid.grid(row=3, padx=(12,10))
            
            empty1 = Label(self.root3)
            empty1.grid(row=4, padx=(12,10))
            
            sub_btn = Button(self.root3, text="Check Out", command=self.add_card)
            sub_btn.grid(row=5, padx=(12,10))
            
        else:
            self.return_card()
            
    def check_card(self):
        self.inDictionary = self.hall_pass.check_card(self.cid.get())
        return self.inDictionary
        
    
    def run_program(self):
        while True:
            self.root1 = Tk()
            self.root1.title("Hall Pass")
            self.root1.minsize(200, 150)  # corrected to self.root.minsize
            empty = Label(self.root1)
            empty.grid(row=0, padx=(12,10))

            label_card = Label(self.root1, text="Please tap the card")
            label_card.grid(row=1, padx=(12,10))

            self.cid = Entry(self.root1)
            self.cid.grid(row=2, padx=(12,10))
            
            empty1 = Label(self.root1)
            empty1.grid(row=3, padx=(12,10))
            
            sub_btn = Button(self.root1, text="Submit", command=self.submit)
            sub_btn.grid(row=4, padx=(12,10))

            self.root1.mainloop()

        
m = Main()
m.run_program()