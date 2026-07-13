from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import cv2
import numpy as np

class Train_Data:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("Train Data")
        self.root.wm_iconbitmap("face.ico")

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

        #IMAGES
        img4 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\34.png")
        img4 = img4.resize((500, 620), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        l4 = Label(self.root, image=self.photoimg4)
        l4.place(x=0, y=175, width=500, height=620)

        img5 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\44.png")
        img5 = img5.resize((500, 550), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        l5 = Label(self.root, image=self.photoimg5)
        l5.place(x=500, y=176, width=500, height=500)

        img6 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\30.jpg")
        img6 = img6.resize((500, 620), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        l6 = Label(self.root, image=self.photoimg6)
        l6.place(x=1000, y=175, width=500, height=620)


        

        # TITLE
        title = Label(self.root, text="TRAIN DATA", font=("times new roman", 30, "bold"), bg="purple", fg="white")
        title.place(x=0, y=130, width=1500, height=45)

        #BUTTON
        b = Button(self.root, text="TRAIN DATA", font=("times new roman", 15, "bold"), bg="purple", fg="white", command=self.train_classifier)
        b.place(x=500, y=678, width=500, height=100)

    # FUNCTION
    def train_classifier(self):
        img_dir = "USER_IMAGES"
        path = [os.path.join(img_dir, f) for f in os.listdir(img_dir)]
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")
            imgNP = np.array(img, "uint8")
            id = int(os.path.split(image)[1].split(".")[1])
            faces.append(imgNP)
            ids.append(id)
            cv2.imshow("TRAINING", imgNP)
            cv2.waitKey(1) == 13

        ids = np.array(ids)
        c = cv2.face.LBPHFaceRecognizer_create()
        c.train(faces, ids)
        c.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("SUCCESS", "ALL IMAGES TRAINED", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Train_Data(root)
    root.mainloop()
