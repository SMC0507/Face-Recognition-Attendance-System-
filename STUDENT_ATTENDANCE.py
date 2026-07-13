from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import os
import csv

mydata = []

class stu_attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("STUDENT ATTENDANCE")
        self.root.wm_iconbitmap("face.ico")

        # VARIABLES
        self.var_en = StringVar()
        self.var_name = StringVar()
        self.var_dept = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()

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
        title = Label(self.root, text="STUDENT ATTENDANCE", font=("times new roman", 30, "bold"), bg="purple", fg="white")
        title.place(x=0, y=130, width=1500, height=45)

        # MAIN FRAME
        main_frame = LabelFrame(self.root, bd=4, bg="white")
        main_frame.place(x=0, y=175, width=1500, height=600)

        # LEFT FRAME
        l_frame = LabelFrame(main_frame, bd=2, bg="white", text="STUDENT ATTENDANCE DETAILS", font=("times new roman", 12, "bold"))
        l_frame.place(x=10, y=0, width=730, height=580)
        
        # RIGHT FRAME
        r_frame = LabelFrame(main_frame, bd=2, bg="white", text="STUDENT ATTENDANCE INFORMATION", font=("times new roman", 12, "bold"))
        r_frame.place(x=755, y=0, width=725, height=580)

        # DETAIL FRAME
        d_frame = LabelFrame(l_frame, bg="beige")
        d_frame.place(x=8, y=50, width=710, height=440)

        eno = Label(d_frame, text="ENROLMENT NUMBER : ", font=("times new roman", 12, "bold"), bg="white", width=21)
        eno.grid(row=0, column=0, padx=10, pady=10)
        e1 = ttk.Entry(d_frame, width=50, font=("times new roman", 12, "bold"), textvariable=self.var_en)
        e1.grid(row=0, column=5, padx=10, pady=10)

        name = Label(d_frame, text="NAME : ", font=("times new roman", 12, "bold"), bg="white", width=21)
        name.grid(row=1, column=0, padx=10, pady=10)
        e2 = ttk.Entry(d_frame, width=50, font=("times new roman", 12, "bold"), textvariable=self.var_name)
        e2.grid(row=1, column=5, padx=10, pady=10)
        
        dept = Label(d_frame, text="DEPARTMENT: ", font=("times new roman", 12, "bold"), bg="white", width=21)
        dept.grid(row=2, column=0, padx=10, pady=10)
        e3 = ttk.Entry(d_frame, width=50, font=("times new roman", 12, "bold"), textvariable=self.var_dept)
        e3.grid(row=2, column=5, padx=10, pady=10)
        
        time = Label(d_frame, text="TIME: ", font=("times new roman", 12, "bold"), bg="white", width=21)
        time.grid(row=3, column=0, padx=10, pady=10)
        e4 = ttk.Entry(d_frame, width=50, font=("times new roman", 12, "bold"), textvariable=self.var_time)
        e4.grid(row=3, column=5, padx=10, pady=10)

        date = Label(d_frame, text="DATE: ", font=("times new roman", 12, "bold"), bg="white", width=21)
        date.grid(row=4, column=0, padx=10, pady=10)
        e5 = ttk.Entry(d_frame, width=50, font=("times new roman", 12, "bold"), textvariable=self.var_date)
        e5.grid(row=4, column=5, padx=10, pady=10)
        
        atten = Label(d_frame, text="ATTENDANCE: ", font=("times new roman", 12, "bold"), bg="white", width=21)
        atten.grid(row=5, column=0, padx=10, pady=10)
        combo = ttk.Combobox(d_frame, font=("times new roman", 10, "bold"), width=50, state="readonly", textvariable=self.var_attendance)
        combo['values'] = ("STATUS", "PRESENT", "ABSENT")
        combo.current(0)
        combo.grid(row=5, column=5, padx=5, pady=5)
        
        b1 = Button(d_frame, text="IMPORT CSV", font=("times new roman", 10, "bold"), bg="purple", width=23, fg="white", command=self.importCSV)
        b1.place(x=10, y=360)

        b2 = Button(d_frame, text="EXPORT CSV", font=("times new roman", 10, "bold"), bg="purple", width=23, fg="white", command=self.exportCSV)
        b2.place(x=160, y=360)
        
        b3 = Button(d_frame, text="UPDATE", font=("times new roman", 10, "bold"), bg="purple", width=23, fg="white", command=self.update_data)
        b3.place(x=310, y=360)

        b4 = Button(d_frame, text="RESET", font=("times new roman", 10, "bold"), bg="purple", width=23, fg="white", command=self.reset)
        b4.place(x=460, y=360)

        # TABLE FRAME
        t_frame = LabelFrame(r_frame, bg="beige")
        t_frame.place(x=8, y=50, width=710, height=440)

        scroll_x = ttk.Scrollbar(t_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(t_frame, orient=VERTICAL)

        self.stu_table = ttk.Treeview(t_frame, column=("ENROLMENT NUMBER", "NAME", "DEPARTMENT", "TIME", "DATE", "ATTENDANCE"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.stu_table.xview)
        scroll_y.config(command=self.stu_table.yview)

        self.stu_table.heading("ENROLMENT NUMBER", text="ENROLMENT NUMBER")
        self.stu_table.heading("NAME", text="NAME")
        self.stu_table.heading("DEPARTMENT", text="DEPARTMENT")
        self.stu_table.heading("TIME", text="TIME")
        self.stu_table.heading("DATE", text="DATE")
        self.stu_table.heading("ATTENDANCE", text="ATTENDANCE")
        self.stu_table["show"] = "headings"

        self.stu_table.pack(side=TOP, fill=BOTH, expand=1)
        self.stu_table.bind("<ButtonRelease>", self.get_cur)

    # FUNCTIONS
    def fetch_data(self, rows):
        self.stu_table.delete(*self.stu_table.get_children())
        for i in rows:
            self.stu_table.insert("", END, values=i)

    def importCSV(self):
        global mydata
        mydata.clear()
        f = filedialog.askopenfilename(initialdir=os.getcwd(), title="OPEN CSV", filetypes=(("CSV File", "*csv"), ("All Files", "*.*")), parent=self.root)
        with open(f) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)
            
    def exportCSV(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("ERROR", "NO DATA FOUND", parent=self.root)
            f = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="OPEN CSV", filetypes=(("CSV File", "*csv"), ("All Files", "*.*")), parent=self.root)
            with open(f, mode="w", newline="") as myfile:
                csvwrite = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    csvwrite.writerow(i)
                messagebox.showinfo("SUCCESS", "DATA EXPORTED SUCCESSFULLY", parent=self.root)
        except Exception as e:
            messagebox.showerror("ERROR", f"{str(e)}", parent=self.root)

    def get_cur(self, event=""):
        cursor_row = self.stu_table.focus()
        content = self.stu_table.item(cursor_row)
        data = content['values']
        
        if data:
            self.var_en.set(data[0])
            self.var_name.set(data[1])
            self.var_dept.set(data[2])
            self.var_time.set(data[3])
            self.var_date.set(data[4])
            self.var_attendance.set(data[5])
        else:
            messagebox.showerror("ERROR", "No data available for the selected row.", parent=self.root)

    def update_data(self):
        if not self.var_en.get() or not self.var_name.get() or not self.var_dept.get() or not self.var_time.get() or not self.var_date.get() or not self.var_attendance.get():
            messagebox.showerror("ERROR", "All fields are required", parent=self.root)
            return

        selected = self.stu_table.focus()
        if selected:
            index = self.stu_table.index(selected)
            mydata[index] = [self.var_en.get(), self.var_name.get(), self.var_dept.get(), self.var_time.get(), self.var_date.get(), self.var_attendance.get()]
            self.fetch_data(mydata)
            messagebox.showinfo("SUCCESS", "Record updated successfully", parent=self.root)
        else:
            messagebox.showerror("ERROR", "No record selected", parent=self.root)

    def reset(self):
        self.var_en.set("")
        self.var_name.set("")
        self.var_dept.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = stu_attendance(root)
    root.mainloop()
