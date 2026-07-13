from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("Student")
        self.root.wm_iconbitmap("face.ico")

        #VARIABLES
        self.var_dept=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_en=StringVar()
        self.var_name=StringVar()
        self.var_gen=StringVar()
        self.var_dob=StringVar()
        self.var_pn=StringVar()
        self.var_email=StringVar()
        self.var_cc=StringVar()
        self.var_search=StringVar()
        self.var_searchbar=StringVar()
        self.var_r = StringVar()
        
        
        
        # TOP IMAGES
        img1 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\3.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        l1 = Label(self.root, image=self.photoimg1)
        l1.place(x=0, y=0, width=500, height=130)

        img2 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\21.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        l2 = Label(self.root, image=self.photoimg2)
        l2.place(x=500, y=0, width=500, height=130)

        img3 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\4.jpg")
        img3 = img3.resize((500, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        l3 = Label(self.root, image=self.photoimg3)
        l3.place(x=1000, y=0, width=500, height=130)

        # TITLE
        title = Label(self.root, text="STUDENT DETAILS", font=("times new roman", 30, "bold"), bg="purple", fg="white")
        title.place(x=0, y=130, width=1500, height=45)

        # MAIN FRAME
        main_frame = LabelFrame(self.root, bd=4, bg="white")
        main_frame.place(x=0, y=175, width=1500, height=600)

        # LEFT FRAME
        l_frame = LabelFrame(main_frame, bd=2, bg="white", text="STUDENT DETAILS", font=("times new roman", 12, "bold"))
        l_frame.place(x=10, y=0, width=730, height=580)
        
        # RIGHT FRAME
        r_frame = LabelFrame(main_frame, bd=2, bg="white", text="STUDENT INFORMATION", font=("times new roman", 12, "bold"))
        r_frame.place(x=755, y=0, width=725, height=580)

        # COURSE FRAME
        c_frame = LabelFrame(l_frame, bg="beige")
        c_frame.place(x=8, y=5, width=710, height=100)

        dept = Label(c_frame, text="DEPARTMENT : ", font=("times new roman", 10, "bold"),bg="white",width=21)
        dept.grid(row=0, column=0, padx=5, pady=5)

        combo = ttk.Combobox(c_frame, font=("times new roman", 10, "bold"), width=50, state="readonly",textvariable=self.var_dept)
        combo['values'] = ("SELECT DEPARTMENT", "BCA", "BBA(G)", "BBA(B&I)", "BA-LLB", "BBA-LLB", "BTECH", "BCOM", "BED")
        combo.current(0)
        combo.grid(row=0, column=1, padx=5, pady=5)

        year = Label(c_frame, text="YEAR : ", font=("times new roman", 10, "bold"),bg="white",width=21)
        year.grid(row=1, column=0, padx=5, pady=5)

        combo2 = ttk.Combobox(c_frame, font=("times new roman", 10, "bold"), width=50, state="readonly",textvariable=self.var_year)
        combo2['values'] = ("SELECT YEAR", "1", "2", "3", "4", "5")
        combo2.current(0)
        combo2.grid(row=1, column=1, padx=5, pady=5)

        sem = Label(c_frame, text="SEMESTER : ", font=("times new roman", 10, "bold"),bg="white",width=21)
        sem.grid(row=2, column=0, padx=5, pady=5)

        combo3 = ttk.Combobox(c_frame, font=("times new roman", 10, "bold"), width=50, state="readonly",textvariable=self.var_sem)
        combo3['values'] = ("SELECT SEMESTER", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        combo3.current(0)
        combo3.grid(row=2, column=1, padx=5, pady=5)

        # DETAIL FRAME
        d_frame = LabelFrame(l_frame, bg="beige")
        d_frame.place(x=8, y=110, width=710, height=440)

        eno = Label(d_frame, text="ENROLMENT NUMBER : ", font=("times new roman", 12, "bold"), bg="white", width=21)
        eno.grid(row=0, column=0, padx=10, pady=10)
        e1 = ttk.Entry(d_frame, width=50, font=("times new roman", 12, "bold"),textvariable=self.var_en)
        e1.grid(row=0, column=5, padx=10, pady=10)

        name = Label(d_frame, text="NAME : ", font=("times new roman", 12, "bold"), bg="white", width=21)
        name.grid(row=1, column=0, padx=10, pady=10)
        e2 = ttk.Entry(d_frame, width=50, font=("times new roman", 12, "bold"),textvariable=self.var_name)
        e2.grid(row=1, column=5, padx=10, pady=10)
        
        gen = Label(d_frame, text="GENDER: ", font=("times new roman", 12, "bold"), bg="white", width=21)
        gen.grid(row=2, column=0, padx=10, pady=10)
        combo = ttk.Combobox(d_frame, width=50, font=("times new roman", 12, "bold"),textvariable=self.var_gen,state="readonly")
        combo["values"]=("SELECT GENDER","MALE","FEMALE","OTHER")
        combo.current(0)
        combo.grid(row=2, column=5, padx=10, pady=10)
        
        dob = Label(d_frame, text="DOB : ", font=("times new roman", 12, "bold"), bg="white", width=21)
        dob.grid(row=3, column=0, padx=10, pady=5)
        e4 = ttk.Entry(d_frame, width=50, font=("times new roman", 12, "bold"),textvariable=self.var_dob)
        e4.grid(row=3, column=5, padx=10, pady=10)
    
        pno = Label(d_frame, text="PHONE NUMBER : ", font=("times new roman", 12, "bold"), bg="white", width=21)
        pno.grid(row=4, column=0, padx=10, pady=10)
        e5 = ttk.Entry(d_frame, width=50, font=("times new roman", 12, "bold"),textvariable=self.var_pn)
        e5.grid(row=4, column=5, padx=10, pady=10)
        
        email = Label(d_frame, text="EMAIL : ", font=("times new roman", 12, "bold"), bg="white", width=21)
        email.grid(row=5, column=0, padx=10, pady=10)
        e6 = ttk.Entry(d_frame, width=50, font=("times new roman", 12, "bold"),textvariable=self.var_email)
        e6.grid(row=5, column=5, padx=10, pady=10)

        cc = Label(d_frame, text="CLASS COORDINATOR : ", font=("times new roman", 12, "bold"), bg="white", width=21)
        cc.grid(row=6, column=0, padx=10, pady=10)
        e7 = ttk.Entry(d_frame, width=50, font=("times new roman", 12, "bold"),textvariable=self.var_cc)
        e7.grid(row=6, column=5, padx=10, pady=10)

        r1 = ttk.Radiobutton(d_frame, text="TAKE PHOTO SAMPLE",variable=self.var_r,width=29, value="yes")
        r1.grid(row=7, column=0, padx=10, pady=10)

        r2 = ttk.Radiobutton(d_frame, text="NO PHOTO SAMPLE",variable=self.var_r, width=64, value="no")
        r2.grid(row=7, column=5, padx=10, pady=10)
        
        b1 = Button(d_frame, text="SAVE", font=("times new roman", 10, "bold"), bg="purple", width=23, fg="white",command=self.add_data)
        b1.place(x=10,y=360)

        b2 = Button(d_frame, text="UPDATE", font=("times new roman", 10, "bold"), bg="purple", width=23, fg="white",command=self.update_data)
        b2.place(x=160,y=360)
        
        b3 = Button(d_frame, text="DELETE", font=("times new roman", 10, "bold"), bg="purple", width=23, fg="white",command=self.delete_data)
        b3.place(x=310,y=360)

        b4 = Button(d_frame, text="RESET", font=("times new roman", 10, "bold"), bg="purple", width=23, fg="white",command=self.reset_data)
        b4.place(x=460,y=360)

        b5 = Button(d_frame, text="TAKE SAMPLE PHOTO", font=("times new roman", 10, "bold"), bg="purple", width=87, fg="white",command=self.generate_data)
        b5.place(x=10,y=400)



        #SELECT FRAME
        s_frame = LabelFrame(r_frame, bg="beige")
        s_frame.place(x=8, y=5, width=710, height=100)

        search = Label(s_frame, text="SEARCH BY : ", font=("times new roman", 10, "bold"),bg="white",width=21)
        search.grid(row=0, column=0, padx=5, pady=5)

        combo = ttk.Combobox(s_frame, font=("times new roman", 10, "bold"), width=50, state="readonly",textvariable=self.var_search)
        combo['values'] = ("SELECT ","ENROLMENT NUMBER","PHONE NUMBER")
        combo.current(0)
        combo.grid(row=0, column=1, padx=5, pady=5)

        e = ttk.Entry(s_frame, width=21, font=("times new roman", 12, "bold"),textvariable=self.var_searchbar)
        e.grid(row=1, column=0, padx=10, pady=10)

        but1 = Button(s_frame, text="SEARCH", font=("times new roman", 10, "bold"), bg="purple", width=10, fg="white",command=self.search_data)
        but1.place(x=200,y=40)

        but2 = Button(s_frame, text="SHOW ALL", font=("times new roman", 10, "bold"), bg="purple", width=10, fg="white",command=self.show_all)
        but2.place(x=300,y=40)

        #TABLE FRAME
        t_frame = LabelFrame(r_frame, bg="beige")
        t_frame.place(x=8, y=110, width=710, height=440)

        scroll_x=ttk.Scrollbar(t_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(t_frame,orient=VERTICAL)

        self.stu_table=ttk.Treeview(t_frame,column=("DEPARTMENT","YEAR","SEMESTER","ENROLMENT NUMBER","NAME","GENDER","DOB","PHONE NUMBER","EMAIL","CLASS COORDINATOR"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.stu_table.xview)
        scroll_y.config(command=self.stu_table.yview)

        self.stu_table.heading("DEPARTMENT",text="DEPARTMENT")
        self.stu_table.heading("YEAR",text="YEAR")
        self.stu_table.heading("SEMESTER",text="SEMESTER")
        self.stu_table.heading("ENROLMENT NUMBER",text="ENROLMENT NUMBER")
        self.stu_table.heading("NAME",text="NAME")
        self.stu_table.heading("GENDER",text="GENDER")
        self.stu_table.heading("DOB",text="DOB")
        self.stu_table.heading("PHONE NUMBER",text="PHONE NUMBER")
        self.stu_table.heading("EMAIL",text="EMAIL")
        self.stu_table.heading("CLASS COORDINATOR",text="CLASS COORDINATOR")
        self.stu_table["show"]="headings"

        self.stu_table.pack(side=TOP, fill=BOTH, expand=1)
        self.stu_table.bind("<ButtonRelease>",self.get_cur)
        self.fetch_data()

    #FUNCTIONS
    def add_data(self):
        if self.var_dept.get()=="SELECT DEPARTMENT" or self.var_year.get()=="SELECT YEAR" or self.var_sem.get()=="SELECT SEMESTER" or self.var_en.get()=="" or self.var_name.get()=="" or self.var_gen.get()=="" or self.var_dob.get()=="" or self.var_pn.get()=="" or self.var_email.get()=="" or self.var_cc.get()=="":
            messagebox.showerror("ERROR","ALL FIELDS REQUIRED",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="frs")
                cur=conn.cursor()
                cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dept.get(),
                                                                                         self.var_year.get(),
                                                                                         self.var_sem.get(),
                                                                                         self.var_en.get(),
                                                                                         self.var_name.get(),
                                                                                         self.var_gen.get(),
                                                                                         self.var_dob.get(),
                                                                                         self.var_pn.get(),
                                                                                         self.var_email.get(),
                                                                                         self.var_cc.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("SUCCESS","STUDENT DETAILS ADDED SUCCESSFULLY",parent=self.root)
            except Exception as e:
                messagebox.showerror("ERROR",f"{str(e)}",parent=self.root)
                
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="frs")
         cur=conn.cursor()
         cur.execute("select * from student")
         data=cur.fetchall()
         if len(data)!=0:
             self.stu_table.delete(*self.stu_table.get_children())
             for i in data:
                 self.stu_table.insert("",END,values=i)
             conn.commit()
         conn.close()
         
    def get_cur(self, event=""):
        cursor_row = self.stu_table.focus()
        content = self.stu_table.item(cursor_row)
        data = content['values']
        
        if data:
            self.var_dept.set(data[0])
            self.var_year.set(data[1])
            self.var_sem.set(data[2])
            self.var_en.set(data[3])
            self.var_name.set(data[4])
            self.var_gen.set(data[5])
            self.var_dob.set(data[6])
            self.var_pn.set(data[7])
            self.var_email.set(data[8])
            self.var_cc.set(data[9])
        else:
            messagebox.showerror("ERROR", "No data available for the selected row.", parent=self.root)


    def update_data(self):
        if self.var_dept.get()=="SELECT DEPARTMENT" or self.var_year.get()=="SELECT YEAR" or self.var_sem.get()=="SELECT SEMESTER" or self.var_en.get()=="SELECT GENDER" or self.var_name.get()=="" or self.var_gen.get()=="" or self.var_dob.get()=="" or self.var_pn.get()=="" or self.var_email.get()=="" or self.var_cc.get()=="":
            messagebox.showerror("ERROR","ALL FIELDS REQUIRED",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("UPDATE","DO YOU WANT TO UPDATE THE VALUES ?",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="frs")
                    cur=conn.cursor()
                    cur.execute("update student set department=%s,year=%s,semester=%s,enrolment_number=%s,name=%s,gender=%s,dob=%s,phone_number=%s,email=%s,class_coordinator=%s",(self.var_dept.get(),
                                                                                                                                                                                     self.var_year.get(),
                                                                                                                                                                                     self.var_sem.get(),
                                                                                                                                                                                     self.var_en.get(),
                                                                                                                                                                                     self.var_name.get(),
                                                                                                                                                                                     self.var_gen.get(),
                                                                                                                                                                                     self.var_dob.get(),
                                                                                                                                                                                     self.var_pn.get(),
                                                                                                                                                                                     self.var_email.get(),
                                                                                                                                                                                     self.var_cc.get()))

                else:
                     if not update:
                         return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("SUCCESS","UPDATED SUCCESSFULLY",parent=self.root)
            except Exception as e:
                messagebox.showerror("ERROR",f"{str(e)}",parent=self.root)

    def delete_data(self):
        if self.var_en=="":
            messagebox.error("ERROR","ENROLMENT NUMBER IS REQUIRED",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("DELETE","DO YOU WANT TO DELETE THE VALUES ?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="frs")
                    cur=conn.cursor()
                    sql=("delete from student where enrolment_number=%s")
                    val=(self.var_en.get(),)
                    cur.execute(sql,val)

                else:
                     if not delete:
                         return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("DELETE","DELETED SUCCESSFULLY",parent=self.root)
            except Exception as e:
                messagebox.showerror("ERROR",f"{str(e)}",parent=self.root)
                
    def reset_data(self):
        self.var_dept.set("SELECT DEPARTMENT")
        self.var_year.set("SELECT YEAR")
        self.var_sem.set("SELECT SEMESTER")
        self.var_en.set("")
        self.var_name.set("")
        self.var_gen.set("SELECT GENDER")
        self.var_dob.set("")
        self.var_pn.set("")
        self.var_email.set("")
        self.var_cc.set("")

    def generate_data(self):
        if self.var_dept.get() == "SELECT DEPARTMENT" or self.var_year.get() == "SELECT YEAR" or self.var_sem.get() == "SELECT SEMESTER" or self.var_en.get() == "SELECT GENDER" or self.var_name.get() == "" or self.var_gen.get() == "" or self.var_dob.get() == "" or self.var_pn.get() == "" or self.var_email.get() == "" or self.var_cc.get() == "":
            messagebox.showerror("ERROR", "ALL FIELDS REQUIRED", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="admin", database="frs")
                cur = conn.cursor()
                cur.execute("select * from student")
                data = cur.fetchall()
                id = 0
                for i in data:
                    id += 1

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped
                    return None

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if not ret:
                        continue
                    cropped_face = face_cropped(my_frame)
                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        path = "USER_IMAGES/user." + str(id) + "." + str(img_id) + ".jpeg"
                        cv2.imwrite(path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("RESULT", "GENERATING DATA SETS COMPLETED", parent=self.root)

            except Exception as e:
                messagebox.showerror("ERROR", f"{str(e)}", parent=self.root)



    def search_data(self):
        if self.var_search.get() == "SELECT":
            messagebox.showerror("ERROR", "SELECT SEARCH OPTION", parent=self.root)
            
        if self.var_searchbar.get() == "":
            messagebox.showerror("ERROR", "SEARCH BAR IS EMPTY", parent=self.root)

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="admin", database="frs")
            cur = conn.cursor()
            
            if self.var_search.get() == "ENROLMENT NUMBER":
                query = "SELECT * FROM student WHERE enrolment_number = %s"
                value = (self.var_searchbar.get(),)
            elif self.var_search.get() == "PHONE NUMBER":
                query = "SELECT * FROM student WHERE phone_number = %s"
                value = (self.var_searchbar.get(),)
            else:
                messagebox.showerror("ERROR", "INVALID SEARCH OPTION", parent=self.root)

            cur.execute(query, value)
            data = cur.fetchall()
            
            if len(data) != 0:
                self.stu_table.delete(*self.stu_table.get_children())
                for i in data:
                    self.stu_table.insert("", END, values=i)
            else:
                messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.root)

            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("ERROR", f"{str(e)}", parent=self.root)

    def show_all(self):
        self.fetch_data()

        
        

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
