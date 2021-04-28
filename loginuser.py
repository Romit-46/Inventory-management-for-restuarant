from tkinter import *
import tkinter as tk  
from PIL import Image, ImageTk
from dtabase import Databasein
import cv2
from tkinter import messagebox

database=Databasein("inventory.db")

def manager():
    window=tk.Toplevel(log)
    window.configure(bg='azure',highlightbackground="DeepPink4", highlightthickness=8,cursor='hand1')
    imagetest = PhotoImage(file="backbutton.png")
    imagetest=imagetest.subsample(6,6)
    searchi = PhotoImage(file="search1.png")
    searchi=searchi.subsample(12,12)
    viewi = PhotoImage(file="view3.png")
    viewi=viewi.subsample(14,14)
    deletei = PhotoImage(file="delete.png")
    deletei=deletei.subsample(13,13)
    def addrecipe():
        ar = tk.Toplevel(window)
        ar.configure(bg='azure',highlightbackground="DeepPink4", highlightthickness=8,cursor='hand1')
        def callback(input): 
            if input.isdigit(): 
                messagebox.showwarning("showwarning", "Inavalid input",parent=ar)
                return False
                          
            elif (input== ""): 
                 
                return True
        
            else: 
                return True
        def get_selected_row(event):
            global selected_tuple
            index=list1.curselection()[0]
            selected_tuple=list1.get(index)
            e1.delete(0,END)
            e1.insert(END,selected_tuple[1])
            e2.delete(0,END)
            e2.insert(END,selected_tuple[2])
            e3.delete(0,END)
            e3.insert(END,selected_tuple[3])
            e4.delete(0,END)
            e4.insert(END,selected_tuple[4])
        def view_command():
            list1.delete(0,END)
            for row in database.view():
                list1.insert(END,row)

        def addrec_command():
            database.addrec(name_text.get(),i1_text.get(),i2_text.get(),q_text.get())
            list1.delete(0,END)
            list1.insert(END,(name_text.get(),i1_text.get(),i2_text.get(),q_text.get()))
            messagebox.showinfo("showinfo", "Information",parent=ar)

        def update_command():
            database.update(selected_tuple[0],name_text.get(),i1_text.get(),i2_text.get(),q_text.get())

        
        def search_command():
            list1.delete(0,END)
            for row in database.searchrec(name_text.get(),):
                list1.insert(END,row)

        def delete_command():
            database.delete(selected_tuple[0])

        l0=Label(ar,text="ADD RECIPE",bg='azure',fg='DeepPink4',font=("Helvetica", 16))
        l0.grid(row=0,column=2)
        l1=Label(ar,text="RECIPE NAME",bg='azure',fg='DeepPink4',font=("Helvetica", 11))
        l1.grid(row=1,column=0)
        name_text=StringVar()
        e1=Entry(ar,textvariable=name_text,bg='alice blue')
        e1.grid(row=1,column=1)
        l2=Label(ar,text="C-INGREDIENTS",bg='azure',fg='DeepPink4',font=("Helvetica", 11))
        l2.grid(row=2,column=0)
        i1_text=StringVar()
        e2=Entry(ar,textvariable=i1_text,bg='alice blue')
        e2.grid(row=2,column=1)
        reg=ar.register(callback)
        e2.configure(validate='key',validatecommand=(reg,'%P'))
        l3=Label(ar,text="S-INGREDIENTS",bg='azure',fg='DeepPink4',font=("Helvetica", 11))
        l3.grid(row=3,column=0)
        i2_text=StringVar()
        e3=Entry(ar,textvariable=i2_text,bg='alice blue')
        e3.grid(row=3,column=1)
        reg=ar.register(callback)
        e3.configure(validate='key',validatecommand=(reg,'%P'))
        l4=Label(ar,text="QUANTITY",bg='azure',fg='DeepPink4',font=("Helvetica", 11))
        l4.grid(row=4,column=0)
        q_text=StringVar()
        e4=Entry(ar,textvariable=q_text,bg='alice blue')
        e4.grid(row=4,column=1)
        list1=Listbox(ar, height=10,width=45,bg='alice blue')
        list1.grid(row=2,column=2,rowspan=3,columnspan=2)
        sb1=Scrollbar(ar)
        sb1.grid(row=3,column=3,rowspan=3)

        list1.configure(yscrollcommand=sb1.set)
        list1.insert("end")
        sb1.configure(bg='black',command=list1.yview)
        list1.bind('<<ListboxSelect>>',get_selected_row)
        b1=Button(ar,text="ADD",width=16,font='sans 10 bold',bg='DarkOrange1',fg='white',activebackground="#00ffff",command=addrec_command)
        b1.grid(row=7,column=0,padx=10, pady=10)   
        b5=Button(ar,text="VIEW",image=viewi,compound=RIGHT, width=100,font='sans 10 bold',bg='DarkOrange1',fg='white',activebackground="#00ffff",activeforeground="black",command=view_command)
        b5.grid(row=7,column=1,padx=10, pady=10)
        b6=Button(ar,text="SEARCH", image=searchi,width=100,compound=RIGHT,font='sans 10 bold',bg='DarkOrange1',fg='white',activebackground="#00ffff",activeforeground="black",command=search_command)
        b6.grid(row=7,column=2,padx=10, pady=10)
        b4=Button(ar,image=imagetest, width=50,font='sans 8 bold',relief=FLAT,bg='azure',fg='white',command = lambda: close_window(),activebackground="#00ffff",activeforeground="black")
        b4.grid(row=0,column=0,padx=10, pady=10) 

        def e11(e):
            b1['background'] = 'gold'

        def l11(e):
            b1['background'] = 'DarkOrange1'

        b1.bind("<Enter>", e11)
        b1.bind("<Leave>", l11)

        def f2(e):
            b7['background'] = 'red'

        def l20(e):
            b7['background'] = 'firebrick1'

        b7.bind("<Enter>", f2)
        b7.bind("<Leave>", l20)

        def f3(e):
            b3['background'] = 'gold'

        def l30(e):
            b3['background'] = 'SystemButtonFace'

        b3.bind("<Enter>", f3)
        b3.bind("<Leave>", l30)

        def f4(e):
            b4['background'] = 'gold'

        def l40(e):
            b4['background'] = 'azure'

        b4.bind("<Enter>", f4)
        b4.bind("<Leave>", l40)

        def f4555(e):
            b5['background'] = 'gold'

        def l4055(e):
            b5['background'] = 'DarkOrange1'

        b5.bind("<Enter>", f4555)
        b5.bind("<Leave>", l4055)


        def a5(e):
            b6['background'] = 'gold'
        def b50(e):
            b6['background'] = 'DarkOrange1'

        b6.bind("<Enter>", a5)
        b6.bind("<Leave>", b50)

        def close_window():
            ar.destroy()
    

    def removerecipe():
        rr = tk.Toplevel(window)
        def get_selected_row(event):
            global selected_tuple
            index=list1.curselection()[0]
            selected_tuple=list1.get(index)
            e1.delete(0,END)
            e1.insert(END,selected_tuple[1])
            e2.delete(0,END)
            e2.insert(END,selected_tuple[2])
            e3.delete(0,END)
            e3.insert(END,selected_tuple[3])
            e4.delete(0,END)
            e4.insert(END,selected_tuple[4])
        def view_command():
            list1.delete(0,END)
            for row in database.view():
                list1.insert(END,row)

        
        def search_command():
            list1.delete(0,END)
            for row in database.searchrec(name_text.get(),):
                list1.insert(END,row)

        def delete_command():
            database.delete(selected_tuple[0])

        l0=Label(rr,text="REMOVE RECIPE")
        l0.grid(row=0,column=2)
        l1=Label(rr,text="Recipe name")
        l1.grid(row=1,column=0)
        name_text=StringVar()
        i1_text=StringVar()
        i2_text=StringVar()
        q_text=StringVar()
        e1=Entry(rr,textvariable=name_text)
        e1.grid(row=1,column=1)
        e2=Entry(rr,textvariable=i1_text)
        e3=Entry(rr,textvariable=i2_text)
        e4=Entry(rr,textvariable=q_text)
        
        list1=Listbox(rr, height=6,width=35)
        list1.grid(row=2,column=1,rowspan=3,columnspan=2)
        sb1=Scrollbar(rr)
        sb1.grid(row=2,column=2,rowspan=3)

        list1.configure(yscrollcommand=sb1.set)
        list1.insert("end")
        sb1.configure(command=list1.yview)
        list1.bind('<<ListboxSelect>>',get_selected_row)
        b0=Button(rr,text="ref",width=18,activebackground="#00ffff",activeforeground="black",command=view_command)
        b0.grid(row=1,column=4,padx=10, pady=10)
        b1=Button(rr,text="view all", width=18,activebackground="#00ffff",activeforeground="black",command=view_command)
        b1.grid(row=2,column=4,padx=10, pady=10)
        b2=Button(rr,text="search", width=18,activebackground="#00ffff",activeforeground="black",command=search_command)
        b2.grid(row=3,column=4,padx=10, pady=10)
        b3=Button(rr,text="delete", width=18,activebackground="#00ffff",activeforeground="black",command=delete_command)
        b3.grid(row=4,column=4,padx=10, pady=10)
        b4=Button(rr,text="close", width=16,command = lambda: close_window(),activebackground="#00ffff",activeforeground="black")
        b4.grid(row=5,column=4,padx=10, pady=10)
        def close_window():
            rr.destroy() 
        def f1(e):
            b1['background'] = 'gold'

        def l12(e):
            b1['background'] = 'SystemButtonFace'

        b1.bind("<Enter>", f1)
        b1.bind("<Leave>", l12)

        def f4(e):
            b4['background'] = 'gold'
        def l4(e):
            b4['background'] = 'SystemButtonFace'

        b4.bind("<Enter>", f4)
        b4.bind("<Leave>", l4)

        def e44(e):
            b2['background'] = 'gold'
        def l44(e):
            b2['background'] = 'SystemButtonFace'

        b2.bind("<Enter>", e44)
        b2.bind("<Leave>", l44)

        def e45(e):
            b3['background'] = 'red'
        def l45(e):
            b3['background'] = 'SystemButtonFace'

        b3.bind("<Enter>", e45)
        b3.bind("<Leave>", l45)

        def v45(e):
            b0['background'] = 'gold'
        def u45(e):
            b0['background'] = 'SystemButtonFace'

        b0.bind("<Enter>", v45)
        b0.bind("<Leave>", u45)

    def updaterecipe():
        ur = tk.Toplevel(window)
        ur.configure(bg='azure',highlightbackground="DeepPink4", highlightthickness=8,cursor='hand1')
        def get_selected_row(event):
            global selected_tuple
            index=list1.curselection()[0]
            selected_tuple=list1.get(index)
            e1.delete(0,END)
            e1.insert(END,selected_tuple[1])
            e2.delete(0,END)
            e2.insert(END,selected_tuple[2])
            e3.delete(0,END)
            e3.insert(END,selected_tuple[3])
            e4.delete(0,END)
            e4.insert(END,selected_tuple[4])
        def view_command():
            list1.delete(0,END)
            for row in database.view():
                list1.insert(END,row)

        def update_command():
            mg=messagebox.askquestion("askquestion", "Are you sure?",parent=ur)            
            if(mg=='yes'):
                database.update(selected_tuple[0],name_text.get(),i1_text.get(),i2_text.get(),q_text.get())

        
        def search_command():
            list1.delete(0,END)
            for row in database.searchrec(name_text.get(),):
                list1.insert(END,row)

        def delete_command():
            mg=messagebox.askquestion("askquestion", "Are you sure?",parent=ur)            
            if(mg=='yes'):
                database.delete(selected_tuple[0])
            
            

        l0=Label(ur,text="UPDATE RECIPE",bg='azure',fg='DeepPink4',font=("Helvetica", 16))
        l0.grid(row=0,column=2)
        l1=Label(ur,text="RECIPE NAME",bg='azure',fg='DeepPink4',font=("Helvetica", 11))
        l1.grid(row=1,column=0)
        name_text=StringVar()
        e1=Entry(ur,textvariable=name_text,bg='alice blue')
        e1.grid(row=1,column=1)
        l2=Label(ur,text="C-INGREDIENTS",bg='azure',fg='DeepPink4',font=("Helvetica", 11))
        l2.grid(row=2,column=0)
        i1_text=StringVar()
        e2=Entry(ur,textvariable=i1_text,bg='alice blue')
        e2.grid(row=2,column=1)
        l3=Label(ur,text="S-INGREDIENTS",bg='azure',fg='DeepPink4',font=("Helvetica", 11))
        l3.grid(row=3,column=0)
        i2_text=StringVar()
        e3=Entry(ur,textvariable=i2_text,bg='alice blue')
        e3.grid(row=3,column=1)
        l4=Label(ur,text="QUANTITY",bg='azure',fg='DeepPink4',font=("Helvetica", 11))
        l4.grid(row=4,column=0)
        q_text=StringVar()
        e4=Entry(ur,textvariable=q_text,bg='alice blue')
        e4.grid(row=4,column=1)
        list1=Listbox(ur, height=10,width=45,bg='alice blue')
        list1.grid(row=2,column=2,rowspan=3,columnspan=2)
        sb1=Scrollbar(ur)
        sb1.grid(row=3,column=3,rowspan=3)

        list1.configure(yscrollcommand=sb1.set)
        list1.insert("end")
        sb1.configure(bg='black',command=list1.yview)
        list1.bind('<<ListboxSelect>>',get_selected_row)
        b1=Button(ur,text="UPDATE",width=16,font='sans 10 bold',bg='DarkOrange1',fg='white',activebackground="#00ffff",command=update_command)
        b1.grid(row=7,column=0,padx=10, pady=10)  
        b5=Button(ur,text="VIEW", image=viewi,compound=RIGHT, width=100,font='sans 10 bold',bg='DarkOrange1',fg='white',activebackground="#00ffff",activeforeground="black",command=view_command)
        b5.grid(row=7,column=1,padx=10, pady=10)
        b6=Button(ur,text="SEARCH", image=searchi,width=100,compound=RIGHT,font='sans 10 bold',bg='DarkOrange1',fg='white',activebackground="#00ffff",activeforeground="black",command=search_command)
        b6.grid(row=7,column=2,padx=10, pady=10)
        b7=Button(ur,text="DELETE", image=deletei,width=100,compound=RIGHT,font='sans 10 bold',bg='firebrick1',fg='white',activebackground="#00ffff",activeforeground="black",command=delete_command)
        b7.grid(row=7,column=3,padx=10, pady=10)
        b4=Button(ur,image=imagetest, width=50,relief=FLAT,font='sans 8 bold',bg='azure',fg='white',command = lambda: close_window(),activebackground="#00ffff",activeforeground="black")
        b4.grid(row=0,column=0,padx=10, pady=10) 

        def e11(e):
            b1['background'] = 'gold'

        def l11(e):
            b1['background'] = 'DarkOrange1'

        b1.bind("<Enter>", e11)
        b1.bind("<Leave>", l11)

        def f2(e):
            b7['background'] = 'red'

        def l20(e):
            b7['background'] = 'firebrick1'

        b7.bind("<Enter>", f2)
        b7.bind("<Leave>", l20)

        def f3(e):
            b3['background'] = 'gold'

        def l30(e):
            b3['background'] = 'SystemButtonFace'

        b3.bind("<Enter>", f3)
        b3.bind("<Leave>", l30)

        def f4(e):
            b4['background'] = 'gold'

        def l40(e):
            b4['background'] = 'azure'

        b4.bind("<Enter>", f4)
        b4.bind("<Leave>", l40)

        def f4555(e):
            b5['background'] = 'gold'

        def l4055(e):
            b5['background'] = 'DarkOrange1'

        b5.bind("<Enter>", f4555)
        b5.bind("<Leave>", l4055)


        def a5(e):
            b6['background'] = 'gold'
        def b50(e):
            b6['background'] = 'DarkOrange1'

        b6.bind("<Enter>", a5)
        b6.bind("<Leave>", b50)

        def close_window():
            ur.destroy()

    def addvendor():
        av = tk.Toplevel(window)
        l0=Label(av,text="ADD VENDOR")
        l0.grid(row=0,column=2)
        l1=Label(av,text="Vendor name")
        l1.grid(row=1,column=0)
        title_text=StringVar()
        e1=Entry(av,textvariable=title_text)
        e1.grid(row=1,column=1)
        l1=Label(av,text="Vendor details")
        l1.grid(row=2,column=0)
        title_text=StringVar()
        e1=Entry(av,textvariable=title_text)
        e1.grid(row=2,column=1)
        list1=Listbox(av, height=6,width=35)
        list1.grid(row=3,column=1,rowspan=6,columnspan=2)
        sb1=Scrollbar(av)
        sb1.grid(row=3,column=2,rowspan=6)
        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)
        list1.insert("end","ingredients from vendor")
        l3=Label(av,text="details of ingredients")
        l3.grid(row=3,column=0)
        b3=Button(av,text="add ingreident", width=16,activebackground="#00ffff",activeforeground="black")
        b3.grid(row=2,column=3,padx=10, pady=10) 
        b4=Button(av,text="add ingredient not on list", width=20,activebackground="#00ffff",activeforeground="black")
        b4.grid(row=3,column=3,padx=10, pady=10) 
        b2=Button(av,text="submit changes", width=20,activebackground="#00ffff",activeforeground="black")
        b2.grid(row=4,column=3,padx=10, pady=10) 
        b5=Button(av,text="close", width=16,command = lambda: close_window(),activebackground="#00ffff",activeforeground="black")
        b5.grid(row=5,column=4,padx=10, pady=10) 

        mb= Menubutton ( av, text="select ingredient", relief=RAISED )
        mb.grid(row=1,column=3,padx=10, pady=10)
        mb.menu = Menu ( mb, tearoff = 0 )
        mb["menu"] =  mb.menu

        mayoVar = IntVar()
        ketchVar = IntVar()
        riceVar= IntVar()
        pastaVar= IntVar()

        mb.menu.add_checkbutton ( label="mayo",variable=mayoVar )
        mb.menu.add_checkbutton ( label="ketchup",variable=ketchVar )
        mb.menu.add_checkbutton ( label="pasta",variable=pastaVar )
        mb.menu.add_checkbutton ( label="rice",variable=riceVar )

        def e11(e):
            b1['background'] = 'gold'

        def l11(e):
            b1['background'] = 'SystemButtonFace'

        b1.bind("<Enter>", e11)
        b1.bind("<Leave>", l11)

        def e25(e):
            b2['background'] = 'gold'

        def l2(e):
            b2['background'] = 'SystemButtonFace'

        b2.bind("<Enter>", e25)
        b2.bind("<Leave>", l2)

        def e35(e):
            b3['background'] = 'gold'

        def l31(e):
            b3['background'] = 'SystemButtonFace'

        b3.bind("<Enter>", e35)
        b3.bind("<Leave>", l31)

        def e48(e):
            b4['background'] = 'gold'

        def l4(e):
            b4['background'] = 'SystemButtonFace'

        b4.bind("<Enter>", e48)
        b4.bind("<Leave>", l4)

        def e5(e):
            b5['background'] = 'gold'
        def l5(e):
            b5['background'] = 'SystemButtonFace'

        b5.bind("<Enter>", e5)
        b5.bind("<Leave>", l5)

        def close_window():
            av.destroy()

    def updatevendor():
        uv = tk.Toplevel(window)
        l0=Label(uv,text="UPDATE VENDOR")
        l0.grid(row=0,column=2)
        l1=Label(uv,text="Vendor name")
        l1.grid(row=1,column=0)
        list1=Listbox(uv, height=6,width=35)
        list1.grid(row=3,column=1,rowspan=6,columnspan=2)
        sb1=Scrollbar(uv)
        sb1.grid(row=3,column=2,rowspan=6)
        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)
        list1.insert("end","ingredients from vendor")
        l3=Label(uv,text="details of ingredients")
        l3.grid(row=3,column=0)
        b4=Button(uv,text="remove ingredient", width=16,activebackground="#00ffff",activeforeground="black")
        b4.grid(row=3,column=3,padx=10, pady=10) 
        b2=Button(uv,text="submit changes", width=20,activebackground="#00ffff",activeforeground="black")
        b2.grid(row=4,column=3,padx=10, pady=10) 
        b5=Button(uv,text="close", width=16,command = lambda: close_window(),activebackground="#00ffff",activeforeground="black")
        b5.grid(row=5,column=4,padx=10, pady=10) 

        mb= Menubutton ( uv, text="select ingredient", relief=RAISED )
        mb.grid(row=1,column=3,padx=10, pady=10)
        mb.menu = Menu ( mb, tearoff = 0 )
        mb["menu"] =  mb.menu

        mayoVar = IntVar()
        ketchVar = IntVar()
        riceVar= IntVar()
        pastaVar= IntVar()

        mb.menu.add_checkbutton ( label="mayo",variable=mayoVar )
        mb.menu.add_checkbutton ( label="ketchup",variable=ketchVar )
        mb.menu.add_checkbutton ( label="pasta",variable=pastaVar )
        mb.menu.add_checkbutton ( label="rice",variable=riceVar )

        mb2= Menubutton ( uv, text="change quantity", relief=RAISED )
        mb2.grid(row=2,column=3,padx=10, pady=10)
        mb2.menu = Menu ( mb2, tearoff = 0 )
        mb2["menu"] =  mb2.menu

        mayoVar = IntVar()
        ketchVar = IntVar()
        riceVar= IntVar()
        pastaVar= IntVar()

        mb2.menu.add_checkbutton ( label="10",variable=mayoVar )
        mb2.menu.add_checkbutton ( label="20",variable=ketchVar )
        mb2.menu.add_checkbutton ( label="30",variable=pastaVar )
        mb2.menu.add_checkbutton ( label="40",variable=riceVar )
        
        mb1= Menubutton ( uv, text="select vendor", relief=RAISED )
        mb1.grid(row=1,column=1,padx=10, pady=10)
        mb1.menu = Menu ( mb1, tearoff = 0 )
        mb1["menu"] =  mb1.menu

        riceVar = IntVar()
        pizzaVar = IntVar()
        nachosVar= IntVar()
        friesVar= IntVar()

        mb1.menu.add_checkbutton ( label="Troy",variable=riceVar )
        mb1.menu.add_checkbutton ( label="Lab",variable=pizzaVar )
        mb1.menu.add_checkbutton ( label="TREVOR",variable=nachosVar )
        mb1.menu.add_checkbutton ( label="Mike",variable=friesVar )

        def e11(e):
            b1['background'] = 'gold'

        def l11(e):
            b1['background'] = 'SystemButtonFace'

        b1.bind("<Enter>", e11)
        b1.bind("<Leave>", l11)

        def e21(e):
            b2['background'] = 'gold'

        def l2(e):
            b2['background'] = 'SystemButtonFace'

        b2.bind("<Enter>", e21)
        b2.bind("<Leave>", l2)

        def e33(e):
            b3['background'] = 'gold'

        def l31(e):
            b3['background'] = 'SystemButtonFace'

        b3.bind("<Enter>", e33)
        b3.bind("<Leave>", l31)

        def e45(e):
            b4['background'] = 'gold'

        def l4(e):
            b4['background'] = 'SystemButtonFace'

        b4.bind("<Enter>", e45)
        b4.bind("<Leave>", l4)

        def e5(e):
            b5['background'] = 'gold'
        def l5(e):
            b5['background'] = 'SystemButtonFace'

        b5.bind("<Enter>", e5)
        b5.bind("<Leave>", l5)

        def close_window():
            uv.destroy()

            
    def removevendor():
        rv = tk.Toplevel(window)
        l0=Label(rv,text="REMOVE VENDOR")
        l0.grid(row=0,column=2)
        l1=Label(rv,text="Vendor name")
        l1.grid(row=2,column=0)
        mb= Menubutton ( rv, text="remove vendor", relief=RAISED )
        mb.grid(row=2,column=2,padx=10, pady=10)
        mb.menu = Menu ( mb, tearoff = 0 )
        mb["menu"] =  mb.menu

        riceVar = IntVar()
        pizzaVar = IntVar()
        nachosVar= IntVar()
        friesVar= IntVar()

        mb.menu.add_checkbutton ( label="Troy",variable=riceVar )
        mb.menu.add_checkbutton ( label="Lab",variable=pizzaVar )
        mb.menu.add_checkbutton ( label="TREVOR",variable=nachosVar )
        mb.menu.add_checkbutton ( label="Mike",variable=friesVar )
        b1=Button(rv,text="remove selected vendor", width=18,activebackground="#00ffff",activeforeground="black")
        b1.grid(row=3,column=2,padx=10, pady=10)
        b4=Button(rv,text="close", width=16,command = lambda: close_window(),activebackground="#00ffff",activeforeground="black")
        b4.grid(row=4,column=4,padx=10, pady=10)
        def close_window():
            rv.destroy() 
        def e1(e):
            b1['background'] = 'gold'

        def l12(e):
            b1['background'] = 'SystemButtonFace'

        b1.bind("<Enter>", e1)
        b1.bind("<Leave>", l12)

        def e4(e):
            b4['background'] = 'gold'
        def l4(e):
            b4['background'] = 'SystemButtonFace'

        b4.bind("<Enter>", e4)
        b4.bind("<Leave>", l4)

    def correctinventory():
        ci = tk.Toplevel(window)
        l0=Label(ci,text="CORRECT INVENTORY")
        l0.grid(row=0,column=1)
        l1=Label(ci,text="Select")
        l1.grid(row=1,column=0)
        l2=Label(ci,text="Current quantity")
        l2.grid(row=3,column=0)
        title_text=StringVar()
        e1=Entry(ci,textvariable=title_text)
        e1.grid(row=3,column=1)
        l2=Label(ci,text="Current expiration dates")
        l2.grid(row=4,column=0)
        title_text=StringVar()
        e1=Entry(ci,textvariable=title_text)
        e1.grid(row=4,column=1)
        l2=Label(ci,text="enter new quantity")
        l2.grid(row=5,column=0)
        title_text=StringVar()
        e1=Entry(ci,textvariable=title_text)
        e1.grid(row=5,column=1)
        l2=Label(ci,text="enter new dates")
        l2.grid(row=6,column=0)
        title_text=StringVar()
        e1=Entry(ci,textvariable=title_text)
        e1.grid(row=6,column=1)
        b2=Button(ci,text="submit changes", width=20,activebackground="#00ffff",activeforeground="black")
        b2.grid(row=5,column=3,padx=10, pady=10) 
        b3=Button(ci,text="Delete ingredient", width=20,activebackground="#00ffff",activeforeground="black")
        b3.grid(row=4,column=3,padx=10, pady=10)
        b5=Button(ci,text="close", width=16,command = lambda: close_window(),activebackground="#00ffff",activeforeground="black")
        b5.grid(row=6,column=3,padx=10, pady=10) 

        mb= Menubutton ( ci, text="select ingredient to change", relief=RAISED )
        mb.grid(row=1,column=1,padx=10, pady=10)
        mb.menu = Menu ( mb, tearoff = 0 )
        mb["menu"] =  mb.menu

        mayoVar = IntVar()
        ketchVar = IntVar()
        riceVar= IntVar()
        pastaVar= IntVar()

        mb.menu.add_checkbutton ( label="mayo",variable=mayoVar )
        mb.menu.add_checkbutton ( label="ketchup",variable=ketchVar )
        mb.menu.add_checkbutton ( label="pasta",variable=pastaVar )
        mb.menu.add_checkbutton ( label="rice",variable=riceVar )

        def e11(e):
            b1['background'] = 'gold'

        def l11(e):
            b1['background'] = 'SystemButtonFace'

        b1.bind("<Enter>", e11)
        b1.bind("<Leave>", l11)

        def e2(e):
            b2['background'] = 'gold'

        def l21(e):
            b2['background'] = 'SystemButtonFace'

        b2.bind("<Enter>", e2)
        b2.bind("<Leave>", l21)

        def e3(e):
            b3['background'] = 'gold'

        def l31(e):
            b3['background'] = 'SystemButtonFace'

        b3.bind("<Enter>", e3)
        b3.bind("<Leave>", l31)

        def e4(e):
            b4['background'] = 'gold'

        def l4(e):
            b4['background'] = 'SystemButtonFace'

        b4.bind("<Enter>", e4)
        b4.bind("<Leave>", l4)

        def e5(e):
            b5['background'] = 'gold'
        def l5(e):
            b5['background'] = 'SystemButtonFace'

        b5.bind("<Enter>", e5)
        b5.bind("<Leave>", l5)

        def close_window():
            ci.destroy()

    

    b1=Button(window,text="ADD RECIPE",font='sans 10 bold',bg='DarkOrange1',fg='white',activebackground="#00ffff",activeforeground="black", width=12,command=addrecipe)
    b1.grid(row=0,column=1)

    b2=Button(window,text="REMOVE RECIPE", width=16,font='sans 10 bold',bg='DarkOrange1',fg='white',activebackground="#00ffff",activeforeground="black",command=removerecipe)
    b2.grid(row=0,column=3,padx=10, pady=10)

    b3=Button(window,text="UPDATE RECIPE", width=12,font='sans 10 bold',bg='DarkOrange1',fg='white',activebackground="#00ffff",activeforeground="black",command=updaterecipe)
    b3.grid(row=0,column=6)

    b4=Button(window,text="CHECK INVENTORY LEVEL",font='sans 10 bold',bg='DarkOrange1',fg='white',activebackground="#00ffff",activeforeground="black", width=22)
    b4.grid(row=2,column=3,padx=10, pady=10)
    b5=Button(window,text="CORRECT INVENTORY LEVEL",justify=CENTER, width=22,font='sans 10 bold',bg='DarkOrange1',fg='white',command=correctinventory,activebackground="#00ffff",activeforeground="black")
    b5.grid(row=4,column=3,padx=10, pady=10)

    b6=Button(window,text="REMOVE VENDOR", width=22,command=removevendor,font='sans 10 bold',bg='DarkOrange1',fg='white',activebackground="#00ffff",activeforeground="black")
    b6.grid(row=6,column=3,padx=10, pady=10)

    b7=Button(window,text="ADD VENDOR", width=22,command=addvendor,font='sans 10 bold',bg='DarkOrange1',fg='white',activebackground="#00ffff",activeforeground="black")
    b7.grid(row=8,column=3,padx=10, pady=10)

    b8=Button(window,text="UPDATE VENDOR", width=22,command=updatevendor,font='sans 10 bold',bg='DarkOrange1',fg='white',activebackground="#00ffff",activeforeground="black")
    b8.grid(row=10,column=3,padx=10, pady=10)

    b9=Button(window,text="CHECK STATS", width=12,activebackground="#00ffff",font='sans 10 bold',bg='DarkOrange1',fg='white',activeforeground="black")
    b9.grid(row=14,column=1,padx=10, pady=10)

    b10=Button(window,text="UPDATE RESOURCE DATABASE", width=22,activebackground="#00ffff",font='sans 10 bold',bg='DarkOrange1',fg='white',activeforeground="black")
    b10.grid(row=12,column=3,padx=10, pady=10)

    b11=Button(window,text="LOG OUT", width=12,command = lambda: close_window(),font='sans 10 bold',bg='DarkOrange1',fg='white',activebackground="#00ffff",activeforeground="black")
    b11.grid(row=14,column=6,padx=10, pady=10)

    def close_window():
            window.destroy()
    
    def e1(e):
        b1['background'] = 'gold'

    def l1(e):
        b1['background'] = 'DarkOrange1'

    def e2(e):
        b2['background'] = 'gold'

    def l2(e):
        b2['background'] = 'DarkOrange1'

    def e3(e):
        b3['background'] = 'gold'

    def l3(e):
        b3['background'] = 'DarkOrange1'

    def e4(e):
        b4['background'] = 'gold'

    def l4(e):
        b4['background'] = 'DarkOrange1'

    def e5(e):
        b5['background'] = 'gold'

    def l5(e):
        b5['background'] = 'DarkOrange1'

    def e6(e):
        b6['background'] = 'gold'

    def l6(e):
        b6['background'] = 'DarkOrange1'

    def e7(e):
        b7['background'] = 'gold'

    def l7(e):
        b7['background'] = 'DarkOrange1'

    def e8(e):
        b8['background'] = 'gold'

    def l8(e):
        b8['background'] = 'DarkOrange1'

    def e9(e):
        b9['background'] = 'gold'

    def l9(e):
        b9['background'] = 'DarkOrange1'

    def e10(e):
        b10['background'] = 'gold'

    def l10(e):
        b10['background'] = 'DarkOrange1'

    def e11(e):
        b11['background'] = 'gold'

    def l11(e):
        b11['background'] = 'DarkOrange1'

    b1.bind("<Enter>", e1)
    b1.bind("<Leave>", l1)
    b2.bind("<Enter>", e2)
    b2.bind("<Leave>", l2)
    b3.bind("<Enter>", e3)
    b3.bind("<Leave>", l3)
    b4.bind("<Enter>", e4)
    b4.bind("<Leave>", l4)
    b5.bind("<Enter>", e5)
    b5.bind("<Leave>", l5)
    b6.bind("<Enter>", e6)
    b6.bind("<Leave>", l6)
    b7.bind("<Enter>", e7)
    b7.bind("<Leave>", l7)
    b8.bind("<Enter>", e8)
    b8.bind("<Leave>", l8)
    b9.bind("<Enter>", e9)
    b9.bind("<Leave>", l9)
    b10.bind("<Enter>", e10)
    b10.bind("<Leave>", l10)
    b11.bind("<Enter>", e11)
    b11.bind("<Leave>", l11)

