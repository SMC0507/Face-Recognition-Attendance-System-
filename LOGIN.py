from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from FRS_GUI import FRS
import mysql.connector

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("Student")
        self.root.wm_iconbitmap("face.ico")

        f = Frame(self.root, highlightbackground="purple", highlightthickness=20)
        f.place(x=0, y=0, width=1500, height=800)

        img1 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\42.jpg")
        img1 = img1.resize((1000, 753), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        l1 = Label(f, image=self.photoimg1)
        l1.place(x=0, y=0, width=1000, height=753)

        l2 = Label(f,bg="white")
        l2.place(x=1000, y=0, width=453, height=753)

        l3 = Label(l2,text="LOGIN",font=("arial",40,"bold"),fg="black",bg="white")
        l3.place(x=120,y=50)

        img2 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\43.jpg")
        img2 = img2.resize((220, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        l4 = Label(l2, image=self.photoimg2)
        l4.place(x=98, y=110, width=220, height=200)

        img3 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\39.jpg")
        img3 = img3.resize((30, 30), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        l5 = Label(l2, image=self.photoimg3)
        l5.place(x=100, y=350, width=30, height=30)

        l6 = Label(l2,text="ENTER YOUR MAIL ID",font=("times new roman", 12, "bold"),bg="white")
        l6.place(x=140, y=313, width=170, height=100)
        
        self.e = ttk.Entry(l2,font=("times new roman", 12, "bold"))
        self.e.place(x=100,y=400,width=260,height=30)
        
        img4 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\40.jpg")
        img4 = img4.resize((20, 22), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        l7 = Label(l2, image=self.photoimg4)
        l7.place(x=100, y=480, width=20, height=22)

        l8 = Label(l2,text="ENTER YOUR PASSWORD",font=("times new roman", 12, "bold"),bg="white")
        l8.place(x=140, y=443, width=200, height=100)
        
        self.p = ttk.Entry(l2,font=("times new roman", 12, "bold"),show="*")
        self.p.place(x=100,y=530,width=260,height=30)

        b1 = Button(l2, text="LOGIN", font=("times new roman", 15, "bold"), bg="purple", fg="white",width=10,command=self.login)
        b1.place(x=160,y=600)

    #FUNCTIONS
    def login(self):
        if self.e.get()=="" or self.p.get()=="":
            messagebox.showerror("ERROR","ALL FIELDS REQUIRED",parent=self.root)
        else:
            try:
                db = mysql.connector.connect(host="localhost", user="root", password="admin", database="frs")
                cursor = db.cursor()
                cursor.execute("SELECT * FROM student WHERE email = %s AND phone_number = %s", (self.e.get(), self.p.get()))
                row = cursor.fetchone()
                if row:
                    messagebox.showinfo("SUCCESS","WELCOME TO FACE RECOGINITION ATTENDANCE SYSTEM")
                    self.new_win=Toplevel(self.root)
                    self.n=FRS(self.new_win)
                else:
                    messagebox.showerror("INVALID","INVALID MAIL ID OR PASSWORD")
            except Exception as e:
                messagebox.showerror("ERROR",str(e),parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
