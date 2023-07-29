from tkinter import *
from tkinter import ttk #them of tk
from tkinter import messagebox

GUI = Tk() #หน้าจอหลัก
GUI.title('โปรแกรมบันทึกข้อมูล') #หัวข้อ
GUI.geometry('500x400') #ขนาดหน้าจอโปรแกรม

L1 = Label(GUI, text='โปรแกรมเตือนความจำ',font=('Angsana New',30),fg='green')
L1.place(x=30, y=20)

def Button1():
    text = 'Math : 8.30 - 16.30'
    messagebox.showinfo('วิชา', text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=100)
B1 = ttk.Button(FB1,text='Course', command=Button1)
B1.pack(ipadx=20,ipady=20)#กำหนด location


def Button2():
    text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showinfo('เงินในบัญชี', text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=100,y=170)
B2 = ttk.Button(FB2,text='เงินมีอยู่กี่บาท', command=Button2)
B2.pack(ipadx=20,ipady=20)#กำหนด location


def Button3():
    text = 'ซื้อครีมอาทิตย์หน้า'
    messagebox.showinfo('รายการ', text)

FB3 = Frame(GUI) #คล้ายกระดาน
FB3.place(x=100,y=240)
B3 = ttk.Button(FB3,text='ซื้อของ', command=Button3)
B3.pack(ipadx=20,ipady=20)#กำหนด location


def Button4():
    text = 'วิ่งมาราธอนวันศุกร์'
    messagebox.showinfo('สุขภาพร่างกาย', text)

FB4 = Frame(GUI) #คล้ายกระดาน
FB4.place(x=100,y=310)
B4 = ttk.Button(FB4,text='ออกกำลังกาย', command=Button4)
B4.pack(ipadx=20,ipady=20)#กำหนด location


GUI.mainloop()
