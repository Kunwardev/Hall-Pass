from tkinter import *

class Interface:

    def submit(self):
        # Process the input data
        self.card_id = self.cid.get()
        self.student_id = self.sid.get()
        self.root.destroy()
        
    def __init__(self):
        self.root = Toplevel()
        self.root.title("Hall Pass")
        self.root.minsize(200, 150)  # corrected to self.root.minsize
        empty = Label(self.root)
        empty.grid(row=0)

        label_card = Label(self.root, text="Please add the Card Id: ")
        label_card.grid(row=1)

        self.cid = Entry(self.root)
        self.cid.grid(row=2)

        empty1 = Label(self.root)
        empty1.grid(row=3)
        
        label_student = Label(self.root, text="Please add the Student Id: ")
        label_student.grid(row=4)

        self.sid = Entry(self.root)
        self.sid.grid(row=5)

        empty2 = Label(self.root)
        empty2.grid(row=6)

        sub_btn = Button(self.root, text="Submit", command=self.submit)
        sub_btn.grid(row=7)

        self.root.mainloop()
        
        
i = Interface()
