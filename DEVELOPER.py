from tkinter import *
from tkinter import ttk,messagebox,filedialog
from PIL import Image, ImageTk

class dev:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("DEVELOPER")
        self.root.wm_iconbitmap("face.ico")

        #LEFT FRAME
        l_frame = LabelFrame(self.root,bg="purple")
        l_frame.place(x=10, y=10, width=500, height=780)

        f1= LabelFrame(l_frame)
        f1.place(x=10, y=10, width=475, height=370)

        f2= LabelFrame(l_frame)
        f2.place(x=10, y=390, width=475, height=370)

        l=Label(f2,text="SUMMARY",font=("arial",15,"bold"),bg="#c285d4",fg="white")
        l.place(x=0,y=0,width=470,height=50)

        img1 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\me.jpg")
        img1 = img1.resize((475, 370), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        i = Label(f1, image=self.photoimg1)
        i.place(x=0, y=0, width=475, height=370)

        s=Label(f2,text="Hello I'm shaurya , a passionate BCA student currently pursuing my degree at Maharaja Surajmal Institute. My academic journey is fueled by my curiosity for all things tech, and I'm excited to be on the path of exploring the world of computer applications.", wraplength=450, justify=LEFT,font=("arial",15,"bold"),fg="black")
        s.place(x=0,y=50,width=475,height=270)
        
        #MIDDLE FRAME
        c_frame = LabelFrame(self.root,bg="purple")
        c_frame.place(x=510, y=10, width=500, height=780)

        f3= LabelFrame(c_frame,bg="white")
        f3.place(x=10, y=10, width=475, height=270)

        l2=Label(f3,text="CONTACT",font=("arial",15,"bold"),bg="#c285d4",fg="white")
        l2.place(x=0,y=0,width=470,height=50)

        img2 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\tele.webp")
        img2 = img2.resize((60,60), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        i2 = Label(f3, image=self.photoimg2)
        i2.place(x=30, y=80, width=60, height=60)

        tele=Label(f3,text="+91 9210482055",font=("arial",10,"bold"),bg="white",fg="black")
        tele.place(x=100,y=100)

        img3 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\email.jpg")
        img3 = img3.resize((60,60), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        i3= Label(f3, image=self.photoimg3)
        i3.place(x=30, y=130, width=60, height=60)

        email=Label(f3,text="shaurya03421202023@msijanakpuri.com",font=("arial",10,"bold"),bg="white",fg="black")
        email.place(x=100,y=145)

        img4 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\linkedin.webp")
        img4 = img4.resize((60,60), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        i4 = Label(f3, image=self.photoimg4)
        i4.place(x=30, y=180, width=60, height=60)

        linkedin=Label(f3,text="www.linkedin.com/in/shaurya--490311291",font=("arial",10,"bold"),bg="white",fg="black")
        linkedin.place(x=100,y=197)

        

        f4= LabelFrame(c_frame,bg="white")
        f4.place(x=10, y=290, width=475, height=470)

        l3=Label(f4,text="EDUCATION",font=("arial",15,"bold"),bg="#c285d4",fg="white")
        l3.place(x=0,y=0,width=470,height=50)

        img5 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\msi.jpg")
        img5 = img5.resize((60,60), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        i4 = Label(f4, image=self.photoimg5)
        i4.place(x=30, y=80, width=60, height=60)

        msi=Label(f4,text="Persuing BCA from Maharaja Surajmal Institute\n(Batch 2025)",justify=LEFT,font=("arial",10,"bold"),fg="black",bg="white")
        msi.place(x=120,y=80,width=300,height=50)

        img6 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\mss.jpg")
        img6 = img6.resize((60,60), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        i5= Label(f4, image=self.photoimg6)
        i5.place(x=30, y=200, width=60, height=60)

        mss=Label(f4,text="Completed Senior Seconday from Manav Sthali\nSchool (Batch 2022)",font=("arial",10,"bold"),fg="black",bg="white",justify=LEFT)
        mss.place(x=100,y=210,width=320,height=50)

        img7 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\mss.jpg")
        img7 = img7.resize((60,60), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        i6 = Label(f4, image=self.photoimg7)
        i6.place(x=30, y=340, width=60, height=60)

        mss2=Label(f4,text="Completed Marticulation from Manav Sthali\nSchool (Batch 2020",font=("arial",10,"bold"),fg="black",bg="white",justify=LEFT)
        mss2.place(x=80,y=340,width=320,height=50)


        

        #RIGHT FRAME
        r_frame = LabelFrame(self.root,bg="purple")
        r_frame.place(x=1010, y=10, width=490, height=780)

        f5= LabelFrame(r_frame,bg="white")
        f5.place(x=10, y=10, width=465, height=370)

        l4=Label(f5,text="INTERESTS",font=("arial",15,"bold"),bg="#c285d4",fg="white")
        l4.place(x=0,y=0,width=460,height=50)

        img8 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\music.webp")
        img8 = img8.resize((100,100), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        i7= Label(f5, image=self.photoimg8)
        i7.place(x=190, y=100, width=100, height=100)

        img9 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\coding.jpg")
        img9 = img9.resize((100,100), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        i8 = Label(f5, image=self.photoimg9)
        i8.place(x=200, y=230, width=100, height=100)
        


        f6= LabelFrame(r_frame,bg="white")
        f6.place(x=10, y=390, width=465, height=370)

        l5=Label(f6,text="SKILLS",font=("arial",15,"bold"),bg="#c285d4",fg="white")
        l5.place(x=0,y=0,width=460,height=50)

        img10 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\c.png")
        img10= img10.resize((65,70), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        i9 = Label(f6, image=self.photoimg10)
        i9.place(x=80, y=82, width=65, height=70)

        img11 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\cpp.jpg")
        img11= img11.resize((110,80), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        i10 = Label(f6, image=self.photoimg11)
        i10.place(x=190, y=80, width=110, height=80)

        img12 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\python.jpg")
        img12= img12.resize((105,85), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        i11 = Label(f6, image=self.photoimg12)
        i11.place(x=300, y=80, width=105, height=85)

        img13 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\java.png")
        img13= img13.resize((80,100), Image.LANCZOS)
        self.photoimg13 = ImageTk.PhotoImage(img13)

        i12 = Label(f6, image=self.photoimg13)
        i12.place(x=120, y=200, width=80, height=100)

        img14 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\php.png")
        img14= img14.resize((150,70), Image.LANCZOS)
        self.photoimg14 = ImageTk.PhotoImage(img14)

        i13 = Label(f6, image=self.photoimg14)
        i13.place(x=250, y=210, width=150, height=70)



if __name__ == "__main__":
    root = Tk()
    obj = dev(root)
    root.mainloop()
