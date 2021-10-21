from tkinter import *
import qrcode
from PIL import ImageTk,Image
from resizeimage import resizeimage


class QR_generator:
    def Clear(self):
        self.Employee_name.set(" ")
        self.Employee_department.set(" ")
        self.Employee_id.set(" ")
        self.Employee_designation.set(" ")
        self.msg = " "
        self.msg_lable.config(text=self.msg)
        self.image = " "


    def generate(self):
        if self.Employee_id.get() == " " and self.Employee_name.get() == " " and self.Employee_designation.get() == " " and self.Employee_department.get() == " ":
            self.msg = "All Fields Are Required!!"
            self.msg_lable.config(text=self.msg,fg="Red")

        else:
            self.qr_data = (f"Employee ID:{self.Employee_id.get()}\nEmployee Name:{self.Employee_name.get()}\nEmployee deparment:{self.Employee_department.get()}\nEmployee desigination:{self.Employee_designation.get()}")
            self.qr_code =qrcode.make(self.qr_data)
            # ========Saving Qr In Folder===========
            self.qr_code.save("Emp_qr_code/Emp_"+str(self.Employee_id.get()+".png"))


            # ============Updating image========
            qr_code = resizeimage.resize_cover(self.qr_code,[180,180])
            self.img = ImageTk.PhotoImage(qr_code)
            self.qr_code_label.config(image=self.img)
            # ============Notification==========
            self.msg = "QR is Generated Successfully!!!"
            self.msg_lable.config(text=self.msg,fg="green")


    def __init__(self,root):
        self.root = root
        self.root.geometry("900x500")
        self.root.title("QR Code Generator")
        self.root.resizable(False,False)

        title = Label(self.root,text="QR Code Generator",font=("times new roman ",40),bg= "#003366",fg="#FFFFFF",anchor="w")

        title.place(x=0,y=0,relwidth=1)

        #-----------------------Employee window ------------------

        emp_frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        emp_frame.place(x=45,y=100,width=500,height=380)

        emp_title = Label(emp_frame,text="Employee Details",font=("goudy old style",20),bg= "#003366",fg="#FFFFFF")
        emp_title.place(x=0,y=0,relwidth=1)

        emp_code_id = Label(emp_frame,text="Employee ID",font=("times new roman",15,"bold"),bg= "#FFFFFF",anchor="w")\
            .place(x=20,y=60,relwidth=1)

        emp_name = Label(emp_frame, text=" Name", font=("times new roman", 15, "bold"), bg="#FFFFFF",
                            anchor="w") \
            .place(x=20, y=100, relwidth=1)

        emp_department = Label(emp_frame, text=" Department", font=("times new roman", 15, "bold"), bg="#FFFFFF",
                            anchor="w") \
            .place(x=20, y=140, relwidth=1)

        emp_designation = Label(emp_frame, text=" Designation", font=("times new roman", 15, "bold"), bg="#FFFFFF",
                               anchor="w") \
            .place(x=20, y=180, relwidth=1)

        # -------------variables------------------

        self.Employee_id = StringVar()
        self.Employee_name = StringVar()
        self.Employee_department = StringVar()
        self.Employee_designation = StringVar()



        emp_text = Entry(emp_frame,textvariable=self.Employee_id, font=("times new roman", 15), bg="#BCD2E8",fg="#003366")
        emp_text.place(x=200, y=60)

        emp_name_text =  Entry(emp_frame,  font=("times new roman", 15),textvariable=self.Employee_name,  bg="#BCD2E8",fg="#003366")
        emp_name_text.place(x=200, y=100)

        emp_department_text = Entry(emp_frame,font=("times new roman", 15),textvariable=self.Employee_department, bg="#BCD2E8",fg="#003366")
        emp_department_text.place(x=200, y=140)

        emp_designation_text = Entry(emp_frame, font=("times new roman", 15),textvariable=self.Employee_designation, bg="#BCD2E8",fg="#003366")
        emp_designation_text.place(x=200, y=180)



        btn_gen = Button(emp_frame,text="Generate ",font=("times new roman" ,15 ,"bold"),bg="#003366",fg="white",command=self.generate)
        btn_gen.place(x=150,y=250)
        btn_clear = Button(emp_frame,text="Clear",font=("times new roman" ,15 ,"bold"),bg="#003366",fg="white",command=self.Clear)
        btn_clear.place(x=280,y=250)

        self.msg = ""
        self.msg_lable = Label(emp_frame,text=self.msg,font=("times new roman" ,15 ,"bold"),bg="white",fg="green")
        self.msg_lable.place(x=0,y=325,relwidth=1)
        # self.not_msg_lable = Label(emp_frame,text=self.msg,font=("times new roman" ,15 ,"bold"),bg="white",fg="green")
        # self.not_msg_lable.place(x=0,y=325,relwidth=1)



        # ------------QR Code window ---------------------------------------------------------------------------

        qr_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        qr_frame.place(x=580, y=100, width=300, height=380)

        qr_title = Label(qr_frame, text="QR Code", font=("goudy old style", 20), bg="#003366", fg="#FFFFFF")
        qr_title.place(x=0, y=0, relwidth=1)

        self.qr_code_label = Label(qr_frame,text="QR Code \n not available",font=("times new roman" ,15),bg="#003366",fg="white",bd=1,relief=RIDGE)
        self.qr_code_label.place(x=50,y=110,width=180,height=180)













root = Tk()
window = QR_generator(root)
root.mainloop()