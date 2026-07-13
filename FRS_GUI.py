from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from STUDENT import Student
from TRAIN import Train_Data
from FACE_RECOGINITION import Face_Rec
from STUDENT_ATTENDANCE import stu_attendance
from DEVELOPER import dev
from CHATBOT import CB
import os

class FRS:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        #TOP IMAGES 
        img1=Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\3.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        l1=Label(self.root,image=self.photoimg1)
        l1.place(x=0,y=0,width=500,height=130)

        img2=Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\21.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        l2=Label(self.root,image=self.photoimg2)
        l2.place(x=500,y=0,width=500,height=130)

        img3=Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\4.jpg")
        img3=img3.resize((500,130),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        l3=Label(self.root,image=self.photoimg3)
        l3.place(x=1000,y=0,width=500,height=130)
        
        #BACKGROUND
        bgimg=Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\bg6.jpg")
        bgimg=bgimg.resize((1500,800),Image.LANCZOS)
        self.photo_bgimg=ImageTk.PhotoImage(bgimg)

        l4=Label(self.root,image=self.photo_bgimg)
        l4.place(x=0,y=130,width=1500,height=800)

        #TITLE
        title=Label(l4,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",30,"bold"),bg="purple",fg="white")
        title.place(x=0,y=0,width=1500,height=45)

        #STUDENT
        img4=Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\17.jpg")
        img4=img4.resize((200,150),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(l4,image=self.photoimg4,cursor="hand2",command=self.stu_details)
        b1.place(x=150,y=100,width=200,height=150)
        but1=Button(l4,text="STUDENT DETAILS",font=("times new roman",12,"bold"),bg="purple",fg="white",cursor="hand2",command=self.stu_details)
        but1.place(x=150,y=250,width=200,height=30)

        #FACE RECOGINITION 
        img5=Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\1.jpg")
        img5=img5.resize((200,150),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(l4,image=self.photoimg5,cursor="hand2",command=self.open_fr)
        b2.place(x=500,y=100,width=200,height=150)
        but2=Button(l4,text="FACE RECOGNITION",font=("times new roman",12,"bold"),bg="purple",fg="white",cursor="hand2",command=self.open_fr)
        but2.place(x=500,y=250,width=200,height=30)

        #ATTENDANCE
        img6=Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\7.jpg")
        img6=img6.resize((200,150),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(l4,image=self.photoimg6,cursor="hand2",command=self.open_atten)
        b3.place(x=800,y=100,width=200,height=150)
        but3=Button(l4,text="ATTENDANCE",font=("times new roman",12,"bold"),bg="purple",fg="white",cursor="hand2",command=self.open_atten)
        but3.place(x=800,y=250,width=200,height=30)

        #CHAT BOT
        img10=Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\8.jpg")
        img10=img10.resize((200,150),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(l4,image=self.photoimg10,cursor="hand2",command=self.open_cb)
        b7.place(x=1100,y=100,width=200,height=150)
        but7=Button(l4,text="CHATBOT",font=("times new roman",12,"bold"),bg="purple",fg="white",cursor="hand2",command=self.open_cb)
        but7.place(x=1100,y=250,width=200,height=30)

        #TRAIN DATA
        img7=Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\9.jpg")
        img7=img7.resize((200,150),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(l4,image=self.photoimg7,cursor="hand2",command=self.open_train)
        b4.place(x=150,y=350,width=200,height=150)
        but4=Button(l4,text="TRAIN DATA",font=("times new roman",12,"bold"),bg="purple",fg="white",cursor="hand2",command=self.open_train)
        but4.place(x=150,y=500,width=200,height=30)

        #GALLERY
        img8=Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\23.png")
        img8=img8.resize((200,150),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(l4,image=self.photoimg8,cursor="hand2",command=self.open_gal)
        b5.place(x=500,y=350,width=200,height=150)
        but5=Button(l4,text="GALLERY",font=("times new roman",12,"bold"),bg="purple",fg="white",cursor="hand2",command=self.open_gal)
        but5.place(x=500,y=500,width=200,height=30)

        #DEVELOPER
        img9=Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\11.jfif")
        img9=img9.resize((200,150),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(l4,image=self.photoimg9,cursor="hand2",command=self.open_dev)
        b6.place(x=800,y=350,width=200,height=150)
        but6=Button(l4,text="DEVELOPER",font=("times new roman",12,"bold"),bg="purple",fg="white",cursor="hand2",command=self.open_dev)
        but6.place(x=800,y=500,width=200,height=30)
        
        #EXIT
        img11=Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\24.jpg")
        img11=img11.resize((200,150),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(l4,image=self.photoimg11,cursor="hand2",command=self.Exit)
        b8.place(x=1100,y=350,width=200,height=150)
        but8=Button(l4,text="EXIT",font=("times new roman",12,"bold"),bg="purple",fg="white",cursor="hand2",command=self.Exit)
        but8.place(x=1100,y=500,width=200,height=30)

    #FUNCTION
    def stu_details(self):
            self.new_win=Toplevel(self.root)
            self.app=Student(self.new_win)

    def open_gal(self):
        os.startfile("USER_IMAGES")

    def open_train(self):
            self.new_win=Toplevel(self.root)
            self.app=Train_Data(self.new_win)
        
    def open_fr(self):
            self.new_win=Toplevel(self.root)
            self.app=Face_Rec(self.new_win)      

    def open_atten(self):
            self.new_win=Toplevel(self.root)
            self.app=stu_attendance(self.new_win)
            
    def open_dev(self):
        self.new_win=Toplevel(self.root)
        self.app=dev(self.new_win)

    def open_cb(self):
        self.new_win=Toplevel(self.root)
        self.app=CB(self.new_win)
        
    def Exit(self):
        self.Exit=messagebox.askyesno("EXIT","ARE YOU SURE YOU WANT TO EXIT")
        if self.Exit>0:
            self.root.destroy()
        else:
            return
            
            
        
if __name__ == "__main__":
    root=Tk()
    obj=FRS(root)
    root.mainloop()