def admin():
    window=tk.Toplevel(log)
     

log=Tk()
log.wm_title("Inventory")
l0=Label(log,text="*")
l0.grid(row=0,column=1)
l2=Label(log,text="*")
l2.grid(row=7,column=10)
l3=Label(log,text="*")
l3.grid(row=0,column=6)
l4=Label(log,text="*")
l4.grid(row=7,column=10)
b1=Button(log,text="login as manager", width=12,command=manager,activebackground="#00ffff",activeforeground="black")
b1.grid(row=1,column=5,padx=10, pady=10)

b2=Button(log,text="login as chef", width=16,activebackground="#00ffff",activeforeground="black")
b2.grid(row=3,column=5,padx=10, pady=10)

b3=Button(log,text="login as admin", width=12,activebackground="#00ffff",activeforeground="black")
b3.grid(row=5,column=5,padx=10, pady=10)
def f1(e):
    b1['background'] = 'white'

def l1(e):
    b1['background'] = 'SystemButtonFace'

def f2(e):
    b2['background'] = 'gold'

def l22(e):
    b2['background'] = 'SystemButtonFace'

def f3(e):
    b3['background'] = 'gold'

def l33(e):
    b3['background'] = 'SystemButtonFace'

    

b1.bind("<Enter>", f1)
b1.bind("<Leave>", l1)
b2.bind("<Enter>", f2)
b2.bind("<Leave>", l22)
b3.bind("<Enter>", f3)
b3.bind("<Leave>", l33)

log.mainloop()
