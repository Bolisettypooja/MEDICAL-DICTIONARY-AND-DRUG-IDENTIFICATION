import mysql.connector
from tkinter import *
from PIL import Image, ImageTk

db_connection = mysql.connector.connect( 
host= "localhost", 
user= "root", 
passwd= "Poojasree#07") 

class GUI:
    def __init__(self):
        self.db_cursor = db_connection.cursor()
        self.db_cursor.execute("USE medical_db")
        self.main_window=Tk()
        self.main_window.title("Medical Dictionary and Drug Identification")
        self.main_window.geometry(str(self.main_window.winfo_screenwidth()-600)+"x"+str(self.main_window.winfo_screenheight()-400))
        self.img=Image.open('BG.png')
        self.reimg=self.img.resize((self.main_window.winfo_screenwidth(),self.main_window.winfo_screenheight()))
        self.bgImage=ImageTk.PhotoImage(self.reimg)
        self.background=Label(self.main_window,image=self.bgImage)
        self.top_frame=Frame(self.main_window)
        self.middle_frame=Frame(self.main_window)
        self.bottom_frame=Frame(self.main_window)
        self.variable = StringVar()
        self.variable = StringVar(self.top_frame)
        self.variable.set("Select user type")
        self.userTypeSelection = OptionMenu(self.top_frame, self.variable, "Professional", "Layman",command=self.options)
        self.userTypeSelection.config(width = 30)
        self.enter_input=Entry(self.middle_frame,width=30,font=('monospace',18))
        self.my_button=Button(self.middle_frame,text="Search",command=self.search,bg='#4285F4',fg='white',width=10,font=('monospace',16,"bold"),activebackground="yellow", activeforeground="#4285F4")
        self.printOut=StringVar()
        self.out=Label(self.bottom_frame,textvariable=self.printOut,wraplength=(self.main_window.winfo_screenwidth()-35), justify="center",font=("monospace", 18))
        self.userTypeSelection.pack()
        self.enter_input.pack(side="left",padx=4)
        self.my_button.pack(padx=4)
        self.background.place(x=0, y=0)
        self.top_frame.pack(pady=7)
        self.middle_frame.pack(pady=64)
        self.professionalinfo=Label(self.top_frame,text= "Professional- Doctors & Medical students")
        self.laymaninfo=Label(self.top_frame,text= "Layman- consumers,common people")
        self.professionalinfo.pack()
        self.laymaninfo.pack()
        self.out.pack()
        self.bottom_frame.pack()
        self.main_window.mainloop()
        
    def options(self,*args):
        print(self.variable.get())
        
    def search(self):
        if self.variable.get()=="Layman":
            self.query="SELECT * FROM generic_drug WHERE Generic LIKE \'%"+self.enter_input.get()+"%\'"+" OR Brands LIKE \'%"+self.enter_input.get()+"%\'"
            self.db_cursor.execute(self.query)
            self.myresult=self.db_cursor.fetchall()
            if len(self.myresult)!=0 and len(self.enter_input.get())>=3:
                self.printOut.set("Drug info\n\n"+self.myresult[0][0]+" :- "+self.myresult[0][1])
            elif len(self.enter_input.get())<3:
                self.printOut.set("Enter atlest 3 characters")
            else:
                self.printOut.set("Sorry, no results found!\n try again")
        elif self.variable.get()=="Professional":
            self.query="SELECT * FROM generic_drug WHERE Generic LIKE \'%"+self.enter_input.get()+"%\'"+" OR Brands LIKE \'%"+self.enter_input.get()+"%\'"
            self.db_cursor.execute(self.query)
            self.myresult=self.db_cursor.fetchall()
            if len(self.myresult)!=0 and len(self.enter_input.get())>=3:
                self.printOut.set("Drug info\n\nBrands for "+self.myresult[0][0]+" :- "+self.myresult[0][1])
            elif len(self.enter_input.get())<3:
                self.printOut.set("Enter atlest 3 characters")
            else:
                self.query="SELECT * FROM medicalTerms WHERE Term LIKE \'%"+self.enter_input.get()+"%\'"
                self.db_cursor.execute(self.query)
                self.myresult=self.db_cursor.fetchall()
                if len(self.myresult)!=0:
                    self.printOut.set("Meaning for the term\n"+self.myresult[0][0]+" = "+self.myresult[0][1])
                else:
                    self.printOut.set("Sorry, no results found!\n try again")
        else:
            self.printOut.set("Please select user type before searching something")
my_gui=GUI()
