from tkinter import *
from resizeimage import resizeimage
from tkinter.messagebox import showinfo
import qrcode
import os

class Window():
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("900x500+200+50")
        self.root.resizable(False, False)   

        self.head = Label(self.root, text="QR Code Generator", font="Helvetica 36 bold", bg="dark slate grey", fg="white", anchor="w")
        self.head.place(x=0, y=0, relwidth=1.0)

        # Employee Details Window
        self.emp_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.emp_frame.place(x=50, y=90, height=380, width=410)

        # Employee Title
        self.emp_title = Label(self.emp_frame, text="Employee Details", font="Helvetica 20 bold", bg="slate grey", fg="white")
        self.emp_title.pack(fill=X)

        # Employee Id
        self.emp_id_code = Label(self.emp_frame, text="Employee Id", bg="white", font="Helvetica 16").place(x=10, y=70)
        self.emp_id = StringVar()
        Entry(self.emp_frame, textvariable=self.emp_id, bg="lightyellow").place(x=170, y=72, height=25, width=220)

        # Employee Name
        self.emp_code_name = Label(self.emp_frame, text="Name", bg="white", font="Helvetica 16").place(x=10, y=110)
        self.emp_name = StringVar()
        Entry(self.emp_frame, textvariable=self.emp_name, bg="lightyellow").place(x=170, y=112, height=25, width=220)

        # Employee Department
        self.emp_code_depart = Label(self.emp_frame, text="Department", bg="white", font="Helvetica 16").place(x=10, y=150)
        self.emp_depart = StringVar()
        Entry(self.emp_frame, textvariable=self.emp_depart, bg="lightyellow").place(x=170, y=152, height=25, width=220)

        # Employee Designation
        emp_code_desig = Label(self.emp_frame, text="Designation", bg="white", font="Helvetica 16").place(x=10, y=190)
        self.emp_desig = StringVar()
        Entry(self.emp_frame, textvariable=self.emp_desig, bg="lightyellow").place(x=170, y=192, height=25, width=220)

        self.generate_btn = Button(self.emp_frame, text="Generate QR", font="Helvetica 14 bold", bg="cornflower blue", fg="white", command=self.generate)
        self.generate_btn.place(x=140, y=250, width=150)

        self.clear_btn = Button(self.emp_frame, text="Clear", font="Helvetica 14 bold", bg="light grey", fg="black", command=self.clear)
        self.clear_btn.place(x=300, y=250, width=90)

        # Success and Error Label
        self.msg_label = Label(self.emp_frame, text="Generate Your QR Code!", font="Helvetica 18 bold", bg="cornsilk3", fg="black")
        self.msg_label.pack(side=BOTTOM, fill=X)

        # ================================ QR Code Frame =====================================
        self.qr_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.qr_frame.place(x=510, y=90, height=380, width=340)

        Label(self.qr_frame, text="QR Code", font="Helvetica 20 bold", bg="slate grey", fg="white").pack(fill=X)

        self.qr_code_img = Label(self.qr_frame, text="No QR Code Available", font="Helvetica 14 bold")
        self.qr_code_img.place(x=60, y=80, height=250, width=220)

    def generate(self):
        name = self.emp_name.get()
        id1 = self.emp_id.get()
        depart = self.emp_depart.get()
        desig = self.emp_desig.get()
        
        if name=="" or id1=="" or depart=="" or desig=="":
            self.msg_label.config(text="All Fields Required", bg="red")
            showinfo("Improper Entry", "All Entry Fields Are Required to Be Filled.")
        else:
            qr_data = f"Employee Id : {id1}\nEmployee Name : {name}\nEmployee Department : {depart}\nEmployee Designation : {desig}"
            qr_code = qrcode.make(qr_data)
            # qr_code.show()

            if not(os.path.exists("./Employee_QR/")):
                os.mkdir("./Employee_QR/")

            qr_code = resizeimage.resize_cover(qr_code, [220, 250])
            qr_code.save("Employee_QR/EMP_"+(str(id1))+".png")
            self.img = PhotoImage(file="Employee_QR/EMP_"+(str(id1))+".png")
        
            self.qr_code_img.config(image=self.img)
            
            # Update Notification
            self.msg_label.config(text="QR Code Generated Successfully!", fg="green", bg="lightgrey") 

    def clear(self):
        self.emp_name.set("")
        self.emp_id.set("")
        self.emp_depart.set("")
        self.emp_desig.set("")
        self.msg_label.config(text="Generate Your QR Code!", font="Helvetica 18 bold", bg="cornsilk3", fg="black")
        self.qr_code_img.config(text="No QR Code Available", font="Helvetica 14 bold", image="")

root = Tk()
window = Window(root)
root.mainloop()
