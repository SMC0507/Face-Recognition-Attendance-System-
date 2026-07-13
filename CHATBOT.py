from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class CB:
    def __init__ (self, root):
        self.root = root
        self.root.geometry("400x550+600+0")
        self.root.title("Chatbot")
        self.root.bind("<Return>",self.enter)
        self.root.wm_iconbitmap("face.ico")

        # TOP FRAME
        t_frame = LabelFrame(self.root, bd=4, bg="purple")
        t_frame.place(x=0, y=0, width=400, height=100)
        
        img = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\36.jpg")
        img = img.resize((90, 90), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        l = Label(t_frame, image=self.photoimg)
        l.place(x=0, y=0, width=90, height=90)

        l1 = Label(t_frame, text="CHATBOT", font=("times new roman", 25, "bold"), fg="white", bg="purple")
        l1.place(x=85, y=0, width=300, height=90)

        # MIDDLE FRAME
        m_frame = LabelFrame(self.root, bd=10, bg="white")
        m_frame.place(x=0, y=100, width=400, height=350)

        scroll_y = ttk.Scrollbar(m_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.t = Text(m_frame, width=50, height=30, bd=3, font=("times new roman", 15, "bold"), fg="black", relief=RAISED, yscrollcommand=scroll_y.set)
        self.t.pack()
        scroll_y.config(command=self.t.yview)

        # BOTTOM FRAME
        b_frame = LabelFrame(self.root, bd=4, bg="purple")
        b_frame.place(x=0, y=450, width=400, height=100)

        l2 = Label(b_frame, text="TYPE HERE", font=("times new roman", 10, "bold"), fg="black", bg="#fb8500")
        l2.place(x=10, y=10, width=80, height=40)

        self.e = ttk.Entry(b_frame, font=("times new roman", 12, "bold"))
        self.e.place(x=90, y=10, width=240, height=40)

        img2 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\37.jpg")
        img2 = img2.resize((50, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        self.b = Button(b_frame, text="CLEAR", font=("times new roman", 15, "bold"), fg="black", bg="#8ecae6", cursor="hand2", command=self.clear)
        self.b.place(x=10, y=52, width=370, height=30)

        self.b1 = Button(b_frame, image=self.photoimg2, cursor="hand2", command=self.send)
        self.b1.place(x=330, y=10, width=50, height=40)

    # FUNCTIONS
    def send(self):
        user_message = self.e.get().strip()
        if user_message:
            self.t.insert(END, "\n\n" + "YOU : " + user_message)
            self.e.delete(0, END)
            self.t.yview(END)
            
            # Check for specific user questions
            if user_message.lower() == "hello":
                bot_response = "HI"
            elif user_message.lower() == "what is machine learning":
                bot_response = "Machine learning is a branch of artificial intelligence (AI) focused on building applications that learn from data and improve their accuracy over time without being programmed to do so."
            elif user_message.lower() == "how do i use the face recognition system":
                bot_response = "To use a face recognition system, you need to have a camera to capture the image, software to process the image, and a database of known faces to compare against. The system will match the captured image with the database to identify the person."
            elif user_message.lower() == "bye":
                bot_response = "Goodbye! Have a great day!"
            else:
                bot_response = "Sorry, I didn't get it."
            
            self.t.insert(END, "\n\n" + "BOT : " + bot_response)
                
    def clear(self):
        self.t.delete(1.0, END)
        self.e.delete(0, END)

    def enter(self, event):
        self.send()

if __name__ == "__main__":
    root = Tk()
    obj = CB(root)
    root.mainloop()
