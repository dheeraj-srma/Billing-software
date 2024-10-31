from tkinter import*
from tkinter import messagebox
import math,random   
import os
from tkinter.messagebox import showerror
from PIL import ImageTk
num2wors = 10001


class Bill_App:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x730+0+0")
        self.root.title("Bill App")
        bg_color="#074463"
        title=Label(self.root,text="Annapurna Logsitics Solutions",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2,padx=2).pack(fill=X)



        #variables
        #details
        self.movement=StringVar()
        self.lorry_size=StringVar()
        self.particular=StringVar()
        self.destination=StringVar()
        self.lorry_frieght=StringVar()
        self.gr_charge=StringVar()
        self.toll_tax=StringVar()
        self.total_amount=StringVar()
        self.gstin=StringVar()

        #taxes and cash
        self.amuntbfrgst=IntVar()
        self.gst=IntVar()
        self.cgst=IntVar()
        self.sgst=IntVar()
        self.igst=IntVar()
        self.rsinwords=StringVar()

        #appendix
        self.date=StringVar()
        self.pin=StringVar()
        self.address=StringVar()
        self.pan=StringVar()

        #total price and tax variables
        self.grand_total=StringVar()


        # #customer
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(999,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

        #customer Detail Frame
        F1=LabelFrame(self.root,bd=10,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_label=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",fg="black",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=20,pady=5)
        cphone_label=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_label=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.bill_no,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Refresh",command=self.clear_bill,width=10,bd=7,bg="white",fg="black",font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)

   
        #details
        F2=LabelFrame(self.root,bd=10,text="Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=0,y=180,width=635,height=320)

        mvmnt_lbl=Label(F2,text="Movement Date",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=11,sticky="w")
        mvmnt_txt=Entry(F2,width=10,textvariable=self.movement,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=11)
        
        lrysize_lbl=Label(F2,text="Lorry Size",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=11,sticky="w")
        lrysize_txt=Entry(F2,width=10,textvariable=self.lorry_size,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=11)

        prticlr_lbl=Label(F2,text="Particular",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=11,sticky="w")
        prticlr_txt=Entry(F2,width=10,textvariable=self.particular,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=11)

        dstntion_lbl=Label(F2,text="Destination",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=11,sticky="w")
        dstntion_txt=Entry(F2,width=10,textvariable=self.destination,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=11)
        
        lryfrigt_lbl=Label(F2,text="Lorry Frieght",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=2,padx=10,pady=11,sticky="w")
        lryfrigt_txt=Entry(F2,width=10,textvariable=self.lorry_frieght,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=3,padx=8,pady=11)
        
        grchrg_lbl=Label(F2,text="GR Charge",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=2,padx=10,pady=11,sticky="w")
        grchrg_txt=Entry(F2,width=10,textvariable=self.gr_charge,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=3,padx=8,pady=12)
        
        tolltx_lbl=Label(F2,text="Toll Tax",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=2,padx=10,pady=12,sticky="w")
        tolltx_txt=Entry(F2,width=10,textvariable=self.toll_tax,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=3,padx=8,pady=11)

        gstin_lbl=Label(F2,text="GSTIN",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=2,padx=10,pady=11,sticky="w")
        gstin_txt=Entry(F2,width=10,textvariable=self.gstin,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=3,padx=8,pady=11)

        total_amount_lbl=Label(F2,text="Total Amount",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=8,sticky="w")
        total_amount_txt=Entry(F2,width=10,textvariable=self.amuntbfrgst,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=8)


        #amounts
        F3=LabelFrame(self.root,bd=10,text="Amount",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=0,y=500,width=925,height=150)

        amuntbfrgst_lbl=Label(F3,text="Amount Before GST",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=2,padx=0,pady=10,sticky="w")
        amuntbfrgst_txt=Entry(F3,width=10,textvariable=self.amuntbfrgst,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=3,padx=0,pady=10,sticky="w")
        
        gst_lbl=Label(F3,text="GST",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=20,pady=11,sticky="w")
        gst_txt=Entry(F3,width=10,textvariable=self.gst,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        cgst_lbl=Label(F3,text="CGST @ 6%",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=2,padx=0,pady=11,sticky="w")
        cgst_txt=Entry(F3,width=10,textvariable=self.cgst,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=3,padx=0,pady=10)

        sgst_lbl=Label(F3,text="SGST @ 6%",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=4,padx=10,pady=11,sticky="w")
        sgst_txt=Entry(F3,width=10,textvariable=self.sgst,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=10)

        igst_lbl=Label(F3,text="IGST @ 6%",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=11,sticky="w")
        igst_txt=Entry(F3,width=10,textvariable=self.igst,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        rsinwords_lbl=Label(F3,text="Rs in Words",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=4,padx=0,pady=11,sticky="w")
        rsinwords_txt=Entry(F3,width=10,textvariable=self.rsinwords,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=5,padx=0,pady=10)

        #others
        F4=LabelFrame(self.root,bd=10,text="Appendix",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=637,y=180,width=290,height=320)

        date_lbl=Label(F4,text="Date",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        date_txt=Entry(F4,width=10,textvariable=self.movement,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky="w")
        
        invno_lbl=Label(F4,text="Invoice No.",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        invno_txt=Entry(F4,width=10,textvariable=self.bill_no,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky="w")

        pan_lbl=Label(F4,text="PAN",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        pan_txt=Entry(F4,width=10,textvariable=self.pan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky="w")

        pin_lbl=Label(F4,text="PIN",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        pin_txt=Entry(F4,width=10,textvariable=self.pin,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky="w")

        addrs_lbl=Label(F4,text="Address",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        addrs_txt=Entry(F4,width=10,textvariable=self.address,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky="w")

        #button frame 
        F7=LabelFrame(self.root,bd=10,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F7.place(x=0,y=650,width=925,height=93)
        m1_lbl=Label(F7,text="Grand Total Amount",font=("times new roman",19,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=15,sticky="w")
        m1_txt=Entry(F7,width=10,textvariable=self.grand_total,font=("times new roman",19,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=15)


        #billing area
        F5=LabelFrame(self.root,bd=5,bg="black")
        F5.place(x=928,y=180,width=435,height=320)
        bill_title=Label(F5,text="Bill Area",fg="black",font="arial 15 bold",bd=5,relief=GROOVE,bg="white").pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack()

        #buttons
        F6=LabelFrame(self.root,bd=10,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=928,y=500,width=435,height=246)

        btn_F=Frame(F6,bd=7,bg="white",relief=GROOVE)
        btn_F.place(x=0,y=0,width=420,height=240)


        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",bd=5,fg="white",pady=15,width=14,height=2,font="arial 14 bold").grid(row=0,column=0,padx=10,pady=11)
        gbill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",bd=5,fg="white",pady=15,width=14,height=2,font="arial 14 bold").grid(row=0,column=1,padx=10,pady=11)
        save_btn=Button(btn_F,text="Save",command=self.save_bill,bg="cadetblue",bd=5,fg="white",pady=15,width=14,height=2,font="arial 14 bold").grid(row=1,column=1,padx=10,pady=11)
        exit_btn=Button(btn_F,text="Exit",command=self.exit_app,bg="cadetblue",bd=5,fg="white",pady=15,width=14,height=2,font="arial 14 bold").grid(row=1,column=0,padx=10,pady=11)
        self.welcome_bill()

    def total(self):
        self.grand_total_amount=float(
                                    (self.gst.get()*1)+
                                    (self.cgst.get()*1)+
                                    (self.sgst.get()*1)+
                                    (self.igst.get()*1)+
                                    (self.amuntbfrgst.get()*1)
                                    ) 
        self.grand_total.set("Rs"+str(self.grand_total_amount))
        

    def welcome_bill(self):
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,"           \t Anapurna Logistics Retailer")
            self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
            self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
            self.txtarea.insert(END,f"\n Customer Phone : {self.c_phone.get()}")
            self.txtarea.insert(END,f"\n =================================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("ERROR","Customer details are must")

        else:
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,"           \t Anapurna Logistics Retailer")
            self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
            self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
            self.txtarea.insert(END,f"\n Customer Phone : {self.c_phone.get()}")
            self.txtarea.insert(END,f"\n =================================================")
            self.txtarea.insert(END,f"\n Date : {self.movement.get()}")
            self.txtarea.insert(END,f"\n Invoice No. : {self.bill_no.get()}")
            self.txtarea.insert(END,f"\n PIN : {self.pin.get()}")
            self.txtarea.insert(END,f"\n PAN : {self.pan.get()}")
            self.txtarea.insert(END,f"\n Address : {self.address.get()}")
            self.txtarea.insert(END,f"\n =================================================")

            self.txtarea.insert(END,f"\n Movement Date : {self.movement.get()}")
            self.txtarea.insert(END,f"\n Lorry Frieght : {self.lorry_frieght.get()}")
            self.txtarea.insert(END,f"\n Lorry Size : {self.lorry_size.get()}")
            self.txtarea.insert(END,f"\n GR Charge : {self.gr_charge.get()}")
            self.txtarea.insert(END,f"\n Particular : {self.particular.get()}")
            self.txtarea.insert(END,f"\n Toll Tax : {self.toll_tax.get()}")
            self.txtarea.insert(END,f"\n Destination : {self.destination.get()}")
            self.txtarea.insert(END,f"\n GSTIN : {self.gstin.get()}")
            self.txtarea.insert(END,f"\n =================================================")
            self.txtarea.insert(END,f"\n Amount Before GST : {self.amuntbfrgst.get()}")
            self.txtarea.insert(END,f"\n GST: {self.gst.get()}")
            self.txtarea.insert(END,f"\n CGST @ 6% : {self.cgst.get()}")
            self.txtarea.insert(END,f"\n SGST @ 6% : {self.sgst.get()}")
            self.txtarea.insert(END,f"\n IGST @ 6% : {self.igst.get()}")
            self.txtarea.insert(END,f"\n Grand Total : {self.grand_total.get()}")
            self.txtarea.insert(END,f"\n Rs in words : Rs. {self.rsinwords.get()} only")
            self.txtarea.insert(END,f"\n =================================================")
            self.txtarea.insert(END,f"\n Terms and Conditions")
            self.txtarea.insert(END,f"\n 1. Our responsiblities ceases after delievery of goods to the carrier ")
            self.txtarea.insert(END,f"\n 2. Interest will be charged @24% if the bill is not paid on due date")
            self.txtarea.insert(END,f"\n 3. All disputes are subjected to Gurugram Jurisdiction only")
            


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:    
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".pdf","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Save",f"Bill no:{self.bill_no.get()}; Saved Successfully")

        else:
           return



    def exit_app(self):
        op=messagebox.askyesno("EXIT","Do you want to exit?")
        if op>0:
            self.root.destroy()





    def find_bill(self):
        present="yes"
        for bills in os.listdir("E:\\python tuturials\\softwares\\Billing Software\\bills/"):
            print(bills)
            if bills.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{bills}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present=="no"

        if present=="yes":
            messagebox.showerror("ERROR","Bill not found")

    
    def clear_bill(self):
        # #customer
        self.bill_no.set("")
        x=random.randint(999,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"           \t Anapurna Logistics Retailer")
        self.txtarea.insert(END,f"\n Bill No : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : ")
        self.txtarea.insert(END,f"\n Customer Phone : ")
        self.txtarea.insert(END,f"\n =================================================")





root=Tk()
obj = Bill_App(root)
root.mainloop()

