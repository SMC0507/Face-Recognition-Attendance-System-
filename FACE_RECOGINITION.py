from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
from time import strftime
from datetime import datetime 

class Face_Rec:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("Face Recognition")
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

        # TITLE
        title = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 30, "bold"), bg="purple", fg="white")
        title.place(x=0, y=130, width=1500, height=45)

        # IMAGES

        img4 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\32.jpg")
        img4 = img4.resize((500, 620), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        l4 = Label(self.root, image=self.photoimg4)
        l4.place(x=0, y=175, width=500, height=620)

        img5 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\33.jpg")
        img5 = img5.resize((500, 550), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        l5 = Label(self.root, image=self.photoimg5)
        l5.place(x=500, y=175, width=500, height=500)

        img6 = Image.open(r"C:\Users\shaurya\OneDrive\Desktop\Minor Project\images\25.jpg")
        img6 = img6.resize((500, 620), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        l6 = Label(self.root, image=self.photoimg6)
        l6.place(x=1000, y=175, width=500, height=620)

        # BUTTON
        b = Button(self.root, text="FACE RECOGNITION", font=("times new roman", 15, "bold"), bg="purple", fg="white", command=self.face_rec)
        b.place(x=500, y=675, width=500, height=100)

    # FUNCTIONS
    def mark_attendance(self,e,n,d):
        with open ("ATTENDANCE_REPORT/Attendance.csv","r+",newline="\n") as f:
            myList=f.readlines()
            List=[]
            for line in myList:
                entry=line.split(",")
                List.append(entry[0])
            if ((e not in List) and (n not in List) and (d not in List)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H/%M/%S")
                f.writelines(f"\n{e},{n},{d},{dtString},{d1},Present")
                
            
            
    
    def face_rec(self):
        def boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbours)
            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_img[y:y + w, x:x + h])
                confidence = int((100 * (1 - predict / 300)))
                conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="frs")
                cur = conn.cursor()

                cur.execute("select name from student where enrolment_number=" + str(id))
                n = cur.fetchone()
                n = "+".join(map(str,n)) if n else "Unknown"

                cur.execute("select enrolment_number from student where enrolment_number=" + str(id))
                e = cur.fetchone()
                e = "+".join(map(str,e)) if e else "Unknown"

                cur.execute("select department from student where enrolment_number=" + str(id))
                d = cur.fetchone()
                d = "+".join(map(str,d)) if d else "Unknown"

                if confidence > 75:
                    cv2.putText(img, f"Enrolment Number : {e}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name : {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department : {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(e,n,d)
                    
                else:
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)


                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("FACE RECOGNITION", img)
            cv2.moveWindow("FACE RECOGNITION",x=450,y=50)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Rec(root)
    root.mainloop()
